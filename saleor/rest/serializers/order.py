from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from ..fields import MoneyField, TaxedMoneyField, MeasurementField
from .account.address import AddressSerializer
from .order_line import OrderLineSerializer
from .order_extension import OrderExtensionSerializer
from .order_event import OrderEventSerializer

__all__ = [
    'OrderSerializer',
]

Order = apps.get_model(*'order.Order'.split())
OrderLine = apps.get_model(*'order.OrderLine'.split())
Address = apps.get_model(*'account.Address'.split())


class OrderSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`order.Order`:

    `**Fields:**`
        01. `billing_address`             : `ForeignKey` [:model:`account.Address`]
        02. `created`                     : `DateTimeField`
        03. `customer_note`               : `TextField`
        04. `discount_amount`             : `DecimalField`
        05. `discount_name`               : `CharField`
        06. `display_gross_prices`        : `BooleanField`
        07. `id`                          : `AutoField`
        08. `language_code`               : `CharField`
        09. `shipping_address`            : `ForeignKey` [:model:`account.Address`]
        10. `shipping_method`             : `ForeignKey` [:model:`shipping.ShippingMethod`]
        11. `shipping_method_name`        : `CharField`
        12. `shipping_price`              : `TaxedMoneyField`
        13. `shipping_price_gross`        : `DecimalField`
        14. `shipping_price_net`          : `DecimalField`
        15. `status`                      : `CharField`
        16. `token`                       : `CharField`
        17. `total`                       : `TaxedMoneyField`
        18. `total_gross`                 : `DecimalField`
        19. `total_net`                   : `DecimalField`
        20. `tracking_client_id`          : `CharField`
        21. `translated_discount_name`    : `CharField`
        22. `user`                        : `ForeignKey` [:model:`account.User`]
        23. `user_email`                  : `CharField`
        24. `voucher`                     : `ForeignKey` [:model:`discount.Voucher`]
        25. `weight`                      : `FloatField`

    `**Reverse Fields:**`
        01. `events`                      : `ForeignKey` [:model:`order.OrderEvent`]
        02. `fulfillments`                : `ForeignKey` [:model:`order.Fulfillment`]
        03. `lines`                       : `ForeignKey` [:model:`order.OrderLine`]
        04. `payments`                    : `ForeignKey` [:model:`payment.Payment`]
    """

    discount_amount = MoneyField()
    shipping_price_gross = MoneyField()
    shipping_price_net = MoneyField()
    shipping_price = TaxedMoneyField()

    total_gross = MoneyField()
    total_net = MoneyField()
    total = TaxedMoneyField()
    weight = MeasurementField()

    payment_status = serializers.SerializerMethodField()
    payment_proof = serializers.SerializerMethodField()

    expandable_fields = {
        'lines': (
            OrderLineSerializer, {
                'fields': [
                    'id',
                    'is_shipping_required',
                    'order',
                    'product_name',
                    'product_sku',
                    'quantity',
                    'quantity_fulfilled',
                    'tax_rate',
                    'translated_product_name',
                    'unit_price',
                    'unit_price_gross',
                    'unit_price_net',
                    'variant',
                ],
                'many': True
            }
        ),
        'shipping_address': (
            AddressSerializer, {
                'fields': [
                    'city',
                    'city_area',
                    'company_name',
                    'country',
                    'country_area',
                    'first_name',
                    'id',
                    'last_name',
                    'phone',
                    'postal_code',
                    'street_address_1',
                    'street_address_2',
                ]
            }
        ),
        'billing_address': (
            AddressSerializer, {
                'fields': [
                    'city',
                    'city_area',
                    'company_name',
                    'country',
                    'country_area',
                    'first_name',
                    'id',
                    'last_name',
                    'phone',
                    'postal_code',
                    'street_address_1',
                    'street_address_2',
                ]
            }
        ),
        'events': (
            OrderEventSerializer, {
                'fields': [
                    'date',
                    'id',
                    'parameters',
                    'type',
                    'user',
                ],
                'many': True,
            }
        )
    }

    class Meta:
        model = Order
        fields = [
            # Fields
            'billing_address',
            'created',
            'customer_note',
            'discount_amount',
            'discount_name',
            'display_gross_prices',
            'id',
            'language_code',
            'shipping_address',
            # 'address',
            'shipping_method',
            'shipping_method_name',
            'shipping_price',
            'shipping_price_gross',
            'shipping_price_net',
            'status',
            'token',
            'total',
            'total_gross',
            'total_net',
            'tracking_client_id',
            'translated_discount_name',
            'user',
            'user_email',
            'voucher',
            'weight',

            # Reverse Fields
            'events',
            # 'fulfillments',
            'lines',
            # 'payments',

            'shipping_type',
            'billing_type',

            'payment_status',
            'shipping_status',
            'payment_proof'

        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_payment_status(self, obj):
        return obj.get_payment_status()

    def get_payment_proof(self, obj):
        if getattr(obj, 'orderextension', None):
            return OrderExtensionSerializer(obj.orderextension).data['payment_proof']
        return None

    def get_shipping_status(self, obj):
        return obj.get_shipping_status()
