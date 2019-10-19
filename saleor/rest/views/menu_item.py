from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import MenuItemSerializer


__all__ = [
    'MenuItemViewSet',
]

MenuItem = apps.get_model(*'menu.MenuItem'.split())


class MenuItemViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`menu.MenuItem`

    `** Actions **`:

    create:
    Create a new `menu.MenuItem` instance.

    retrieve:
    Return the given `menu.MenuItem`.

    update:
    Update the given `menu.MenuItem`..

    delete:
    Delete the given `menu.MenuItem`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`MenuItem`.
    """

    lookup_field = 'id'
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'category', # [product.Category]
        # 'collection', # [product.Collection]
        # 'id',
        # 'level',
        # 'lft',
        # 'menu', # [menu.Menu]
        # 'name',
        # 'page', # [page.Page]
        # 'parent', # [menu.MenuItem]
        # 'rght',
        # 'sort_order',
        # 'tree_id',
        # 'url',

        # Reverse Fields
        # 'children',
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'category',
        # 'collection',
        # 'id',
        # 'level',
        # 'lft',
        # 'menu',
        # 'name',
        # 'page',
        # 'parent',
        # 'rght',
        # 'sort_order',
        # 'tree_id',
        # 'url',

        # Reverse Fields
        # 'children',
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'category',
        # 'collection',
        # 'id',
        # 'level',
        # 'lft',
        # 'menu',
        # 'name',
        # 'page',
        # 'parent',
        # 'rght',
        # 'sort_order',
        # 'tree_id',
        # 'url',

        # Reverse Fields
        # 'children',
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
