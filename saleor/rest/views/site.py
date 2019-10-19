from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import SiteSerializer


__all__ = [
    'SiteViewSet',
]

Site = apps.get_model(*'sites.Site'.split())


class SiteViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`sites.Site`

    `** Actions **`:

    create:
    Create a new `sites.Site` instance.

    retrieve:
    Return the given `sites.Site`.

    update:
    Update the given `sites.Site`..

    delete:
    Delete the given `sites.Site`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Site`.
    """

    lookup_field = 'id'
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'domain',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'settings',
    ]
    search_fields = [
        # Fields
        # 'domain',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'settings',
    ]
    ordering_fields = [
        # Fields
        # 'domain',
        # 'id',
        # 'name',

        # Reverse Fields
        # 'settings',
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
