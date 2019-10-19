from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import RateTypesSerializer


__all__ = [
    'RateTypesViewSet',
]

RateTypes = apps.get_model(*'django_prices_vatlayer.RateTypes'.split())


class RateTypesViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`django_prices_vatlayer.RateTypes`

    `** Actions **`:

    create:
    Create a new `django_prices_vatlayer.RateTypes` instance.

    retrieve:
    Return the given `django_prices_vatlayer.RateTypes`.

    update:
    Update the given `django_prices_vatlayer.RateTypes`..

    delete:
    Delete the given `django_prices_vatlayer.RateTypes`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`RateTypes`.
    """

    lookup_field = 'id'
    queryset = RateTypes.objects.all()
    serializer_class = RateTypesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'types',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'types',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'types',

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
