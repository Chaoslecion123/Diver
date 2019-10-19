from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'VATSerializer',
]

VAT = apps.get_model(*'django_prices_vatlayer.VAT'.split())


class VATSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`django_prices_vatlayer.VAT`:

    `**Fields:**`
        01. `country_code`                : `CharField`
        02. `data`                        : `TextField`
        03. `id`                          : `AutoField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = VAT
        fields = [
            # Fields
            'country_code',
            'data',
            'id',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
