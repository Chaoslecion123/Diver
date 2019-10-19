from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import ProductImageSerializer


__all__ = [
    'ProductImageViewSet',
]

ProductImage = apps.get_model(*'product.ProductImage'.split())


class ProductImageViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`product.ProductImage`

    `** Actions **`:

    create:
    Create a new `product.ProductImage` instance.

    retrieve:
    Return the given `product.ProductImage`.

    update:
    Update the given `product.ProductImage`..

    delete:
    Delete the given `product.ProductImage`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`ProductImage`.
    """

    lookup_field = 'id'
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'alt',
        # 'id',
        # 'image',
        # 'ppoi',
        # 'product', # [product.Product]
        # 'sort_order',

        # Reverse Fields
        # 'productvariant',
        # 'variant_images',
    ]
    search_fields = [
        # Fields
        # 'alt',
        # 'id',
        # 'image',
        # 'ppoi',
        # 'product',
        # 'sort_order',

        # Reverse Fields
        # 'productvariant',
        # 'variant_images',
    ]
    ordering_fields = [
        # Fields
        # 'alt',
        # 'id',
        # 'image',
        # 'ppoi',
        # 'product',
        # 'sort_order',

        # Reverse Fields
        # 'productvariant',
        # 'variant_images',
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
