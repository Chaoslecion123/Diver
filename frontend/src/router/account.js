import { namespacedRoute, verifyAuth } from './_utils.js'
import { STOREFRONT_INDEX } from './storefront'

export const NAMESPACE = 'account'
export const ACCOUNT_ORDERS = namespacedRoute(NAMESPACE, 'orders')
export const ACCOUNT_ORDER_DETAIL = namespacedRoute(NAMESPACE, 'order', [
  'detail'
])
export const ACCOUNT_ORDER_TRACKING = namespacedRoute(NAMESPACE, 'order', [
  'tracking'
])
export const ACCOUNT_COUPONS = namespacedRoute(NAMESPACE, 'coupons')
export const ACCOUNT_TRACKING = namespacedRoute(NAMESPACE, 'tracking')
export const ACCOUNT_ADDRESSES = namespacedRoute(NAMESPACE, 'addresses')
export const ACCOUNT_FAVORITES = namespacedRoute(NAMESPACE, 'favorites')
export const ACCOUNT_SETTINGS = namespacedRoute(NAMESPACE, 'settings')

export default [
  {
    path: '/account',
    name: NAMESPACE,
    component: () => import('@/views/Base'),
    beforeEnter: verifyAuth,
    redirect: {
      name: ACCOUNT_ORDERS
    },
    children: [
      {
        path: '/account/orders',
        name: ACCOUNT_ORDERS,
        component: () => import('@/views/Account/Base'),
        props: {
          contentComponent: () => import('@/views/Account/Orders')
        },
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
              text: 'Mi cuenta',
              disabled: false,
              href: {
                name: NAMESPACE
              }
            },
            {
              text: 'Mis pedidos',
              disabled: true,
              href: {
                name: ACCOUNT_ORDERS
              }
            }
          ]
        }
      },
      {
        path: '/account/order/:id',
        name: ACCOUNT_ORDER_DETAIL,
        component: () => import('@/views/Account/Base'),
        props: {
          contentComponent: () => import('@/views/Account/OrderDetail')
        },
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
              text: 'Mi cuenta',
              disabled: false,
              href: {
                name: NAMESPACE
              }
            },
            {
              text: 'Mis pedidos',
              disabled: false,
              href: {
                name: ACCOUNT_ORDERS
              }
            },
            {
              text: 'Detalles',
              disabled: true,
              href: {
                name: ACCOUNT_ORDERS
              }
            }
          ]
        }
      },
      {
        path: '/account/order/:id/tracking',
        name: ACCOUNT_ORDER_TRACKING,
        component: () => import('@/views/Account/Base'),
        props: {
          contentComponent: () => import('@/views/Account/OrderTracking')
        },
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
              text: 'Mi cuenta',
              disabled: false,
              href: {
                name: NAMESPACE
              }
            },
            {
              text: 'Mis pedidos',
              disabled: false,
              href: {
                name: ACCOUNT_ORDERS
              }
            },
            {
              text: 'Seguimiento',
              disabled: true,
              href: {
                name: ACCOUNT_ORDERS
              }
            }
          ]
        }
      },
      {
        path: '/account/addresses',
        name: ACCOUNT_ADDRESSES,
        component: () => import('@/views/Account/Base'),
        props: {
          contentComponent: () => import('@/views/Account/Addresses')
        },
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
              text: 'Mi cuenta',
              disabled: false,
              href: {
                name: NAMESPACE
              }
            },
            {
              text: 'Mis direcciones',
              disabled: true,
              href: {
                name: ACCOUNT_ADDRESSES
              }
            }
          ]
        }
      },
      {
        path: '/account/favorites',
        name: ACCOUNT_FAVORITES,
        component: () => import('@/views/Account/Base'),
        props: {
          contentComponent: () => import('@/views/Account/Favorites')
        },
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
              text: 'Mi cuenta',
              disabled: false,
              href: {
                name: NAMESPACE
              }
            },
            {
              text: 'Mis favoritos',
              disabled: true,
              href: {
                name: ACCOUNT_FAVORITES
              }
            }
          ]
        }
      },
      {
        path: '/account/settings',
        name: ACCOUNT_SETTINGS,
        component: () => import('@/views/Account/Base'),
        props: {
          contentComponent: () => import('@/views/Account/Settings')
        },
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
              text: 'Mi cuenta',
              disabled: false,
              href: {
                name: NAMESPACE
              }
            },
            {
              text: 'Configuración',
              disabled: true,
              href: {
                name: ACCOUNT_SETTINGS
              }
            }
          ]
        }
      }
    ]
  }
]
