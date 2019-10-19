/**
 * Shortcut fuctions to make calls to API endpoints related to Address object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { ADDRESS } from './_endpoints'

export default {
  /**
   * Performs options request to get address's schema.
   */
  options (config = {}) {
    return session.options(ADDRESS, config)
  },
  /**
   * Performs address listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(ADDRESS, config)
  },
  /**
   * Performs address creation
   *
   * @param {object} - Address data
   */
  create (data, config = {}) {
    return session.post(ADDRESS, data, config)
  },
  /**
   * Performs address retrieve
   *
   * @param {{int}} - Address ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${ADDRESS}${id}/`, config)
  },
  /**
   * Performs address update
   *
   * @param {int}    - Address ID
   * @param {object} - Address data
   */
  update (id, data, config = {}) {
    return session.patch(`${ADDRESS}${id}/`, data, config)
  },
  /**
   * Performs address retrieve
   *
   * @param {{int}} - ID of Address to delete
   */
  delete (id, config = {}) {
    return session.delete(`${ADDRESS}${id}/`, config)
  }
}
