from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import OrderLineSerializer


__all__ = [
    'OrderLineViewSet',
]

OrderLine = apps.get_model(*'order.OrderLine'.split())


class OrderLineViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.OrderLine`

    `** Actions **`:

    create:
    Create a new `order.OrderLine` instance.

    retrieve:
    Return the given `order.OrderLine`.

    update:
    Update the given `order.OrderLine`..

    delete:
    Delete the given `order.OrderLine`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`OrderLine`.
    """

    lookup_field = 'id'
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'is_shipping_required',
        # 'order', # [order.Order]
        # 'product_name',
        # 'product_sku',
        # 'quantity',
        # 'quantity_fulfilled',
        # 'tax_rate',
        # 'translated_product_name',
        # 'unit_price',
        # 'unit_price_gross',
        # 'unit_price_net',
        # 'variant', # [product.ProductVariant]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'is_shipping_required',
        # 'order',
        # 'product_name',
        # 'product_sku',
        # 'quantity',
        # 'quantity_fulfilled',
        # 'tax_rate',
        # 'translated_product_name',
        # 'unit_price',
        # 'unit_price_gross',
        # 'unit_price_net',
        # 'variant',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'is_shipping_required',
        # 'order',
        # 'product_name',
        # 'product_sku',
        # 'quantity',
        # 'quantity_fulfilled',
        # 'tax_rate',
        # 'translated_product_name',
        # 'unit_price',
        # 'unit_price_gross',
        # 'unit_price_net',
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

    # def update(self, request, *args, **kwargs):
    #    return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
