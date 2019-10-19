from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import FulfillmentSerializer
from saleor.order.models import Fulfillment

__all__ = [
    'FulfillmentViewSet',
]

Fulfillment = apps.get_model(*'order.Fulfillment'.split())


class FulfillmentViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.Fulfillment`

    `** Actions **`:

    create:
    Create a new `order.Fulfillment` instance.

    retrieve:
    Return the given `order.Fulfillment`.

    update:
    Update the given `order.Fulfillment`..

    delete:
    Delete the given `order.Fulfillment`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Fulfillment`.
    """

    lookup_field = 'id'
    queryset = Fulfillment.objects.all()
    serializer_class = FulfillmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'fulfillment_order',
        # 'id',
        # 'order', # [order.Order]
        # 'shipping_date',
        # 'status',
        # 'tracking_number',

        # Reverse Fields
        # 'lines',
    ]
    search_fields = [
        # Fields
        # 'fulfillment_order',
        # 'id',
        # 'order',
        # 'shipping_date',
        # 'status',
        # 'tracking_number',

        # Reverse Fields
        # 'lines',
    ]
    ordering_fields = [
        # Fields
        # 'fulfillment_order',
        # 'id',
        # 'order',
        # 'shipping_date',
        # 'status',
        # 'tracking_number',

        # Reverse Fields
        # 'lines',
    ]
    # '__all__'

"""
    def get_queryset(self):
        user = self.request.user
        qs = Fulfillment.objects.filter(fulfillments=user)
        return qs
"""
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
