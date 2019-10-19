from django import forms
from django.utils.translation import pgettext_lazy

from ....store.models import FooterItem
from ...forms import OrderedModelMultipleChoiceField


class FooterItemForm(forms.ModelForm):
    class Meta:
        model = FooterItem
        fields = [
            'site_settings',
            'menu'
        ]
        labels = {
            'menu': pgettext_lazy(
                'Menu form field', 'Menu a pie de página')}
        widgets = {'site_settings': forms.widgets.HiddenInput()}


class ReorderFooterItemForm(forms.ModelForm):
    ordered_values = OrderedModelMultipleChoiceField(
        queryset=FooterItem.objects.none()
    )

    class Meta:
        model = FooterItem
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['ordered_values'].queryset = self.instance.footer_items.all()

    def save(self):
        for order, value in enumerate(self.cleaned_data['ordered_values']):
            value.sort_order = order
            value.save()

        return self.instance
