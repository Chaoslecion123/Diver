from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<site_settings_pk>\d+)/footer-item/add/$',
        views.footer_item_add,
        name='footer-item-add',
    ),
    url(
        r'^(?P<site_settings_pk>\d+)/footer-item/(?P<pk>\d+)/update/$',
        views.footer_item_edit,
        name='footer-item-edit',
    ),
    url(
        r'^(?P<site_settings_pk>\d+)/footer-item/(?P<pk>\d+)/delete/$',
        views.footer_item_delete,
        name='footer-item-delete',
    ),
    url(
        r'^(?P<site_settings_pk>\d+)/footer-item/reorder/$',
        views.ajax_reorder_footer_items,
        name='ajax-reorder-footer-items',
    ),
]
