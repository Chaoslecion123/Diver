from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from ..menu import MenuSerializer

__all__ = [
    'FooterItemSerializer',
]

FooterItem = apps.get_model(*'store.FooterItem'.split())


class FooterItemSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`store.FooterItem`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `menu`                        : `ForeignKey` [:model:`menu.Menu`]
        03. `site_settings`               : `ForeignKey` [:model:`site.SiteSettings`]
        04. `sort_order`                  : `PositiveIntegerField`

    `**Reverse Fields:**`
    """
    menu = MenuSerializer()

    class Meta:
        model = FooterItem
        fields = [
            # Fields
            'id',
            'menu',
            'site_settings',
            'sort_order',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
