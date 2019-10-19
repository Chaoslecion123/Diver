import json

from django.contrib.sites.models import Site
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext_lazy
from versatileimagefield.fields import VersatileImageField
from colorfield.fields import ColorField
from ..core.utils.translations import TranslationProxy
from ..core.weight import WeightUnits
from . import AuthenticationBackends
from .patch_sites import patch_contrib_sites

patch_contrib_sites()


# BEGIN :: SoftButterfly Extensions --------------------------------------------
def site_settings_dashboard_logo_upload_to(instance, filename):
    filename = 'logo.png'
    domain = instance.site.domain.split(':')[0]
    return '/'.join(['dashboard-logo', domain, filename])


def site_settings_store_logo_upload_to(instance, filename):
    filename = 'logo.png'
    domain = instance.site.domain.split(':')[0]
    return '/'.join(['store-logo', domain, filename])
# END :: SoftButterfly Extensions ----------------------------------------------


class SiteSettings(models.Model):
    site = models.OneToOneField(
        Site,
        related_name='settings',
        on_delete=models.CASCADE, )
    header_text = models.CharField(
        max_length=200,
        blank=True, )
    description = models.CharField(
        max_length=500,
        blank=True, )
    top_menu = models.ForeignKey(
        'menu.Menu',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True, )
    bottom_menu = models.ForeignKey(
        'menu.Menu',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True, )
    include_taxes_in_prices = models.BooleanField(
        default=True, )
    display_gross_prices = models.BooleanField(
        default=True, )
    charge_taxes_on_shipping = models.BooleanField(
        default=True, )
    track_inventory_by_default = models.BooleanField(
        default=True, )
    homepage_collection = models.ForeignKey(
        'product.Collection',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True, )
    default_weight_unit = models.CharField(
        max_length=10,
        choices=WeightUnits.CHOICES,
        default=WeightUnits.KILOGRAM, )
    automatic_fulfillment_digital_products = models.BooleanField(
        default=False, )
    default_digital_max_downloads = models.IntegerField(
        blank=True,
        null=True, )
    default_digital_url_valid_days = models.IntegerField(
        blank=True,
        null=True, )

    # BEGIN :: SoftButterfly Extensions ----------------------------------------
    # Dashboard style settings -------------------------------------------------
    dashboard_logo = VersatileImageField(
        upload_to=site_settings_dashboard_logo_upload_to,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'png', ], ), ], )
    dashboard_header_color = ColorField(
        default='#2784FF',
        blank=True, )
    dashboard_subheader_color = ColorField(
        default='#4796FC',
        blank=True, )
    dashboard_header_text_color = ColorField(
        default='#FFFFFF',
        blank=True, )
    dashboard_button_color = ColorField(
        default='#00BCD4',
        blank=True, )

    # Store style settings -----------------------------------------------------
    store_logo = VersatileImageField(
        upload_to=site_settings_store_logo_upload_to,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'png',
                ],
            ),
        ],
    )
    store_accent_color = ColorField(
        default='#2784FF',
        blank=True,
    )
    store_header_color = ColorField(
        default='#2784FF',
        blank=True,
    )
    store_header_text_color = ColorField(
        default='#FFFFFF',
        blank=True,
    )

    # Storefront settings ------------------------------------------------------
    store_logo = VersatileImageField(
        upload_to=site_settings_store_logo_upload_to,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'png',
                ],
            ),
        ],
    )
    store_accent_color = ColorField(
        default='#2784FF',
        blank=True,
    )
    store_header_color = ColorField(
        default='#2784FF',
        blank=True,
    )
    store_header_text_color = ColorField(
        default='#FFFFFF',
        blank=True,
    )

    # Store business settings --------------------------------------------------
    # business_name = models.CharField(
    #     max_length=256,
    #     blank=True, )

    # business_tax_id = models.CharField(
    #     max_length=256,
    #     blank=True, )

    # Aditional payment settings -----------------------------------------------
    cash_payment_enabled = models.BooleanField(default=True)
    payment_against_delivery_enabled = models.BooleanField(default=True)

    # END :: SoftButterfly Extensions ------------------------------------------

    translated = TranslationProxy()

    class Meta:
        permissions = (
            (
                'manage_settings',
                pgettext_lazy(
                    'Permission description',
                    'Manage settings.'
                )
            ),
            (
                'manage_translations',
                pgettext_lazy(
                    'Permission description',
                    'Manage translations.'
                )
            ),
        )

    def __str__(self):
        return self.site.name

    def available_backends(self):
        return self.authorizationkey_set.values_list('name', flat=True)

    # BEGIN :: SoftButterfly Extensions ----------------------------------------
    # Payment settings ---------------------------------------------------------
    def payment(self):
        payments = {
            'cashPayment': {
                'enabled': self.cash_payment_enabled and self.bank_accounts.exists(),
                'bankAccounts': None
            },
            'deliveryPayment': {
                'enabled': self.payment_against_delivery_enabled,
            },
        }

        if payments['cashPayment']['enabled']:
            payments['cashPayment']['bankAccounts'] = [
                {
                    'number': bank_account.number,
                    'provider': bank_account.provider_short_name,
                } for bank_account in self.bank_accounts.all()
            ]

        return json.dumps(payments)

    # Storefront settings ------------------------------------------------------
    def dashboard_css(self):
        return mark_safe(f'''
            <style>
                .top-nav {{
                    background: {self.dashboard_header_color};
                }}
                .top-nav.subheader {{
                    background: {self.dashboard_subheader_color};
                }}
                .btn-fab-default, .btn-fab-presentation {{
                    background: {self.dashboard_button_color};
                }}
                .btn-fab-default:hover,
                .btn-fab-presentation:hover {{
                    background: {self.dashboard_button_color};
                }}
                header .top-nav #toggle-menu svg path {{
                    fill: {self.dashboard_header_text_color};
                }}
                .hide-on-small-only svg {{
                    fill: {self.dashboard_header_text_color};
                }}
                header .top-nav .dropdown-button svg {{
                    fill: {self.dashboard_header_text_color};
                }}
                .nav-wrapper .input-field input[type=search]::placeholder {{
                    color: {self.dashboard_header_text_color};
                }}
                .breadcrumbs li {{
                    color: {self.dashboard_header_text_color};
                }}
                .breadcrumbs li a {{
                    color: {self.dashboard_header_text_color};
                }}
                .breadcrumbs li a:hover {{
                    color: {self.dashboard_header_text_color};
                }}
                .breadcrumb:last-child {{
                    color: {self.dashboard_header_text_color};
                }}
                .breadcrumbs li.back-mobile svg {{
                    fill: {self.dashboard_header_text_color};
                }}
                #search:focus {{
                    border-bottom: 1px solid {self.dashboard_button_color};
                    box-shadow: 0 1px 0 0 {self.dashboard_button_color};
                }}
                .pagination li.active {{
                    background-color: {self.dashboard_button_color};
                }}
                @media (max-width: 600px) {{
                    .search {{
                        background: {self.dashboard_button_color};
                    }}
                }}
            </style>
        ''')

    @property
    def facebook_key(self):
        facebook = self.authorizationkey_set.filter(name=AuthenticationBackends.FACEBOOK)
        if facebook.exists():
            return facebook.first().key

        return None

    @property
    def google_key(self):
        google = self.authorizationkey_set.filter(name=AuthenticationBackends.GOOGLE)
        if google.exists():
            return google.first().key

        return None

    # END :: SoftButterfly Extensions ------------------------------------------


class SiteSettingsTranslation(models.Model):
    site_settings = models.ForeignKey(
        SiteSettings,
        related_name='translations',
        on_delete=models.CASCADE
    )
    language_code = models.CharField(
        max_length=10
    )
    header_text = models.CharField(
        max_length=200,
        blank=True
    )
    description = models.CharField(
        max_length=500,
        blank=True
    )

    class Meta:
        unique_together = (
            ('language_code', 'site_settings'),
        )

    def __repr__(self):
        class_ = type(self)
        return '%s(pk=%r, site_settings_pk=%r)' % (
            class_.__name__, self.pk, self.site_settings_id)

    def __str__(self):
        return self.site_settings.site.name


class AuthorizationKey(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20, choices=AuthenticationBackends.BACKENDS)
    key = models.TextField()
    password = models.TextField()

    class Meta:
        unique_together = (('site_settings', 'name'),)

    def __str__(self):
        return self.name

    def key_and_secret(self):
        return self.key, self.password
