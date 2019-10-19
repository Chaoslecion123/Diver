/**
 * Shortcut fuctions to make calls to API endpoints related to User_Social_Auth object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { USER_SOCIAL_AUTH } from './_endpoints'

export default {
  /**
   * Performs options request to get user_social_auth's schema.
   */
  options (config = {}) {
    return session.options(USER_SOCIAL_AUTH, config)
  },
  /**
   * Performs user_social_auth listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(USER_SOCIAL_AUTH, config)
  },
  /**
   * Performs user_social_auth creation
   *
   * @param {object} - User_Social_Auth data
   */
  create (data, config = {}) {
    return session.post(USER_SOCIAL_AUTH, data, config)
  },
  /**
   * Performs user_social_auth retrieve
   *
   * @param {{int}} - User_Social_Auth ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${USER_SOCIAL_AUTH}${id}/`, config)
  },
  /**
   * Performs user_social_auth update
   *
   * @param {int}    - User_Social_Auth ID
   * @param {object} - User_Social_Auth data
   */
  update (id, data, config = {}) {
    return session.patch(`${USER_SOCIAL_AUTH}${id}/`, data, config)
  },
  /**
   * Performs user_social_auth retrieve
   *
   * @param {{int}} - ID of User_Social_Auth to delete
   */
  delete (id, config = {}) {
    return session.delete(`${USER_SOCIAL_AUTH}${id}/`, config)
  }
}
