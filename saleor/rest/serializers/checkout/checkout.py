from decimal import Decimal
from django.apps import apps
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from ....checkout.utils import get_taxes_for_checkout
from ....glovo.utils import glovo_get_lowest_price
from ....runningbox.utils import runningbox_order_estimate
from ...fields import MoneyField, TaxedMoneyField
from ..shipping_method import ShippingMethodSerializer
from .checkout_line import CheckoutLineSerializer
from .glovo_order import GlovoOrderSerializer
from .runningbox_order import RunningBoxOrderSerializer

__all__ = [
    'CheckoutSerializer',
]

Checkout = apps.get_model(*'checkout.Checkout'.split())
CheckoutLine = apps.get_model(*'checkout.CheckoutLine'.split())
Address = apps.get_model(*'account.Address'.split())
ShippingMethod = apps.get_model(*'shipping.ShippingMethod'.split())
PhysicalStore = apps.get_model(*'store.PhysicalStore'.split())
GlovoOrder = apps.get_model(*'glovo.GlovoOrder'.split())
RunningBoxOrder = apps.get_model(*'runningbox.RunningBoxOrder'.split())


class CheckoutSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`checkout.Checkout`:

    `**Fields:**`
        01. `billing_address`             : `ForeignKey` [:model:`account.Address`]
        02. `created`                     : `DateTimeField`
        03. `discount_amount`             : `DecimalField`
        04. `discount_name`               : `CharField`
        05. `email`                       : `CharField`
        06. `last_change`                 : `DateTimeField`
        07. `note`                        : `TextField`
        08. `quantity`                    : `PositiveIntegerField`
        09. `shipping_address`            : `ForeignKey` [:model:`account.Address`]
        10. `shipping_method`             : `ForeignKey` [:model:`shipping.ShippingMethod`]
        11. `token`                       : `UUIDField`
        12. `translated_discount_name`    : `CharField`
        13. `user`                        : `ForeignKey` [:model:`account.User`]
        14. `voucher_code`                : `CharField`

    **Reverse Fields:**
        01. `lines`                       : `ForeignKey` [:model:`checkout.CheckoutLine`]
        02. `payments`                    : `ForeignKey` [:model:`payment.Payment`]
    """
    lines = serializers.PrimaryKeyRelatedField(
        queryset=CheckoutLine.objects.all(),
        allow_null=False,
        required=False,
        many=True,
    )

    shipping_address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        allow_null=True,
        required=True
    )

    billing_address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        allow_null=True,
        required=False
    )

    glovo_order = serializers.PrimaryKeyRelatedField(
        queryset=GlovoOrder.objects.all(),
        allow_null=True,
        required=False
    )

    runningbox_order = serializers.PrimaryKeyRelatedField(
        queryset=RunningBoxOrder.objects.all(),
        allow_null=True,
        required=False
    )

    discount_amount = MoneyField()

    total = serializers.SerializerMethodField()
    subtotal = serializers.SerializerMethodField()
    shipping_price = serializers.SerializerMethodField()

    applicable_shipping_methods = serializers.SerializerMethodField()

    expandable_fields = {
        'lines': (
            CheckoutLineSerializer, {
                'fields': [
                    'id',
                    'quantity',
                    'variant',
                ],
                'many': True
            }
        ),
        'shipping_method': (
            ShippingMethodSerializer, {
                'fields': [
                    'id',
                    'name',
                    'price',
                ]
            }
        ),
        'glovo_order': (
            GlovoOrderSerializer, {
                'fields': [
                    'id',
                    'price',
                ]
            }
        ),
        'runningbox_order': (
            RunningBoxOrder, {
                'fields': [
                    'id',
                    'price',
                ]
            }
        )
    }

    class Meta:
        model = Checkout
        fields = [
            # Fields
            'token',
            'created',
            'user',
            'email',
            'quantity',
            'voucher_code',
            'discount_name',
            'discount_amount',

            'shipping_type',
            'shipping_address',
            'shipping_method',

            'billing_type',
            'billing_address',

            'note',
            # 'last_change',
            # 'translated_discount_name',

            # Reverse Fields
            'lines',
            # 'payments',
            'glovo_order',
            'runningbox_order',

            # other fields
            'subtotal',
            'total',
            'shipping_price',
            'applicable_shipping_methods',
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_subtotal(self, obj):
        discounts = None
        taxes = None
        context = self.context.get('request', None)

        if context is not None:
            discounts = context.discounts
            taxes = context.taxes

        subtotal = obj.get_subtotal(discounts, taxes)

        return TaxedMoneyField().to_representation(subtotal)

    def get_shipping_price(self, obj):
        taxes = None
        context = self.context.get('request', None)

        if context is not None:
            taxes = context.taxes

        shipping_price = obj.get_shipping_price(taxes)

        return TaxedMoneyField().to_representation(shipping_price)

    def get_total(self, obj):
        discounts = None
        taxes = None
        context = self.context.get('request', None)

        if context is not None:
            discounts = context.discounts
            taxes = context.taxes

        total = obj.get_total(discounts, taxes)

        return TaxedMoneyField().to_representation(total)

    def get_applicable_shipping_methods(self, obj):
        if obj.shipping_address is None:
            return None

        request = self.context.get('request', None)
        discounts = None
        taxes = None

        if request is None:
            discounts = request.discounts
            taxes = get_taxes_for_checkout(obj, request.taxes)

        # country_code = obj.shipping_address.country.code
        shpping_methods = ShippingMethod.objects.applicable_shipping_methods(
            price=obj.get_subtotal(discounts, taxes).gross,
            weight=obj.get_total_weight(),
            address=obj.shipping_address
        )

        shpping_methods = ShippingMethodSerializer(shpping_methods, many=True)
        shpping_methods = shpping_methods.data

        stores = PhysicalStore.objects.filter(
            glovo_delivery_permission__glovo_enabled=True)

        if stores.exists():
            if getattr(obj.shipping_address, 'position', None):
                glovo_shipping_method = glovo_get_lowest_price(
                    stores, obj.shipping_address)
                if glovo_shipping_method is not None:
                    glovo_shipping_method['price']['amount'] = Decimal(
                        str(glovo_shipping_method['price']['amount'] / 100))
                    glovo_shipping_method['name'] = 'Glovo'
                    glovo_shipping_method['id'] = 'shipping-with-glovo'
                    shpping_methods.append(glovo_shipping_method)

        stores = PhysicalStore.objects.filter(
            runningbox_delivery_permission__runningbox_enabled=True)

        if stores.exists():
            if getattr(obj.shipping_address, 'ubigeo', None):
                runningbox_shipping_method = runningbox_order_estimate(
                    obj.get_total_weight().value,
                    obj.shipping_address.ubigeo,
                    'EXPRESS'
                )
                if runningbox_shipping_method is not None:
                    runningbox_shipping_method['name'] = 'RunningBox'
                    runningbox_shipping_method['id'] = 'shipping-with-runningbox'
                    shpping_methods.append(runningbox_shipping_method)

        return shpping_methods
