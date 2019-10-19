from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.benefit_list, name='benefit-list'),
    url(r'^add/$',
        views.benefit_create, name='benefit-create'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        views.benefit_edit, name='benefit-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.benefit_delete, name='benefit-delete'),
]
