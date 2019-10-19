import { namespacedRoute, verifyNoAuth, handleLogout, socialLogin } from './_utils.js'

export const NAMESPACE = 'auth'
export const LOGIN = namespacedRoute(NAMESPACE, 'login')
export const LOGIN_SOCIAL = namespacedRoute(NAMESPACE, 'login', ['social'])
export const SIGNUP = namespacedRoute(NAMESPACE, 'signup')
export const LOGOUT = namespacedRoute(NAMESPACE, 'logout')
export const PASSWORD_RECOVERY = namespacedRoute(NAMESPACE, 'password', ['recovery'])
export const PASSWORD_RESET = namespacedRoute(NAMESPACE, 'password', ['reset'])

export default [
  {
    path: '/auth',
    name: NAMESPACE,
    component: () => import('@/views/Base'),
    redirect: {
      name: LOGIN
    },
    children: [
      {
        path: 'login',
        name: LOGIN,
        component: () => import('@/views/Auth/LogIn'),
        beforeEnter: verifyNoAuth,
        meta: {
          hideTopBarAuthButton: true
        }
      },
      {
        path: 'login/:provider',
        name: LOGIN_SOCIAL,
        beforeEnter: socialLogin,
        meta: {
          hideTopBarAuthButton: true
        }
      },
      {
        path: 'signup',
        name: SIGNUP,
        component: () => import('@/views/Auth/SignUp'),
        beforeEnter: verifyNoAuth,
        meta: {
          hideTopBarAuthButton: true
        }
      },
      {
        path: 'logout',
        name: LOGOUT,
        beforeEnter: handleLogout
      },
      {
        path: 'password/recovery',
        name: PASSWORD_RECOVERY,
        component: () => import('@/views/Auth/PasswordRecovery'),
        beforeEnter: verifyNoAuth,
        meta: {
          hideTopBarAuthButton: true
        }
      },
      {
        // path: 'password/reset',
        path: 'password/reset/:uid/:token',
        name: PASSWORD_RESET,
        component: () => import('@/views/Auth/PasswordReset'),
        beforeEnter: verifyNoAuth,
        meta: {
          hideTopBarAuthButton: true
        }
      }
    ]
  }
]
