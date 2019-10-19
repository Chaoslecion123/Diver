/**
 * Shortcut fuctions to make calls to API endpoints related to Partial object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { PARTIAL } from './_endpoints'

export default {
  /**
   * Performs options request to get partial's schema.
   */
  options (config = {}) {
    return session.options(PARTIAL, config)
  },
  /**
   * Performs partial listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(PARTIAL, config)
  },
  /**
   * Performs partial creation
   *
   * @param {object} - Partial data
   */
  create (data, config = {}) {
    return session.post(PARTIAL, data, config)
  },
  /**
   * Performs partial retrieve
   *
   * @param {{int}} - Partial ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${PARTIAL}${id}/`, config)
  },
  /**
   * Performs partial update
   *
   * @param {int}    - Partial ID
   * @param {object} - Partial data
   */
  update (id, data, config = {}) {
    return session.patch(`${PARTIAL}${id}/`, data, config)
  },
  /**
   * Performs partial retrieve
   *
   * @param {{int}} - ID of Partial to delete
   */
  delete (id, config = {}) {
    return session.delete(`${PARTIAL}${id}/`, config)
  }
}
