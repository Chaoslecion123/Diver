from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'SessionSerializer',
]

Session = apps.get_model(*'sessions.Session'.split())


class SessionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`sessions.Session`:

    `**Fields:**`
        01. `expire_date`                 : `DateTimeField`
        02. `session_data`                : `TextField`
        03. `session_key`                 : `CharField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = Session
        fields = [
            # Fields
            'expire_date',
            'session_data',
            'session_key',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
