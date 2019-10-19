from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CollectionSerializer
from ...permissions import ReadOnly

__all__ = [
    'CollectionViewSet',
]

Collection = apps.get_model(*'product.Collection'.split())


class CollectionViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`product.Collection`

    `** Actions **`:

    create:
    Create a new `product.Collection` instance.

    retrieve:
    Return the given `product.Collection`.

    update:
    Update the given `product.Collection`..

    delete:
    Delete the given `product.Collection`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Collection`.
    """

    permission_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'background_image',
        # 'background_image_alt',
        # 'description',
        # 'id',
        # 'is_published',
        # 'name',
        # 'products', # [product.Product]
        # 'published_date',
        # 'seo_description',
        # 'seo_title',
        # 'slug',

        # Reverse Fields
        # 'menuitem',
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
        # 'is_published',
        # 'name',
        # 'products',
        # 'published_date',
        # 'seo_description',
        # 'seo_title',
        # 'slug',

        # Reverse Fields
        # 'menuitem',
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
        # 'is_published',
        # 'name',
        # 'products',
        # 'published_date',
        # 'seo_description',
        # 'seo_title',
        # 'slug',

        # Reverse Fields
        # 'menuitem',
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
