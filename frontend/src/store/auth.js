import session from '@/api/_session'
import AUTH from '@/api/auth'

import {
  /* Login flow */
  LOGIN_BEGIN,
  LOGIN_FAILURE,
  LOGIN_SUCCESS,
  SET_LOGIN_MESSAGES,
  REMOVE_LOGIN_MESSAGES,

  /* Login flow */
  SIGNUP_BEGIN,
  SIGNUP_FAILURE,
  SIGNUP_SUCCESS,
  SET_SIGNUP_MESSAGES,
  REMOVE_SIGNUP_MESSAGES,

  /* Social Logi flow */
  SOCIAL_LOGIN_BEGIN,
  SOCIAL_LOGIN_FAILURE,
  SOCIAL_LOGIN_SUCCESS,
  SET_SOCIAL_LOGIN_MESSAGES,
  REMOVE_SOCIAL_LOGIN_MESSAGES,

  /* Password recovery request flow */
  RECOVERY_BEGIN,
  RECOVERY_FAILURE,
  RECOVERY_SUCCESS,
  SET_RECOVERY_MESSAGES,
  REMOVE_RECOVERY_MESSAGES,

  /* Password reset flow */
  RESET_BEGIN,
  RESET_FAILURE,
  RESET_SUCCESS,
  SET_RESET_MESSAGES,
  REMOVE_RESET_MESSAGES,

  /* Other processes */
  SET_SESSION_PERSISTENCE,
  REMOVE_SESSION_PERSISTENCE,
  SET_CURRENT_USER,

  /* Logout flow */
  LOGOUT,

  /* Token flow */
  SET_TOKEN,
  REMOVE_TOKEN,

  /* Verify Token process */
  TOKEN_VERIFY_BEGIN,
  TOKEN_VERIFY_FAILURE,
  TOKEN_VERIFY_SUCCESS,
  SET_TOKEN_VERIFY_MESSAGES,
  REMOVE_TOKEN_VERIFY_MESSAGES,

  /* Refresh Token process */
  TOKEN_REFRESH_BEGIN,
  TOKEN_REFRESH_FAILURE,
  TOKEN_REFRESH_SUCCESS,
  SET_TOKEN_REFRESH_MESSAGES,
  REMOVE_TOKEN_REFRESH_MESSAGES
} from './_processes'

const SESSION_PERSISTENCE_KEY = 'AuthPersistence'
const TOKEN_STORAGE_KEY = 'AuthToken'
const NULL_TOKEN = null

const initialState = {
  /* Login process */
  authenticating: false,
  loginSuccess: false,
  loginFailure: false,
  loginMessages: null,

  /* Login process */
  socialAuthenticating: false,
  socialLoginSuccess: false,
  socialLoginFailure: false,
  socialLoginMessages: null,

  /* Signup process */
  signingup: false,
  signupSuccess: false,
  signupFailure: false,
  signupMessages: null,

  /* Pasord recovery request process */
  requesting: false,
  recoverySuccess: false,
  recoveryFailure: false,
  recoveryMessages: null,

  /* Pasord reset process */
  restoring: false,
  resetSuccess: false,
  resetFailure: false,
  resetMessages: null,

  /* Token verify reset process */
  verifying: false,
  verifySuccess: false,
  verifyFailure: false,
  verifyMessages: null,

  /* Token verify reset process */
  refreshing: false,
  refreshSuccess: false,
  refreshFailure: false,
  refreshMessages: null,

  /* Other processes */
  token: NULL_TOKEN,
  sessionPersistence: null,
  currentUser: null,
  /**
   * Cada media hora
   */
  tokenRefreshInterval: 30 * 60 * 1000
}

const getters = {
  isAuthenticated: state => {
    return state.token !== NULL_TOKEN
  }
}

