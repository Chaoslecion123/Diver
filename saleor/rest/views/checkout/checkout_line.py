from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CheckoutLineSerializer

from ...permissions import ReadOnly


__all__ = [
    'CheckoutLineViewSet',
]

Checkout = apps.get_model(*'checkout.Checkout'.split())
CheckoutLine = apps.get_model(*'checkout.CheckoutLine'.split())


class CheckoutLineViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`checkout.CheckoutLine`

    `** Actions **`:

    create:
    Create a new `checkout.CheckoutLine` instance.

    retrieve:
    Return the given `checkout.CheckoutLine`.

    update:
    Update the given `checkout.CheckoutLine`..

    delete:
    Delete the given `checkout.CheckoutLine`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`CheckoutLine`.
    """

    permissions_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = CheckoutLine.objects.all()
    serializer_class = CheckoutLineSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'checkout', # [checkout.Checkout]
        # 'data',
        # 'id',
        # 'quantity',
        # 'variant', # [product.ProductVariant]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'checkout',
        # 'data',
        # 'id',
        # 'quantity',
        # 'variant',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'checkout',
        # 'data',
        # 'id',
        # 'quantity',
        # 'variant',

        # Reverse Fields
    ]
    # '__all__'

    # def get_object(self):
    #     return super().get_object()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)  # pylint: disable=no-member
        line = self.get_object()
        checkout = line.checkout
        checkout = Checkout.objects.get(token=checkout.token)
        checkout.quantity = sum(
            checkout.lines.all().values_list('quantity', flat=True)
        )
        checkout.save()
        return response

    def destroy(self, request, *args, **kwargs):
        line = self.get_object()
        checkout = line.checkout
        response = super().destroy(request, *args, **kwargs)  # pylint: disable=no-member
        checkout = Checkout.objects.get(token=checkout.token)
        checkout.quantity = sum(
            checkout.lines.all().values_list('quantity', flat=True)
        )
        checkout.save()
        return response  # pylint: disable=no-member

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
