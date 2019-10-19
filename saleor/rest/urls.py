from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework_jwt import views as jwt_views
from rest_auth import views as rest_auth_views
from saleor.jwt.views import refresh_jwt_token


from .views import (
    SignUpView,
    PasswordResetConfirmView,
    NewsletterSubscriptionViewSet,

    BrandViewSet,
    CollectionViewSet,
    CategoryViewSet,
    ProductViewSet,

    SliderViewSet,
    BannerViewSet,
    SceneViewSet,
    PageViewSet,
    BenefitViewSet,

    AddressViewSet,
    UserViewSet,
    CustomerNoteViewSet,
    ReviewViewSet,
    FavoriteViewSet,

    CountryAreaViewSet,
    CityViewSet,
    CityAreaViewSet,

    AuthorizationKeyViewSet,
    CheckoutLineViewSet,
    CheckoutViewSet,
    CodeViewSet,
    ConversionRateViewSet,
    # culqiCheckout,
    # FulfillmentLineViewSet,
    # FulfillmentViewSet,
    MenuItemViewSet,
    MenuViewSet,
    # NonceViewSet,
    OrderEventViewSet,
    OrderLineViewSet,
    OrderViewSet,
    OrderExtensionViewSet,
    # PaymentViewSet,
    PhysicalStoreViewSet,
    # RateTypesViewSet,
    SaleViewSet,
    # SessionViewSet,
    ShippingMethodViewSet,
    ShippingZoneViewSet,
    SiteSettingsViewSet,
    SiteViewSet,
    # TaskResultViewSet,
    TokenViewSet,
    # TransactionViewSet,
    # VATViewSet,
    VoucherViewSet,
)

auth_urls = [
    path('signup/', SignUpView.as_view(), name='rest_user_details'),

    path('login/', include('rest_social_auth.urls_jwt')),
    path('login/',
        rest_auth_views.LoginView.as_view(),
        name='rest_login'
    ),
    path('logout/',
        rest_auth_views.LogoutView.as_view(),
        name='rest_logout'
    ),
    path(
        'password/reset/',
        rest_auth_views.PasswordResetView.as_view(),
        name='rest_password_reset'
    ),
    path(
        'password/reset/confirm/',
        PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'
    ),
    path(
        'password/change/',
        rest_auth_views.PasswordChangeView.as_view(),
        name='rest_password_change'
    ),
    path(
        'user/',
        rest_auth_views.UserDetailsView.as_view(),
        name='rest_user_details'
    ),
]

token_urls = [
    path('', jwt_views.obtain_jwt_token),
    path('verify/', jwt_views.verify_jwt_token),
    path('refresh/', refresh_jwt_token),
]

diver_urls = routers.DefaultRouter()

diver_urls.register(r'^address', AddressViewSet)
diver_urls.register(r'^newsletter-subscription', NewsletterSubscriptionViewSet)

diver_urls.register(r'^authorization-key', AuthorizationKeyViewSet)
diver_urls.register(r'^brand', BrandViewSet)
diver_urls.register(r'^checkout-line', CheckoutLineViewSet)
diver_urls.register(r'^checkout', CheckoutViewSet)
diver_urls.register(r'^code', CodeViewSet)
diver_urls.register(r'^conversion-rate', ConversionRateViewSet)
diver_urls.register(r'^customer-note', CustomerNoteViewSet)

diver_urls.register(r'^customer-review', ReviewViewSet)
diver_urls.register(r'^favorite', FavoriteViewSet)

diver_urls.register(r'^city', CityViewSet)
diver_urls.register(r'^city-area', CityAreaViewSet)
diver_urls.register(r'^country-area', CountryAreaViewSet)

# diver_urls.register(r'^fulfillment-line', FulfillmentLineViewSet)
# diver_urls.register(r'^fulfillment', FulfillmentViewSet)
diver_urls.register(r'^menu-item', MenuItemViewSet)
diver_urls.register(r'^menu', MenuViewSet)
# diver_urls.register(r'^nonce', NonceViewSet)
diver_urls.register(r'^order-event', OrderEventViewSet)
diver_urls.register(r'^order-line', OrderLineViewSet)
diver_urls.register(r'^order', OrderViewSet)
diver_urls.register(r'^order-extension', OrderExtensionViewSet)

diver_urls.register(r'^page', PageViewSet)
# diver_urls.register(r'^payment', PaymentViewSet)
diver_urls.register(r'^physical-store', PhysicalStoreViewSet)
# diver_urls.register(r'^rate-types', RateTypesViewSet)
diver_urls.register(r'^sale', SaleViewSet)
diver_urls.register(r'^scene', SceneViewSet)
# diver_urls.register(r'^session', SessionViewSet)
diver_urls.register(r'^shipping-method', ShippingMethodViewSet)
diver_urls.register(r'^shipping-zone', ShippingZoneViewSet)
diver_urls.register(r'^site-settings', SiteSettingsViewSet)
diver_urls.register(r'^site', SiteViewSet)
# diver_urls.register(r'^task-result', TaskResultViewSet)
diver_urls.register(r'^token', TokenViewSet)
# diver_urls.register(r'^transaction', TransactionViewSet)
diver_urls.register(r'^user', UserViewSet)
# diver_urls.register(r'^vat', VATViewSet)
diver_urls.register(r'^voucher', VoucherViewSet)

diver_urls.register(r'^collection', CollectionViewSet)
diver_urls.register(r'^category', CategoryViewSet)
diver_urls.register(r'^product', ProductViewSet)

diver_urls.register(r'^banner', BannerViewSet)
diver_urls.register(r'^slider', SliderViewSet)
diver_urls.register(r'^benefit', BenefitViewSet)

diver_urls = diver_urls.urls

app_name = 'api'
urlpatterns = [
    path('auth/', include((auth_urls, 'auth'), namespace='auth')),
    path('token/', include((token_urls, 'token'), namespace='token')),
    # path('culqi/checkout/', culqiCheckout, name="culqi"),
    path('', include((diver_urls, 'diver'), namespace='diver-api')),
]
