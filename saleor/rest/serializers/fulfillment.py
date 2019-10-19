from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'FulfillmentSerializer',
]

Fulfillment = apps.get_model(*'order.Fulfillment'.split())


class FulfillmentSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`order.Fulfillment`:

    `**Fields:**`
        01. `fulfillment_order`           : `PositiveIntegerField`
        02. `id`                          : `AutoField`
        03. `order`                       : `ForeignKey` [:model:`order.Order`]
        04. `shipping_date`               : `DateTimeField`
        05. `status`                      : `CharField`
        06. `tracking_number`             : `CharField`

    `**Reverse Fields:**`
        01. `lines`                       : `ForeignKey` [:model:`order.FulfillmentLine`]
    """
    class Meta:
        model = Fulfillment
        fields = [
            # Fields
            'fulfillment_order',
            'id',
            'order',
            'shipping_date',
            'status',
            'tracking_number',

            # Reverse Fields
            # 'lines',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
