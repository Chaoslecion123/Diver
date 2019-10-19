from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'CustomerNoteSerializer',
]

CustomerNote = apps.get_model(*'account.CustomerNote'.split())


class CustomerNoteSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`account.CustomerNote`:

    `**Fields:**`
        01. `content`                     : `TextField`
        02. `customer`                    : `ForeignKey` [:model:`account.User`]
        03. `date`                        : `DateTimeField`
        04. `id`                          : `AutoField`
        05. `is_public`                   : `BooleanField`
        06. `user`                        : `ForeignKey` [:model:`account.User`]

    `**Reverse Fields:**`
    """
    class Meta:
        model = CustomerNote
        fields = [
            # Fields
            'content',
            'customer',
            'date',
            'id',
            'is_public',
            'user',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
