from django.apps import apps
from django.conf import settings
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer


__all__ = [
    'ProductImageSerializer',
]

ProductImage = apps.get_model(*'product.ProductImage'.split())


def get_rendition_keys():
    rendition_keys = getattr(
        settings,
        'VERSATILEIMAGEFIELD_RENDITION_KEY_SETS',
        None
    )

    if rendition_keys is not None:
        rendition_keys = rendition_keys.get('products', None)

    if rendition_keys is None:
        return [
            ('product_gallery', 'thumbnail__540x540'),
            ('product_small', 'thumbnail__60x60'),
            ('product_list', 'thumbnail__255x255'),
            ('product_tiny', 'thumbnail__10x10')
        ]

    return rendition_keys


class ProductImageSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.ProductImage`:

    `**Fields:**`
        01. `alt`                         : `CharField`
        02. `id`                          : `AutoField`
        03. `image`                       : `FileField`
        04. `ppoi`                        : `CharField`
        05. `product`                     : `ForeignKey` [:model:`product.Product`]
        06. `sort_order`                  : `PositiveIntegerField`

    `**Reverse Fields:**`
        01. `productvariant`              : `ManyToManyField` [:model:`product.ProductVariant`]
        02. `variant_images`              : `ForeignKey` [:model:`product.VariantImage`]
    """
    image = VersatileImageFieldSerializer(
        sizes=get_rendition_keys()
    )

    class Meta:
        model = ProductImage
        fields = [
            # Fields
            'alt',
            'id',
            'image',
            'ppoi',
            'product',
            'sort_order',

            # Reverse Fields
            # 'productvariant',
            # 'variant_images',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
