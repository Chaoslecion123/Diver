/**
 * Shortcut fuctions to make calls to API endpoints related to Rate_Types object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { RATE_TYPES } from './_endpoints'

export default {
  /**
   * Performs options request to get rate_types's schema.
   */
  options (config = {}) {
    return session.options(RATE_TYPES, config)
  },
  /**
   * Performs rate_types listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(RATE_TYPES, config)
  },
  /**
   * Performs rate_types creation
   *
   * @param {object} - Rate_Types data
   */
  create (data, config = {}) {
    return session.post(RATE_TYPES, data, config)
  },
  /**
   * Performs rate_types retrieve
   *
   * @param {{int}} - Rate_Types ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${RATE_TYPES}${id}/`, config)
  },
  /**
   * Performs rate_types update
   *
   * @param {int}    - Rate_Types ID
   * @param {object} - Rate_Types data
   */
  update (id, data, config = {}) {
    return session.patch(`${RATE_TYPES}${id}/`, data, config)
  },
  /**
   * Performs rate_types retrieve
   *
   * @param {{int}} - ID of Rate_Types to delete
   */
  delete (id, config = {}) {
    return session.delete(`${RATE_TYPES}${id}/`, config)
  }
}
