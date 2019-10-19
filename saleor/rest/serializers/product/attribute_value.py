from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'AttributeValueSerializer',
]

AttributeValue = apps.get_model(*'product.AttributeValue'.split())


class AttributeValueSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.AttributeValue`:

    `**Fields:**`
        01. `attribute`                   : `ForeignKey` [:model:`product.Attribute`]
        02. `id`                          : `AutoField`
        03. `name`                        : `CharField`
        04. `slug`                        : `SlugField`
        05. `sort_order`                  : `PositiveIntegerField`
        06. `value`                       : `CharField`

    `**Reverse Fields:**`
        01. `translations`                : `ForeignKey` [:model:`product.AttributeValueTranslation`]
    """
    class Meta:
        model = AttributeValue
        fields = [
            # Fields
            'attribute',
            'id',
            'name',
            'slug',
            'sort_order',
            'value',

            # Reverse Fields
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
