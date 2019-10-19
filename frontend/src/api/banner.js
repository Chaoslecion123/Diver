/**
 * Shortcut fuctions to make calls to API endpoints related to Banner object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { BANNER } from './_endpoints'

export default {
  /**
   * Performs options request to get banner's schema.
   */
  options (config = {}) {
    return session.options(BANNER, config)
  },
  /**
   * Performs banner listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(BANNER, config)
  },
  /**
   * Performs banner creation
   *
   * @param {object} - Banner data
   */
  create (data, config = {}) {
    return session.post(BANNER, data, config)
  },
  /**
   * Performs banner retrieve
   *
   * @param {{int}} - Banner ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${BANNER}${id}/`, config)
  },
  /**
   * Performs banner update
   *
   * @param {int}    - Banner ID
   * @param {object} - Banner data
   */
  update (id, data, config = {}) {
    return session.patch(`${BANNER}${id}/`, data, config)
  },
  /**
   * Performs banner retrieve
   *
   * @param {{int}} - ID of Banner to delete
   */
  delete (id, config = {}) {
    return session.delete(`${BANNER}${id}/`, config)
  },
  /**
   * Performs slider listing
   */
  homepage (config = {}) {
    return session.get(`${BANNER}homepage/`, config)
  }
}
