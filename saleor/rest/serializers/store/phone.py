from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'PhoneSerializer',
]

Phone = apps.get_model(*'store.Phone'.split())


class PhoneSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`store.Phone`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `number`                      : `CharField`
        03. `physical_store`              : `ForeignKey` [:model:`store.PhysicalStore`]

    `**Reverse Fields:**`
    """

    class Meta:
        model = Phone
        fields = [
            # Fields
            'id',
            'number',
            'physical_store',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
