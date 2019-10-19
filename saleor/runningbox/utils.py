from decimal import Decimal
from django.utils import timezone
from runningbox_api.client import Client

from .conf import settings
# from . import GlovoAddrressType


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


def runningbox_order_estimate(weight, ubigeo, service):
    runningbox_client = get_client()
    try:
        print("runningbox_order_estimate")
        print({
            "clave_api": settings.API_KEY,
            "ubigeo": ubigeo,
            "servicio": service,
            "peso": weight,
        })

        estimate = runningbox_client.rate.rate_service({  # pylint: disable=no-member
            "clave_api": settings.API_KEY,
            "ubigeo": str(ubigeo),
            "servicio": service,
            "peso": str(weight),
        })

        if estimate['status'] == 200:
            return {
                'price': {
                    'amount': Decimal(estimate['data']),
                    'currency': 'PEN'
                }
            }
    except Exception as msg:  # pylint: disable=broad-except
        print("*** *** ***")
        print("Estimation error")
        print(msg)
        print("*** *** ***")

    return None


"""




def runningbox_get_lowest_price(stores, delivery_address):
    estimated_prices = [
        runningbox_order_estimate(
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
"""
