from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'ShippingZoneSerializer',
]

ShippingZone = apps.get_model(*'shipping.ShippingZone'.split())


class ShippingZoneSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`shipping.ShippingZone`:

    `**Fields:**`
        01. `countries`                   : `CharField`
        02. `default`                     : `BooleanField`
        03. `id`                          : `AutoField`
        04. `name`                        : `CharField`

    `**Reverse Fields:**`
        01. `shipping_methods`            : `ForeignKey` [:model:`shipping.ShippingMethod`]
    """
    class Meta:
        model = ShippingZone
        fields = [
            # Fields
            'countries',
            'default',
            'id',
            'name',

            # Reverse Fields
            # 'shipping_methods',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
