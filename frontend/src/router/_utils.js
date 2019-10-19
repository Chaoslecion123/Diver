/**
 * Utility functions for handling routing tasks
 */
import store from '@/store'
import router from '@/router'

import { ROOT, LOGOUT } from './index'

export const trim = (s, c) => {
  if (c === ']') c = '\\]'
  if (c === '\\') c = '\\\\'
  return s.replace(new RegExp('^[' + c + ']+|[' + c + ']+$', 'g'), '')
}

export const namespacedRoute = (namespace, routeName, action = []) => {
  return trim([namespace, routeName, ...action].join(':'), ':')
}

export const getNamespace = routeName => {
  let namespace = routeName.split(':')
  return trim(namespace.slice(0, namespace.length - 1).join(':'), ':')
}

export const handleLogout = () => {
  store.dispatch('auth/logout').then(() => {
    router.push({
      name: LOGOUT
    })
  })
}

export const verifyNoAuth = (to, from, next) => {
  //  store.dispatch('auth/initialize').then(() => {
  if (store.getters['auth/isAuthenticated']) {
    next({
      name: ROOT,
      query: {}
    })
  } else {
    next()
  }
  //  })
}

export const verifyAuth = (to, from, next) => {
  //  store.dispatch('auth/initialize').then(() => {
  if (!store.getters['auth/isAuthenticated']) {
    next({
      name: 'auth:login',
      query: {
        next: to.fullPath
      }
    })
  } else {
    next()
  }
  //  })
}

export const verifyShoppingCart = (to, from, next) => {
  store.dispatch('cart/initialize').then(() => {
    if (!store.getters['cart/isCartAvailable']) {
      next({
        name: 'storefront:cart'
      })
    } else {
      next()
    }
  })
}

export const socialLogin = (to, from, next) => {
  const provider = to.params.provider
  const code = to.query.code
  const persistence = true

  store
    .dispatch('auth/socialLogin', { provider, code, persistence })
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next({
          name: 'auth:login',
          query: {}
        })
      } else {
        next({
          name: ROOT,
          query: {}
        })
      }
    })
}

export default {
  namespacedRoute,
  getNamespace,
  verifyAuth,
  verifyNoAuth,
  handleLogout
}
