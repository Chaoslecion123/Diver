import logging
import uuid
from decimal import Decimal
from typing import Dict

import culqipy

from ...interface import PaymentData, GatewayResponse
from .forms import CulqiPaymentForm
from .utils import get_amount_for_culqi, get_error_response
from . import errors

TEMPLATE_PATH = 'order/payment/culqi.html'

# The list of currencies supported by culqi
# ('PEN', 'USD', )
SUPPORTED_CURRENCIES = ['PEN']
EMPTY_VALUES = [None, '', [], 0]
# Get the logger for this file, it will allow us to log
# error responses from culqi.
logger = logging.getLogger(__name__)


class TransactionKind:
    AUTH = 'auth'
    CAPTURE = 'capture'
    CHARGE = 'charge'
    REFUND = 'refund'
    VOID = 'void'


def _generate_response(payment_information: PaymentData, kind: str, data: Dict) -> Dict:
    """Generate Saleor transaction information from
    Culqi's success payload or from passed data."""
    return GatewayResponse(
        **{
            'transaction_id': data.get('id', payment_information.token),
            'kind': kind,
            'amount': data.get('amount', payment_information.amount),
            'currency': data.get('currency', payment_information.currency),
            'error': data.get('error', None),
            'is_success': data.get('is_success', True),
            'raw_response': data
        }
    )


def _format_charge_payload(payment_information: PaymentData):
    payload = {
        'source_id': payment_information.token,
        'amount': get_amount_for_culqi(payment_information.amount),
        'currency_code': payment_information.currency,
        'email': payment_information.customer_email,
    }

    if getattr(payment_information, 'installments', None) not in EMPTY_VALUES:
        payload.update({
            'installments': payment_information.installments
        })

    billing_address = payment_information.billing

    antifraud_details = {
        'address': billing_address.street_address_1,
        'address_city': billing_address.city,
        'country_code': billing_address.country,
        'first_name': billing_address.first_name,
        'last_name': billing_address.last_name,
    }

    metadata = {
        'order_id': payment_information.order_id,
        'ip': payment_information.customer_ip_address,
        'email': payment_information.customer_email,
        'first_name': billing_address.first_name,
        'last_name': billing_address.last_name,
    }

    fields = [
        'company_name',
        'street_address_1',
        'street_address_2',
        'city',
        'city_area',
        'postal_code',
        'country',
        'country_area',
        'phone',
        'position',
    ]

    fields = [
        'company_name',
        'street_address_1',
        'street_address_2',
        'city',
        'city_area',
        'postal_code',
        'country',
        'country_area',
        'phone',
        'position',
    ]

    for field in fields:
        if getattr(billing_address, field, None) not in EMPTY_VALUES:
            metadata.update({
                field: getattr(billing_address, field),
            })

            if field == 'phone':
                antifraud_details.update({
                    'phone_number': getattr(billing_address, field),
                })

    payload.update({
        'antifraud_details': antifraud_details,
        'metadata': metadata
    })

    return payload


def _format_refund_payload(payment_information: PaymentData):
    # {
    #     'token': 'chr_test_w14iPBiSSRy6NSb6',
    #     'amount': Decimal('72.56'),
    #     'currency': 'PEN',
    #     'billing': {
    #         'first_name': 'Russell',
    #         'last_name': 'Watson',
    #         'company_name': '',
    #         'street_address_1': '80083 Joseph Village Suite 848',
    #         'street_address_2': '',
    #         'city': 'West Michael',
    #         'city_area': '',
    #         'postal_code': '09652',
    #         'country': 'LU',
    #         'country_area': '',
    #         'phone': '',
    #         'position': None
    #     },
    #     'shipping': {
    #         'first_name': 'Russell',
    #         'last_name': 'Watson',
    #         'company_name': '',
    #         'street_address_1': '80083 Joseph Village Suite 848',
    #         'street_address_2': '',
    #         'city': 'West Michael',
    #         'city_area': '',
    #         'postal_code': '09652',
    #         'country': 'LU',
    #         'country_area': '',
    #         'phone': '',
    #         'position': None},
    #     'order_id': 22, 'customer_ip_address': '172.22.0.1',
    #     'customer_email': 'admin@example.com'
    # }
    return {
        "amount": get_amount_for_culqi(payment_information.amount),
        "charge_id": payment_information.token,
        "reason": "solicitud_comprador"
    }


