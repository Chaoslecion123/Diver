from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import SiteSettingsSerializer


__all__ = [
    'SiteSettingsViewSet',
]

SiteSettings = apps.get_model(*'site.SiteSettings'.split())


class SiteSettingsViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`site.SiteSettings`

    `** Actions **`:

    create:
    Create a new `site.SiteSettings` instance.

    retrieve:
    Return the given `site.SiteSettings`.

    update:
    Update the given `site.SiteSettings`..

    delete:
    Delete the given `site.SiteSettings`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`SiteSettings`.
    """

    lookup_field = 'id'
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'bottom_menu', # [menu.Menu]
        # 'charge_taxes_on_shipping',
        # 'default_weight_unit',
        # 'description',
        # 'display_gross_prices',
        # 'header_text',
        # 'homepage_collection', # [product.Collection]
        # 'id',
        # 'include_taxes_in_prices',
        # 'site', # [sites.Site]
        # 'top_menu', # [menu.Menu]
        # 'track_inventory_by_default',

        # Reverse Fields
        # 'authorizationkey',
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'bottom_menu',
        # 'charge_taxes_on_shipping',
        # 'default_weight_unit',
        # 'description',
        # 'display_gross_prices',
        # 'header_text',
        # 'homepage_collection',
        # 'id',
        # 'include_taxes_in_prices',
        # 'site',
        # 'top_menu',
        # 'track_inventory_by_default',

        # Reverse Fields
        # 'authorizationkey',
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'bottom_menu',
        # 'charge_taxes_on_shipping',
        # 'default_weight_unit',
        # 'description',
        # 'display_gross_prices',
        # 'header_text',
        # 'homepage_collection',
        # 'id',
        # 'include_taxes_in_prices',
        # 'site',
        # 'top_menu',
        # 'track_inventory_by_default',

        # Reverse Fields
        # 'authorizationkey',
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
