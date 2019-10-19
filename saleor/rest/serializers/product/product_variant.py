from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from saleor.core.utils.taxes import display_gross_prices

from ...fields import MoneyField, MeasurementField, TaxedMoneyField

from .product_image import ProductImageSerializer


__all__ = [
    'ProductVariantSerializer',
]

ProductVariant = apps.get_model(*'product.ProductVariant'.split())
ProductImage = apps.get_model(*'product.ProductImage'.split())
Product = apps.get_model(*'product.Product'.split())


class ProductSerializer(FlexFieldsModelSerializer):

    slug = serializers.CharField(
        source='get_slug',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            # Fields
            'id',
            'name',
            'slug',
        ]


class ProductVariantSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.ProductVariant`:

    `**Fields:**`
        01. `attributes`                  : `HStoreField`
        02. `cost_price`                  : `DecimalField`
        03. `id`                          : `AutoField`
        04. `images`                      : `ManyToManyField` [:model:`product.ProductImage`]
        05. `name`                        : `CharField`
        06. `price_override`              : `DecimalField`
        07. `product`                     : `ForeignKey` [:model:`product.Product`]
        08. `quantity`                    : `IntegerField`
        09. `quantity_allocated`          : `IntegerField`
        10. `sku`                         : `CharField`
        11. `track_inventory`             : `BooleanField`
        12. `weight`                      : `FloatField`

    `**Reverse Fields:**`
        01. `order_lines`                 : `ForeignKey` [:model:`order.OrderLine`]
        02. `product_spotlights`          : `ForeignKey` [:model:`homepage.Spotlight`]
        03. `translations`                : `ForeignKey` [:model:`product.ProductVariantTranslation`]
        04. `variant_images`              : `ForeignKey` [:model:`product.VariantImage`]
    """
    # cost_price = MoneyField()
    # product = ProductSerializer()
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        allow_null=False,
        required=False,
    )

    image = serializers.PrimaryKeyRelatedField(
        queryset=ProductImage.objects.all(),
        source='get_first_image',
        allow_null=False,
        required=False,
    )

    weight = MeasurementField()
    display_name = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    price_undiscounted = serializers.SerializerMethodField()
    price_display = serializers.SerializerMethodField()

    expandable_fields = {
        'image': (
            ProductImageSerializer, {
                'fields': [
                    'id',
                    'alt',
                    'image',
                ]
            }
        ),
        'product': (
            ProductSerializer, {
                'fields': [
                    'id',
                    'name',
                    'slug',
                ]
            }
        )
    }

    class Meta:
        model = ProductVariant
        fields = [
            # Fields
            'id',
            'sku',
            'images',
            'name',
            'product',
            'weight',

            # 'cost_price',
            # 'attributes',
            # 'price_override',
            # 'quantity',
            # 'quantity_allocated',
            # 'track_inventory',

            # Reverse Fields
            # 'order_lines',
            # 'product_spotlights',
            # 'translations',
            # 'variant_images',

            # Other fields
            'display_name',
            'image',
            'price_undiscounted',
            'price',
            'price_display'
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    # def get_attributes(self, obj):
    #     attributes = {}
    #     for key in obj.attributes:

    def get_display_name(self, obj):
        return obj.display_product()

    def get_price_undiscounted(self, obj):
        return MoneyField().to_representation(obj.base_price)

    def get_price(self, obj):
        taxes = None
        discounts = None
        context = self.context.get('request', None)

        if context is not None:
            taxes = context.taxes
            discounts = context.discounts

        return TaxedMoneyField().to_representation(obj.get_price(discounts, taxes))

    def get_price_display(self, obj):
        taxes = None
        context = self.context.get('request', None)

        if context is not None:
            taxes = context.taxes

        return {
            'display_gross': display_gross_prices(),
            'handle_taxes': bool(taxes)
        }
