from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import ShippingZoneSerializer


__all__ = [
    'ShippingZoneViewSet',
]

ShippingZone = apps.get_model(*'shipping.ShippingZone'.split())


class ShippingZoneViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`shipping.ShippingZone`

    `** Actions **`:

    create:
    Create a new `shipping.ShippingZone` instance.

    retrieve:
    Return the given `shipping.ShippingZone`.

    update:
    Update the given `shipping.ShippingZone`..

    delete:
    Delete the given `shipping.ShippingZone`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`ShippingZone`.
    """

    lookup_field = 'id'
    queryset = ShippingZone.objects.all()
    serializer_class = ShippingZoneSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'countries',
        # 'default',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'shipping_methods',
    ]
    search_fields = [
        # Fields
        # 'countries',
        # 'default',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'shipping_methods',
    ]
    ordering_fields = [
        # Fields
        # 'countries',
        # 'default',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'shipping_methods',
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
