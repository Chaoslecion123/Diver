from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'MenuItemSerializer',
]

MenuItem = apps.get_model(*'menu.MenuItem'.split())


class MenuItemSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`menu.MenuItem`:

    `**Fields:**`
        01. `category`                    : `ForeignKey` [:model:`product.Category`]
        02. `collection`                  : `ForeignKey` [:model:`product.Collection`]
        03. `id`                          : `AutoField`
        04. `level`                       : `PositiveIntegerField`
        05. `lft`                         : `PositiveIntegerField`
        06. `menu`                        : `ForeignKey` [:model:`menu.Menu`]
        07. `name`                        : `CharField`
        08. `page`                        : `ForeignKey` [:model:`page.Page`]
        09. `parent`                      : `ForeignKey` [:model:`menu.MenuItem`]
        10. `rght`                        : `PositiveIntegerField`
        11. `sort_order`                  : `PositiveIntegerField`
        12. `tree_id`                     : `PositiveIntegerField`
        13. `url`                         : `CharField`

    `**Reverse Fields:**`
        01. `children`                    : `ForeignKey` [:model:`menu.MenuItem`]
        02. `translations`                : `ForeignKey` [:model:`menu.MenuItemTranslation`]
    """
    class Meta:
        model = MenuItem
        fields = [
            # Fields
            'category',
            'collection',
            'id',
            'level',
            'lft',
            'menu',
            'name',
            'page',
            'parent',
            'rght',
            'sort_order',
            'tree_id',
            'url',

            # Reverse Fields
            # 'children',
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
