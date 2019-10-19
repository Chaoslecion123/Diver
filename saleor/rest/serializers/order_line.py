from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from ..fields import MoneyField, TaxedMoneyField
from .product import ProductVariantSerializer


__all__ = [
    'OrderLineSerializer',
]

OrderLine = apps.get_model(*'order.OrderLine'.split())
ProductVariant = apps.get_model(*'product.ProductVariant'.split())


class OrderLineSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`order.OrderLine`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `is_shipping_required`        : `BooleanField`
        03. `order`                       : `ForeignKey` [:model:`order.Order`]
        04. `product_name`                : `CharField`
        05. `product_sku`                 : `CharField`
        06. `quantity`                    : `IntegerField`
        07. `quantity_fulfilled`          : `IntegerField`
        08. `tax_rate`                    : `DecimalField`
        09. `translated_product_name`     : `CharField`
        10. `unit_price`                  : `TaxedMoneyField`
        11. `unit_price_gross`            : `DecimalField`
        12. `unit_price_net`              : `DecimalField`
        13. `variant`                     : `ForeignKey` [:model:`product.ProductVariant`]

    `**Reverse Fields:**`
    """
    unit_price_gross = MoneyField()
    unit_price_net = MoneyField()
    unit_price = TaxedMoneyField()

    variant = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all(),
        allow_null=False,
        required=False
    )

    expandable_fields = {
        'variant': (
            ProductVariantSerializer, {
                'fields': [
                    'id',
                    'sku',
                    'display_name',
                    'image',
                    'weight',
                    'product',
                    'attributes',
                    'price_undiscounted',
                    'price',
                    'price_display',
                ]
            }
        )
    }

    class Meta:
        model = OrderLine
        fields = [
            # Fields
            'id',
            'is_shipping_required',
            'order',
            'product_name',
            'product_sku',
            'quantity',
            'quantity_fulfilled',
            'tax_rate',
            'translated_product_name',
            'unit_price',
            'unit_price_gross',
            'unit_price_net',
            'variant',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
