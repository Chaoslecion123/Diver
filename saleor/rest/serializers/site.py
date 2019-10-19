from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'SiteSerializer',
]

Site = apps.get_model(*'sites.Site'.split())


class SiteSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`sites.Site`:

    `**Fields:**`
        01. `domain`                      : `CharField`
        02. `id`                          : `AutoField`
        03. `name`                        : `CharField`

    `**Reverse Fields:**`
        01. `settings`                    : `OneToOneField` [:model:`site.SiteSettings`]
    """
    class Meta:
        model = Site
        fields = [
            # Fields
            'domain',
            'id',
            'name',

            # Reverse Fields
            # 'settings',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
