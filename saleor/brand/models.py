from django.db import models
from django.utils.translation import pgettext_lazy
from versatileimagefield.fields import VersatileImageField
from colorfield.fields import ColorField

from ..core.utils.translations import TranslationProxy
from ..seo.models import SeoModel, SeoModelTranslation
from ..product.models import Product


class Brand(SeoModel):
    name = models.CharField(
        max_length=64, )
    slug = models.SlugField(
        max_length=64,
        unique=True, )
    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='brands',
        related_query_name='brand', )
    image = VersatileImageField(
        upload_to='brands', )
    color = ColorField(
        default='#FFFFFF',
        blank=True, )
    is_featured = models.BooleanField(
        default=False, )

    translated = TranslationProxy()

    class Meta:
        ordering = ('slug', )
        permissions = (
            ('manage_brands', pgettext_lazy(
                'Permission description', 'Manage brands.'), ), )

    def __str__(self):
        return self.name

    @property
    def slider(self):
        if self.pk is not None:
            slider = self.sliders.filter(is_active=True).first()
            if slider is not None:
                return slider

            slider = self.sliders.filter(is_default=True).first()
            if slider is not None:
                return slider

        return None


class BrandTranslation(SeoModelTranslation):
    language_code = models.CharField(
        max_length=10, )
    brand = models.ForeignKey(
        Brand, related_name='translations',
        on_delete=models.CASCADE, )
    name = models.CharField(
        max_length=64, )

    class Meta:
        unique_together = (('language_code', 'brand'),)

    def __str__(self):
        return f'{self.brand.name} ({self.language_code})'
