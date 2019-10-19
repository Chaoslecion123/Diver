from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'ConversionRateSerializer',
]

ConversionRate = apps.get_model(
    *'django_prices_openexchangerates.ConversionRate'.split())


class ConversionRateSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`django_prices_openexchangerates.ConversionRate`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `modified_at`                 : `DateTimeField`
        03. `rate`                        : `DecimalField`
        04. `to_currency`                 : `CharField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = ConversionRate
        fields = [
            # Fields
            'id',
            'modified_at',
            'rate',
            'to_currency',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
