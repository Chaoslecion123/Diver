from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import AuthorizationKeySerializer


__all__ = [
    'AuthorizationKeyViewSet',
]

AuthorizationKey = apps.get_model(*'site.AuthorizationKey'.split())


class AuthorizationKeyViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`site.AuthorizationKey`

    `** Actions **`:

    create:
    Create a new `site.AuthorizationKey` instance.

    retrieve:
    Return the given `site.AuthorizationKey`.

    update:
    Update the given `site.AuthorizationKey`..

    delete:
    Delete the given `site.AuthorizationKey`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`AuthorizationKey`.
    """

    lookup_field = 'id'
    queryset = AuthorizationKey.objects.all()
    serializer_class = AuthorizationKeySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'key',
        # 'name',
        # 'password',
        # 'site_settings', # [site.SiteSettings]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'key',
        # 'name',
        # 'password',
        # 'site_settings',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'key',
        # 'name',
        # 'password',
        # 'site_settings',

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
