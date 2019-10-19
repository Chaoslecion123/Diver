from django import forms
from django.utils.translation import pgettext_lazy

from ....widget.models import Banner
from ...product.widgets import ImagePreviewWidget


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = [
            'name',
            'image',
            'alt',
            'is_active',
            'active_on',
            'active_until',
            'is_default',
        ]

        labels = {
            'name': pgettext_lazy(
                'Banner field name', 'Name', ),
            'image': pgettext_lazy(
                'Banner field name', 'Image', ),
            'alt': pgettext_lazy(
                'Banner field name', 'Alternative text', ),
            'is_active': pgettext_lazy(
                'Slider active state', 'Is public', ),
            'active_on': pgettext_lazy(
                'Slider active state', 'Public since', ),
            'active_until': pgettext_lazy(
                'active_until', 'Public until', ),
            'is_default': pgettext_lazy(
                'is_default', 'Use as default', ), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.image:
            self.fields['image'].widget = ImagePreviewWidget()
