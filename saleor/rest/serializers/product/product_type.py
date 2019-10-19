from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ...fields import MeasurementField



__all__ = [
    'ProductTypeSerializer',
]

ProductType = apps.get_model(*'product.ProductType'.split())


class ProductTypeSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.ProductType`:

    `**Fields:**`
        01. `has_variants`                : `BooleanField`
        02. `id`                          : `AutoField`
        03. `is_shipping_required`        : `BooleanField`
        04. `name`                        : `CharField`
        05. `tax_rate`                    : `CharField`
        06. `weight`                      : `FloatField`

    `**Reverse Fields:**`
        01. `product_attributes`          : `ForeignKey` [:model:`product.Attribute`]
        02. `products`                    : `ForeignKey` [:model:`product.Product`]
        03. `variant_attributes`          : `ForeignKey` [:model:`product.Attribute`]
    """
    weight = MeasurementField()

    class Meta:
        model = ProductType
        fields = [
            # Fields
            'has_variants',
            'id',
            'is_shipping_required',
            'name',
            'tax_rate',
            'weight',

            # Reverse Fields
            # 'product_attributes',
            # 'products',
            # 'variant_attributes',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
