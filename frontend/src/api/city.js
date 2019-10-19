/**
 * Shortcut fuctions to make calls to API endpoints related to City object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CITY } from './_endpoints'

export default {
  /**
   * Performs options request to get city's schema.
   */
  options (config = {}) {
    return session.options(CITY, config)
  },
  /**
   * Performs city listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CITY, config)
  },
  /**
   * Performs city creation
   *
   * @param {object} - City data
   */
  create (data, config = {}) {
    return session.post(CITY, data, config)
  },
  /**
   * Performs city retrieve
   *
   * @param {{int}} - City ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CITY}${id}/`, config)
  },
  /**
   * Performs city update
   *
   * @param {int}    - City ID
   * @param {object} - City data
   */
  update (id, data, config = {}) {
    return session.patch(`${CITY}${id}/`, data, config)
  },
  /**
   * Performs city retrieve
   *
   * @param {{int}} - ID of City to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CITY}${id}/`, config)
  }
}
