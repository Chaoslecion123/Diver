from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from . import views as core_views
from .category.urls import urlpatterns as category_urls
from .collection.urls import urlpatterns as collection_urls
from .customer.urls import urlpatterns as customer_urls
from .discount.urls import urlpatterns as discount_urls
from .menu.urls import urlpatterns as menu_urls
from .order.urls import urlpatterns as order_urls
from .page.urls import urlpatterns as page_urls
from .product.urls import urlpatterns as product_urls
from .search.urls import urlpatterns as search_urls
from .shipping.urls import urlpatterns as shipping_urls
from .sites.urls import urlpatterns as site_urls
from .staff.urls import urlpatterns as staff_urls
from .taxes.urls import urlpatterns as taxes_urls
# BEGIN :: SoftButterfly Extensions --------------------------------------------
from .brand.urls import urlpatterns as brand_urls
from .widget.slider.urls import urlpatterns as slider_urls
from .widget.banner.urls import urlpatterns as banner_urls
from .widget.scene.urls import urlpatterns as scene_urls
from .widget.benefit.urls import urlpatterns as benefit_urls
from .store.physical_store.urls import urlpatterns as store_urls
from .store.social_network.urls import urlpatterns as social_network_urls
from .store.special_page.urls import urlpatterns as special_page_urls
from .store.bank_account.urls import urlpatterns as bank_account_urls
from .store.footer_item.urls import urlpatterns as footer_item_urls
# END :: SoftButterfly Extensions ----------------------------------------------


urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^categories/', include(category_urls)),
    url(r'^collections/', include(collection_urls)),
    url(r'^orders/', include(order_urls)),
    url(r'^page/', include(page_urls)),
    url(r'^products/', include(product_urls)),
    url(r'^customers/', include(customer_urls)),
    url(r'^staff/', include(staff_urls)),
    url(r'^discounts/', include(discount_urls)),
    url(r'^settings/', include(
        site_urls + social_network_urls
        + special_page_urls + bank_account_urls + footer_item_urls)),  # Extensions
    url(r'^menu/', include(menu_urls)),
    url(r'^shipping/', include(shipping_urls)),
    url(r'^style-guide/', core_views.styleguide, name='styleguide'),
    url(r'^search/', include(search_urls)),
    url(r'^taxes/', include(taxes_urls)),
    url(r'^next/', TemplateView.as_view(template_name='dashboard/next.html')),
    # BEGIN :: SoftButterfly Extensions ----------------------------------------
    url(r'^brand/', include(brand_urls)),
    url(r'^slider/', include(slider_urls)),
    url(r'^banner/', include(banner_urls)),
    url(r'^scene/', include(scene_urls)),
    url(r'^store/', include(store_urls)),
    url(r'^benefit/', include(benefit_urls)),
    # END :: SoftButterfly Extensions ------------------------------------------
]
