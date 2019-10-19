import json
import culqipy

from django.db import transaction
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ...checkout.models import Checkout
from ...core.utils import get_client_ip
from ...order.models import Order
from ...payment import ChargeStatus, TransactionKind, get_payment_gateway
from ...payment.utils import (
    create_payment, create_payment_information, gateway_process_payment)


# @csrf_exempt
@api_view(http_method_names=['POST'])
def culqiCheckout(request):
    order_token = request.data.get('order', None)
    order = Order.objects.get(token=order_token)
    gateway = 'culqi'
    payment_gateway, connection_params = get_payment_gateway(gateway)
    extra_data = {
        'customer_user_agent': request.META.get('HTTP_USER_AGENT', None)
    }
    response_data = {}
    response_status = status.HTTP_200_OK

    with transaction.atomic():
        payment = create_payment(
            gateway=gateway,
            currency=order.total.gross.currency,
            email=order.user_email,
            billing_address=order.billing_address,
            customer_ip_address=get_client_ip(request),
            total=order.total.gross.amount,
            order=order,
            extra_data=extra_data)

        if (order.is_fully_paid()
                or payment.charge_status == ChargeStatus.FULLY_REFUNDED):
            return Response(response_data, status=response_status)

        payment_info = create_payment_information(payment)
        form = payment_gateway.create_form(
            data=request.data or None,
            payment_information=payment_info,
            connection_params=connection_params)
        if form.is_valid():
            try:
                gateway_process_payment(
                    payment=payment, payment_token=form.get_payment_token())
            except Exception as exc:
                response_data['detail'] = exc
                response_status = status.HTTP_400_BAD_REQUEST
                return Response(response_data, status=response_status)
            else:
                # if order.is_fully_paid():
                #     return redirect('order:payment-success', token=order.token)
                # return redirect(order.get_absolute_url())
                return Response(response_data, status=response_status)

    return Response(response_data, status=response_status)
