from django.apps import apps
from django.utils import timezone
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import SaleSerializer


__all__ = [
    'SaleViewSet',
]

Sale = apps.get_model(*'discount.Sale'.split())


class SaleViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`discount.Sale`

    `** Actions **`:

    create:
    Create a new `discount.Sale` instance.

    retrieve:
    Return the given `discount.Sale`.

    update:
    Update the given `discount.Sale`..

    delete:
    Delete the given `discount.Sale`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Sale`.
    """

    lookup_field = 'id'
    permit_list_expands = ['products', 'categories', 'collections']
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'name',
        # 'type',
        # 'value',
        # 'start_date',
        # 'end_date',
        'show_countdown',
        # 'categories', # [product.Category]
        # 'collections', # [product.Collection]
        # 'products', # [product.Product]

        # Reverse Fields
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'name',
        # 'type',
        # 'value',
        # 'start_date',
        # 'end_date',
        # 'show_countdown',
        # 'categories', # [product.Category]
        # 'collections', # [product.Collection]
        # 'products', # [product.Product]

        # Reverse Fields
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'name',
        # 'type',
        # 'value',
        # 'start_date',
        # 'end_date',
        # 'show_countdown',
        # 'categories', # [product.Category]
        # 'collections', # [product.Collection]
        # 'products', # [product.Product]

        # Reverse Fields
        # 'translations',
    ]
    # '__all__'

    # def get_object(self):
    #     return super().get_object()

    def get_queryset(self):
        today = timezone.now()
        return self.queryset.active(today)

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
