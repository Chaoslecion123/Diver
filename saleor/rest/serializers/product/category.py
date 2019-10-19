from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from .attribute import AttributeSerializer

__all__ = [
    'CategorySerializer',
]

Product = apps.get_model(*'product.Product'.split())
Category = apps.get_model(*'product.Category'.split())
Attribute = apps.get_model(*'product.Attribute'.split())


class CategorySerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.Category`:

    `**Fields:**`
        01. `background_image`            : `FileField`
        02. `background_image_alt`        : `CharField`
        03. `description`                 : `TextField`
        04. `id`                          : `AutoField`
        05. `level`                       : `PositiveIntegerField`
        06. `lft`                         : `PositiveIntegerField`
        07. `name`                        : `CharField`
        08. `parent`                      : `ForeignKey` [:model:`product.Category`]
        09. `rght`                        : `PositiveIntegerField`
        10. `seo_description`             : `CharField`
        11. `seo_title`                   : `CharField`
        12. `slug`                        : `SlugField`
        13. 'icon_image'                  : 'FileField'
        14. 'icon_image_alt'              : 'CharField'
        13. `tree_id`                     : `PositiveIntegerField`

    `**Reverse Fields:**`
        01. `children`                    : `ForeignKey` [:model:`product.Category`]
        02. `menuitem`                    : `ForeignKey` [:model:`menu.MenuItem`]
        03. `products`                    : `ForeignKey` [:model:`product.Product`]
        04. `sale`                        : `ManyToManyField` [:model:`discount.Sale`]
        05. `translations`                : `ForeignKey` [:model:`product.CategoryTranslation`]
        06. `voucher`                     : `ManyToManyField` [:model:`discount.Voucher`]
    """
    slider = serializers.SerializerMethodField()

    filter_data = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            # Fields
            'id',
            # 'lft',
            # 'rght',
            'level',
            'parent',
            # 'tree_id',

            'name',
            'slug',
            'description',
            'background_image',
            'background_image_alt',
            'icon_image',
            'icon_image_alt',
            'seo_title',
            'seo_description',

            # Reverse Fields
            # 'children',
            # 'menuitem',
            # 'products',
            # 'sale',
            # 'translations',
            # 'voucher',

            # Other fields
            'filter_data',
            'slider',
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

    def get_slider(self, obj):
        # Prevent circular import with product
        from ..widget.slider import SliderSerializer

        slider = obj.slider

        if slider is not None:
            slider = SliderSerializer(
                slider,
                fields=[
                    'id',
                    'name',
                    'slides'
                ],
                expand=[
                    'slides'
                ],
                allow_null=False,
                required=False,
            ).data

        return slider
