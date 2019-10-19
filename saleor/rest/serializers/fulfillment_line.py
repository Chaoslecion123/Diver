from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'FulfillmentLineSerializer',
]

FulfillmentLine = apps.get_model(*'order.FulfillmentLine'.split())


class FulfillmentLineSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`order.FulfillmentLine`:

    `**Fields:**`
        01. `fulfillment`                 : `ForeignKey` [:model:`order.Fulfillment`]
        02. `id`                          : `AutoField`
        03. `order_line`                  : `ForeignKey` [:model:`order.OrderLine`]
        04. `quantity`                    : `IntegerField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = FulfillmentLine
        fields = [
            # Fields
            'fulfillment',
            'id',
            'order_line',
            'quantity',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
