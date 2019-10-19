from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import PhoneSerializer


__all__ = [
    'PhoneViewSet',
]

Phone = apps.get_model(*'store.Phone'.split())


class PhoneViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`store.Phone`

    `** Actions **`:

    create:
    Create a new `store.Phone` instance.

    retrieve:
    Return the given `store.Phone`.

    update:
    Update the given `store.Phone`..

    delete:
    Delete the given `store.Phone`, and return an empty response 
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Phone`.
    """

    lookup_field = 'id'
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'number',
        # 'physical_store', # [store.PhysicalStore]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'number',
        # 'physical_store',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'number',
        # 'physical_store',

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
