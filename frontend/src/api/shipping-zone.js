/**
 * Shortcut fuctions to make calls to API endpoints related to Shipping_Zone object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SHIPPING_ZONE } from './_endpoints'

export default {
  /**
   * Performs options request to get shipping_zone's schema.
   */
  options (config = {}) {
    return session.options(SHIPPING_ZONE, config)
  },
  /**
   * Performs shipping_zone listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SHIPPING_ZONE, config)
  },
  /**
   * Performs shipping_zone creation
   *
   * @param {object} - Shipping_Zone data
   */
  create (data, config = {}) {
    return session.post(SHIPPING_ZONE, data, config)
  },
  /**
   * Performs shipping_zone retrieve
   *
   * @param {{int}} - Shipping_Zone ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SHIPPING_ZONE}${id}/`, config)
  },
  /**
   * Performs shipping_zone update
   *
   * @param {int}    - Shipping_Zone ID
   * @param {object} - Shipping_Zone data
   */
  update (id, data, config = {}) {
    return session.patch(`${SHIPPING_ZONE}${id}/`, data, config)
  },
  /**
   * Performs shipping_zone retrieve
   *
   * @param {{int}} - ID of Shipping_Zone to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SHIPPING_ZONE}${id}/`, config)
  }
}
