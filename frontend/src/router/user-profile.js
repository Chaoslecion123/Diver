import { verifyAuth } from './_utils.js'
import User from '@/views/UserProfile'

export const NAMESPACE = 'user-profile'
export const PROFILE_SETTINGS = `${NAMESPACE}:settings`
export const PROFILE_ADDRESSES = `${NAMESPACE}:addresses`
export const PROFILE_BILLS = `${NAMESPACE}:bills`
export const PROFILE_ORDERS = `${NAMESPACE}:orders`
export const PROFILE_TRACKING = `${NAMESPACE}:tracking`
export const PROFILE_COUPONS = `${NAMESPACE}:coupons`

export default [
  {
    name: NAMESPACE,
    path: '/profile',
    beforeEnter: verifyAuth,
    redirect: {
      name: PROFILE_SETTINGS
    },
    component: () => import('@/views/Base'),
    children: [
      {
        path: '',
        components: {
          default: User.profile,
          helper: User.settings
        },
        children: [
          {
            name: PROFILE_SETTINGS,
            path: '/profile/my-settings',
            components: {
              default: User.profile,
              helper: User.settings
            }
          },
          {
            name: PROFILE_ADDRESSES,
            path: '/profile/my-addresses',
            components: {
              default: User.profile,
              helper: User.addresses
            }
          },
          {
            name: PROFILE_BILLS,
            path: '/profile/my-bills',
            components: {
              default: User.profile,
              helper: User.bills
            }
          },
          {
            name: PROFILE_TRACKING,
            path: '/profile/orders-tracking',
            components: {
              default: User.profile,
              helper: User.tracking
            }
          },
          {
            name: PROFILE_COUPONS,
            path: '/profile/my-coupons',
            components: {
              default: User.profile,
              helper: User.coupons
            }
          },
          {
            name: PROFILE_ORDERS,
            path: '/profile/my-orders',
            components: {
              default: User.profile,
              helper: User.orders
            }
          }
        ]
      }
    ]
  }
]
