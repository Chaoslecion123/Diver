/**
 * Shortcut fuctions to make calls to API endpoints related to User object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { USER } from './_endpoints'

export default {
  /**
   * Performs options request to get user's schema.
   */
  options (config = {}) {
    return session.options(USER, config)
  },
  /**
   * Performs user listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(USER, config)
  },
  /**
   * Performs user creation
   *
   * @param {object} - User data
   */
  create (data, config = {}) {
    return session.post(USER, data, config)
  },
  /**
   * Performs user retrieve
   *
   * @param {{int}} - User ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${USER}${id}/`, config)
  },
  /**
   * Performs user update
   *
   * @param {int}    - User ID
   * @param {object} - User data
   */
  update (id, data, config = {}) {
    return session.patch(`${USER}${id}/`, data, config)
  },
  /**
   * Performs user retrieve
   *
   * @param {{int}} - ID of User to delete
   */
  delete (id, config = {}) {
    return session.delete(`${USER}${id}/`, config)
  },
  /**
   * Performs user verification
   *
   * @param {object} - User data
   */
  verify (data, config = {}) {
    return session.post(`${USER}verify/`, data, config)
  }
}
