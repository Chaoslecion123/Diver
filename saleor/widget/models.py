from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import pgettext_lazy

from versatileimagefield.fields import PPOIField, VersatileImageField

from ..core.utils.translations import TranslationProxy
from ..core.models import SortableModel
from . import SliderType


class Slider(models.Model):
    type = models.CharField(
        max_length=20,
        choices=SliderType.CHOICES,
        default=SliderType.HOMEPAGE, )
    name = models.CharField(
        max_length=128, )
    is_active = models.BooleanField(
        default=False, )
    active_on = models.DateField(
        blank=True,
        null=True, )
    active_until = models.DateField(
        blank=True,
        null=True, )
    is_default = models.BooleanField(
        default=False, )
    collections = models.ManyToManyField(
        'product.Collection',
        blank=True,
        related_name='sliders',
        related_query_name='slider', )
    categories = models.ManyToManyField(
        'product.Category',
        blank=True,
        related_name='sliders',
        related_query_name='slider', )
    brands = models.ManyToManyField(
        'brand.Brand',
        blank=True,
        related_name='sliders',
        related_query_name='slider', )

    class Meta:
        ordering = ('name', )
        permissions = (
            ('manage_sliders', pgettext_lazy(
                'Permission description', 'Manage sliders.'), ), )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ
        if self.pk and self.type == SliderType.HOMEPAGE:
            self.collections.clear()
            self.categories.clear()
            self.brands.clear()

        if self.pk and self.type == SliderType.COLLECTION:
            self.categories.clear()
            self.brands.clear()

        if self.pk and self.type == SliderType.CATEGORY:
            self.collections.clear()
            self.brands.clear()

        if self.pk and self.type == SliderType.BRAND:
            self.collections.clear()
            self.categories.clear()

        return super().save(*args, **kwargs)

    def set_active(self):
        self.is_active = True
        self.save()

    def set_default(self):
        self.is_default = True
        self.save()

    @classmethod
    def post_save_handler(cls, instance, **kwargs):  # pylint: disable=W0613
        if instance.is_active and instance.type == SliderType.HOMEPAGE:
            cls.objects\
                .exclude(pk=instance.pk)\
                .filter(type=instance.type)\
                .update(is_active=False)

        if instance.is_default:
            cls.objects\
                .exclude(pk=instance.pk)\
                .filter(type=instance.type)\
                .update(is_default=False)


post_save.connect(
    Slider.post_save_handler,
    sender=Slider
)


class Slide(SortableModel):
    slider = models.ForeignKey(
        Slider,
        related_name='slides',
        related_query_name='slide',
        on_delete=models.CASCADE,
    )

    image = VersatileImageField(
        upload_to='slides',
        ppoi_field='ppoi',
        blank=False,
    )

    ppoi = PPOIField()

    alt = models.CharField(
        max_length=128,
        blank=True,
    )

    class Meta:
        ordering = ('sort_order', )

    def __str__(self):
        return f"Slide {self.sort_order + 1}"

    def get_ordering_queryset(self):
        return self.slider.slides.all()


class Banner(models.Model):
    name = models.CharField(
        max_length=128, )
    image = VersatileImageField(
        upload_to='banners',
        ppoi_field='ppoi',
        blank=False, )
    ppoi = PPOIField()
    alt = models.CharField(
        max_length=128,
        blank=True, )
    is_active = models.BooleanField(
        default=False, )
    active_on = models.DateField(
        blank=True,
        null=True, )
    active_until = models.DateField(
        blank=True,
        null=True, )
    is_default = models.BooleanField(
        default=False, )

    class Meta:
        ordering = ('name', )
        permissions = (
            ('manage_banners', pgettext_lazy(
                'Permission description', 'Manage banners.'), ), )

    def __str__(self):
        return self.name

    def set_active(self):
        self.is_active = True
        self.save()

    @classmethod
    def post_save_handler(cls, instance, **kwargs):  # pylint: disable=W0613
        if instance.is_active:
            cls.objects.exclude(pk=instance.pk).update(is_active=False)

        if instance.is_default:
            cls.objects.exclude(pk=instance.pk).update(is_default=False)


post_save.connect(Banner.post_save_handler, sender=Banner)


class Scene(models.Model):
    name = models.CharField(
        max_length=128,
    )
    image = VersatileImageField(
        upload_to='scenes',
        ppoi_field='ppoi',
        blank=False,
    )
    ppoi = PPOIField()
    alt = models.CharField(
        max_length=128,
        blank=True,
    )
    is_active = models.BooleanField(
        default=False,
    )
    active_on = models.DateField(
        blank=True,
        null=True,
    )
    active_until = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('name', )
        permissions = (
            ('manage_scenes', pgettext_lazy(
                'Permission description', 'Manage scenes.'), ), )

    def __str__(self):
        return self.name


class Spotlight(models.Model):
    scene = models.ForeignKey(
        Scene,
        related_name='spotlights',
        related_query_name='spotlight',
        on_delete=models.CASCADE
    )
    point_x = models.DecimalField(
        max_digits=5,
        decimal_places=2, )
    point_y = models.DecimalField(
        max_digits=5,
        decimal_places=2, )
    product = models.ForeignKey(
        'product.Product',
        related_name='+',
        on_delete=models.CASCADE, )

    def __str__(self):
        return str(self.product)


class Benefit(models.Model):
    name = models.CharField(
        max_length=32,
    )
    text = models.TextField()
    image = VersatileImageField()
    is_active = models.BooleanField(
        default=False,
    )

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_benefits', pgettext_lazy(
                'Permission description', 'Administrar beneficios.'), ), )

    def __str__(self):
        return self.name


class BenefitTranslation(models.Model):
    language_code = models.CharField(
        max_length=10,
    )
    benefit = models.ForeignKey(
        Benefit, related_name='translations',
        on_delete=models.CASCADE,
    )
    text = models.TextField()

    class Meta:
        unique_together = (('language_code', 'benefit'),)

    def __str__(self):
        return f'{self.benefit.name} ({self.language_code})'
