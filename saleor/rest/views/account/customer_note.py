from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import CustomerNoteSerializer

from ...permissions import ReadOnly


__all__ = [
    'CustomerNoteViewSet',
]

CustomerNote = apps.get_model(*'account.CustomerNote'.split())


class CustomerNoteViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`account.CustomerNote`

    `** Actions **`:

    create:
    Create a new `account.CustomerNote` instance.

    retrieve:
    Return the given `account.CustomerNote`.

    update:
    Update the given `account.CustomerNote`..

    delete:
    Delete the given `account.CustomerNote`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`CustomerNote`.
    """
    permission_classes = [ReadOnly]
    lookup_field = 'id'
    queryset = CustomerNote.objects.all()
    serializer_class = CustomerNoteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'content',
        # 'customer', # [account.User]
        # 'date',
        # 'id',
        # 'is_public',
        # 'user', # [account.User]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'content',
        # 'customer',
        # 'date',
        # 'id',
        # 'is_public',
        # 'user',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'content',
        # 'customer',
        # 'date',
        # 'id',
        # 'is_public',
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
