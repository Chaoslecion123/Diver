from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<site_settings_pk>\d+)/special-page/add/$',
        views.special_page_add, name='special-page-add'),
    url(r'^(?P<site_settings_pk>\d+)/special-page/'
        r'(?P<pk>\d+)/update/$',
        views.special_page_edit, name='special-page-edit'),
    url(r'^(?P<site_settings_pk>\d+)/special-page/'
        r'(?P<pk>\d+)/delete/$',
        views.special_page_delete, name='special-page-delete')
]
