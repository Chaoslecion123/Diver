from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import BrandSerializer
from ...permissions import ReadOnly
<<<<<<< HEAD

=======
>>>>>>> 20169ee7ed6f21d0604c8d15b2a20a4e56f19385

__all__ = [
    'BrandViewSet',
]

Brand = apps.get_model(*'brand.Brand'.split())


class BrandViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`brand.Brand`

    `** Actions **`:

    create:
    Create a new `brand.Brand` instance.

    retrieve:
    Return the given `brand.Brand`.

    update:
    Update the given `brand.Brand`..

    delete:
    Delete the given `brand.Brand`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Brand`.
    """
<<<<<<< HEAD
    permission_classes = [ReadOnly]
=======
    permission_classes = (ReadOnly, )
>>>>>>> 20169ee7ed6f21d0604c8d15b2a20a4e56f19385
    lookup_field = 'id'
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        # OrderingFilter,
    ]
    filter_fields = [
        # Fields
        # 'color',
        # 'id',
        # 'image',
        'is_featured',
        # 'name',
        # 'products', # [product.Product]
        # 'seo_description',
        # 'seo_title',
        # 'slug',

        # Reverse Fields
        # 'slider',
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'color',
        # 'id',
        # 'image',
        # 'is_featured',
        'name',
        # 'products',
        # 'seo_description',
        # 'seo_title',
        # 'slug',

        # Reverse Fields
        # 'slider',
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'color',
        # 'id',
        # 'image',
        # 'is_featured',
        # 'name',
        # 'products',
        # 'seo_description',
        # 'seo_title',
        # 'slug',

        # Reverse Fields
        # 'slider',
        # 'translations',
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

    @action(
        methods=['get'],
        detail=False,
        name='featured',
        url_path='featured',
        url_name='featured'
    )
    def add_to_checkout(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(is_featured=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
