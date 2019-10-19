from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import FulfillmentLineSerializer


__all__ = [
    'FulfillmentLineViewSet',
]

FulfillmentLine = apps.get_model(*'order.FulfillmentLine'.split())


class FulfillmentLineViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.FulfillmentLine`

    `** Actions **`:

    create:
    Create a new `order.FulfillmentLine` instance.

    retrieve:
    Return the given `order.FulfillmentLine`.

    update:
    Update the given `order.FulfillmentLine`..

    delete:
    Delete the given `order.FulfillmentLine`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`FulfillmentLine`.
    """

    lookup_field = 'id'
    queryset = FulfillmentLine.objects.all()
    serializer_class = FulfillmentLineSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'fulfillment', # [order.Fulfillment]
        # 'id',
        # 'order_line', # [order.OrderLine]
        # 'quantity',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'fulfillment',
        # 'id',
        # 'order_line',
        # 'quantity',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'fulfillment',
        # 'id',
        # 'order_line',
        # 'quantity',

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
