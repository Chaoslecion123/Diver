from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import VATSerializer


__all__ = [
    'VATViewSet',
]

VAT = apps.get_model(*'django_prices_vatlayer.VAT'.split())


class VATViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`django_prices_vatlayer.VAT`

    `** Actions **`:

    create:
    Create a new `django_prices_vatlayer.VAT` instance.

    retrieve:
    Return the given `django_prices_vatlayer.VAT`.

    update:
    Update the given `django_prices_vatlayer.VAT`..

    delete:
    Delete the given `django_prices_vatlayer.VAT`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`VAT`.
    """

    lookup_field = 'id'
    queryset = VAT.objects.all()
    serializer_class = VATSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'country_code',
        # 'data',
        # 'id',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'country_code',
        # 'data',
        # 'id',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'country_code',
        # 'data',
        # 'id',

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