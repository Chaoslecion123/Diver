from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField


__all__ = [
    'CountryAreaSerializer',
]

CountryArea = apps.get_model(*'world.CountryArea'.split())


class CountryAreaSerializer(CountryFieldMixin, FlexFieldsModelSerializer):
    """Serializer for :model:`world.CountryArea`:

    `**Fields:**`
        01. `country`                     : `CharField`
        02. `id`                          : `AutoField`
        03. `name`                        : `CharField`

    `**Reverse Fields:**`
        01. `city`                        : `ForeignKey` [:model:`world.City`]
    """
    country = CountryField(country_dict=True)

    class Meta:
        model = CountryArea
        fields = [
            # Fields
            'country',
            'id',
            'name',

            # Reverse Fields
            # 'city',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
