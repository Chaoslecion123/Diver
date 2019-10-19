from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CodeSerializer


__all__ = [
    'CodeViewSet',
]

Code = apps.get_model(*'social_django.Code'.split())


class CodeViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`social_django.Code`

    `** Actions **`:

    create:
    Create a new `social_django.Code` instance.

    retrieve:
    Return the given `social_django.Code`.

    update:
    Update the given `social_django.Code`..

    delete:
    Delete the given `social_django.Code`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Code`.
    """

    lookup_field = 'id'
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'code',
        # 'email',
        # 'id',
        # 'timestamp',
        # 'verified',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'code',
        # 'email',
        # 'id',
        # 'timestamp',
        # 'verified',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'code',
        # 'email',
        # 'id',
        # 'timestamp',
        # 'verified',

        # Reverse Fields
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
