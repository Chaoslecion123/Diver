from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CountryAreaSerializer
from ...permissions import ReadOnly


__all__ = [
    'CountryAreaViewSet',
]

CountryArea = apps.get_model(*'world.CountryArea'.split())


class CountryAreaViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`world.CountryArea`

    `** Actions **`:

    create:
    Create a new `world.CountryArea` instance.

    retrieve:
    Return the given `world.CountryArea`.

    update:
    Update the given `world.CountryArea`..

    delete:
    Delete the given `world.CountryArea`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`CountryArea`.
    """
    permission_classes = [ReadOnly]
    http_method_names = ['get', 'head', 'options']

    lookup_field = 'id'
    queryset = CountryArea.objects.all()
    serializer_class = CountryAreaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'country',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'city',
    ]
    search_fields = [
        # Fields
        # 'country',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'city',
    ]
    ordering_fields = [
        # Fields
        # 'country',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'city',
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
