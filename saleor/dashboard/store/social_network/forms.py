from django import forms
from django.utils.translation import pgettext_lazy

from ....store.models import SocialNetwork


class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        fields = [
            'site_settings',
            'provider',
            'link',
        ]
        labels = {
            'provider': pgettext_lazy(
                'Social network provider form field', 'Provider'),
            'link': pgettext_lazy(
                'Password', 'Enlace')}
        widgets = {'site_settings': forms.widgets.HiddenInput()}
