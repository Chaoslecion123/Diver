from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'SocialNetworkSerializer',
]

SocialNetwork = apps.get_model(*'store.SocialNetwork'.split())


class SocialNetworkSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`store.SocialNetwork`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `link`                        : `CharField`
        03. `provider`                    : `CharField`
        04. `site_settings`               : `ForeignKey` [:model:`site.SiteSettings`]

    `**Reverse Fields:**`
    """

    class Meta:
        model = SocialNetwork
        fields = [
            # Fields
            'id',
            'link',
            'provider',
            'site_settings',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
