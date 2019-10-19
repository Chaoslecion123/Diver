from django import forms
from django.utils.translation import pgettext_lazy

from ....widget.models import Scene, Spotlight
from ...product.widgets import ImagePreviewWidget


class SceneForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = [
            'name',
            'image',
            'alt',
            'is_active',
            'active_on',
            'active_until',
        ]

        labels = {
            'name': pgettext_lazy(
                'Scene field name', 'Name', ),
            'image': pgettext_lazy(
                'Scene field name', 'Image', ),
            'alt': pgettext_lazy(
                'Scene field name', 'Alternative text', ),
            'is_active': pgettext_lazy(
                'Scene active state', 'Is public', ),
            'active_on': pgettext_lazy(
                'Scene active state', 'Public since', ),
            'active_until': pgettext_lazy(
                'active_until', 'Public until', ),
            'is_default': pgettext_lazy(
                'is_default', 'Use as default', ), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.image:
            self.fields['image'].widget = ImagePreviewWidget()


class SpotlightForm(forms.ModelForm):
    class Meta:
        model = Spotlight
        fields = [
            'scene',
            'point_x',
            'point_y',
            'product', ]
        labels = {
            'scene': pgettext_lazy(
                'Spotlight field name', 'Scene'),
            'point_x': pgettext_lazy(
                'Spotlight field name', 'X'),
            'point_y': pgettext_lazy(
                'Spotlight field name', 'Y'),
            'product': pgettext_lazy(
                'Spotlight field name', 'Featured product'), }
        widgets = {
            'scene': forms.widgets.HiddenInput(), }
