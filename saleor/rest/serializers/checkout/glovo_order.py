from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ...fields import MoneyField


__all__ = [
    'GlovoOrderSerializer',
]

GlovoOrder = apps.get_model(*'glovo.GlovoOrder'.split())


class GlovoOrderSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`glovo.GlovoOrder`:

    `**Fields:**`
        01. `checkout`                    : `OneToOneField` [:model:`checkout.Checkout`]
        02. `delivery_address`            : `ForeignKey` [:model:`account.Address`]
        03. `description`                 : `TextField`
        04. `glovo_order_id`              : `CharField`
        05. `id`                          : `AutoField`
        06. `order`                       : `OneToOneField` [:model:`order.Order`]
        07. `origin_store`                : `ForeignKey` [:model:`store.PhysicalStore`]
        08. `price`                       : `DecimalField`
        09. `schedule_time`               : `DateTimeField`

    `**Reverse Fields:**`
    """
    price = MoneyField()

    class Meta:
        model = GlovoOrder
        fields = [
            # Fields
            'id',
            'order',
            'checkout',
            'price',
            'glovo_order_id',
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
