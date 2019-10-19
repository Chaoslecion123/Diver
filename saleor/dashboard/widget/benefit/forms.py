from django import forms
from django.utils.translation import pgettext_lazy

from ....widget.models import Benefit
from ...product.widgets import ImagePreviewWidget
from ....widget.thumbnails import create_benefit_thumbnails


class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = [
            'name',
            'text',
            'image',
            'is_active',
        ]

        labels = {
            'name': pgettext_lazy(
                'Benefit field name',
                'Nombre',
            ),
            'text': pgettext_lazy(
                'Benefit field name',
                'Texto',
            ),
            'image': pgettext_lazy(
                'Benefit field name',
                'Imagen',
            ),
            'is_active': pgettext_lazy(
                'Slider active state',
                'Activo',
            ),
        }

    def save(self, commit=True):
        print("*** *** ***")
        print("save benefit from form")
        print("*** *** ***")
        benefit = super().save(commit=commit)
        create_benefit_thumbnails.delay(benefit.pk)
        return benefit
