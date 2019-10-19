from django import forms
from django.utils.translation import pgettext_lazy

from ....widget.models import Slider, Slide
from ....widget.thumbnails import create_slide_thumbnails
from ...product.widgets import ImagePreviewWidget
from ...forms import OrderedModelMultipleChoiceField


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [
            'type',
            'name',
            'is_active',
            'active_on',
            'active_until',
            'is_default',
        ]
        labels = {
            'type': pgettext_lazy(
                'Slider type', 'Use with', ),
            'name': pgettext_lazy(
                'Slider name', 'Name', ),
            'is_active': pgettext_lazy(
                'Slider active state', 'Is public', ),
            'active_on': pgettext_lazy(
                'Slider active state', 'Public since', ),
            'active_until': pgettext_lazy(
                'active_until', 'Public until', ),
            'is_default': pgettext_lazy(
                'is_default', 'Use as default', ), }


class CollectionSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [
            'collections', ]
        labels = {
            'collections': pgettext_lazy(
                'Slider for collections', 'Collections', ), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['collections'].required = True


class CategorySliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [
            'categories', ]
        labels = {
            'categories': pgettext_lazy(
                'Slider for categories', 'Categories', ), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].required = True


class BrandSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [
            'brands', ]
        labels = {
            'brands': pgettext_lazy(
                'Slider for brands', 'Brands', ), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brands'].required = True


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = [
            'slider',
            'image',
            'alt',
        ]

        labels = {
            'slider': pgettext_lazy(
                'Slide field name', 'Slider'
            ),
            'image': pgettext_lazy(
                'Slide field name', 'Imagen'
            ),
            'alt': pgettext_lazy(
                'Slide field name', 'Texto alternativo'
            ),
        }

        widgets = {
            'slider': forms.widgets.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.image:
            self.fields['image'].widget = ImagePreviewWidget()

    def save(self, commit=True):
        slide = super().save(commit=commit)
        create_slide_thumbnails.delay(slide.pk)
        return slide


class ReorderSlideForm(forms.ModelForm):
    ordered_values = OrderedModelMultipleChoiceField(
        queryset=Slide.objects.none()
    )

    class Meta:
        model = Slider
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['ordered_values'].queryset = self.instance.slides.all()

    def save(self):
        for order, value in enumerate(self.cleaned_data['ordered_values']):
            value.sort_order = order
            value.save()

        return self.instance
