from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from saleor.rest.serializers import ProductVariantSerializer


__all__ = [
    'ProductVariantViewSet',
]

ProductVariant = apps.get_model(*'product.ProductVariant'.split())


class ProductVariantViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`product.ProductVariant`

    `** Actions **`:

    create:
    Create a new `product.ProductVariant` instance.

    retrieve:
    Return the given `product.ProductVariant`.

    update:
    Update the given `product.ProductVariant`..

    delete:
    Delete the given `product.ProductVariant`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`ProductVariant`.
    """

    lookup_field = 'id'
    permit_list_expands = ['image']
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'attributes',
        # 'cost_price',
        # 'id',
        # 'images', # [product.ProductImage]
        # 'name',
        # 'price_override',
        # 'product', # [product.Product]
        # 'quantity',
        # 'quantity_allocated',
        # 'sku',
        # 'track_inventory',
        # 'weight',

        # Reverse Fields
        # 'order_lines',
        # 'product_spotlights',
        # 'translations',
        # 'variant_images',
    ]
    search_fields = [
        # Fields
        # 'attributes',
        # 'cost_price',
        # 'id',
        # 'images',
        # 'name',
        # 'price_override',
        # 'product',
        # 'quantity',
        # 'quantity_allocated',
        # 'sku',
        # 'track_inventory',
        # 'weight',

        # Reverse Fields
        # 'order_lines',
        # 'product_spotlights',
        # 'translations',
        # 'variant_images',
    ]
    ordering_fields = [
        # Fields
        # 'attributes',
        # 'cost_price',
        # 'id',
        # 'images',
        # 'name',
        # 'price_override',
        # 'product',
        # 'quantity',
        # 'quantity_allocated',
        # 'sku',
        # 'track_inventory',
        # 'weight',

        # Reverse Fields
        # 'order_lines',
        # 'product_spotlights',
        # 'translations',
        # 'variant_images',
    ]
    # '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'slides'):
            queryset = queryset.prefetch_related('slides')
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
