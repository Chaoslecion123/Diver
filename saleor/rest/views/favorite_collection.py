from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import FavoriteCollectionSerializer

__all__ = [
    'FavoriteCollectionViewSet',
]

FavoriteCollection = apps.get_model(*'account.FavoriteCollection'.split())


class FavoriteCollectionViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.FavoriteCollection`

    `** Actions **`:

    create:
    Create a new `order.FavoriteCollection` instance.

    retrieve:
    Return the given `order.FavoriteCollection`.

    update:
    Update the given `order.FavoriteCollection`..

    delete:
    Delete the given `order.FavoriteCollection`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`FavoriteCollection`.
    """

    lookup_field = 'id'
    queryset = FavoriteCollection.objects.all()
    serializer_class = FavoriteCollectionSerializer
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
