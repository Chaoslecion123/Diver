/**
 * Shortcut fuctions to make calls to API endpoints related to Site object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SITE } from './_endpoints'

export default {
  /**
   * Performs options request to get site's schema.
   */
  options (config = {}) {
    return session.options(SITE, config)
  },
  /**
   * Performs site listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SITE, config)
  },
  /**
   * Performs site creation
   *
   * @param {object} - Site data
   */
  create (data, config = {}) {
    return session.post(SITE, data, config)
  },
  /**
   * Performs site retrieve
   *
   * @param {{int}} - Site ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SITE}${id}/`, config)
  },
  /**
   * Performs site update
   *
   * @param {int}    - Site ID
   * @param {object} - Site data
   */
  update (id, data, config = {}) {
    return session.patch(`${SITE}${id}/`, data, config)
  },
  /**
   * Performs site retrieve
   *
   * @param {{int}} - ID of Site to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SITE}${id}/`, config)
  }
}
