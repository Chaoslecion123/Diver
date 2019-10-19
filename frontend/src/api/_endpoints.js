/* global process */
/**
 * API Endpoints
 */
const ROOT =
  process.env.NODE_ENV !== 'production'
    ? '/' // 'http://127.0.0.1:8000/'
    : '/'
export const BASE = ROOT + 'api/'

// Endpoints for autentication process
export const AUTH_SIGNUP = BASE + 'auth/signup/'
export const AUTH_LOGIN = BASE + 'auth/login/'
export const AUTH_SOCIAL_LOGIN = BASE + 'auth/login/social/jwt_user/'
export const AUTH_LOGOUT = BASE + 'auth/logout/'
export const AUTH_USER = BASE + 'auth/user/'
export const AUTH_PASSWORD_RESET = BASE + 'auth/password/reset/confirm/'
export const AUTH_PASSWORD_RECOVERY = BASE + 'auth/password/reset/'

export const TOKEN_VERIFY = BASE + 'token/verify/'
export const TOKEN_REFRESH = BASE + 'token/refresh/'

// Endpoints for system objects
export const ADDRESS = BASE + 'address/'
export const FAVORITE = BASE + 'favorite/'
export const ASSOCIATION = BASE + 'association/'
export const ATTRIBUTE = BASE + 'attribute/'
export const ATTRIBUTE_TRANSLATION = BASE + 'attribute-translation/'
export const ATTRIBUTE_VALUE = BASE + 'attribute-value/'
export const ATTRIBUTE_VALUE_TRANSLATION = BASE + 'attribute-value-translation/'
export const AUTHORIZATION_KEY = BASE + 'authorization-key/'
export const CART = BASE + 'checkout/'
export const CART_LINE = BASE + 'checkout-line/'
export const CATEGORY = BASE + 'category/'
export const CATEGORY_TRANSLATION = BASE + 'category-translation/'
export const CODE = BASE + 'code/'
export const COLLECTION = BASE + 'collection/'
export const COLLECTION_TRANSLATION = BASE + 'collection-translation/'
export const CONTENT_TYPE = BASE + 'content-type/'
export const CONVERSION_RATE = BASE + 'conversion-rate/'
export const CUSTOMER_NOTE = BASE + 'customer-note/'
export const CUSTOMER_REVIEW = BASE + 'customer-review/'
export const BRAND = BASE + 'brand/'
export const FULFILLMENT = BASE + 'fulfillment/'
export const FULFILLMENT_LINE = BASE + 'fulfillment-line/'
export const GROUP = BASE + 'group/'
export const IMPERSONATION_LOG = BASE + 'impersonation-log/'
export const LOG_ENTRY = BASE + 'log-entry/'
export const MENU = BASE + 'menu/'
export const MENU_ITEM = BASE + 'menu-item/'
export const MENU_ITEM_TRANSLATION = BASE + 'menu-item-translation/'
export const NONCE = BASE + 'nonce/'
export const ORDER = BASE + 'order/'
export const ORDER_EVENT = BASE + 'order-event/'
export const ORDER_LINE = BASE + 'order-line/'
export const PAGE = BASE + 'page/'
export const PAGE_TRANSLATION = BASE + 'page-translation/'
export const PARTIAL = BASE + 'partial/'
export const PAYMENT = BASE + 'payment/'
export const PERMISSION = BASE + 'permission/'
export const PRODUCT = BASE + 'product/'
export const PRODUCT_IMAGE = BASE + 'product-image/'
export const PRODUCT_TRANSLATION = BASE + 'product-translation/'
export const PRODUCT_TYPE = BASE + 'product-type/'
export const PRODUCT_VARIANT = BASE + 'product-variant/'
export const PRODUCT_VARIANT_TRANSLATION = BASE + 'product-variant-translation/'
export const RATE_TYPES = BASE + 'rate-types/'
export const SALE = BASE + 'sale/'
export const SCENE = BASE + 'scene/'
export const SESSION = BASE + 'session/'
export const SHIPPING_METHOD = BASE + 'shipping-method/'
export const SHIPPING_METHOD_TRANSLATION = BASE + 'shipping-method-translation/'
export const SHIPPING_ZONE = BASE + 'shipping-zone/'
export const SITE = BASE + 'site/'
export const SITE_SETTINGS = BASE + 'site-settings/'
export const SITE_SETTINGS_TRANSLATION = BASE + 'site-settings-translation/'
export const SLIDE = BASE + 'slide/'
export const SLIDER = BASE + 'slider/'
export const SPOTLIGHT = BASE + 'spotlight/'
export const TASK_RESULT = BASE + 'task-result/'
export const TOKEN = BASE + 'token/'
export const TRANSACTION = BASE + 'transaction/'
export const USER = BASE + 'user/'
export const USER_SOCIAL_AUTH = BASE + 'user-social-auth/'
export const VAT = BASE + 'vat/'
export const VARIANT_IMAGE = BASE + 'variant-image/'
export const VOUCHER = BASE + 'voucher/'
export const VOUCHER_TRANSLATION = BASE + 'voucher-translation/'
export const PHYSICAL_STORE = BASE + 'physical-store/'

export const BANNER = BASE + 'banner/'
export const STOREFRONT_SLIDER = BASE + 'storefront-slider/'

export const CITY = BASE + 'city/'
export const CITY_AREA = BASE + 'city-area/'
export const COUNTRY_AREA = BASE + 'country-area/'