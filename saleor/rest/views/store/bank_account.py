from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import BankAccountSerializer


__all__ = [
    'BankAccountViewSet',
]

BankAccount = apps.get_model(*'store.BankAccount'.split())


class BankAccountViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`store.BankAccount`

    `** Actions **`:

    create:
    Create a new `store.BankAccount` instance.

    retrieve:
    Return the given `store.BankAccount`.

    update:
    Update the given `store.BankAccount`..

    delete:
    Delete the given `store.BankAccount`, and return an empty response 
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`BankAccount`.
    """

    lookup_field = 'id'
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'number',
        # 'provider',
        # 'site_settings', # [site.SiteSettings]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'number',
        # 'provider',
        # 'site_settings',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'number',
        # 'provider',
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
