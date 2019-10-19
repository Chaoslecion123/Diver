from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from ...serializers import FavoriteSerializer

from ...permissions import ReadOnly


__all__ = [
    'FavoriteViewSet',
]

Favorite = apps.get_model(*'favorites.Favorite'.split())


class FavoriteViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`account.Favorite`

    `** Actions **`:

    create:
    Create a new `account.Favorite` instance.

    retrieve:
    Return the given `account.Favorite`.

    update:
    Update the given `account.Favorite`..

    delete:
    Delete the given `account.Favorite`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Favorite`.
    """

    permission_classes = [ReadOnly]
    lookup = 'id'
    permit_list_expands = ['user', 'product']

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        'user',
        'product',
        'collection',
    ]
