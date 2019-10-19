/**
 * Login process
 */
export const LOGIN_BEGIN = 'LOGIN_BEGIN'
export const LOGIN_FAILURE = 'LOGIN_FAILURE'
export const LOGIN_SUCCESS = 'LOGIN_SUCCESS'

/**
 * Messages for login process
 */
export const SET_LOGIN_MESSAGES = 'SET_LOGIN_MESSAGES'
export const REMOVE_LOGIN_MESSAGES = 'REMOVE_LOGIN_MESSAGES'

/**
 * Login process
 */
export const SOCIAL_LOGIN_BEGIN = 'SOCIAL_LOGIN_BEGIN'
export const SOCIAL_LOGIN_FAILURE = 'SOCIAL_LOGIN_FAILURE'
export const SOCIAL_LOGIN_SUCCESS = 'SOCIAL_LOGIN_SUCCESS'

/**
 * Messages for login process
 */
export const SET_SOCIAL_LOGIN_MESSAGES = 'SET_SOCIAL_LOGIN_MESSAGES'
export const REMOVE_SOCIAL_LOGIN_MESSAGES = 'REMOVE_SOCIAL_LOGIN_MESSAGES'

/**
 * Sign up process
 */
export const SIGNUP_BEGIN = 'SIGNUP_BEGIN'
export const SIGNUP_FAILURE = 'SIGNUP_FAILURE'
export const SIGNUP_SUCCESS = 'SIGNUP_SUCCESS'

/**
 * Messages for sign up process
 */
export const SET_SIGNUP_MESSAGES = 'SET_SIGNUP_MESSAGES'
export const REMOVE_SIGNUP_MESSAGES = 'REMOVE_SIGNUP_MESSAGES'

/**
 * Request password reset process
 */
export const RECOVERY_BEGIN = 'RECOVERY_BEGIN'
export const RECOVERY_FAILURE = 'RECOVERY_FAILURE'
export const RECOVERY_SUCCESS = 'RECOVERY_SUCCESS'

/**
 * Messages for request password reset process
 */
export const SET_RECOVERY_MESSAGES = 'SET_RECOVERY_MESSAGES'
export const REMOVE_RECOVERY_MESSAGES = 'REMOVE_RECOVERY_MESSAGES'

/**
 * Request password reset process
 */
export const RESET_BEGIN = 'RESET_BEGIN'
export const RESET_FAILURE = 'RESET_FAILURE'
export const RESET_SUCCESS = 'RESET_SUCCESS'

/**
 * Messages for request password reset process
 */
export const SET_RESET_MESSAGES = 'SET_RESET_MESSAGES'
export const REMOVE_RESET_MESSAGES = 'REMOVE_RESET_MESSAGES'

/**
 * Session persistence process
 */
export const SET_SESSION_PERSISTENCE = 'SET_SESSION_PERSISTENCE'
export const REMOVE_SESSION_PERSISTENCE = 'REMOVE_SESSION_PERSISTENCE'
/**
 * Logout process
 */
export const LOGOUT = 'LOGOUT'

/**
 * Current logged user
 */
export const SET_CURRENT_USER = 'SET_CURRENT_USER'

/**
 * Account activation process
 */
export const ACTIVATION_BEGIN = 'ACTIVATION_BEGIN'
export const ACTIVATION_CLEAR = 'ACTIVATION_CLEAR'
export const ACTIVATION_FAILURE = 'ACTIVATION_FAILURE'
export const ACTIVATION_SUCCESS = 'ACTIVATION_SUCCESS'

/**
 * Password reset process
 */
export const PASSWORD_EMAIL_BEGIN = 'PASSWORD_EMAIL_BEGIN'
export const PASSWORD_EMAIL_CLEAR = 'PASSWORD_EMAIL_CLEAR'
export const PASSWORD_EMAIL_FAILURE = 'PASSWORD_EMAIL_FAILURE'
export const PASSWORD_EMAIL_SUCCESS = 'PASSWORD_EMAIL_SUCCESS'
export const PASSWORD_RESET_BEGIN = 'PASSWORD_RESET_BEGIN'
export const PASSWORD_RESET_CLEAR = 'PASSWORD_RESET_CLEAR'
export const PASSWORD_RESET_FAILURE = 'PASSWORD_RESET_FAILURE'
export const PASSWORD_RESET_SUCCESS = 'PASSWORD_RESET_SUCCESS'

/**
 * Token related processes
 */
