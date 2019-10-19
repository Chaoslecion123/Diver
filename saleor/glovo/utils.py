from django.utils import timezone
from glovo_api_python.client import Client

from .conf import settings
from . import GlovoAddrressType


def get_client():
    return Client(
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET
    )


def format_address(address, kind):
    return {
        "lat": float(address.position.latitude),
        "lon": float(address.position.longitude),
        "type": kind,
        "label": address.street_address_1,
        "details": address.street_address_2,
        "contactPhone": str(address.phone),
        "contactPerson": address.full_name
    }


def glovo_order_estimate(pickup_address, delivery_address):
    schedule_time = timezone.now() + timezone.timedelta(hours=settings.DELIVERY_DELAY)
    schedule_time = schedule_time.timestamp()
    glovo_client = get_client()

    pickup_address = format_address(
        pickup_address, GlovoAddrressType.PICKUP)
    delivery_address = format_address(
        delivery_address, GlovoAddrressType.DELIVERY)

    try:
        return glovo_client.order.estimate({  # pylint: disable=no-member
            "scheduleTime": schedule_time,
            "description": "Some useful description",
            "addresses": [
                pickup_address,
                delivery_address
            ]
        })
    except Exception as msg:  # pylint: disable=broad-except
        print("*** *** ***")
        print(msg)
        print("*** *** ***")
        return None


def glovo_get_lowest_price(stores, delivery_address):
    estimated_prices = [
        glovo_order_estimate(
            store.address,
            delivery_address
        )
        for store in stores
    ]

    store_price = [
        {
            'store': store.id,
            'price': estimated_price['data']['total']
        }
        for store, estimated_price in zip(stores, estimated_prices)
        if estimated_price is not None and estimated_price['status'] == 200
    ] or None

    if store_price is None:
        return None

    return min(store_price, key=lambda x: x['price']['amount'])
