/**
 * Shortcut fuctions to make calls to API endpoints related to Authorization_Key object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { AUTHORIZATION_KEY } from './_endpoints'

export default {
  /**
   * Performs options request to get authorization_key's schema.
   */
  options (config = {}) {
    return session.options(AUTHORIZATION_KEY, config)
  },
  /**
   * Performs authorization_key listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(AUTHORIZATION_KEY, config)
  },
  /**
   * Performs authorization_key creation
   *
   * @param {object} - Authorization_Key data
   */
  create (data, config = {}) {
    return session.post(AUTHORIZATION_KEY, data, config)
  },
  /**
   * Performs authorization_key retrieve
   *
   * @param {{int}} - Authorization_Key ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${AUTHORIZATION_KEY}${id}/`, config)
  },
  /**
   * Performs authorization_key update
   *
   * @param {int}    - Authorization_Key ID
   * @param {object} - Authorization_Key data
   */
  update (id, data, config = {}) {
    return session.patch(`${AUTHORIZATION_KEY}${id}/`, data, config)
  },
  /**
   * Performs authorization_key retrieve
   *
   * @param {{int}} - ID of Authorization_Key to delete
   */
  delete (id, config = {}) {
    return session.delete(`${AUTHORIZATION_KEY}${id}/`, config)
  }
}
