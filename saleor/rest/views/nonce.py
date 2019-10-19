from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import NonceSerializer


__all__ = [
    'NonceViewSet',
]

Nonce = apps.get_model(*'social_django.Nonce'.split())


class NonceViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`social_django.Nonce`

    `** Actions **`:

    create:
    Create a new `social_django.Nonce` instance.

    retrieve:
    Return the given `social_django.Nonce`.

    update:
    Update the given `social_django.Nonce`..

    delete:
    Delete the given `social_django.Nonce`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Nonce`.
    """

    lookup_field = 'id'
    queryset = Nonce.objects.all()
    serializer_class = NonceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'salt',
        # 'server_url',
        # 'timestamp',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'salt',
        # 'server_url',
        # 'timestamp',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'salt',
        # 'server_url',
        # 'timestamp',

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
