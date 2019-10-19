from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from .city import CitySerializer

__all__ = [
    'CityAreaSerializer',
]

City = apps.get_model(*'world.City'.split())
CityArea = apps.get_model(*'world.CityArea'.split())


class CityAreaSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`world.CityArea`:

    `**Fields:**`
        01. `city`                        : `ForeignKey` [:model:`world.City`]
        02. `id`                          : `AutoField`
        03. `name`                        : `CharField`

    `**Reverse Fields:**`
    """
    city = CitySerializer()

    class Meta:
        model = CityArea
        fields = [
            # Fields
            'city',
            'id',
            'name',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
