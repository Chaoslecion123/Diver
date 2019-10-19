from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from ..product import ProductVariantSerializer


__all__ = [
    'CheckoutLineSerializer',
]

CheckoutLine = apps.get_model(*'checkout.CheckoutLine'.split())
ProductVariant = apps.get_model(*'product.ProductVariant'.split())


class CheckoutLineSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`checkout.CheckoutLine`:

    `**Fields:**`
        01. `checkout`                        : `ForeignKey` [:model:`checkout.Checkout`]
        02. `data`                        : `JSONField`
        03. `id`                          : `AutoField`
        04. `quantity`                    : `PositiveIntegerField`
        05. `variant`                     : `ForeignKey` [:model:`product.ProductVariant`]

    `**Reverse Fields:**`
    """
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
        model = CheckoutLine
        fields = [
            # Fields
            'checkout',
            'data',
            'id',
            'quantity',
            'variant',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
