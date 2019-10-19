from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'RateTypesSerializer',
]

RateTypes = apps.get_model(*'django_prices_vatlayer.RateTypes'.split())


class RateTypesSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`django_prices_vatlayer.RateTypes`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `types`                       : `TextField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = RateTypes
        fields = [
            # Fields
            'id',
            'types',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
