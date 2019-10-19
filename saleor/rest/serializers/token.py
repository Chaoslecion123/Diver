from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'TokenSerializer',
]

Token = apps.get_model(*'authtoken.Token'.split())


class TokenSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`authtoken.Token`:

    `**Fields:**`
        01. `created`                     : `DateTimeField`
        02. `key`                         : `CharField`
        03. `user`                        : `OneToOneField` [:model:`account.User`]

    `**Reverse Fields:**`
    """
    class Meta:
        model = Token
        fields = [
            # Fields
            'created',
            'key',
            'user',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
