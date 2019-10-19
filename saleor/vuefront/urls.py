from django.views.generic import TemplateView
from django.urls import path, re_path

from .views.storefront import product_detail, category_detail, brand_detail, collection_detail
from .views.error import bad_request, forbidden, not_found, server_error
from .views.page import page_detail


error_urls = [
    path(
        'error/400/',
        bad_request,
        name="error-bad-request"),
    path(
        'error/403/',
        forbidden,
        name="error-forbidden"),
    path(
        'error/404/',
        not_found,
        name="error-not-found"),
    path(
        'error/500/',
        server_error,
        name="error-server-error"), ]

auth_urls = [
    path(
        'auth/',
        TemplateView.as_view(template_name="app.html"),
        name="auth"),
    path(
        'auth/login/',
        TemplateView.as_view(template_name="app.html"),
        name="auth-login"),
    re_path(
        r'^auth/login/(?P<provider>[^/]+)/$',
        TemplateView.as_view(template_name="app.html"),
        name="auth-login-social"),
    path(
        'auth/logout/',
        TemplateView.as_view(template_name="app.html"),
        name="auth-logout"),
    path(
        'auth/signup/',
        TemplateView.as_view(template_name="app.html"),
        name="auth-signup"),
    path(
        'auth/password/recovery/',
        TemplateView.as_view(template_name="app.html"),
        name="auth-password-recovery"),
    re_path(
        r'^auth/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="app.html"),
        name="auth-password-reset"),
]


storefront_urls = [
    path(
        '',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-home"),
    path(
        'index.html',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-home-index"),
    path(
        'search/',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-search"),
    path(
        'product/<slug:slug>/<int:id>/',
        product_detail,
        name="storefront-product"),
    path(
        'category/<slug:slug>/<int:id>/',
        category_detail,
        name="storefront-category"),
    path(
        'collection/<slug:slug>/<int:id>/',
        collection_detail,
        name="storefront-collection"),
    path(
        'brands/',
        TemplateView.as_view(template_name="app.html"),
        name="brand-list"),
    path(
        'brands/<slug:slug>/<int:id>/',
        brand_detail,
        name="brand"),
    path(
        'cart/',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-shpoing-cart"),
    path(
        'cart/checkout/',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-shpoing-cart"),
    path(
        'order/',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-order"),
    path(
        'order/<uuid:token>/',
        TemplateView.as_view(template_name="app.html"),
        name="storefront-order-detail"),
]

profile_urls = [
    path(
        'profile/',
        TemplateView.as_view(template_name="app.html"),
        name='profile'),
    path(
        'profile/my-settings/',
        TemplateView.as_view(template_name="app.html"),
        name='profile-settings'),
    path(
        'profile/my-addresses/',
        TemplateView.as_view(template_name="app.html"),
        name='profile-addresses'),
    path(
        'profile/my-bills/',
        TemplateView.as_view(template_name="app.html"),
        name='profile-bills'),
    path(
        'profile/orders-tracking/',
        TemplateView.as_view(template_name="app.html"),
        name='profile-tracking'),
    path(
        'profile/my-coupons/',
        TemplateView.as_view(template_name="app.html"),
        name='profile-coupons'),
    path(
        'profile/my-orders/',
        TemplateView.as_view(template_name="app.html"),
        name='profile-orders'), ]


account_url = [
    path(
        'account/',
        TemplateView.as_view(template_name="app.html"),
        name='account'),
    path(
        'account/orders/',
        TemplateView.as_view(template_name="app.html"),
        name='account-orders'),
    path(
        'account/order/<uuid:token>/',
        TemplateView.as_view(template_name="app.html"),
        name='account-order-detail'),
    path(
        'account/order/<uuid:token>/tracking/',
        TemplateView.as_view(template_name="app.html"),
        name='account-order-tracking'),
    path(
        'account/addresses/',
        TemplateView.as_view(template_name="app.html"),
        name='account-addresses'),
    path(
        'account/favorites/',
        TemplateView.as_view(template_name="app.html"),
        name='account-favorites'),
    path(
        'account/settings/',
        TemplateView.as_view(template_name="app.html"),
        name='account-settings'),
]

page_urls = [
    path(
        'page/<slug:slug>/',
        page_detail,
        name="page"
    ),
]

urlpatterns = [
    *error_urls,
    *auth_urls,
    *storefront_urls,
    *profile_urls,
    *page_urls,
    *account_url
]
