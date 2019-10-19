from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import ContentTypeSerializer


__all__ = [
    'ContentTypeViewSet',
]

ContentType = apps.get_model(*'contenttypes.ContentType'.split())


class ContentTypeViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`contenttypes.ContentType`

    `** Actions **`:

    create:
    Create a new `contenttypes.ContentType` instance.

    retrieve:
    Return the given `contenttypes.ContentType`.

    update:
    Update the given `contenttypes.ContentType`..

    delete:
    Delete the given `contenttypes.ContentType`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`ContentType`.
    """

    lookup_field = 'id'
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'app_label',
        # 'id',
        # 'model',

        # Reverse Fields
        # 'logentry',
        # 'permission',
    ]
    search_fields = [
        # Fields
        # 'app_label',
        # 'id',
        # 'model',

        # Reverse Fields
        # 'logentry',
        # 'permission',
    ]
    ordering_fields = [
        # Fields
        # 'app_label',
        # 'id',
        # 'model',

        # Reverse Fields
        # 'logentry',
        # 'permission',
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
