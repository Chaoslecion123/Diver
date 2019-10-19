from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import PaymentSerializer


__all__ = [
    'PaymentViewSet',
]

Payment = apps.get_model(*'payment.Payment'.split())


class PaymentViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`payment.Payment`

    `** Actions **`:

    create:
    Create a new `payment.Payment` instance.

    retrieve:
    Return the given `payment.Payment`.

    update:
    Update the given `payment.Payment`..

    delete:
    Delete the given `payment.Payment`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Payment`.
    """

    lookup_field = 'id'
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'billing_address_1',
        # 'billing_address_2',
        # 'billing_city',
        # 'billing_city_area',
        # 'billing_company_name',
        # 'billing_country_area',
        # 'billing_country_code',
        # 'billing_email',
        # 'billing_first_name',
        # 'billing_last_name',
        # 'billing_postal_code',
        # 'captured_amount',
        # 'cc_brand',
        # 'cc_exp_month',
        # 'cc_exp_year',
        # 'cc_first_digits',
        # 'cc_last_digits',
        # 'charge_status',
        # 'checkout', # [checkout.Checkout]
        # 'created',
        # 'currency',
        # 'customer_ip_address',
        # 'extra_data',
        # 'gateway',
        # 'id',
        # 'is_active',
        # 'modified',
        # 'order', # [order.Order]
        # 'token',
        # 'total',

        # Reverse Fields
        # 'transactions',
    ]
    search_fields = [
        # Fields
        # 'billing_address_1',
        # 'billing_address_2',
        # 'billing_city',
        # 'billing_city_area',
        # 'billing_company_name',
        # 'billing_country_area',
        # 'billing_country_code',
        # 'billing_email',
        # 'billing_first_name',
        # 'billing_last_name',
        # 'billing_postal_code',
        # 'captured_amount',
        # 'cc_brand',
        # 'cc_exp_month',
        # 'cc_exp_year',
        # 'cc_first_digits',
        # 'cc_last_digits',
        # 'charge_status',
        # 'checkout',
        # 'created',
        # 'currency',
        # 'customer_ip_address',
        # 'extra_data',
        # 'gateway',
        # 'id',
        # 'is_active',
        # 'modified',
        # 'order',
        # 'token',
        # 'total',

        # Reverse Fields
        # 'transactions',
    ]
    ordering_fields = [
        # Fields
        # 'billing_address_1',
        # 'billing_address_2',
        # 'billing_city',
        # 'billing_city_area',
        # 'billing_company_name',
        # 'billing_country_area',
        # 'billing_country_code',
        # 'billing_email',
        # 'billing_first_name',
        # 'billing_last_name',
        # 'billing_postal_code',
        # 'captured_amount',
        # 'cc_brand',
        # 'cc_exp_month',
        # 'cc_exp_year',
        # 'cc_first_digits',
        # 'cc_last_digits',
        # 'charge_status',
        # 'checkout',
        # 'created',
        # 'currency',
        # 'customer_ip_address',
        # 'extra_data',
        # 'gateway',
        # 'id',
        # 'is_active',
        # 'modified',
        # 'order',
        # 'token',
        # 'total',

        # Reverse Fields
        # 'transactions',
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
