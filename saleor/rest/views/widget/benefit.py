from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import BenefitSerializer
from ...permissions import ReadOnly


__all__ = [
    'BenefitViewSet',
]

Benefit = apps.get_model(*'widget.Benefit'.split())


class BenefitViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`widget.Benefit`

    `** Actions **`:

    create:
    Create a new `widget.Benefit` instance.

    retrieve:
    Return the given `widget.Benefit`.

    update:
    Update the given `widget.Benefit`..

    delete:
    Delete the given `widget.Benefit`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Benefit`.
    """
    permission_classes = (ReadOnly, )
    lookup_field = 'id'
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'image',
        # 'is_active',
        # 'name',
        # 'text',

        # Reverse Fields
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'image',
        # 'is_active',
        # 'name',
        # 'text',

        # Reverse Fields
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'image',
        # 'is_active',
        # 'name',
        # 'text',

        # Reverse Fields
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
