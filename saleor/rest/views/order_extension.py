from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import OrderExtensionSerializer


__all__ = [
    'OrderExtensionViewSet',
]

OrderExtension = apps.get_model(*'order.OrderExtension'.split())


class OrderExtensionViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`order.OrderExtension`

    `** Actions **`:

    create:
    Create a new `order.OrderExtension` instance.

    retrieve:
    Return the given `order.OrderExtension`.

    update:
    Update the given `order.OrderExtension`..

    delete:
    Delete the given `order.OrderExtension`, and return an empty response 
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`OrderExtension`.
    """

    lookup_field = 'id'
    queryset = OrderExtension.objects.all()
    serializer_class = OrderExtensionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'id',
        # 'order', # [order.Order]
        # 'payment_proof',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'id',
        # 'order',
        # 'payment_proof',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'id',
        # 'order',
        # 'payment_proof',

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
