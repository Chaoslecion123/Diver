/**
 * Shortcut fuctions to make calls to API endpoints related to Menu_Item object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { MENU_ITEM } from './_endpoints'

export default {
  /**
   * Performs options request to get menu_item's schema.
   */
  options (config = {}) {
    return session.options(MENU_ITEM, config)
  },
  /**
   * Performs menu_item listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(MENU_ITEM, config)
  },
  /**
   * Performs menu_item creation
   *
   * @param {object} - Menu_Item data
   */
  create (data, config = {}) {
    return session.post(MENU_ITEM, data, config)
  },
  /**
   * Performs menu_item retrieve
   *
   * @param {{int}} - Menu_Item ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${MENU_ITEM}${id}/`, config)
  },
  /**
   * Performs menu_item update
   *
   * @param {int}    - Menu_Item ID
   * @param {object} - Menu_Item data
   */
  update (id, data, config = {}) {
    return session.patch(`${MENU_ITEM}${id}/`, data, config)
  },
  /**
   * Performs menu_item retrieve
   *
   * @param {{int}} - ID of Menu_Item to delete
   */
  delete (id, config = {}) {
    return session.delete(`${MENU_ITEM}${id}/`, config)
  }
}
