/**
 * Shortcut fuctions to make calls to API endpoints related to Category object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CATEGORY } from './_endpoints'

export default {
  /**
   * Performs options request to get category's schema.
   */
  options (config = {}) {
    return session.options(CATEGORY, config)
  },
  /**
   * Performs category listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CATEGORY, config)
  },
  /**
   * Performs category creation
   *
   * @param {object} - Category data
   */
  create (data, config = {}) {
    return session.post(CATEGORY, data, config)
  },
  /**
   * Performs category retrieve
   *
   * @param {{int}} - Category ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CATEGORY}${id}/`, config)
  },
  /**
   * Performs category update
   *
   * @param {int}    - Category ID
   * @param {object} - Category data
   */
  update (id, data, config = {}) {
    return session.patch(`${CATEGORY}${id}/`, data, config)
  },
  /**
   * Performs category retrieve
   *
   * @param {{int}} - ID of Category to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CATEGORY}${id}/`, config)
  }
}