const actions = {
  /**
   * Initialize the authentication process.
   */
  initialize ({ commit, dispatch }) {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY)
    const persistence = localStorage.getItem(SESSION_PERSISTENCE_KEY)

    if (persistence === 'true') {
      commit(SET_SESSION_PERSISTENCE, true)
    } else {
      commit(SET_SESSION_PERSISTENCE, false)
    }

    if (token) {
      return dispatch('verifyToken')
    } else {
      commit(REMOVE_TOKEN)
      commit(REMOVE_SESSION_PERSISTENCE)
    }
  },

  /**
     * gets the current autheticated user
     */
  getAutenticatedUser ({ commit }, { query = {}, config = {} } = {}) {
    return AUTH
      .getCurrentUser(query, config)
      .then(response => {
        commit(SET_CURRENT_USER, response.data)
      })
  },

  /**
     * Performs token verification
     */
  verifyToken ({ commit, dispatch }) {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY)

    commit(TOKEN_VERIFY_BEGIN)
    commit(REMOVE_TOKEN_VERIFY_MESSAGES)

    return AUTH
      .verifyToken(token)
      .then(response => {
        commit(TOKEN_VERIFY_SUCCESS)
        commit(SET_TOKEN, response.data.token)
        return dispatch('getAutenticatedUser')
      })
      .catch(error => {
        commit(TOKEN_VERIFY_FAILURE)
        try {
          commit(SET_TOKEN_VERIFY_MESSAGES, error.response.data)
        } catch (error) {
          commit(SET_TOKEN_VERIFY_MESSAGES, {})
        }
        return dispatch('refreshToken')
      })
  },

  /**
     * Performs token refresh
     */
  refreshToken ({ commit, dispatch }) {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY)

    commit(TOKEN_REFRESH_BEGIN)
    commit(REMOVE_TOKEN_REFRESH_MESSAGES)

    return AUTH
      .refreshToken(token)
      .then(response => {
        commit(TOKEN_REFRESH_SUCCESS)
        commit(SET_TOKEN, response.data.token)
        dispatch('getAutenticatedUser')
      })
      .catch(error => {
        commit(TOKEN_REFRESH_FAILURE)
        commit(REMOVE_TOKEN)
        commit(SET_TOKEN_REFRESH_MESSAGES, error.response.data)
      })
  },

  /**
     * Performs login process
     *
     * @param {string} email - User email
     * @param {string} password - User password
     */
  login ({ commit, dispatch }, { email, password, persistence = false }) {
    commit(LOGIN_BEGIN)
    commit(REMOVE_LOGIN_MESSAGES)
    return AUTH
      .login(email, password)
      .then(response => {
        commit(SET_TOKEN, response.data.token)
        commit(SET_CURRENT_USER, response.data.user)
        commit(SET_SESSION_PERSISTENCE, persistence)
      })
      .then(() => {
        commit(LOGIN_SUCCESS)
        dispatch('getAutenticatedUser')
      })
      .catch(error => {
        commit(LOGIN_FAILURE)
        commit(SET_LOGIN_MESSAGES, error.response.data)
      })
  },

  /**
     * Performs login process
     *
     * @param {string} provider - provider
     * @param {string} code - code
     */
  socialLogin ({ commit, dispatch }, { provider, code, persistence = false }) {
    commit(SOCIAL_LOGIN_BEGIN)
    commit(REMOVE_SOCIAL_LOGIN_MESSAGES)
    return AUTH
      .socialLogin(provider, code)
      .then(response => {
        commit(SET_TOKEN, response.data.token)
        commit(SET_CURRENT_USER, response.data.user)
        commit(SET_SESSION_PERSISTENCE, persistence)
      })
      .then(() => {
        commit(SOCIAL_LOGIN_SUCCESS)
        dispatch('getAutenticatedUser')
      })
      .catch(error => {
        commit(SOCIAL_LOGIN_FAILURE)
        commit(SET_SOCIAL_LOGIN_MESSAGES, error.response.data)
      })
  },

  /**
     * Performs signup process
     *
     * @param {string} email - User email
     * @param {string} password - User password
     */
  signup ({ commit, dispatch }, { email, password, passwordConfirm, suscribedToNewsletter, termsAndConditions }) {
    commit(SIGNUP_BEGIN)
    commit(REMOVE_SIGNUP_MESSAGES)
    return AUTH
      .signup(email, password, passwordConfirm, suscribedToNewsletter, termsAndConditions)
      .then(response => {
        commit(SET_TOKEN, response.data.token)
        commit(SET_CURRENT_USER, response.data.user)
        commit(SET_SESSION_PERSISTENCE, true)
      })
      .then(() => {
        commit(SIGNUP_SUCCESS)
      })
      .catch(error => {
        commit(SIGNUP_FAILURE)
        commit(SET_SIGNUP_MESSAGES, error.response.data)
      })
  },

  /**
     * Performs password recovery request process
     *
     * @param {string} email - User email
     */
  passwordRecoveryRequest ({ commit }, { email }) {
    // passwordReset
    commit(RECOVERY_BEGIN)
    commit(REMOVE_RECOVERY_MESSAGES)
    return AUTH
      .passwordRecoveryRequest(email)
      .then((/* response */) => {
        commit(RECOVERY_SUCCESS)
      })
      .catch(error => {
        commit(RECOVERY_FAILURE)
        commit(SET_RECOVERY_MESSAGES, error.response.data)
      })
  },

  /**
     * Performs password reset process
     *
     * @param {string} newPassword1 - Password 1
     * @param {string} newPassword2 - Password 2 (for confirmation)
     * @param {string} uid          - Password recovery uid
     * @param {string} token        - Password recovery token
     */
  passwordReset ({ commit }, { newPassword1, newPassword2, uid, token }) {
    commit(RESET_BEGIN)
    commit(REMOVE_RESET_MESSAGES)
    return AUTH
      .passwordReset(newPassword1, newPassword2, uid, token)
      .then((/* response */) => {
        commit(RESET_SUCCESS)
      })
      .catch(error => {
        commit(RESET_FAILURE)
        commit(SET_RESET_MESSAGES, error.response.data)
      })
  },

  /**
     * Performs logout process
     */
  logout ({ commit }) {
    commit(REMOVE_LOGIN_MESSAGES)
    AUTH.logout()
    commit(LOGOUT)
    commit(REMOVE_TOKEN)
    commit(SET_CURRENT_USER, null)
  }

  /**
     * Gets currrent user
     */
}

