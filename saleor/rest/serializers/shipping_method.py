from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ..fields import MoneyField, MeasurementField


__all__ = [
    'ShippingMethodSerializer',
]

ShippingMethod = apps.get_model(*'shipping.ShippingMethod'.split())


class ShippingMethodSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`shipping.ShippingMethod`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `maximum_order_price`         : `DecimalField`
        03. `maximum_order_weight`        : `FloatField`
        04. `minimum_order_price`         : `DecimalField`
        05. `minimum_order_weight`        : `FloatField`
        06. `name`                        : `CharField`
        07. `price`                       : `DecimalField`
        08. `shipping_zone`               : `ForeignKey` [:model:`shipping.ShippingZone`]
        09. `type`                        : `CharField`

    `**Reverse Fields:**`
        01. `checkouts`                       : `ForeignKey` [:model:`checkout.Checkout`]
        02. `orders`                      : `ForeignKey` [:model:`order.Order`]
        03. `translations`                : `ForeignKey` [:model:`shipping.ShippingMethodTranslation`]
    """
    maximum_order_price = MoneyField()
    minimum_order_price = MoneyField()
    price = MoneyField()
    maximum_order_weight = MeasurementField()
    minimum_order_weight = MeasurementField()

    class Meta:
        model = ShippingMethod
        fields = [
            # Fields
            'id',
            'maximum_order_price',
            'maximum_order_weight',
            'minimum_order_price',
            'minimum_order_weight',
            'name',
            'price',
            'shipping_zone',
            'type',

            # Reverse Fields
            # 'checkouts',
            # 'orders',
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
