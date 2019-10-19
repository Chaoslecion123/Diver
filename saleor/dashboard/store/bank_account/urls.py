from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<site_settings_pk>\d+)/bank-account/add/$',
        views.bank_account_add, name='bank-account-add'),
    url(r'^(?P<site_settings_pk>\d+)/bank-account/'
        r'(?P<pk>\d+)/update/$',
        views.bank_account_edit, name='bank-account-edit'),
    url(r'^(?P<site_settings_pk>\d+)/bank-account/'
        r'(?P<pk>\d+)/delete/$',
        views.bank_account_delete, name='bank-account-delete')
]
