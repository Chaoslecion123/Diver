/**
 * Shortcut fuctions to make calls to API endpoints related to Association object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { ASSOCIATION } from './_endpoints'

export default {
  /**
   * Performs options request to get association's schema.
   */
  options (config = {}) {
    return session.options(ASSOCIATION, config)
  },
  /**
   * Performs association listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(ASSOCIATION, config)
  },
  /**
   * Performs association creation
   *
   * @param {object} - Association data
   */
  create (data, config = {}) {
    return session.post(ASSOCIATION, data, config)
  },
  /**
   * Performs association retrieve
   *
   * @param {{int}} - Association ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${ASSOCIATION}${id}/`, config)
  },
  /**
   * Performs association update
   *
   * @param {int}    - Association ID
   * @param {object} - Association data
   */
  update (id, data, config = {}) {
    return session.patch(`${ASSOCIATION}${id}/`, data, config)
  },
  /**
   * Performs association retrieve
   *
   * @param {{int}} - ID of Association to delete
   */
  delete (id, config = {}) {
    return session.delete(`${ASSOCIATION}${id}/`, config)
  }
}
