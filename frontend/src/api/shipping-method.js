/**
 * Shortcut fuctions to make calls to API endpoints related to Shipping_Method object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SHIPPING_METHOD } from './_endpoints'

export default {
  /**
   * Performs options request to get shipping_method's schema.
   */
  options (config = {}) {
    return session.options(SHIPPING_METHOD, config)
  },
  /**
   * Performs shipping_method listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SHIPPING_METHOD, config)
  },
  /**
   * Performs shipping_method creation
   *
   * @param {object} - Shipping_Method data
   */
  create (data, config = {}) {
    return session.post(SHIPPING_METHOD, data, config)
  },
  /**
   * Performs shipping_method retrieve
   *
   * @param {{int}} - Shipping_Method ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SHIPPING_METHOD}${id}/`, config)
  },
  /**
   * Performs shipping_method update
   *
   * @param {int}    - Shipping_Method ID
   * @param {object} - Shipping_Method data
   */
  update (id, data, config = {}) {
    return session.patch(`${SHIPPING_METHOD}${id}/`, data, config)
  },
  /**
   * Performs shipping_method retrieve
   *
   * @param {{int}} - ID of Shipping_Method to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SHIPPING_METHOD}${id}/`, config)
  }
}
