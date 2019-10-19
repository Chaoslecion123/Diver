from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'NonceSerializer',
]

Nonce = apps.get_model(*'social_django.Nonce'.split())


class NonceSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`social_django.Nonce`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `salt`                        : `CharField`
        03. `server_url`                  : `CharField`
        04. `timestamp`                   : `IntegerField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = Nonce
        fields = [
            # Fields
            'id',
            'salt',
            'server_url',
            'timestamp',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
