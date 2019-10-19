from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CategorySerializer
from ...permissions import ReadOnly

__all__ = [
    'CategoryViewSet',
]

Category = apps.get_model(*'product.Category'.split())


class CategoryViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`product.Category`

    `** Actions **`:

    create:
    Create a new `product.Category` instance.

    retrieve:
    Return the given `product.Category`.

    update:
    Update the given `product.Category`..

    delete:
    Delete the given `product.Category`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Category`.
    """

    permission_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'background_image',
        # 'background_image_alt',
        # 'description',
        # 'id',
        # 'level',
        # 'lft',
        # 'name',
        'parent',  # [product.Category]
        # 'rght',
        # 'seo_description',
        # 'seo_title',
        # 'slug',
        # 'tree_id',

        # Reverse Fields
        # 'children',
        # 'menuitem',
        # 'products',
        # 'sale',
        # 'translations',
        # 'voucher',
    ]
    search_fields = [
        # Fields
        # 'background_image',
        # 'background_image_alt',
        # 'description',
        # 'id',
        # 'level',
        # 'lft',
        # 'name',
        # 'parent',
        # 'rght',
        # 'seo_description',
        # 'seo_title',
        # 'slug',
        # 'tree_id',

        # Reverse Fields
        # 'children',
        # 'menuitem',
        # 'products',
        # 'sale',
        # 'translations',
        # 'voucher',
    ]
    ordering_fields = [
        # Fields
        # 'background_image',
        # 'background_image_alt',
        # 'description',
        # 'id',
        # 'level',
        # 'lft',
        # 'name',
        # 'parent',
        # 'rght',
        # 'seo_description',
        # 'seo_title',
        # 'slug',
        # 'tree_id',

        # Reverse Fields
        # 'children',
        # 'menuitem',
        # 'products',
        # 'sale',
        # 'translations',
        # 'voucher',
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
