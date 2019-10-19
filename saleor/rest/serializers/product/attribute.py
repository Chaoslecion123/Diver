from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .attribute_value import AttributeValueSerializer


__all__ = [
    'AttributeSerializer',
]

Attribute = apps.get_model(*'product.Attribute'.split())
AttributeValue = apps.get_model(*'product.AttributeValue'.split())


class AttributeSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.Attribute`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `name`                        : `CharField`
        03. `product_type`                : `ForeignKey` [:model:`product.ProductType`]
        04. `product_variant_type`        : `ForeignKey` [:model:`product.ProductType`]
        05. `slug`                        : `SlugField`

    `**Reverse Fields:**`
        01. `translations`                : `ForeignKey` [:model:`product.AttributeTranslation`]
        02. `values`                      : `ForeignKey` [:model:`product.AttributeValue`]
    """
    values = AttributeValueSerializer(
        fields=[
            "id",
            "name",
            "slug",
            "sort_order",
        ],
        allow_null=True,
        required=False,
        many=True,
    )
    # values = serializers.PrimaryKeyRelatedField(
    #     queryset=AttributeValue.objects.all(),
    #     allow_null=False,
    #     required=False,
    #     many=True,
    # )

    # expandable_fields = {
    #     'values': (
    #         AttributeValueSerializer, {
    #             'fields': [
    #                 'id',
    #                 'name',
    #                 'slug',
    #                 'sort_order',
    #             ],
    #             'many': True
    #         }
    #     )
    # }

    class Meta:
        model = Attribute
        fields = [
            # Fields
            'id',
            'name',
            'product_type',
            'product_variant_type',
            'slug',

            # Reverse Fields
            # 'translations',
            'values',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
