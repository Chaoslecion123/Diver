from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'TransactionSerializer',
]

Transaction = apps.get_model(*'payment.Transaction'.split())


class TransactionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`payment.Transaction`:

    `**Fields:**`
        01. `amount`                      : `DecimalField`
        02. `created`                     : `DateTimeField`
        03. `currency`                    : `CharField`
        04. `error`                       : `CharField`
        05. `gateway_response`            : `JSONField`
        06. `id`                          : `AutoField`
        07. `is_success`                  : `BooleanField`
        08. `kind`                        : `CharField`
        09. `payment`                     : `ForeignKey` [:model:`payment.Payment`]
        10. `token`                       : `CharField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = Transaction
        fields = [
            # Fields
            'amount',
            'created',
            'currency',
            'error',
            'gateway_response',
            'id',
            'is_success',
            'kind',
            'payment',
            'token',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
