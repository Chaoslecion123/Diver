from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import ProductTypeSerializer


__all__ = [
    'ProductTypeViewSet',
]

ProductType = apps.get_model(*'product.ProductType'.split())


class ProductTypeViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`product.ProductType`

    `** Actions **`:

    create:
    Create a new `product.ProductType` instance.

    retrieve:
    Return the given `product.ProductType`.

    update:
    Update the given `product.ProductType`..

    delete:
    Delete the given `product.ProductType`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`ProductType`.
    """

    lookup_field = 'id'
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'has_variants',
        # 'id',
        # 'is_shipping_required',
        # 'name',
        # 'tax_rate',
        # 'weight',

        # Reverse Fields
        # 'product_attributes',
        # 'products',
        # 'variant_attributes',
    ]
    search_fields = [
        # Fields
        # 'has_variants',
        # 'id',
        # 'is_shipping_required',
        # 'name',
        # 'tax_rate',
        # 'weight',

        # Reverse Fields
        # 'product_attributes',
        # 'products',
        # 'variant_attributes',
    ]
    ordering_fields = [
        # Fields
        # 'has_variants',
        # 'id',
        # 'is_shipping_required',
        # 'name',
        # 'tax_rate',
        # 'weight',

        # Reverse Fields
        # 'product_attributes',
        # 'products',
        # 'variant_attributes',
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
