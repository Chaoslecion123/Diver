import { namespacedRoute, verifyShoppingCart } from './_utils.js'
import STOREFRONT from '@/views/Storefront'

export const NAMESPACE = 'storefront'
export const STOREFRONT_INDEX = namespacedRoute(NAMESPACE, 'index')
export const STOREFRONT_SEARCH = namespacedRoute(NAMESPACE, 'search')

export const STOREFRONT_PRODUCT = namespacedRoute(NAMESPACE, 'product')
export const STOREFRONT_CATEGORY = namespacedRoute(NAMESPACE, 'category')

export const STOREFRONT_CART = namespacedRoute(NAMESPACE, 'cart')
export const STOREFRONT_CART_CHECKOUT = namespacedRoute(NAMESPACE, 'checkout')

export const STOREFRONT_ORDER = namespacedRoute(NAMESPACE, 'order')
export const STOREFRONT_ORDER_DETAIL = namespacedRoute(NAMESPACE, 'order', [
  'detail'
])

export const STOREFRONT_BRAND_LIST = namespacedRoute(NAMESPACE, 'brand-list')
export const STOREFRONT_BRAND = namespacedRoute(NAMESPACE, 'brand')

// export const STOREFRONT_COLLECTION = namespacedRoute(NAMESPACE, 'collection')

export default [
  {
    name: NAMESPACE,
    path: '',
    component: () => import('@/views/Base'),
    redirect: {
      name: STOREFRONT_INDEX
    },
    children: [
      {
        name: STOREFRONT_INDEX,
        path: '/',
        component: () => import('@/views/Storefront/Home')
      },
      {
        name: STOREFRONT_SEARCH,
        path: '/search',
        component: () => import('@/views/Storefront/Search')
      },
      {
        name: STOREFRONT_PRODUCT,
        path: '/product/:slug/:id',
        component: () => import('@/views/Storefront/Product'),
        // INICIO
        meta: {
          breadcrumbs: [
            {
              text: 'Inicio',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            },
            {
              text: 'Categorias',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            }
          ]
        }
        // FIN
      },
      {
        name: STOREFRONT_CATEGORY,
        path: '/category/:slug/:id',
        component: () => import('@/views/Storefront/Category'),
        // INICIO
        meta: {
          breadcrumbs: [
            {
              text: 'Inicio',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            },
            {
              text: 'Categorias',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            }
          ]
        }
        // FIN
      },
      {
        name: STOREFRONT_BRAND_LIST,
        path: '/brands',
        component: () => import('@/views/Storefront/BrandList'),
        meta: {
          breadcrumbs: [
            {
              text: 'Inicio',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            },
            {
              text: 'Marcas',
              disabled: false,
              href: {
                name: STOREFRONT_BRAND_LIST
              }
            }
          ]
        }
      },
      {
        name: STOREFRONT_BRAND,
        path: '/brands/:slug/:id',
        component: () => import('@/views/Storefront/Brand'),
        meta: {
          breadcrumbs: [
            {
              text: 'Inicio',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            },
            {
              text: 'Marcas',
              disabled: false,
              href: {
                name: STOREFRONT_BRAND_LIST
              }
            }
          ]
        }
      },
      {
        name: STOREFRONT_CART,
        path: '/cart',
        component: () => import('@/views/Storefront/Cart'),
        meta: {
          breadcrumbs: [
            {
              text: 'Inicio',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            },
            {
              text: 'Mi carrito',
              disabled: true,
              href: {
                name: STOREFRONT_CART
              }
            }
          ]
        }
      },
      {
        name: STOREFRONT_CART_CHECKOUT,
        path: '/cart/checkout',
        beforeEnter: verifyShoppingCart,
        component: () => import('@/views/Storefront/Checkout'),
        meta: {
          breadcrumbs: [
            {
              text: 'Inicio',
              disabled: false,
              href: {
                name: STOREFRONT_INDEX
              }
            },
            {
              text: 'Mi carrito',
              disabled: false,
              href: {
                name: STOREFRONT_CART
              }
            },
            {
              text: 'Checkout',
              disabled: true,
              href: {
                name: STOREFRONT_CART_CHECKOUT
              }
            }
          ]
        }
      },
      {
        name: STOREFRONT_ORDER,
        path: '/order',
        component: () => import('@/views/Storefront/Order')
      },
      {
        name: STOREFRONT_ORDER_DETAIL,
        path: '/order/:id',
        component: () => import('@/views/Storefront/OrderDetail')
      },
      {
        name: 'Compras',
        path: '/compras',
        component: () => import('@/views/Storefront/Compras')
      },
      {
        name: 'Favorite',
        path: '/favorito',
        component: STOREFRONT.Favorite
      },
      {
        name: 'Store',
        path: '/tienda',
        component: STOREFRONT.Store
      },
      {
        name: 'FeaturedBrandProducts',
        path: '/tienda/:id',
        component: STOREFRONT.Store
      },
      {
        name: 'Tracking',
        path: '/tracking',
        component: STOREFRONT.Tracking
      },
      {
        name: 'Policies',
        path: '/terms-and-conditions',
        component: STOREFRONT.Policies
      }
    ]
  }
]

// export default [
//   {
//     name: STOREFRONT_INDEX,
//     path: '/storefront',
//     component: () => import('@/views/NewStorefront/Index')
//   },
//   {
//     name: STOREFRONT_CATEGORY,
//     path: '/storefront/category/:slug/:id',
//     component: () => import('@/views/NewStorefront/Category')
//   },
//   {
//     name: STOREFRONT_COLLECTION,
//     path: '/storefront/collection/:slug/:id',
//     component: () => import('@/views/NewStorefront/Collection')
//   },
//   {
//     name: STOREFRONT_PRODUCT,
//     path: '/storefront/product/:slug/:id',
//     component: () => import('@/views/NewStorefront/Product')
//   }
// ]
