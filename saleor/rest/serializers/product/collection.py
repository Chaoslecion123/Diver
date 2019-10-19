from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer


__all__ = [
    'CollectionSerializer',
]

Collection = apps.get_model(*'product.Collection'.split())


class CollectionSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.Collection`:

    `**Fields:**`
        01. `background_image`            : `FileField`
        02. `background_image_alt`        : `CharField`
        03. `description`                 : `TextField`
        04. `id`                          : `AutoField`
        05. `is_published`                : `BooleanField`
        06. `name`                        : `CharField`
        07. `products`                    : `ManyToManyField` [:model:`product.Product`]
        08. `published_date`              : `DateField`
        09. `seo_description`             : `CharField`
        10. `seo_title`                   : `CharField`
        11. `slug`                        : `SlugField`

    `**Reverse Fields:**`
        01. `menuitem`                    : `ForeignKey` [:model:`menu.MenuItem`]
        02. `sale`                        : `ManyToManyField` [:model:`discount.Sale`]
        03. `translations`                : `ForeignKey` [:model:`product.CollectionTranslation`]
        04. `voucher`                     : `ManyToManyField` [:model:`discount.Voucher`]
    """
    class Meta:
        model = Collection
        fields = [
            # Fields
            'id',
            'name',
            'slug',
            'description',
            # 'is_published',
            # 'published_date',
            'products',
            'background_image',
            'background_image_alt',
            'seo_description',
            'seo_title',

            # Reverse Fields
            # 'menuitem',
            # 'sale',
            # 'translations',
            # 'voucher',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
