from django.db import models
from django.db.models.signals import post_save
from django.contrib.sites.models import Site
from django.utils.translation import pgettext_lazy

from ..core.models import SortableModel
from ..page.models import Page
from ..site.models import SiteSettings
from ..account.models import PossiblePhoneNumberField
from . import SocialNetworkProvider, PageType, BankProvider


class PhysicalStore(models.Model):
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name='physical_stores',
        related_query_name='physical_store')
    name = models.CharField(
        max_length=256)
    address = models.ForeignKey(
        'account.Address',
        on_delete=models.CASCADE,
        related_name='physical_stores',
        related_query_name='physical_store',
        blank=True)
    is_main_store = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', )
        permissions = (
            ('manage_physical_stores', pgettext_lazy(
                'Permission description', 'Manage sliders.'), ), )

    def __str__(self):
        return self.name

    def set_as_main_store(self):
        self.is_main_store = True
        self.save()

    @classmethod
    def post_save_handler(cls, instance, **kwargs):  # pylint: disable=W0613
        if instance.is_main_store:
            cls.objects.exclude(pk=instance.pk).update(is_main_store=False)


post_save.connect(
    PhysicalStore.post_save_handler,
    sender=PhysicalStore
)


class Phone(models.Model):
    physical_store = models.ForeignKey(
        PhysicalStore,
        on_delete=models.CASCADE,
        related_name='phones',
        related_query_name='phone')
    number = PossiblePhoneNumberField(
        blank=True,
        default='')

    def __str__(self):
        return '%s - %s' % (self.physical_store - self.number)


class SocialNetwork(models.Model):
    site_settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name='social_networks',
        related_query_name='social_network')
    provider = models.CharField(
        max_length=20,
        choices=SocialNetworkProvider.CHOICES)
    link = models.URLField(
        max_length=256)

    class Meta:
        unique_together = (('site_settings', 'provider'),)

    def __str__(self):
        return '%s: %s' % (self.provider.title(), self.link)


class SpecialPage(models.Model):
    site_settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name='special_pages',
        related_query_name='special_page')
    type = models.CharField(
        max_length=32,
        choices=PageType.CHOICES)
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='site_settings',
        related_query_name='site_setting')

    class Meta:
        unique_together = (('site_settings', 'type'),)

    def __str__(self):
        return '%s: %s' % (self.type.title(), self.page.title)


class BankAccount(models.Model):
    site_settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name='bank_accounts',
        related_query_name='bank_account')
    provider = models.CharField(
        max_length=32,
        choices=BankProvider.CHOICES)
    number = models.CharField(
        max_length=256)

    class Meta:
        unique_together = (('site_settings', 'number'),)

    def __str__(self):
        return '%s: %s' % (self.provider_short_name, self.number)

    @property
    def provider_short_name(self):
        return BankProvider.SHORTNAMES[self.provider]


class FooterItem(SortableModel):
    site_settings = models.ForeignKey(
        'site.SiteSettings',
        related_name='footer_items',
        on_delete=models.CASCADE
    )

    menu = models.ForeignKey(
        'menu.Menu',
        on_delete=models.CASCADE,
        related_name='+',
    )

    class Meta:
        ordering = ('sort_order', )

    def __str__(self):
        return f"Menu: {self.menu.name}"

    def get_ordering_queryset(self):
        return self.site_settings.footer_items.all()
