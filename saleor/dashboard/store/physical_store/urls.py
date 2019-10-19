from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.physical_store_list, name='physical-store-list'),
    # url(r'^(?P<pk>[0-9]+)/$',
    #     views.physical_store_details, name='physical-store-details'),
    url(r'^add/$',
        views.physical_store_create, name='physical-store-create'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        views.physical_store_edit, name='physical-store-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.physical_store_delete, name='physical-store-delete'),
]
