from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from ..product import ProductSerializer, CategorySerializer, CollectionSerializer


__all__ = [
    'SaleSerializer',
]

Sale = apps.get_model(*'discount.Sale'.split())
Product = apps.get_model(*'product.Product'.split())
Category = apps.get_model(*'product.Category'.split())
Collection = apps.get_model(*'product.Collection'.split())


class SaleSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`discount.Sale`:

    `**Fields:**`
        01. `categories`                  : `ManyToManyField` [:model:`product.Category`]
        02. `collections`                 : `ManyToManyField` [:model:`product.Collection`]
        03. `end_date`                    : `DateField`
        04. `id`                          : `AutoField`
        05. `name`                        : `CharField`
        06. `products`                    : `ManyToManyField` [:model:`product.Product`]
        07. `show_countdown`              : `BooleanField`
        08. `start_date`                  : `DateField`
        09. `type`                        : `CharField`
        10. `value`                       : `DecimalField`

    `**Reverse Fields:**`
        01. `translations`                : `ForeignKey` [:model:`discount.SaleTranslation`]
    """
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        allow_null=True,
        required=False,
        many=True,
    )

    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_null=True,
        required=False,
        many=True,
    )

    collections = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all(),
        allow_null=True,
        required=False,
        many=True,
    )

    expandable_fields = {
        'products': (
            ProductSerializer, {
                'fields': [
                    'id',
                    'name',
                    'slug',
                    'image',
                    'availability',
                    'brand',
                ],
                'expand': ['brand'],
                'many': True
            }
        ),
        'categories': (
            CategorySerializer, {
                'fields': [
                    # Fields
                    'id',
                    'name',
                    'slug',
                    'icon_image',
                    'icon_image_alt',
                    'background_image',
                    'background_image_alt',
                ],
                'many': True
            }
        ),
        'collections': (
            CollectionSerializer, {
                'fields': [
                    # Fields
                    'id',
                    'name',
                    'slug',
                    'icon_image',
                    'icon_image_alt',
                    'background_image',
                    'background_image_alt',
                ],
                'many': True
            }
        ),
    }

    class Meta:
        model = Sale
        fields = [
            # Fields
            'id',
            'name',
            'type',
            'value',
            'start_date',
            'end_date',
            'show_countdown',
            'products',
            'categories',
            'collections',

            # Reverse Fields
            # 'translations',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
