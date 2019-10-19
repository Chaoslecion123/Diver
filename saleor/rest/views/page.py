from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import PageSerializer


__all__ = [
    'PageViewSet',
]

Page = apps.get_model(*'page.Page'.split())


class PageViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`page.Page`

    `** Actions **`:

    create:
    Create a new `page.Page` instance.

    retrieve:
    Return the given `page.Page`.

    update:
    Update the given `page.Page`..

    delete:
    Delete the given `page.Page`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Page`.
    """

    lookup_field = 'slug'
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'available_on',
        # 'content',
        # 'created',
        # 'id',
        # 'is_visible',
        # 'seo_description',
        # 'seo_title',
        # 'slug',
        # 'title',

        # Reverse Fields
        # 'menuitem',
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'available_on',
        # 'content',
        # 'created',
        # 'id',
        # 'is_visible',
        # 'seo_description',
        # 'seo_title',
        # 'slug',
        # 'title',

        # Reverse Fields
        # 'menuitem',
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'available_on',
        # 'content',
        # 'created',
        # 'id',
        # 'is_visible',
        # 'seo_description',
        # 'seo_title',
        # 'slug',
        # 'title',

        # Reverse Fields
        # 'menuitem',
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
