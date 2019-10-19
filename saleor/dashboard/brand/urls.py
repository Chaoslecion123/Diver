from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.brand_list, name='brand-list'),
    url(r'^add/$', views.brand_create, name='brand-add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.brand_update, name='brand-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.brand_delete, name='brand-delete')
]
