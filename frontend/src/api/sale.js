/**
 * Shortcut fuctions to make calls to API endpoints related to Sale object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SALE } from './_endpoints'

export default {
  /**
   * Performs options request to get sale's schema.
   */
  options (config = {}) {
    return session.options(SALE, config)
  },
  /**
   * Performs sale listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SALE, config)
  },
  /**
   * Performs sale creation
   *
   * @param {object} - Sale data
   */
  create (data, config = {}) {
    return session.post(SALE, data, config)
  },
  /**
   * Performs sale retrieve
   *
   * @param {{int}} - Sale ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SALE}${id}/`, config)
  },
  /**
   * Performs sale update
   *
   * @param {int}    - Sale ID
   * @param {object} - Sale data
   */
  update (id, data, config = {}) {
    return session.patch(`${SALE}${id}/`, data, config)
  },
  /**
   * Performs sale retrieve
   *
   * @param {{int}} - ID of Sale to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SALE}${id}/`, config)
  }
}
