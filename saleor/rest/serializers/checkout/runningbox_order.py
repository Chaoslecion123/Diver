from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ...fields import MoneyField


__all__ = [
    'RunningBoxOrderSerializer',
]

RunningBoxOrder = apps.get_model(*'runningbox.RunningBoxOrder'.split())


class RunningBoxOrderSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`runningbox.RunningBoxOrder`:

    `**Fields:**`
        01. `checkout`                    : `OneToOneField` [:model:`checkout.Checkout`]
        02. `delivery_address`            : `ForeignKey` [:model:`account.Address`]
        03. `description`                 : `TextField`
        04. `runningbox_order_id`         : `CharField`
        05. `id`                          : `AutoField`
        06. `order`                       : `OneToOneField` [:model:`order.Order`]
        07. `origin_store`                : `ForeignKey` [:model:`store.PhysicalStore`]
        08. `price`                       : `DecimalField`
        09. `schedule_time`               : `DateTimeField`

    `**Reverse Fields:**`
    """
    price = MoneyField()

    class Meta:
        model = RunningBoxOrder
        fields = [
            # Fields
            'id',
            'order',
            'checkout',
            'price',
            'runningbox_order_id',
            'origin_store',
            'delivery_address',
            'description',
            'schedule_time',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
