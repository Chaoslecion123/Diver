from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django_prices.models import MoneyField

from runningbox_api.client import Client

from ..core.utils.taxes import get_taxed_shipping_price
from ..account.models import Address
from ..store.models import PhysicalStore as Store
from .utils import get_client, format_address

RunningBoxClient = get_client()


class RunningBoxDeliveryPermission(models.Model):
    runningbox_enabled = models.BooleanField(
        default=False
    )
    store = models.OneToOneField(
        Store,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='runningbox_delivery_permission',
        related_query_name='runningbox_delivery_permission'
    )

    def __str__(self):
        return _('Delivery con runningbox permitido: %r') % _('Si') if self.enabled else _('No')

    @property
    def enabled(self):
        return self.runningbox_enabled


class RunningBoxOrder(models.Model):
    checkout = models.OneToOneField(
        "checkout.Checkout",
        on_delete=models.SET_NULL,
        related_name='runningbox_order',
        related_query_name='runningbox_order',
        blank=True,
        null=True,
    )
    order = models.OneToOneField(
        "order.Order",
        on_delete=models.SET_NULL,
        related_name='runningbox_order',
        related_query_name='runningbox_order',
        blank=True,
        null=True,
    )
    running_box_order_id = models.CharField(
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
        on_delete=models.CASCADE
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
    def running_box_pickup_address(self):
        return self.format_address(
            self.pickup_address, RunningBoxAddrressType.PICKUP)

    @property
    def running_box_delivery_addres(self):
        return self.format_address(
            self.delivery_address, RunningBoxAddrressType.DELIVERY)

    def estimate(self):
        if not self.running_box_order_id:
            estimation = RunningBoxClient.order.estimate({
                "scheduleTime": self.schedule_time.timestamp(),
                "description": self.description,
                "addresses": [
                    self.running_box_pickup_address,
                    self.running_box_delivery_addres
                ]
            })
            if estimation['status'] == 200:
                self.price = MoneyField(
                    estimation['data']['amount'] / 100.00,
                    estimation['data']['currency']
                )
                self.save()

    def create(self):
        if not self.running_box_order_id:
            order = RunningClient.order.create({
                "scheduleTime": self.schedule_time.timestamp(),
                "description": self.description,
                "addresses": [
                    self.running_box_pickup_address,
                    self.running_box_delivery_addres
                ]
            })

            if estimation['status'] == 200:
                self.running_box_order_id = order['data']['id']
                self.save()

    def tracking(self):
        if self.running_box_order_id:
            return RunningBoxClient.order.tracking(order_id)['data']
        return None

    def get_total(self, taxes=None):
        return get_taxed_shipping_price(self.price, taxes)
