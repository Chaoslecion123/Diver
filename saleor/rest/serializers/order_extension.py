from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from drf_extra_fields.fields import Base64ImageField

__all__ = [
    'OrderExtensionSerializer',
]

Order = apps.get_model(*'order.Order'.split())
OrderExtension = apps.get_model(*'order.OrderExtension'.split())


class OrderExtensionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`order.OrderExtension`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `order`                       : `ForeignKey` [:model:`order.Order`]
        03. `payment_proof`               : `FileField`

    `**Reverse Fields:**`
    """
    order = serializers.SlugRelatedField(
        queryset=Order.objects.all(),
        slug_field='token',
        allow_null=False,
        required=True,
        many=False,
    )

    payment_proof = Base64ImageField(required=False)

    class Meta:
        model = OrderExtension
        fields = [
            # Fields
            'id',
            'order',
            'payment_proof',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
