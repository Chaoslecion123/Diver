from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'PaymentSerializer',
]

Payment = apps.get_model(*'payment.Payment'.split())


class PaymentSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`payment.Payment`:

    `**Fields:**`
        01. `billing_address_1`           : `CharField`
        02. `billing_address_2`           : `CharField`
        03. `billing_city`                : `CharField`
        04. `billing_city_area`           : `CharField`
        05. `billing_company_name`        : `CharField`
        06. `billing_country_area`        : `CharField`
        07. `billing_country_code`        : `CharField`
        08. `billing_email`               : `CharField`
        09. `billing_first_name`          : `CharField`
        10. `billing_last_name`           : `CharField`
        11. `billing_postal_code`         : `CharField`
        12. `captured_amount`             : `DecimalField`
        13. `cc_brand`                    : `CharField`
        14. `cc_exp_month`                : `PositiveIntegerField`
        15. `cc_exp_year`                 : `PositiveIntegerField`
        16. `cc_first_digits`             : `CharField`
        17. `cc_last_digits`              : `CharField`
        18. `charge_status`               : `CharField`
        19. `checkout`                    : `ForeignKey` [:model:`checkout.Checkout`]
        20. `created`                     : `DateTimeField`
        21. `currency`                    : `CharField`
        22. `customer_ip_address`         : `GenericIPAddressField`
        23. `extra_data`                  : `TextField`
        24. `gateway`                     : `CharField`
        25. `id`                          : `AutoField`
        26. `is_active`                   : `BooleanField`
        27. `modified`                    : `DateTimeField`
        28. `order`                       : `ForeignKey` [:model:`order.Order`]
        29. `token`                       : `CharField`
        30. `total`                       : `DecimalField`

    `**Reverse Fields:**`
        01. `transactions`                : `ForeignKey` [:model:`payment.Transaction`]
    """
    class Meta:
        model = Payment
        fields = [
            # Fields
            'billing_address_1',
            'billing_address_2',
            'billing_city',
            'billing_city_area',
            'billing_company_name',
            'billing_country_area',
            'billing_country_code',
            'billing_email',
            'billing_first_name',
            'billing_last_name',
            'billing_postal_code',
            'captured_amount',
            'cc_brand',
            'cc_exp_month',
            'cc_exp_year',
            'cc_first_digits',
            'cc_last_digits',
            'charge_status',
            'checkout',
            'created',
            'currency',
            'customer_ip_address',
            'extra_data',
            'gateway',
            'id',
            'is_active',
            'modified',
            'order',
            'token',
            'total',

            # Reverse Fields
            # 'transactions',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
