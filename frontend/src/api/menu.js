/**
 * Shortcut fuctions to make calls to API endpoints related to Menu object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { MENU } from './_endpoints'

export default {
  /**
   * Performs options request to get menu's schema.
   */
  options (config = {}) {
    return session.options(MENU, config)
  },
  /**
   * Performs menu listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(MENU, config)
  },
  /**
   * Performs menu creation
   *
   * @param {object} - Menu data
   */
  create (data, config = {}) {
    return session.post(MENU, data, config)
  },
  /**
   * Performs menu retrieve
   *
   * @param {{int}} - Menu ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${MENU}${id}/`, config)
  },
  /**
   * Performs menu update
   *
   * @param {int}    - Menu ID
   * @param {object} - Menu data
   */
  update (id, data, config = {}) {
    return session.patch(`${MENU}${id}/`, data, config)
  },
  /**
   * Performs menu retrieve
   *
   * @param {{int}} - ID of Menu to delete
   */
  delete (id, config = {}) {
    return session.delete(`${MENU}${id}/`, config)
  }
}
