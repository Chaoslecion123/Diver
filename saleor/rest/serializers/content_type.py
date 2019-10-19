from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'ContentTypeSerializer',
]

ContentType = apps.get_model(*'contenttypes.ContentType'.split())


class ContentTypeSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`contenttypes.ContentType`:

    `**Fields:**`
        01. `app_label`                   : `CharField`
        02. `id`                          : `AutoField`
        03. `model`                       : `CharField`

    `**Reverse Fields:**`
        01. `logentry`                    : `ForeignKey` [:model:`admin.LogEntry`]
        02. `permission`                  : `ForeignKey` [:model:`auth.Permission`]
    """
    class Meta:
        model = ContentType
        fields = [
            # Fields
            'app_label',
            'id',
            'model',

            # Reverse Fields
            # 'logentry',
            # 'permission',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
