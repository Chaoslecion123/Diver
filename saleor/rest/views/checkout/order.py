import json
import culqipy

from django.apps import apps
from django.db.models import Q
from django.db import transaction
from django.conf import settings

from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet

from saleor.rest.serializers import OrderSerializer
from ....checkout.models import Checkout
from ....core.utils import get_client_ip
from ....order.models import Order
from ....payment import ChargeStatus, TransactionKind, get_payment_gateway
from ....payment.utils import (
    create_payment, create_payment_information, gateway_process_payment)


__all__ = [
    'OrderViewSet',
]

Order = apps.get_model(*'order.Order'.split())
OrdrOrderLine = apps.get_model(*'order.OrderLine'.split())


class OrderViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.Order`

    `** Actions **`:

    create:
    Create a new `order.Order` instance.

    retrieve:
    Return the given `order.Order`.

    update:
    Update the given `order.Order`..

    delete:
    Delete the given `order.Order`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Order`.
    """

    lookup_field = 'token'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'billing_address', # [account.Address]
        # 'created',
        # 'customer_note',
        # 'discount_amount',
        # 'discount_name',
        # 'display_gross_prices',
        # 'id',
        # 'language_code',
        # 'shipping_address', # [account.Address]
        # 'shipping_method', # [shipping.ShippingMethod]
        # 'shipping_method_name',
        # 'shipping_price',
        # 'shipping_price_gross',
        # 'shipping_price_net',
        # 'status',
        # 'token',
        # 'total',
        # 'total_gross',
        # 'total_net',
        # 'tracking_client_id',
        # 'translated_discount_name',
        # 'user', # [account.User]
        # 'user_email',
        # 'voucher', # [discount.Voucher]
        # 'weight',

        # Reverse Fields
        # 'events',
        # 'fulfillments',
        # 'lines',
        # 'payments',
    ]
    search_fields = [
        # Fields
        # 'billing_address',
        # 'created',
        # 'customer_note',
        # 'discount_amount',
        # 'discount_name',
        # 'display_gross_prices',
        # 'id',
        # 'language_code',
        # 'shipping_address',
        # 'shipping_method',
        # 'shipping_method_name',
        # 'shipping_price',
        # 'shipping_price_gross',
        # 'shipping_price_net',
        # 'status',
        # 'token',
        # 'total',
        # 'total_gross',
        # 'total_net',
        # 'tracking_client_id',
        # 'translated_discount_name',
        # 'user',
        # 'user_email',
        # 'voucher',
        # 'weight',

        # Reverse Fields
        # 'events',
        # 'fulfillments',
        # 'lines',
        # 'payments',
    ]
    ordering_fields = [
        # Fields
        # 'billing_address',
        # 'created',
        # 'customer_note',
        # 'discount_amount',
        # 'discount_name',
        # 'display_gross_prices',
        # 'id',
        # 'language_code',
        # 'shipping_address',
        # 'shipping_method',
        # 'shipping_method_name',
        # 'shipping_price',
        # 'shipping_price_gross',
        # 'shipping_price_net',
        # 'status',
        # 'token',
        # 'total',
        # 'total_gross',
        # 'total_net',
        # 'tracking_client_id',
        # 'translated_discount_name',
        # 'user',
        # 'user_email',
        # 'voucher',
        # 'weight',

        # Reverse Fields
        # 'events',
        # 'fulfillments',
        # 'lines',
        # 'payments',
    ]
    # '__all__'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user.orders.all()

        lookup_expr = Q()

        token = self.kwargs.get('token', None)

        if token:
            lookup_expr = lookup_expr | Q(token=token)

        if lookup_expr.children:
            return super().get_queryset().filter(lookup_expr)

        return Order.objects.none()

    # def get_object(self):
    #     return super().get_object()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #    return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(
        methods=['post'],
        detail=True,
        name='pay',
        url_path='pay',
        url_name='pay'
    )
    def pay(self, request, *args, **kwargs):
        order = self.get_object()
        gateway = 'culqi'
        payment_gateway, connection_params = get_payment_gateway(gateway)
        extra_data = {
            'customer_user_agent': request.META.get('HTTP_USER_AGENT', None)
        }
        response_data = {}
        response_status = status.HTTP_200_OK

        with transaction.atomic():
            payment = create_payment(
                gateway=gateway,
                currency=order.total.gross.currency,
                email=order.user_email,
                billing_address=order.billing_address,
                customer_ip_address=get_client_ip(request),
                total=order.total.gross.amount,
                order=order,
                extra_data=extra_data)

            if (order.is_fully_paid()
                    or payment.charge_status == ChargeStatus.FULLY_REFUNDED):
                return Response(response_data, status=response_status)

            payment_info = create_payment_information(payment)
            form = payment_gateway.create_form(
                data=request.data or None,
                payment_information=payment_info,
                connection_params=connection_params)
            if form.is_valid():
                try:
                    gateway_process_payment(
                        payment=payment, payment_token=form.get_payment_token())
                except Exception as msg:  # pylint: disable=broad-except
                    response_data['detail'] = str(msg)
                    response_status = status.HTTP_400_BAD_REQUEST
                    return Response(response_data, status=response_status)
                else:
                    # if order.is_fully_paid():
                    #     return redirect('order:payment-success', token=order.token)
                    # return redirect(order.get_absolute_url())
                    return Response(response_data, status=response_status)

        # client_token = payment_gateway.get_client_token(
        #     connection_params=connection_params)
        # ctx = {
        #     'form': form,
        #     'payment': payment,
        #     'client_token': client_token,
        #     'order': order}
        # return TemplateResponse(request, payment_gateway.TEMPLATE_PATH, ctx)
        return Response(response_data, status=response_status)