const mutations = {
  /**
     * Indicates the begin of the login process
     *
     * @param {object} state - State
     */
  [LOGIN_BEGIN] (state) {
    state.authenticating = true
    state.loginSuccess = false
    state.loginFailure = false
  },

  /**
     * Indicates that the login process ends with failure
     *
     * @param {object} state - State
     */
  [LOGIN_FAILURE] (state) {
    state.authenticating = false
    state.loginSuccess = false
    state.loginFailure = true
  },

  /**
     * Indicates that the login process ends with success
     *
     * @param {object} state - State
     */
  [LOGIN_SUCCESS] (state) {
    state.authenticating = false
    state.loginSuccess = true
    state.loginFailure = false
  },

  /**
     * Sets the messages returned by the login process
     *
     * @param {object} state - State
     */
  [SET_LOGIN_MESSAGES] (state, messages) {
    state.loginMessages = messages
  },

  /**
     * Removes the messages returned by the login process
     *
     * @param {object} state - State
     */
  [REMOVE_LOGIN_MESSAGES] (state) {
    state.loginMessages = null
  },

  /**
     * Indicates the begin of the login process
     *
     * @param {object} state - State
     */
  [SOCIAL_LOGIN_BEGIN] (state) {
    state.socialAuthenticating = true
    state.socialLoginSuccess = false
    state.socialLoginFailure = false
  },

  /**
     * Indicates that the login process ends with failure
     *
     * @param {object} state - State
     */
  [SOCIAL_LOGIN_FAILURE] (state) {
    state.socialAuthenticating = false
    state.socialLoginSuccess = false
    state.socialLoginFailure = true
  },

  /**
     * Indicates that the login process ends with success
     *
     * @param {object} state - State
     */
  [SOCIAL_LOGIN_SUCCESS] (state) {
    state.socialAuthenticating = false
    state.socialLoginSuccess = true
    state.socialLoginFailure = false
  },

  /**
     * Sets the messages returned by the login process
     *
     * @param {object} state - State
     */
  [SET_SOCIAL_LOGIN_MESSAGES] (state, messages) {
    state.socialLoginMessages = messages
  },

  /**
     * Removes the messages returned by the login process
     *
     * @param {object} state - State
     */
  [REMOVE_SOCIAL_LOGIN_MESSAGES] (state) {
    state.socialLoginMessages = null
  },

  /**
     * Indicates the begin of the login process
     *
     * @param {object} state - State
     */
  [SIGNUP_BEGIN] (state) {
    state.signingup = true
    state.signupSuccess = false
    state.signupFailure = false
  },

  /**
     * Indicates that the signup process ends with failure
     *
     * @param {object} state - State
     */
  [SIGNUP_FAILURE] (state) {
    state.signingup = false
    state.signupSuccess = false
    state.signupFailure = true
  },

  /**
     * Indicates that the signup process ends with success
     *
     * @param {object} state - State
     */
  [SIGNUP_SUCCESS] (state) {
    state.signingup = false
    state.signupSuccess = true
    state.signupFailure = false
  },

  /**
     * Sets the messages returned by the signup process
     *
     * @param {object} state - State
     */
  [SET_SIGNUP_MESSAGES] (state, messages) {
    state.signupMessages = messages
  },

  /**
     * Removes the messages returned by the signup process
     *
     * @param {object} state - State
     */
  [REMOVE_SIGNUP_MESSAGES] (state) {
    state.signupMessages = null
  },

  /**
     *  Indicates the begin of the password recovery request process
     *
     * @param {object} state - State
     */
  [RECOVERY_BEGIN] (state) {
    state.requesting = true
    state.recoverySuccess = false
    state.recoveryFailure = false
  },

  /**
     * Indicates that the password recovery request process ends with failure
     *
     * @param {object} state - State
     */
  [RECOVERY_FAILURE] (state) {
    state.requesting = false
    state.recoverySuccess = false
    state.recoveryFailure = true
  },

  /**
     * Indicates that the password recovery request process ends with success
     *
     * @param {object} state - State
     */
  [RECOVERY_SUCCESS] (state) {
    state.requesting = false
    state.recoverySuccess = true
    state.recoveryFailure = false
  },

  /**
     * Sets the messages returned by the password recovery request process
     *
     * @param {object} state - State
     */
  [SET_RECOVERY_MESSAGES] (state, messages) {
    state.recoveryMessages = messages
  },

  /**
     * Removes the messages returned by the password recovery request process
     *
     * @param {object} state - State
     */
  [REMOVE_RECOVERY_MESSAGES] (state) {
    state.recoveryMessages = null
  },

  /**
     *  Indicates the begin of the password reset process
     *
     * @param {object} state - State
     */
  [RESET_BEGIN] (state) {
    state.restoring = true
    state.resetSuccess = false
    state.resetFailure = false
  },

  /**
     * Indicates that the password reset process ends with failure
     *
     * @param {object} state - State
     */
  [RESET_FAILURE] (state) {
    state.restoring = false
    state.resetSuccess = false
    state.resetFailure = true
  },

  /**
     * Indicates that the password reset process ends with success
     *
     * @param {object} state - State
     */
  [RESET_SUCCESS] (state) {
    state.restoring = false
    state.resetSuccess = true
    state.resetFailure = false
  },

  /**
     * Sets the messages returned by the password reset process
     *
     * @param {object} state - State
     */
  [SET_RESET_MESSAGES] (state, messages) {
    state.resetMessages = messages
  },

  /**
     * Removes the messages returned by the password reset process
     *
     * @param {object} state - State
     */
  [REMOVE_RESET_MESSAGES] (state) {
    state.resetMessages = null
  },

  /**
     * Indicates that the logout process has ended
     *
     * @param {object} state - State
     */
  [LOGOUT] (state) {
    state.authenticating = false
    state.loginSuccess = false
    state.loginFailure = false
  },

  /**
     * Sets session persistence
     *
     * @param {object} persistence - State
     */
  [SET_SESSION_PERSISTENCE] (state, persistence) {
    localStorage.setItem(SESSION_PERSISTENCE_KEY, persistence)
    state.sessionPersistence = persistence
  },

  /**
     * Removes session persistence
     *
     * @param {object} persistence - State
     */
  [REMOVE_SESSION_PERSISTENCE] (state) {
    localStorage.removeItem(SESSION_PERSISTENCE_KEY)
    state.sessionPersistence = null
  },

  /**
     * Sets the current user
     *
     * @param {object} state - State
     * @param {boolean} user - logged in user
     */
  [SET_CURRENT_USER] (state, user) {
    state.currentUser = user
  },

  /**
     * Sets the session token and save it to the localStorage
     *
     * @param {object} state - State
     * @param {string} token - Session token
     */
  [SET_TOKEN] (state, token) {
    localStorage.setItem(TOKEN_STORAGE_KEY, token)
    session.defaults.headers.Authorization = `DiverPass ${token}`
    state.token = token
  },

  /**
     * Remove the session token
     *
     * @param {object} state - State
     */
  [REMOVE_TOKEN] (state) {
    localStorage.removeItem(TOKEN_STORAGE_KEY)
    delete session.defaults.headers.Authorization
    state.token = NULL_TOKEN
  },

  /**
     * Indicates the begin of the token verification process
     *
     * @param {object} state - State
     */
  [TOKEN_VERIFY_BEGIN] (state) {
    state.verifying = true
    state.verifySuccess = false
    state.verifyFailure = false
  },

  /**
     * Indicates that the token verification ends with failure
     *
     * @param {object} state - State
     */
  [TOKEN_VERIFY_FAILURE] (state) {
    state.verifying = false
    state.verifySuccess = false
    state.verifyFailure = true
  },

  /**
     * Indicates that the token verification ends with success
     *
     * @param {object} state - State
     */
  [TOKEN_VERIFY_SUCCESS] (state) {
    state.verifying = false
    state.verifySuccess = true
    state.verifyFailure = false
  },

  /**
     * Sets the messages returned by the token verification process
     *
     * @param {object} state - State
     */
  [SET_TOKEN_VERIFY_MESSAGES] (state, messages) {
    state.verifyMessages = messages
  },

  /**
     * Removes the messages returned by the token verification process
     *
     * @param {object} state - State
     */
  [REMOVE_TOKEN_VERIFY_MESSAGES] (state) {
    state.verifyMessages = null
  },

  /**
     * Indicates the begin of the token verification process
     *
     * @param {object} state - State
     */
  [TOKEN_VERIFY_BEGIN] (state) {
    state.verifying = true
    state.verifySuccess = false
    state.verifyFailure = false
  },

  /**
     * Indicates that the token verification ends with failure
     *
     * @param {object} state - State
     */
  [TOKEN_VERIFY_FAILURE] (state) {
    state.verifying = false
    state.verifySuccess = false
    state.verifyFailure = true
  },

  /**
     * Indicates that the token verification ends with success
     *
     * @param {object} state - State
     */
  [TOKEN_VERIFY_SUCCESS] (state) {
    state.verifying = false
    state.verifySuccess = true
    state.verifyFailure = false
  },

  /**
     * Sets the messages returned by the token verification process
     *
     * @param {object} state - State
     */
  [SET_TOKEN_VERIFY_MESSAGES] (state, messages) {
    state.verifyMessages = messages
  },

  /**
     * Removes the messages returned by the token verification process
     *
     * @param {object} state - State
     */
  [REMOVE_TOKEN_VERIFY_MESSAGES] (state) {
    state.verifyMessages = null
  },

  /** --------------------
     * Indicates the begin of the token verification process
     *
     * @param {object} state - State
     */
  [TOKEN_REFRESH_BEGIN] (state) {
    state.refreshing = true
    state.refreshSuccess = false
    state.refreshFailure = false
  },

  /**
     * Indicates that the token verification ends with failure
     *
     * @param {object} state - State
     */
  [TOKEN_REFRESH_FAILURE] (state) {
    state.refreshing = false
    state.refreshSuccess = false
    state.refreshFailure = true
  },

  /**
     * Indicates that the token verification ends with success
     *
     * @param {object} state - State
     */
  [TOKEN_REFRESH_SUCCESS] (state) {
    state.refreshing = false
    state.refreshSuccess = true
    state.refreshFailure = false
  },

  /**
     * Sets the messages returned by the token verification process
     *
     * @param {object} state - State
     */
  [SET_TOKEN_REFRESH_MESSAGES] (state, messages) {
    state.refreshMessages = messages
  },

  /**
     * Removes the messages returned by the token verification process
     *
     * @param {object} state - State
     */
  [REMOVE_TOKEN_REFRESH_MESSAGES] (state) {
    state.refreshMessages = null
  }
}

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations
}
