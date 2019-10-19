from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import VoucherSerializer


__all__ = [
    'VoucherViewSet',
]

Voucher = apps.get_model(*'discount.Voucher'.split())


class VoucherViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`discount.Voucher`

    `** Actions **`:

    create:
    Create a new `discount.Voucher` instance.

    retrieve:
    Return the given `discount.Voucher`.

    update:
    Update the given `discount.Voucher`..

    delete:
    Delete the given `discount.Voucher`, and return an empty response 
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Voucher`.
    """

    lookup_field = 'id'
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'apply_once_per_order',
        # 'categories', # [product.Category]
        # 'code',
        # 'collections', # [product.Collection]
        # 'countries',
        # 'discount_value',
        # 'discount_value_type',
        # 'end_date',
        # 'id',
        # 'min_amount_spent',
        # 'name',
        # 'products', # [product.Product]
        # 'start_date',
        # 'type',
        # 'usage_limit',
        # 'used',

        # Reverse Fields
        # 'translations',
    ]
    search_fields = [
        # Fields
        # 'apply_once_per_order',
        # 'categories',
        # 'code',
        # 'collections',
        # 'countries',
        # 'discount_value',
        # 'discount_value_type',
        # 'end_date',
        # 'id',
        # 'min_amount_spent',
        # 'name',
        # 'products',
        # 'start_date',
        # 'type',
        # 'usage_limit',
        # 'used',

        # Reverse Fields
        # 'translations',
    ]
    ordering_fields = [
        # Fields
        # 'apply_once_per_order',
        # 'categories',
        # 'code',
        # 'collections',
        # 'countries',
        # 'discount_value',
        # 'discount_value_type',
        # 'end_date',
        # 'id',
        # 'min_amount_spent',
        # 'name',
        # 'products',
        # 'start_date',
        # 'type',
        # 'usage_limit',
        # 'used',

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
