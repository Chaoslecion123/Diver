from django.conf.urls import url

from . import views


urlpatterns = [
    # Sliders views ------------------------------------------------------------
    url(
        r'^$',
        views.slider_list,
        name='slider-list', ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.slider_detail,
        name='slider-details', ),
    url(
        r'^add/$',
        views.slider_add,
        name='slider-add', ),
    url(
        r'^(?P<pk>[0-9]+)/edit/$',
        views.slider_edit,
        name='slider-edit', ),
    url(
        r'^(?P<pk>[0-9]+)/delete/$',
        views.slider_delete,
        name='slider-delete', ),

    # Slides views -------------------------------------------------------------
    url(
        r'^(?P<slider_pk>[0-9]+)/slide/add/$',
        views.slide_create,
        name='slide-create', ),
    url(
        r'^(?P<slider_pk>[0-9]+)/slide/(?P<slide_pk>[0-9]+)/edit/$',
        views.slide_edit,
        name='slide-edit', ),
    url(
        r'^(?P<slider_pk>[0-9]+)/slide/(?P<slide_pk>[0-9]+)/delete/$',
        views.slide_delete,
        name='slide-delete', ),
    url(
        r'^(?P<slider_pk>[0-9]+)/slides/reorder/$',
        views.ajax_reorder_slides,
        name='ajax-reorder-slides', ),
]
