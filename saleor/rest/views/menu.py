from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import MenuSerializer


__all__ = [
    'MenuViewSet',
]

Menu = apps.get_model(*'menu.Menu'.split())


class MenuViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`menu.Menu`

    `** Actions **`:

    create:
    Create a new `menu.Menu` instance.

    retrieve:
    Return the given `menu.Menu`.

    update:
    Update the given `menu.Menu`..

    delete:
    Delete the given `menu.Menu`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Menu`.
    """

    lookup_field = 'id'
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'json_content',
        # 'name',

        # Reverse Fields
        # 'items',
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'json_content',
        # 'name',

        # Reverse Fields
        # 'items',
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'json_content',
        # 'name',

        # Reverse Fields
        # 'items',
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
