import { namespacedRoute } from './_utils.js'

export const NAMESPACE = 'page'
export const PAGE_DETAIL = namespacedRoute(NAMESPACE, 'detail')

export default [
  {
    name: NAMESPACE,
    path: '/page',
    component: () => import('@/views/Base'),
    redirect: PAGE_DETAIL,
    children: [
      {
        name: PAGE_DETAIL,
        path: '/page/:slug',
        component: () => import('@/views/Pages/Page')
      }
    ]
  }
]
