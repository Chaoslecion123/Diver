from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from saleor.rest.serializers import PhysicalStoreSerializer


__all__ = [
    'PhysicalStoreViewSet',
]

PhysicalStore = apps.get_model(*'store.PhysicalStore'.split())


class PhysicalStoreViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`store.PhysicalStore`

    `** Actions **`:

    create:
    Create a new `store.PhysicalStore` instance.

    retrieve:
    Return the given `store.PhysicalStore`.

    update:
    Update the given `store.PhysicalStore`..

    delete:
    Delete the given `store.PhysicalStore`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`PhysicalStore`.
    """

    lookup_field = 'id'
    permit_list_expands = ['address']
    queryset = PhysicalStore.objects.all()
    serializer_class = PhysicalStoreSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'address', # [account.Address]
        # 'id',
        # 'is_main_store',
        # 'name',
        # 'site', # [sites.Site]

        # Reverse Fields
        # 'phone',
    ]
    search_fields = [
        # Fields
        # 'address',
        # 'id',
        # 'is_main_store',
        # 'name',
        # 'site',

        # Reverse Fields
        # 'phone',
    ]
    ordering_fields = [
        # Fields
        # 'address',
        # 'id',
        # 'is_main_store',
        # 'name',
        # 'site',

        # Reverse Fields
        # 'phone',
    ]
    # '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'address'):
            queryset = queryset.prefetch_related('address')
        return queryset

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
