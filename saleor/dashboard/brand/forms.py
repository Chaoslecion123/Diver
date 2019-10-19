from django import forms
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.translation import pgettext_lazy
from text_unidecode import unidecode

from ...product.models import Product
from ...brand.models import Brand
from ...brand.thumbnails import create_brand_thumbnails
# from ..forms import AjaxSelect2MultipleChoiceField
from ..seo.fields import SeoDescriptionField, SeoTitleField


class BrandForm(forms.ModelForm):
    # products = AjaxSelect2MultipleChoiceField(
    #     queryset=Product.objects.all(),
    #     fetch_data_url=reverse_lazy('dashboard:ajax-products'), required=False,
    #     label=pgettext_lazy('Products selection', 'Products'))

    class Meta:
        model = Brand
        exclude = ['slug', 'products', 'description_json']
        labels = {
            'name': pgettext_lazy('Item name', 'Name'),
            'image': pgettext_lazy(
                'Brand form', 'Brand logo'),
            'is_featured': pgettext_lazy(
                'Brand form', 'Is featured')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self.instance.pk:
        #     self.fields['products'].set_initial(self.instance.products.all())
        self.fields['seo_description'] = SeoDescriptionField()
        self.fields['seo_title'] = SeoTitleField(
            extra_attrs={
                'data-bind': self['name'].auto_id, }, )

    def save(self, commit=True):
        self.instance.slug = slugify(unidecode(self.instance.name))
        instance = super().save(commit=commit)
        create_brand_thumbnails.delay(instance.pk)
        return instance
