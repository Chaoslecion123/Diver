from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CitySerializer
from ...permissions import ReadOnly


__all__ = [
    'CityViewSet',
]

City = apps.get_model(*'world.City'.split())


class CityViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`world.City`

    `** Actions **`:

    create:
    Create a new `world.City` instance.

    retrieve:
    Return the given `world.City`.

    update:
    Update the given `world.City`..

    delete:
    Delete the given `world.City`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`City`.
    """
    permission_classes = [ReadOnly]
    http_method_names = ['get', 'head', 'options']

    lookup_field = 'id'
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'country_area', # [world.CountryArea]
        # 'id',
        # 'name',

        # Reverse Fields
        # 'city_area',
    ]
    search_fields = [
        # Fields
        # 'country_area',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'city_area',
    ]
    ordering_fields = [
        # Fields
        # 'country_area',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'city_area',
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
