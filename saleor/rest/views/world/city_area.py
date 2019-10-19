from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CityAreaSerializer
from ...permissions import ReadOnly


__all__ = [
    'CityAreaViewSet',
]

CityArea = apps.get_model(*'world.CityArea'.split())


class CityAreaViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`world.CityArea`

    `** Actions **`:

    create:
    Create a new `world.CityArea` instance.

    retrieve:
    Return the given `world.CityArea`.

    update:
    Update the given `world.CityArea`..

    delete:
    Delete the given `world.CityArea`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`CityArea`.
    """
    permission_classes = [ReadOnly]
    http_method_names = ['get', 'head', 'options']
    # permission_classes = [ReadOnly]

    lookup_field = 'id'
    queryset = CityArea.objects.all().order_by('name')
    serializer_class = CityAreaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'city', # [world.City]
        # 'id',
        # 'name',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'city',
        # 'id',
        'name',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'city',
        # 'id',
        # 'name',

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
