from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import TransactionSerializer


__all__ = [
    'TransactionViewSet',
]

Transaction = apps.get_model(*'payment.Transaction'.split())


class TransactionViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`payment.Transaction`

    `** Actions **`:

    create:
    Create a new `payment.Transaction` instance.

    retrieve:
    Return the given `payment.Transaction`.

    update:
    Update the given `payment.Transaction`..

    delete:
    Delete the given `payment.Transaction`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Transaction`.
    """

    lookup_field = 'id'
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'amount',
        # 'created',
        # 'currency',
        # 'error',
        # 'gateway_response',
        # 'id',
        # 'is_success',
        # 'kind',
        # 'payment', # [payment.Payment]
        # 'token',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'amount',
        # 'created',
        # 'currency',
        # 'error',
        # 'gateway_response',
        # 'id',
        # 'is_success',
        # 'kind',
        # 'payment',
        # 'token',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'amount',
        # 'created',
        # 'currency',
        # 'error',
        # 'gateway_response',
        # 'id',
        # 'is_success',
        # 'kind',
        # 'payment',
        # 'token',

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
