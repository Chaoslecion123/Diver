/**
 * Shortcut fuctions to make calls to API endpoints related to Address object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { FAVORITE } from './_endpoints'

export default {
  /**
   * Performs options request to get address's schema.
   */
  options (config = {}) {
    return session.options(FAVORITE, config)
  },
  /**
   * Performs address listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(FAVORITE, config)
  },
  /**
   * Performs address creation
   *
   * @param {object} - Address data
   */
  create (data, config = {}) {
    return session.post(FAVORITE, data, config)
  },
  /**
   * Performs address retrieve
   *
   * @param {{int}} - Address ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${FAVORITE}${id}/`, config)
  },
  /**
   * Performs address update
   *
   * @param {int}    - Address ID
   * @param {object} - Address data
   */
  update (id, data, config = {}) {
    return session.patch(`${FAVORITE}${id}/`, data, config)
  },
  /**
   * Performs address retrieve
   *
   * @param {{int}} - ID of Address to delete
   */
  delete (id, config = {}) {
    return session.delete(`${FAVORITE}${id}/`, config)
  }
}
