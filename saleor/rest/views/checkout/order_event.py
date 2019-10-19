from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import OrderEventSerializer


__all__ = [
    'OrderEventViewSet',
]

OrderEvent = apps.get_model(*'order.OrderEvent'.split())


class OrderEventViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.OrderEvent`

    `** Actions **`:

    create:
    Create a new `order.OrderEvent` instance.

    retrieve:
    Return the given `order.OrderEvent`.

    update:
    Update the given `order.OrderEvent`..

    delete:
    Delete the given `order.OrderEvent`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`OrderEvent`.
    """

    lookup_field = 'id'
    queryset = OrderEvent.objects.all()
    serializer_class = OrderEventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'date',
        # 'id',
        # 'order', # [order.Order]
        # 'parameters',
        # 'type',
        # 'user', # [account.User]

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'date',
        # 'id',
        # 'order',
        # 'parameters',
        # 'type',
        # 'user',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'date',
        # 'id',
        # 'order',
        # 'parameters',
        # 'type',
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
