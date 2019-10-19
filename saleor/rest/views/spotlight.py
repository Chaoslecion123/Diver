from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import SpotlightSerializer


__all__ = [
    'SpotlightViewSet',
]

#Spotlight = apps.get_model(*'homepage.Spotlight'.split())
Spotlight = apps.get_model(*'widget.Spotlight'.split())


class SpotlightViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`homepage.Spotlight`

    `** Actions **`:

    create:
    Create a new `homepage.Spotlight` instance.

    retrieve:
    Return the given `homepage.Spotlight`.

    update:
    Update the given `homepage.Spotlight`..

    delete:
    Delete the given `homepage.Spotlight`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Spotlight`.
    """

    lookup_field = 'id'
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'scene', # [homepage.Slider]
        # 'variant', # [product.ProductVariant]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'scene',
        # 'variant',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'scene',
        # 'variant',

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
