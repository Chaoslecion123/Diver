from django.utils.translation import ugettext_lazy as _


class GlovoAddrressType(object):
    PICKUP = 'PICKUP'
    DELIVERY = 'DELIVERY'

    CHOICES = (
        (PICKUP, _("Recojo")),
        (DELIVERY, _("Entrega"))
    )

    DICT = dict(CHOICES)

    @classmethod
    def get_label(cls, address_type):
        return cls.DICT[address_type]


class GlovoOrderStatus(object):
    SCHEDULED = 'SCHEDULED'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'

    CHOICES = (
        (SCHEDULED, _('Programado')),
        (DELIVERED, _('Entregado')),
        (CANCELED, _('Cancelado')),
    )

    DICT = dict(CHOICES)

    @classmethod
    def get_label(cls, order_status):
        return cls.DICT[order_status]
