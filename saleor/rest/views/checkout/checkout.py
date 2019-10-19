import copy

from prices import Money

from django.apps import apps
from django.db import transaction

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from rest_flex_fields import FlexFieldsModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ....core import analytics
from ....checkout import BillingType
from ....checkout.utils import (
    create_order, get_taxes_for_checkout, recalculate_checkout_discount,
    remove_voucher_from_checkout)
from ....checkout.forms import CheckoutVoucherForm
from ...serializers import CheckoutSerializer
from ...serializers import OrderSerializer
from ...permissions import ReadOnly



__all__ = [
    'CheckoutViewSet',
]

Checkout = apps.get_model(*'checkout.Checkout'.split())
PhysicalStore = apps.get_model(*'store.PhysicalStore'.split())
GlovoOrder = apps.get_model(*'glovo.GlovoOrder'.split())
RunningBoxOrder = apps.get_model(*'runningbox.RunningBoxOrder'.split())
RunningBoxDeliveryPermission = apps.get_model(
    *'runningbox.RunningBoxDeliveryPermission'.split())


class CheckoutViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`checkout.Checkout`

    `** Actions **`:

    create:
    Create a new `checkout.Checkout` instance.

    retrieve:
    Return the given `checkout.Checkout`.

    update:
    Update the given `checkout.Checkout`..

    delete:
    Delete the given `checkout.Checkout`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Checkout`.
    """

    permissions_classes = [ReadOnly]
    lookup_field = 'token'
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'billing_address', # [account.Address]
        # 'created',
        # 'discount_amount',
        # 'discount_name',
        # 'email',
        # 'last_change',
        # 'note',
        # 'quantity',
        # 'shipping_address', # [account.Address]
        # 'shipping_method', # [shipping.ShippingMethod]
        'token',
        # 'translated_discount_name',
        # 'user', # [account.User]
        # 'voucher_code',

        # Reverse Fields
        # 'lines',
        # 'payments',
    ]
    search_fields = [
        # Fields
        # 'billing_address',
        # 'created',
        # 'discount_amount',
        # 'discount_name',
        # 'email',
        # 'last_change',
        # 'note',
        # 'quantity',
        # 'shipping_address',
        # 'shipping_method',
        # 'token',
        # 'translated_discount_name',
        # 'user',
        # 'voucher_code',

        # Reverse Fields
        # 'lines',
        # 'payments',
    ]
    ordering_fields = [
        # Fields
        # 'billing_address',
        # 'created',
        # 'discount_amount',
        # 'discount_name',
        # 'email',
        # 'last_change',
        # 'note',
        # 'quantity',
        # 'shipping_address',
        # 'shipping_method',
        # 'token',
        # 'translated_discount_name',
        # 'user',
        # 'voucher_code',

        # Reverse Fields
        # 'lines',
        # 'payments',
    ]
    # '__all__'

    # def get_object(self):
    #     return super().get_object()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        checkout = self.get_object()

        if request.user.is_authenticated:
            if request.user != checkout.user:
                checkout.user = request.user

        if not request.user.is_authenticated:
            checkout.user = None

        checkout.save()

        return super().retrieve(request, *args, **kwargs)  # pylint: disable=no-member

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        shipping_method = request.data.get('shipping_method', None)
        instance = self.get_object()
        data = copy.deepcopy(request.data)

        if shipping_method == 'shipping-with-glovo':
            # print('*** *** ***')
            # print('shipping-with-glovo')
            # print(request.data)
            # print('*** *** ***')
            data = copy.deepcopy(request.data)
            shipping_method = data.pop('shipping_method')
            shipping_method_info = data.pop('shipping_method_info')
            data['shipping_method'] = None

            if getattr(instance, 'glovo_order', None):
                glovo_order = instance.glovo_order
                glovo_order.origin_store = PhysicalStore.objects.get(
                    id=shipping_method_info['store']
                )
                glovo_order.delivery_address = instance.shipping_address
                glovo_order.price = Money(
                    str(shipping_method_info['price']['amount']),
                    shipping_method_info['price']['currency']
                )
            else:
                glovo_order = GlovoOrder(
                    checkout=instance,
                    origin_store=PhysicalStore.objects.get(
                        id=shipping_method_info['store']
                    ),
                    delivery_address=instance.shipping_address,
                    price=Money(
                        str(shipping_method_info['price']['amount']),
                        shipping_method_info['price']['currency']
                    )
                )

            with transaction.atomic():
                glovo_order.save()
                instance.glovo_order = glovo_order
                runningbox_order = getattr(instance, 'runningbox_order', None)
                if runningbox_order:
                    runningbox_order.delete()
                    instance.runningbox_order = None
                instance.save()

            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial
            )

        elif shipping_method == 'shipping-with-runningbox':
            # print('*** *** ***')
            # print('shipping-with-glovo')
            # print(request.data)
            # print('*** *** ***')
            data = copy.deepcopy(request.data)
            shipping_method = data.pop('shipping_method')
            shipping_method_info = data.pop('shipping_method_info')
            data['shipping_method'] = None

            store = RunningBoxDeliveryPermission.objects.filter(
                runningbox_enabled=True).first().store

            print("*** *** ***")
            print(store)
            print("*** *** ***")
            if getattr(instance, 'runningbox_order', None):
                runningbox_order = instance.runningbox_order
                runningbox_order.origin_store = store
                runningbox_order.delivery_address = instance.shipping_address
                runningbox_order.price = Money(
                    str(shipping_method_info['price']['amount']),
                    shipping_method_info['price']['currency']
                )
            else:
                runningbox_order = RunningBoxOrder(
                    checkout=instance,
                    origin_store=store,
                    delivery_address=instance.shipping_address,
                    price=Money(
                        str(shipping_method_info['price']['amount']),
                        shipping_method_info['price']['currency']
                    )
                )

            with transaction.atomic():
                runningbox_order.save()
                instance.runningbox_order = runningbox_order
                glovo_order = getattr(instance, 'glovo_order', None)
                if glovo_order:
                    glovo_order.delete()
                    instance.glovo_order = None
                instance.save()

            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial
            )

        else:
            if shipping_method is not None and getattr(instance, 'glovo_order', None):
                instance.glovo_order.delete()

            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial
            )

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}  # pylint: disable=W0212

        return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(
        methods=['post'],
        detail=True,
        name='clear',
        url_path='clear',
        url_name='clear'
    )
    def clear(self, request, *args, **kwargs):
        checkout = self.get_object()
        try:
            checkout.lines.all().delete()
            checkout.quantity = 0
            checkout.save()
        except Exception as msg:
            response_data = {
                'error': [msg]
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        return super().retrieve(request, *args, **kwargs)  # pylint: disable=no-member

    @action(
        methods=['post'],
        detail=True,
        name='apply-discount',
        url_path='apply-discount',
        url_name='apply-discount'
    )
    def apply_discount(self, request, *args, **kwargs):
        errors = {}
        prefix = 'discount'
        checkout = self.get_object()
        voucher = request.data.get('voucher', None)
        data = {
            'discount-voucher': voucher
        } if voucher else None

        voucher_form = CheckoutVoucherForm(
            data or None, prefix=prefix, instance=checkout)

        if voucher_form.is_bound:
            if voucher_form.is_valid():
                voucher_form.save()
            else:
                # remove_voucher_from_checkout(checkout)
                for field in voucher_form:
                    if field.errors:
                        errors[field.name] = field.errors
                response_data = {}
                response_data['errors'] = errors
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        else:
            taxes = get_taxes_for_checkout(checkout, request.taxes)
            recalculate_checkout_discount(checkout, request.discounts, taxes)

        return super().retrieve(request, *args, **kwargs)  # pylint: disable=no-member

    @action(
        methods=['post'],
        detail=True,
        name='place-order',
        url_path='place-order',
        url_name='place-order'
    )
    def place_order(self, request, *args, **kwargs):
        response_data = {}

        errors = {}

        first_name = request.data.get('first_name', None)
        if first_name is None:
            errors['first_name'] = "Este campo no puede ser vacío"

        last_name = request.data.get('last_name', None)
        if last_name is None:
            errors['last_name'] = "Este campo no puede ser vacío"

        email = request.data.get('email', None)
        if email is None:
            errors['email'] = "Este campo no puede ser vacío"

        if errors:
            response_data['errors'] = errors
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        try:
            checkout = self.get_object()
            glovo_order = getattr(checkout, 'glovo_order', None)

            if request.user.is_authenticated:
                checkout.user = request.user
                checkout.save()

            if checkout.billing_type == BillingType.BALLOT:
                checkout.billing_address = checkout.shipping_address
                checkout.save()

            print("*** *** ***")
            print("before create_order")
            print("*** *** ***")
            try:
                order = create_order(
                    checkout=checkout,
                    tracking_code=analytics.get_client_id(request),
                    discounts=request.discounts,
                    taxes=get_taxes_for_checkout(checkout, request.taxes),
                    user=request.user)
            except Exception as msg:
                raise Exception(msg)

            order.shipping_type = checkout.shipping_type
            order.billing_type = checkout.billing_type
            order.user_first_name = first_name
            order.user_last_name = last_name
            order.user_email = email
            order.save()
            print("*** *** ***")
            print("after create_order")
            print("*** *** ***")

            if glovo_order is not None:
                glovo_order.checkout = None
                glovo_order.order = order
                glovo_order.save()

            response_data['orderToken'] = order.token

        except Exception as msg:
            errors['transaction'] = "Revisa nuevamente los datos de tu carrito."
            response_data['errors'] = errors
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        return Response(response_data)  # response
