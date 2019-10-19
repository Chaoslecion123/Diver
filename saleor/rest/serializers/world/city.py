from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from .country_area import CountryAreaSerializer

__all__ = [
    'CitySerializer',
]

City = apps.get_model(*'world.City'.split())
CountryArea = apps.get_model(*'world.CountryArea'.split())


class CitySerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`world.City`:

    `**Fields:**`
        01. `country_area`                : `ForeignKey` [:model:`world.CountryArea`]
        02. `id`                          : `AutoField`
        03. `name`                        : `CharField`

    `**Reverse Fields:**`
        01. `city_area`                   : `ForeignKey` [:model:`world.CityArea`]
    """
    country_area = CountryAreaSerializer()

    class Meta:
        model = City
        fields = [
            # Fields
            'country_area',
            'id',
            'name',

            # Reverse Fields
            # 'city_area',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
