import Vue from 'vue'
import Router from 'vue-router'

// import Index from '../views/Index.vue'

import UserProfileUrls from './user-profile'

import ERROR_ROUTES, { NOT_FOUND } from './errors'
import AUTH_ROUTES from './auth'
import ACCOUNT_ROUTES from './account'
import STOREFRONT_ROUTES from './storefront'
import PAGES_ROUTES from './pages'

export { LOGOUT } from './auth'
export { STOREFRONT_INDEX as ROOT } from './storefront'
// export const ROOT = 'index'

Vue.use(Router)

const router = new Router({
  // mode: process.env.NODE_ENV !== 'production' ? 'hash' : 'history',
  mode: 'history',
  base: '/',
  strict: true,
  routes: [
    /**
     * Error views
     */
    ...ERROR_ROUTES,

    /**
     * Pages routes
     */
    ...PAGES_ROUTES,

    /**
     * Autentication views
     */
    ...AUTH_ROUTES,

    /**
     * Account views
     */
    ...ACCOUNT_ROUTES,

    /**
     * Storefront views
     */
    ...STOREFRONT_ROUTES,

    /**
     * Storefront views
     */
    ...UserProfileUrls,

    /**
     * Redirect invalid routes to 404
     */
    {
      path: '*',
      redirect: {
        name: NOT_FOUND
      }
    }
  ],
  scrollBehavior () {
    return { x: 0, y: 0 }
  }
})

export default router