def check_payment_supported(payment_information: PaymentData):
    """Checks that a given payment is supported."""
    if payment_information.currency not in SUPPORTED_CURRENCIES:
        return errors.UNSUPPORTED_CURRENCY % {
            'currency': payment_information.currency}


def get_error_message_from_culqi_error(exc: BaseException):
    """Convert a error culqi error to a user friendly error message
    and log the exception to stderr."""
    logger.exception(exc)
    if isinstance(exc, Exception):  # culqi.errors.BadRequestError):
        return errors.INVALID_REQUEST
    else:
        return errors.SERVER_ERROR


def clean_culqi_response(response: dict):
    """As the Culqi response payload contains the final amount
    in Indian rupees, we convert the amount to paisa (by dividing by 100)."""
    response['amount'] = Decimal(response['amount']) / 100


def format_culqui_payload(payment_information: dict, kind: str) -> Dict:
    if kind == TransactionKind.CHARGE:
        return _format_charge_payload(payment_information)

    if kind == TransactionKind.REFUND:
        return _format_refund_payload(payment_information)

    return payment_information


def create_form(data, payment_information, connection_params):
    """Return the associated culqi payment form."""
    return CulqiPaymentForm(
        data=data,
        payment_information=payment_information,
        connection_params=connection_params,
    )


def setup_client(public_key: str, secret_key: str, **_):
    """Create a Culqi client from set-up application keys."""
    culqipy.public_key = public_key
    culqipy.secret_key = secret_key


def get_client_token(**_):
    """Generate a random client token."""
    return str(uuid.uuid4())


def charge(payment_information: Dict, connection_params: Dict) -> Dict:
    """Charge a authorized payment using the culqi client.

    But it first check if the given payment instance is supported
    by the gateway.

    If an error from culqi occurs,
    we flag the transaction as failed and return
    a short user friendly description of the error
    after logging the error to stderr."""
    error = check_payment_supported(payment_information=payment_information)
    setup_client(**connection_params)
    response_has_errors = False

    if not error:
        try:
            payload = format_culqui_payload(
                payment_information, TransactionKind.CHARGE)
            response = culqipy.Charge.create(payload)

        # Fix: get specific errors
        except Exception as error:
            print(f"DATA::error::{error}")
            response = get_error_response(
                payment_information.amount, error=error,
                id=payment_information.token)
            response_has_errors = True
    else:
        response = get_error_response(
            payment_information.amount, error=error,
            id=payment_information.token)
        response_has_errors = True

    if not response_has_errors:
        if response.get('object', None) == 'error':
            error = response.get('user_message', None)
            if error is None:
                error = response.get('merchant_message', None)

            if error is None:
                error = 'Unkonw error!'

            response = get_error_response(
                payment_information.amount, error=error,
                id=payment_information.token)
        else:
            clean_culqi_response(response)

    return _generate_response(
        payment_information=payment_information,
        kind=TransactionKind.CHARGE, data=response)


def refund(payment_information: Dict, connection_params) -> Dict:
    """Refund a payment using the culqi client.

    But it first check if the given payment instance is supported
    by the gateway.

    It first retrieve a `charge` transaction to retrieve the
    payment id to refund. And return an error with a failed transaction
    if the there is no such transaction, or if an error
    from culqi occurs during the refund."""
    error = check_payment_supported(payment_information=payment_information)
    response_has_errors = False

    if error:

        response = get_error_response(
            payment_information.amount, error=error)
    else:
        setup_client(**connection_params)
        try:
            payload = format_culqui_payload(
                payment_information, TransactionKind.REFUND)

            response = culqipy.Refund.create(payload)
            print(f"DATA::response::{response}")

        # Fix: get specific errors
        except Exception as error:
            response_has_errors = True
            response = get_error_response(
                payment_information.amount, error=error)

    if not response_has_errors:
        if response.get('object', None) == 'error':
            error = response.get('user_message', None)
            if error is None:
                error = response.get('merchant_message', None)

            if error is None:
                error = 'Unkonw error!'

            response = get_error_response(
                payment_information.amount, error=error,
                id=payment_information.token)
        else:
            clean_culqi_response(response)

    return _generate_response(
        payment_information=payment_information,
        kind=TransactionKind.REFUND, data=response)


def process_payment(payment_information: Dict, connection_params) -> Dict:
    print(f"*** *** ***")
    print(f"CALL::process_payment")
    print(f"DATA::payment_information::{payment_information}")
    print(f"DATA::connection_params::{connection_params}")

    return charge(
        payment_information=payment_information,
        connection_params=connection_params)
