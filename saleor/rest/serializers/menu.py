from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from .menu_item import MenuItemSerializer

__all__ = [
    'MenuSerializer',
]

Menu = apps.get_model(*'menu.Menu'.split())


class MenuSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`menu.Menu`:

    `**Fields:**`
        01. `id`                          : `AutoField`
        02. `json_content`                : `JSONField`
        03. `name`                        : `CharField`

    `**Reverse Fields:**`
        01. `items`                       : `ForeignKey` [:model:`menu.MenuItem`]
    """
    class Meta:
        model = Menu
        fields = [
            # Fields
            'id',
            'json_content',
            'name',

            # Reverse Fields
            # 'items',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