export const SET_TOKEN = 'SET_TOKEN'
export const REMOVE_TOKEN = 'REMOVE_TOKEN'

/**
 * Token verify
 */
export const TOKEN_VERIFY_BEGIN = 'TOKEN_VERIFY_BEGIN'
export const TOKEN_VERIFY_FAILURE = 'TOKEN_VERIFY_FAILURE'
export const TOKEN_VERIFY_SUCCESS = 'TOKEN_VERIFY_SUCCESS'

/**
 * Messages for token verification process
 */
export const SET_TOKEN_VERIFY_MESSAGES = 'SET_TOKEN_VERIFY_MESSAGES'
export const REMOVE_TOKEN_VERIFY_MESSAGES = 'REMOVE_TOKEN_VERIFY_MESSAGES'

/**
 * Token verify
 */
export const TOKEN_REFRESH_BEGIN = 'TOKEN_REFRESH_BEGIN'
export const TOKEN_REFRESH_FAILURE = 'TOKEN_REFRESH_FAILURE'
export const TOKEN_REFRESH_SUCCESS = 'TOKEN_REFRESH_SUCCESS'

/**
 * Messages for token verification process
 */
export const SET_TOKEN_REFRESH_MESSAGES = 'SET_TOKEN_REFRESH_MESSAGES'
export const REMOVE_TOKEN_REFRESH_MESSAGES = 'REMOVE_TOKEN_REFRESH_MESSAGES'

/**
 * Messages related processes due to errors in formularies
 */
export const SET_MESSAGES = 'SET_MESSAGES'
export const REMOVE_MESSAGES = 'REMOVE_MESSAGES'

/**
 * Generic Processes
 */
export const CREATE_BEGIN = 'CREATE_BEGIN'
export const CREATE_SUCCESS = 'CREATE_SUCCESS'
export const CREATE_FAILURE = 'CREATE_FAILURE'
export const CREATE_SET_MESSAGES = 'CREATE_SET_MESSAGES'
export const CREATE_SET_STATUS_CODE = 'CREATE_SET_STATUS_CODE'

/* Read object flow */
export const READ_BEGIN = 'READ_BEGIN'
export const READ_SUCCESS = 'READ_SUCCESS'
export const READ_FAILURE = 'READ_FAILURE'
export const READ_SET_MESSAGES = 'READ_SET_MESSAGES'
export const READ_SET_STATUS_CODE = 'READ_SET_STATUS_CODE'

/* update object flow */
export const UPDATE_BEGIN = 'UPDATE_BEGIN'
export const UPDATE_SUCCESS = 'UPDATE_SUCCESS'
export const UPDATE_FAILURE = 'UPDATE_FAILURE'
export const UPDATE_SET_MESSAGES = 'UPDATE_SET_MESSAGES'
export const UPDATE_SET_STATUS_CODE = 'UPDATE_SET_STATUS_CODE'

/* removing object flow */
export const DELETE_BEGIN = 'DELETE_BEGIN'
export const DELETE_SUCCESS = 'DELETE_SUCCESS'
export const DELETE_FAILURE = 'DELETE_FAILURE'
export const DELETE_SET_MESSAGES = 'DELETE_SET_MESSAGES'
export const DELETE_SET_STATUS_CODE = 'DELETE_SET_STATUS_CODE'

/* Get object list flow */
export const LIST_BEGIN = 'LIST_BEGIN'
export const LIST_SUCCESS = 'LIST_SUCCESS'
export const LIST_FAILURE = 'LIST_FAILURE'
export const LIST_SET_MESSAGES = 'LIST_SET_MESSAGES'
export const LIST_SET_STATUS_CODE = 'LIST_SET_STATUS_CODE'

/* Get schema flow */
export const SCHEMA_BEGIN = 'SCHEMA_BEGIN'
export const SCHEMA_SUCCESS = 'SCHEMA_SUCCESS'
export const SCHEMA_FAILURE = 'SCHEMA_FAILURE'
export const SCHEMA_SET_MESSAGES = 'SCHEMA_SET_MESSAGES'
export const SCHEMA_SET_STATUS_CODE = 'SCHEMA_SET_STATUS_CODE'

/* Handle object list */
export const SET_SCHEMA = 'SET_SCHEMA'
export const SET_OBJECT = 'SET_OBJECT'
export const REMOVE_OBJECT = 'REMOVE_OBJECT'
export const SET_OBJECT_LIST = 'SET_OBJECT_LIST'
export const REMOVE_OBJECT_LIST = 'REMOVE_OBJECT_LIST'
