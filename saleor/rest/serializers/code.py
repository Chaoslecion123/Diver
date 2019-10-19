from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'CodeSerializer',
]

Code = apps.get_model(*'social_django.Code'.split())


class CodeSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`social_django.Code`:

    `**Fields:**`
        01. `code`                        : `CharField`
        02. `email`                       : `CharField`
        03. `id`                          : `AutoField`
        04. `timestamp`                   : `DateTimeField`
        05. `verified`                    : `BooleanField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = Code
        fields = [
            # Fields
            'code',
            'email',
            'id',
            'timestamp',
            'verified',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
