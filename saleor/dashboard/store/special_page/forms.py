from django import forms
from django.utils.translation import pgettext_lazy

from ....store.models import SpecialPage


class SpecialPageForm(forms.ModelForm):
    class Meta:
        model = SpecialPage
        fields = [
            'site_settings',
            'type',
            'page',
        ]
        labels = {
            'type': pgettext_lazy(
                'special page provider form field', 'Page type'),
            'page': pgettext_lazy(
                'Password', 'Page')}
        widgets = {'site_settings': forms.widgets.HiddenInput()}
