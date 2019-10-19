from django.conf.urls import url

from . import views


urlpatterns = [
    # Scenes views -------------------------------------------------------------
    url(r'^$',
        views.scene_list, name='scene-list'),
    url(r'^scene/(?P<pk>[0-9]+)/$',
        views.scene_details, name='scene-details'),
    url(r'^add/$',
        views.scene_create, name='scene-create'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        views.scene_edit, name='scene-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.scene_delete, name='scene-delete'),

    # Spotlight views ----------------------------------------------------------
    url(
        r'^(?P<scene_pk>[0-9]+)/spotlight/add/$',
        views.spotlight_create, name='spotlight-create', ),
    url(
        r'^(?P<scene_pk>[0-9]+)/spotlight/(?P<spotlight_pk>[0-9]+)/edit/$',
        views.spotlight_edit, name='spotlight-edit', ),
    url(
        r'^(?P<scene_pk>[0-9]+)/spotlight/(?P<spotlight_pk>[0-9]+)/delete/$',
        views.spotlight_delete, name='spotlight-delete', )
]
