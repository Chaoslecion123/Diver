from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import TokenSerializer


__all__ = [
    'TokenViewSet',
]

Token = apps.get_model(*'authtoken.Token'.split())


class TokenViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`authtoken.Token`

    `** Actions **`:

    create:
    Create a new `authtoken.Token` instance.

    retrieve:
    Return the given `authtoken.Token`.

    update:
    Update the given `authtoken.Token`..

    delete:
    Delete the given `authtoken.Token`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Token`.
    """

    lookup_field = 'id'
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'created',
        # 'key',
        # 'user', # [account.User]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'created',
        # 'key',
        # 'user',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'created',
        # 'key',
        # 'user',

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
