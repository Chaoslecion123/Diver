from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'OrderEventSerializer',
]

OrderEvent = apps.get_model(*'order.OrderEvent'.split())


class OrderEventSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`order.OrderEvent`:

    `**Fields:**`
        01. `date`                        : `DateTimeField`
        02. `id`                          : `AutoField`
        03. `order`                       : `ForeignKey` [:model:`order.Order`]
        04. `parameters`                  : `JSONField`
        05. `type`                        : `CharField`
        06. `user`                        : `ForeignKey` [:model:`account.User`]

    `**Reverse Fields:**`
    """
    class Meta:
        model = OrderEvent
        fields = [
            # Fields
            'date',
            'id',
            'order',
            'parameters',
            'type',
            'user',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
