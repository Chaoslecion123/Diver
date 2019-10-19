import { namespacedRoute } from './_utils.js'

export const NAMESPACE = 'error'
export const BAD_REQUEST = namespacedRoute(NAMESPACE, 'bad-request')
export const FORBIDDEN = namespacedRoute(NAMESPACE, 'forbidden')
export const NOT_FOUND = namespacedRoute(NAMESPACE, 'not-found')
export const SERVER_ERROR = namespacedRoute(NAMESPACE, 'server-error')

export default [
  /**
   * FORBIDDEN
   */
  {
    path: '/error/400/',
    name: BAD_REQUEST,
    // TODO: Make a view for 400 error
    component: () => import('@/views/Error/400')
  },
  /**
   * FORBIDDEN
   */
  {
    path: '/error/403/',
    name: FORBIDDEN,
    component: () => import('@/views/Error/403')
  },
  /**
   * NOT FOUND VIEW
   */
  {
    path: '/error/404/',
    name: NOT_FOUND,
    component: () => import('@/views/Error/404')
  },
  /**
   * SERVER ERROR
   */
  {
    path: '/error/500/',
    name: SERVER_ERROR,
    component: () => import('@/views/Error/500')
  }
]
