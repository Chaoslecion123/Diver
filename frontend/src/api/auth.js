/**
 * Shortcut fuctions to make calls to API endpoints related to the autentication
 * process
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import {
  /* Auth User */
  AUTH_SIGNUP,
  AUTH_LOGIN,
  AUTH_SOCIAL_LOGIN,
  AUTH_LOGOUT,
  AUTH_USER,
  AUTH_PASSWORD_RECOVERY,
  AUTH_PASSWORD_RESET,

  /* Auth Token */
  TOKEN_VERIFY,
  TOKEN_REFRESH
} from './_endpoints'

export default {
  /**
   * Performs user login
   *
   * @param {string} - User email
   * @param {string} - User password
   */
  login (email, password) {
    return session.post(AUTH_LOGIN, {
      email,
      password
    })
  },
  /**
   * Performs user social login
   *
   * @param {string} - provider
   * @param {string} - code
   */
  socialLogin (provider, code) {
    const redirectUri = window.location.origin + `/auth/login/${provider}`

    return session.post(`${AUTH_SOCIAL_LOGIN}${provider}/`, {
      provider,
      code,
      redirectUri
    })
  },
  /**
   * Peroforms signup
   *
   * @param {string}  - email
   * @param {string}  - password
   * @param {string}  - passwordConfirm
   * @param {boolean} - suscribedToNewsletter
   * @param {boolean} - termsAndConditions
   */
  signup (email, password, passwordConfirm, suscribedToNewsletter, termsAndConditions) {
    return session.post(AUTH_SIGNUP, {
      email,
      password,
      passwordConfirm,
      suscribedToNewsletter,
      termsAndConditions
    })
  },
  /**
   * Performs user logout
   */
  logout () {
    return session.post(AUTH_LOGOUT)
  },
  /**
   * Request user password reset
   *
   * @param {string} - User email
   */
  passwordRecoveryRequest (email) {
    return session.post(AUTH_PASSWORD_RECOVERY, { email })
  },
  /**
   * Peroforms password reset
   *
   * @param {string} - Password 1
   * @param {string} - Password 2 (for confirmation)
   * @param {string} - Uid
   * @param {string} - Token
   */
  passwordReset (newPassword1, newPassword2, uid, token) {
    return session.post(AUTH_PASSWORD_RESET, {
      newPassword1,
      newPassword2,
      uid,
      token
    })
  },
  /**
   * Get details for the current logged user
   */
  getCurrentUser (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(AUTH_USER, config)
  },
  /**
   * Get details for the current logged user
   */
  verifyToken (token) {
    return session.post(TOKEN_VERIFY, { token })
  },
  /**
   * Get details for the current logged user
   */
  refreshToken (token) {
    return session.post(TOKEN_REFRESH, { token })
  }
}
