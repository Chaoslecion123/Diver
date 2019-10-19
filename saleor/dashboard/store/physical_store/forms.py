from django import forms
from django.utils.translation import pgettext_lazy

from ....store.models import PhysicalStore
from ....glovo.models import GlovoDeliveryPermission
from ....runningbox.models import RunningBoxDeliveryPermission
from ....account.models import Address
from ....geoposition.widgets import GeopositionWidget


class PhysicalStoreForm(forms.ModelForm):
    class Meta:
        model = PhysicalStore
        fields = [
            'site',
            'name',
            'is_main_store',
        ]

        labels = {
            'site': pgettext_lazy(
                'Physical store field name', 'Site', ),
            'name': pgettext_lazy(
                'Physical store field name', 'Name', ),
            'is_main_store': pgettext_lazy(
                'Physical store field name', 'Is main store', ), }

        widgets = {
            'site': forms.widgets.HiddenInput(),
        }


class GlovoDeliveryPermissionForm(forms.ModelForm):
    class Meta:
        model = GlovoDeliveryPermission
        fields = [
            'glovo_enabled',
            'store',
        ]

        labels = {
            'glovo_enabled': pgettext_lazy('Glovo form field name', 'Delivery con Glovo')
        }


class RunningBoxDeliveryPermissionForm(forms.ModelForm):
    class Meta:
        model = RunningBoxDeliveryPermission
        fields = [
            'runningbox_enabled',
            'store',
        ]

        labels = {
            'runningbox_enabled': pgettext_lazy('RunningBox form field name', 'Delivery con RunningBox')
        }

class RunningBoxDeliveryPermissionForm(forms.ModelForm):
    class Meta:
        model = RunningBoxDeliveryPermission
        fields = [
            'enabled',
            'store',
        ]

        widgets = {
            'hidden': GeopositionWidget(),
        }

        labels = {
            'enabled': pgettext_lazy('Glovo form field name', 'Delivery con Glovo')
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            # 'first_name',
            # 'last_name',
            # 'company_name',
            'street_address_1',
            'street_address_2',
            'city',
            'city_area',
            'country_area',
            'country',
            'postal_code',
            # 'phone',
            'position',
        ]

        widgets = {
            'position': GeopositionWidget(),
        }
