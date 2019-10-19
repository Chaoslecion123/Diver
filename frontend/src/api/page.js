/**
 * Shortcut fuctions to make calls to API endpoints related to Page object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { PAGE } from './_endpoints'

export default {
  /**
   * Performs options request to get page's schema.
   */
  options (config = {}) {
    return session.options(PAGE, config)
  },
  /**
   * Performs page listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(PAGE, config)
  },
  /**
   * Performs page creation
   *
   * @param {object} - Page data
   */
  create (data, config = {}) {
    return session.post(PAGE, data, config)
  },
  /**
   * Performs page retrieve
   *
   * @param {{int}} - Page ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${PAGE}${id}/`, config)
  },
  /**
   * Performs page update
   *
   * @param {int}    - Page ID
   * @param {object} - Page data
   */
  update (id, data, config = {}) {
    return session.patch(`${PAGE}${id}/`, data, config)
  },
  /**
   * Performs page retrieve
   *
   * @param {{int}} - ID of Page to delete
   */
  delete (id, config = {}) {
    return session.delete(`${PAGE}${id}/`, config)
  }
}
