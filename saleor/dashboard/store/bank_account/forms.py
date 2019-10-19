from django import forms
from django.utils.translation import pgettext_lazy

from ....store.models import BankAccount


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = [
            'site_settings',
            'provider',
            'number',
        ]
        labels = {
            'provider': pgettext_lazy(
                'Bank account provider form field', 'Provider'),
            'number': pgettext_lazy(
                'Bank account number form field', 'Account number')}
        widgets = {'site_settings': forms.widgets.HiddenInput()}
