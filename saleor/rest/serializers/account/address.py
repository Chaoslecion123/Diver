from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from ...fields import SERIALIZER_FIELD_MAPPING
from ..world import CityAreaSerializer


__all__ = [
    'AddressSerializer',
]

Address = apps.get_model(*'account.Address'.split())


class AddressSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.Address`:

    `**Fields:**`
        01. `city`                        : `CharField`
        02. `city_area`                   : `CharField`
        03. `company_name`                : `CharField`
        04. `country`                     : `CharField`
        05. `country_area`                : `CharField`
        06. `first_name`                  : `CharField`
        07. `id`                          : `AutoField`
        08. `last_name`                   : `CharField`
        09. `phone`                       : `CharField`
        10. `postal_code`                 : `CharField`
        11. `street_address_1`            : `CharField`
        12. `street_address_2`            : `CharField`
        13. `country_area_object`         : `ForeignKey` [:model:`world.CountryArea`]
        14. `city_object`                 : `ForeignKey` [:model:`world.City`]
        15. `city_area_object`            : `ForeignKey` [:model:`world.CityArea`]
    `**Reverse Fields:**`
        01. `user_addresses`              : `ManyToManyField` [:model:`account.User`]
    """
    serializer_field_mapping = SERIALIZER_FIELD_MAPPING
    # city_area_object = CityAreaSerializer()
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = [
            # Fields
            'city',
            'city_area',
            'company_name',
            'country',
            'country_area',
            'first_name',
            'id',
            'last_name',
            'phone',
            'postal_code',
            'street_address_1',
            'street_address_2',
            'position',
            'location_type',
            'country_area_object',
            'city_object',
            'city_area_object',
            # Reverse user_addressesFields
            # 'user_addresses',

            # oTHER FIELDS
            'country_name',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_country_name(self, obj):
        return obj.country.name
