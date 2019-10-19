from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'AuthorizationKeySerializer',
]

AuthorizationKey = apps.get_model(*'site.AuthorizationKey'.split())


class AuthorizationKeySerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`site.AuthorizationKey`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `key`                         : `TextField`
        03. `name`                        : `CharField`
        04. `password`                    : `TextField`
        05. `site_settings`               : `ForeignKey` [:model:`site.SiteSettings`]

    `**Reverse Fields:**`
    """
    class Meta:
        model = AuthorizationKey
        fields = [
            # Fields
            'id',
            'key',
            'name',
            'password',
            'site_settings',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
