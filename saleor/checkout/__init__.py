import logging

from django.utils.translation import pgettext_lazy

logger = logging.getLogger(__name__)


class AddressType:
    BILLING = 'billing'
    SHIPPING = 'shipping'

    CHOICES = [
        (BILLING, pgettext_lazy(
            'Type of address used to fulfill order',
            'Billing'
        )),
        (SHIPPING, pgettext_lazy(
            'Type of address used to fulfill order',
            'Shipping'
        ))]


class ShippingType:
    DOOR_SHIPPING = 'door-shipping'
    STORE_SHIPPING = 'store-shipping'

    CHOICES = (
        (DOOR_SHIPPING, pgettext_lazy(
            'Shipping type', 'Envío a domicilio')),
        (STORE_SHIPPING, pgettext_lazy(
            'Shipping type', 'Recojo en tienda')),
    )


class BillingType:
    BALLOT = 'ballot'
    FACTURE = 'facture'

    CHOICES = (
        (BALLOT, pgettext_lazy(
            'Billing type', 'Boleta')),
        (FACTURE, pgettext_lazy(
            'Billing type', 'Factura')),
    )
