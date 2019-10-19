from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.banner_list, name='banner-list'),
    # url(r'^banner/(?P<pk>[0-9]+)/$',
    #     views.banner_details, name='banner-details'),
    url(r'^add/$',
        views.banner_create, name='banner-create'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        views.banner_edit, name='banner-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.banner_delete, name='banner-delete'),
]
