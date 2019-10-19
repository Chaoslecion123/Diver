from django.apps import apps
from django.conf import settings
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .attribute import AttributeSerializer

__all__ = [
    'BrandSerializer',
]

Brand = apps.get_model(*'brand.Brand'.split())
Product = apps.get_model(*'product.Product'.split())
Attribute = apps.get_model(*'product.Attribute'.split())


def get_rendition_keys():
    rendition_keys = getattr(
        settings,
        'VERSATILEIMAGEFIELD_RENDITION_KEY_SETS',
        None
    )

    if rendition_keys is not None:
        rendition_keys = rendition_keys.get('brands', None)

    if rendition_keys is None:
        return [
            ("tiny", "thumbnail__60x30"),
            ("tiny_2x", "thumbnail__120x60"),
            ("small", "thumbnail__120x60"),
            ("small_2x", "thumbnail__240x120"),
            ("list", "thumbnail__240x120"),
            ("list_2x", "thumbnail__480x240"),
        ]

    return rendition_keys


class BrandSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`brand.Brand`:

    `**Fields:**`
        01. `color`                       : `CharField`
        02. `id`                          : `AutoField`
        03. `image`                       : `FileField`
        04. `is_featured`                 : `BooleanField`
        05. `name`                        : `CharField`
        06. `products`                    : `ManyToManyField` [:model:`product.Product`]
        07. `seo_description`             : `CharField`
        08. `seo_title`                   : `CharField`
        09. `slug`                        : `SlugField`

    `**Reverse Fields:**`
        01. `slider`                      : `ManyToManyField` [:model:`widget.Slider`]
        02. `translations`                : `ForeignKey` [:model:`brand.BrandTranslation`]
    """
    image = VersatileImageFieldSerializer(
        sizes=get_rendition_keys()
    )
    filter_data = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = [
            # Fields
            'id',
            'name',
            'color',
            'image',
            'is_featured',
            'seo_description',
            'seo_title',
            'slug',
            'products',

            # Reverse Fields
            # 'slider',
            # 'translations',
            'filter_data'
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_filter_data(self, obj):
        # request = self.context.get('request', None)
        product_attributes = obj.products.all().values_list(
            'product_type__product_attributes', flat=True)
        product_attributes = set(product_attributes)
        product_attributes = [
            pa for pa in product_attributes if pa is not None]
        product_attributes = Attribute.objects.filter(
            id__in=product_attributes)
        product_attributes = AttributeSerializer(
            product_attributes,
            fields=['id', 'name', 'slug', 'values'],
            many=True
        )

        variant_attributes = obj.products.all().values_list(
            'product_type__variant_attributes', flat=True)
        variant_attributes = set(variant_attributes)
        variant_attributes = [
            va for va in variant_attributes if va is not None]
        variant_attributes = Attribute.objects.filter(
            id__in=variant_attributes)
        variant_attributes = AttributeSerializer(
            variant_attributes,
            fields=['id', 'name', 'slug', 'values'],
            many=True
        )

        filter_data = []
        filter_data += product_attributes.data
        filter_data += variant_attributes.data

        return filter_data
