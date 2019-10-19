from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ...fields import MoneyField


__all__ = [
    'VoucherSerializer',
]

Voucher = apps.get_model(*'discount.Voucher'.split())


class VoucherSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`discount.Voucher`:

    `**Fields:**`
        01. `apply_once_per_order`        : `BooleanField`
        02. `categories`                  : `ManyToManyField` [:model:`product.Category`]
        03. `code`                        : `CharField`
        04. `collections`                 : `ManyToManyField` [:model:`product.Collection`]
        05. `countries`                   : `CharField`
        06. `discount_value`              : `DecimalField`
        07. `discount_value_type`         : `CharField`
        08. `end_date`                    : `DateField`
        09. `id`                          : `AutoField`
        10. `min_amount_spent`            : `DecimalField`
        11. `name`                        : `CharField`
        12. `products`                    : `ManyToManyField` [:model:`product.Product`]
        13. `start_date`                  : `DateField`
        14. `type`                        : `CharField`
        15. `usage_limit`                 : `PositiveIntegerField`
        16. `used`                        : `PositiveIntegerField`

    `**Reverse Fields:**`
        01. `translations`                : `ForeignKey` [:model:`discount.VoucherTranslation`]
    """
    min_amount_spent = MoneyField()

    class Meta:
        model = Voucher
        fields = [
            # Fields
            'apply_once_per_order',
            'categories',
            'code',
            'collections',
            'countries',
            'discount_value',
            'discount_value_type',
            'end_date',
            'id',
            'min_amount_spent',
            'name',
            'products',
            'start_date',
            'type',
            'usage_limit',
            'used',

            # Reverse Fields
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
