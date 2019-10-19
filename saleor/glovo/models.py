from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django_prices.models import MoneyField

from glovo_api_python.client import Client

from ..core.utils.taxes import get_taxed_shipping_price
from ..account.models import Address
from ..store.models import PhysicalStore as Store
from .utils import get_client, format_address
from . import GlovoAddrressType


GlovoClient = get_client()


class GlovoDeliveryPermission(models.Model):
    glovo_enabled = models.BooleanField(
        default=False
    )
    store = models.OneToOneField(
        Store,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='glovo_delivery_permission',
        related_query_name='glovo_delivery_permission'
    )

    def __str__(self):
        return _('Delivery con glovo permitido: %r') % _('Si') if self.enabled else _('No')

    @property
    def enabled(self):
        return self.glovo_enabled


class GlovoOrder(models.Model):
    checkout = models.OneToOneField(
        "checkout.Checkout",
        on_delete=models.SET_NULL,
        related_name='glovo_order',
        related_query_name='glovo_order',
        blank=True,
        null=True,
    )
    order = models.OneToOneField(
        "order.Order",
        on_delete=models.SET_NULL,
        related_name='glovo_order',
        related_query_name='glovo_order',
        blank=True,
        null=True,
    )
    glovo_order_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    schedule_time = models.DateTimeField(
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
    )
    origin_store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='glovo_orders',
        related_query_name='glovo_order',
    )
    delivery_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='+',
    )
    price = MoneyField(
        currency=settings.DEFAULT_CURRENCY,
        max_digits=settings.DEFAULT_MAX_DIGITS,
        decimal_places=settings.DEFAULT_DECIMAL_PLACES
    )

    @classmethod
    def format_address(cls, address, kind):
        return format_address(address, kind)

    @property
    def pickup_address(self):
        return self.origin_store

    @property
    def glovo_pickup_address(self):
        return self.format_address(self.pickup_address, GlovoAddrressType.PICKUP)

    @property
    def glovo_delivery_addres(self):
        return self.format_address(self.delivery_address, GlovoAddrressType.DELIVERY)

    def estimate(self):
        if not self.glovo_order_id:
            estimation = GlovoClient.order.estimate({
                "scheduleTime": self.schedule_time.timestamp(),
                "description": self.description,
                "addresses": [
                    self.glovo_pickup_address,
                    self.glovo_delivery_addres
                ]
            })
            if estimation['status'] == 200:
                self.price = MoneyField(
                    estimation['data']['amount'] / 100.00,
                    estimation['data']['currency']
                )
                self.save()

    def create(self):
        if not self.glovo_order_id:
            order = GlovoClient.order.create({
                "scheduleTime": self.schedule_time.timestamp(),
                "description": self.description,
                "addresses": [
                    self.glovo_pickup_address,
                    self.glovo_delivery_addres
                ]
            })

            if estimation['status'] == 200:
                self.glovo_order_id = order['data']['id']
                self.save()

    def tracking(self):
        if self.glovo_order_id:
            return GlovoClient.order.tracking(order_id)['data']
        return None

    def get_total(self, taxes=None):
        return get_taxed_shipping_price(self.price, taxes)
