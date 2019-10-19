from django.apps import apps
from django.db.models import Avg, F
from rest_framework import serializers
from rest_flex_fields import is_expanded, FlexFieldsModelSerializer

from ....product.utils.variants_picker import get_variant_picker_data
from ....product.utils.availability import get_product_availability
from ...fields import TaxedMoneyRangeField, TaxedMoneyField
from .product_image import ProductImageSerializer
from .brand import BrandSerializer

__all__ = [
    'ProductSerializer',
]

ProductVariant = apps.get_model(*'product.ProductVariant'.split())
ProductImage = apps.get_model(*'product.ProductImage'.split())
Product = apps.get_model(*'product.Product'.split())
Brand = apps.get_model(*'brand.Brand'.split())


class ProductSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`product.Product`:

    `**Fields:**`
        01. `attributes`                  : `HStoreField`
        02. `available_on`                : `DateField`
        03. `category`                    : `ForeignKey` [:model:`product.Category`]
        04. `charge_taxes`                : `BooleanField`
        05. `description`                 : `TextField`
        06. `id`                          : `AutoField`
        07. `is_published`                : `BooleanField`
        08. `name`                        : `CharField`
        09. `price`                       : `DecimalField`
        10. `product_type`                : `ForeignKey` [:model:`product.ProductType`]
        11. `seo_description`             : `CharField`
        12. `seo_title`                   : `CharField`
        13. `tax_rate`                    : `CharField`
        14. `updated_at`                  : `DateTimeField`
        15. `weight`                      : `FloatField`
        16. 'video'                       : 'UrlField'
        17. 'related_products'            : 'ManyToManyField'

    `**Reverse Fields:**`
        01. `collections`                 : `ManyToManyField` [:model:`product.Collection`]
        02. `images`                      : `ForeignKey` [:model:`product.ProductImage`]
        03. `sale`                        : `ManyToManyField` [:model:`discount.Sale`]
        04. `translations`                : `ForeignKey` [:model:`product.ProductTranslation`]
        05. `variants`                    : `ForeignKey` [:model:`product.ProductVariant`]
        06. `voucher`                     : `ManyToManyField` [:model:`discount.Voucher`]
    """
    # price = MoneyField()
    # weight = MeasurementField()

    # Campo de imagen
    image = ProductImageSerializer(
        source='get_first_image',
        fields=['alt', 'image'],
        allow_null=False,
        required=False,
    )

    slug = serializers.CharField(
        source='get_slug',
        allow_null=True,
        required=False
    )

    images = serializers.PrimaryKeyRelatedField(
        queryset=ProductImage.objects.all(),
        allow_null=True,
        required=False,
        many=True
    )

    raw_price_range = TaxedMoneyRangeField(
        source='get_price_range',
        allow_null=False,
        required=False,
    )

    variant_picker_data = serializers.SerializerMethodField()
    availability = serializers.SerializerMethodField()
    price_range = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
        source='get_brand',
        allow_null=False,
        required=False,
    )

    expandable_fields = {
        'images': (
            ProductImageSerializer, {
                'fields': [
                    'alt',
                    'image',
                ],
                'many': True
            }
        ),
        'brand': (
            BrandSerializer, {
                'fields': [
                    'id',
                    'name',
                    'color',
                    'image',
                ]
            }
        )
    }

    def __init__(self, *args, **kwargs):
        self.expandable_fields['related_products'] = (
            type(self), {
                'fields': [
                    'id',
                    'name',
                    'slug',
                    'image',
                    'availability',
                ],
                'many': True
            }
        )
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = [
            # Fields
            'id',
            'name',
            'slug',

            'product_type',
            'category',
            'description',
            'specs',
            'attributes',
            'price_range',
            'raw_price_range',

            'seo_title',
            'seo_description',

            'image',
            'video',
            'images',
            'related_products',

            # 'is_favorite',

            # 'available_on',
            # 'charge_taxes',
            # 'is_published',
            # 'price',
            # 'tax_rate',
            # 'updated_at',
            # 'weight',

            # Reverse Fields
            # 'collections',
            # 'sale',
            # 'translations',
            # 'variants',
            # 'voucher',
            'variant_picker_data',
            'availability',
            'score',
            'brand',
        ]
        read_only_fields = [
            'related_products',
        ]

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_variant_picker_data(self, obj):
        discounts = None
        taxes = None
        currency = None
        request = self.context.get('request', None)

        if request is not None:
            discounts = request.discounts
            taxes = request.taxes
            currency = request.currency

        return get_variant_picker_data(
            obj,
            discounts,
            taxes,
            currency
        )

    def get_is_sale(self, obj):
        pass

    def get_price_range(self, obj):
        taxes = None
        discounts = None
        context = self.context.get('request', None)

        if context is not None:
            taxes = context.taxes
            discounts = context.discounts

        price_range = obj.get_price_range(
            discounts=discounts,
            taxes=taxes
        )

        return TaxedMoneyRangeField().to_representation(price_range)

    def get_availability(self, obj):
        discounts = None
        taxes = None
        currency = None
        display_gross_prices = True
        request = self.context.get('request', None)

        if request is not None:
            discounts = request.discounts
            taxes = request.taxes
            currency = request.currency
            display_gross_prices = request.site.settings.display_gross_prices

        availability = get_product_availability(
            obj, discounts, taxes, currency)

        availability = availability._asdict()
        availability.update({
            'price_display': {
                'display_gross': display_gross_prices,
                'handle_taxes': bool(taxes)
            }
        })

        if availability['price_range'] is not None:
            availability.update({
                'price_range':
                    TaxedMoneyRangeField().to_representation(
                        availability['price_range'])
            })

        if availability['price_range_undiscounted'] is not None:
            availability.update({
                'price_range_undiscounted':
                    TaxedMoneyRangeField().to_representation(
                        availability['price_range_undiscounted'])
            })

        if availability['price_range_local_currency'] is not None:
            availability.update({
                'price_range_local_currency':
                    TaxedMoneyRangeField().to_representation(
                        availability['price_range_local_currency'])
            })

        if availability['discount'] is not None:
            availability.update({
                'discount':
                    TaxedMoneyField().to_representation(
                        availability['discount'])
            })

        return availability

    def get_score(self, obj):  # pylint: disable=no-self-use
        return obj.reviews.all().aggregate(score=Avg(F('score'))).get('score', 0.0) or 5.0
