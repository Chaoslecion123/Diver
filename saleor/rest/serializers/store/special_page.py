from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'SpecialPageSerializer',
]

SpecialPage = apps.get_model(*'store.SpecialPage'.split())


class SpecialPageSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`store.SpecialPage`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `page`                        : `ForeignKey` [:model:`page.Page`]
        03. `site_settings`               : `ForeignKey` [:model:`site.SiteSettings`]
        04. `type`                        : `CharField`

    `**Reverse Fields:**`
    """

    class Meta:
        model = SpecialPage
        fields = [
            # Fields
            'id',
            'page',
            'site_settings',
            'type',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
