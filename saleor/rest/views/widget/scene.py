from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import SceneSerializer
from ...permissions import ReadOnly


__all__ = [
    'SceneViewSet',
]

Scene = apps.get_model(*'widget.Scene'.split())


class SceneViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`homepage.Scene`

    `** Actions **`:

    create:
    Create a new `homepage.Scene` instance.

    retrieve:
    Return the given `homepage.Scene`.

    update:
    Update the given `homepage.Scene`..

    delete:
    Delete the given `homepage.Scene`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Scene`.
    """
    permission_classes = [ReadOnly]
    lookup_field = 'id'
    permit_list_expands = ['spotlights']

    queryset = Scene.objects.all()
    serializer_class = SceneSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'image',
        # 'name',
        # 'ppoi',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'image',
        # 'name',
        # 'ppoi',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'image',
        # 'name',
        # 'ppoi',

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
