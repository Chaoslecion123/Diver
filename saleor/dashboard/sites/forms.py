from django import forms
from django.contrib.sites.models import Site
from django.utils.translation import pgettext_lazy

from ...site.models import AuthorizationKey, SiteSettings


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = []
        labels = {
            'domain': pgettext_lazy(
                'Domain name (FQDN)', 'Domain name'),
            'name': pgettext_lazy(
                'Display name', 'Display name')}


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'header_text', 'description',
            'track_inventory_by_default', 'default_weight_unit']
        labels = {
            'header_text': pgettext_lazy(
                'Header text', 'Header text'),
            'description': pgettext_lazy(
                'Description', 'Description'),
            'track_inventory_by_default': pgettext_lazy(
                'Inventory tracking by default settings toggle label',
                'Enable inventory tracking for newly created products'),
            'default_weight_unit': pgettext_lazy(
                'Default weight unit', 'Default weight unit')}
        help_texts = {
            'track_inventory_by_default': pgettext_lazy(
                'handle stock by default settings field help text',
                'This will set the default value of stock handling '
                'on product and variant creation')}


class AuthorizationKeyForm(forms.ModelForm):
    class Meta:
        model = AuthorizationKey
        exclude = []
        labels = {
            'key': pgettext_lazy(
                'Key for chosen authorization method', 'Key'),
            'password': pgettext_lazy(
                'Password', 'Password'),
            'name': pgettext_lazy(
                'Item name', 'Name')}
        widgets = {'password': forms.PasswordInput(render_value=True),
                   'key': forms.TextInput(),
                   'site_settings': forms.widgets.HiddenInput()}


# BEGIN :: SoftButterfly Extensions --------------------------------------------
# Payment settings form --------------------------------------------------------
class PaymentSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'cash_payment_enabled',
            'payment_against_delivery_enabled',
        ]
        labels = {
            'cash_payment_enabled': pgettext_lazy(
                'Cash payment enabled field label', 'Enable cash payment '
            ),
            'payment_against_delivery_enabled': pgettext_lazy(
                'Payment against delivery enabled field label', 'Enable payment against delivery'
            ),
        }


# Dashboard style settings form ------------------------------------------------
class DashboardStyleSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'dashboard_logo',
            'dashboard_header_color',
            'dashboard_subheader_color',
            'dashboard_button_color',
            'dashboard_header_text_color',
        ]
        labels = {
            'dashboard_logo': pgettext_lazy(
                'Logo de la tienda para el dashboard', 'Logo'
            ),
            'dashboard_header_color': pgettext_lazy(
                'Color del header', 'Color del header'
            ),
            'dashboard_subheader_color': pgettext_lazy(
                'Color del sub header', 'Color del subheader'
            ),
            'dashboard_button_color': pgettext_lazy(
                'Color del boton añadir', 'Color del boton añadir'
            ),
            'dashboard_header_text_color': pgettext_lazy(
                'Color del texto en el header', 'Color del texto en el header'
            ),
        }


# Storefront style settings form -----------------------------------------------
class StoreStyleSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'store_logo',
            'store_accent_color',
            'store_header_color',
            'store_header_text_color',
        ]
        labels = {
            'store_logo': pgettext_lazy(
                'logo de la tienda', 'Logo'
            ),
            'store_accent_color': pgettext_lazy(
                'store_accent_color', 'Color de acento de la tienda'
            ),
            'store_header_color': pgettext_lazy(
                'store_header_color', 'Color del header de la tienda'
            ),
            'store_header_text_color': pgettext_lazy(
                'store_header_text_color', 'Color del texto en el header de la tienda'
            )
        }


# END :: SoftButterfly Extensions ----------------------------------------------
