from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import SessionSerializer


__all__ = [
    'SessionViewSet',
]

Session = apps.get_model(*'sessions.Session'.split())


class SessionViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`sessions.Session`

    `** Actions **`:

    create:
    Create a new `sessions.Session` instance.

    retrieve:
    Return the given `sessions.Session`.

    update:
    Update the given `sessions.Session`..

    delete:
    Delete the given `sessions.Session`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Session`.
    """

    lookup_field = 'id'
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'expire_date',
        # 'session_data',
        # 'session_key',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'expire_date',
        # 'session_data',
        # 'session_key',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'expire_date',
        # 'session_data',
        # 'session_key',

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
