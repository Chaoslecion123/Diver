from typing import Dict

from django import forms
from django.forms.utils import flatatt
from django.forms.widgets import HiddenInput
from django.utils.html import format_html
from django.utils.translation import pgettext_lazy
from ...interface import PaymentData
from .utils import get_amount_for_culqi

CHECKOUT_SCRIPT_URL = 'https://checkout.culqi.com/plugins/v2'

PRIMARY_BTN_TEXT = pgettext_lazy(
    'Culqi payment gateway primary button', 'Pay now with Culqi')
SECONDARY_TITLE = pgettext_lazy(
    'Culqi payment gateway secondary title', 'Total payment')


class CulqiCheckoutWidget(HiddenInput):

    def __init__(
            self, *,
            payment_information: PaymentData,
            public_key: str,
            prefill: bool,
            store_name: str,
            store_image: str,
            **additional_parameters):
        override_attrs = additional_parameters.get('attrs', None)
        base_attrs = additional_parameters['attrs'] = {
            'src': CHECKOUT_SCRIPT_URL,
            'data-key': public_key,
            'data-buttontext': PRIMARY_BTN_TEXT,
            'data-image': store_image,
            'data-name': store_name,
            'data-description': SECONDARY_TITLE,
            'data-amount': get_amount_for_culqi(
                payment_information.amount),
            'data-currency': payment_information.currency}

        if prefill:
            customer_name = '%s %s' % (
                payment_information.billing.last_name,
                payment_information.billing.first_name)
            base_attrs.update({
                'data-prefill.name': customer_name,
                'data-prefill.email': payment_information.customer_email})

        if override_attrs:
            base_attrs.update(override_attrs)
        super().__init__(attrs=base_attrs)

    def render(self, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.update(self.attrs)
        return format_html('<script{0}></script>', flatatt(attrs))


class CulqiPaymentForm(forms.Form):
    culqi_payment_id = forms.CharField(
        required=True, widget=forms.HiddenInput)

    def __init__(
            self, payment_information, connection_params, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widget = CulqiCheckoutWidget(
            payment_information=payment_information, **connection_params)
        self.fields['culqi'] = forms.CharField(
            widget=widget, required=False)

    def get_payment_token(self):
        return self.cleaned_data['culqi_payment_id']
