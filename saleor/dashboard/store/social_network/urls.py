from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<site_settings_pk>\d+)/social-network/add/$',
        views.social_network_add, name='social-network-add'),
    url(r'^(?P<site_settings_pk>\d+)/social-network/'
        r'(?P<pk>\d+)/update/$',
        views.social_network_edit, name='social-network-edit'),
    url(r'^(?P<site_settings_pk>\d+)/social-network/'
        r'(?P<pk>\d+)/delete/$',
        views.social_network_delete, name='social-network-delete')
]
