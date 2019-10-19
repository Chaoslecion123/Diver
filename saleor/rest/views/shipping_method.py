from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from django_filters import rest_framework as filters
from saleor.rest.serializers import ShippingMethodSerializer


__all__ = [
    'ShippingMethodViewSet',
]

ShippingMethod = apps.get_model(*'shipping.ShippingMethod'.split())


class ShippingMethodFilterSet(filters.FilterSet):
    # country = filters.String(
    #     field_name="shipping_zone__countries", lookup_expr='contains')

    class Meta:
        model = ShippingMethod
        fields = {
            'shipping_zone__countries': ['contains'],
        }


class ShippingMethodViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`shipping.ShippingMethod`

    `** Actions **`:

    create:
    Create a new `shipping.ShippingMethod` instance.

    retrieve:
    Return the given `shipping.ShippingMethod`.

    update:
    Update the given `shipping.ShippingMethod`..

    delete:
    Delete the given `shipping.ShippingMethod`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`ShippingMethod`.
    """

    lookup_field = 'id'
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_class = ShippingMethodFilterSet
    filter_fields = [
        # Fields
        # 'id',
        # 'maximum_order_price',
        # 'maximum_order_weight',
        # 'minimum_order_price',
        # 'minimum_order_weight',
        # 'name',
        # 'price',
        # 'shipping_zone', # [shipping.ShippingZone]
        # 'type',

        # Reverse Fields
        # 'checkouts',
        # 'orders',
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'maximum_order_price',
        # 'maximum_order_weight',
        # 'minimum_order_price',
        # 'minimum_order_weight',
        # 'name',
        # 'price',
        # 'shipping_zone',
        # 'type',

        # Reverse Fields
        # 'checkouts',
        # 'orders',
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'maximum_order_price',
        # 'maximum_order_weight',
        # 'minimum_order_price',
        # 'minimum_order_weight',
        # 'name',
        # 'price',
        # 'shipping_zone',
        # 'type',

        # Reverse Fields
        # 'checkouts',
        # 'orders',
        # 'translations',
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
