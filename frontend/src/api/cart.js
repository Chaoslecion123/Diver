/**
 * Shortcut fuctions to make calls to API endpoints related to Cart object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CART } from './_endpoints'

export default {
  /**
   * Performs options request to get cart's schema.
   */
  options (config = {}) {
    return session.options(CART, config)
  },
  /**
   * Performs cart listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CART, config)
  },
  /**
   * Performs cart creation
   *
   * @param {object} - Cart data
   */
  create (data, config = {}) {
    return session.post(CART, data, config)
  },
  /**
   * Performs cart retrieve
   *
   * @param {{int}} - Cart ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CART}${id}/`, config)
  },
  /**
   * Performs cart update
   *
   * @param {int}    - Cart ID
   * @param {object} - Cart data
   */
  update (id, data, config = {}) {
    return session.patch(`${CART}${id}/`, data, config)
  },

  /**
   * Performs cart delete
   *
   * @param {{int}} - ID of Cart to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CART}${id}/`, config)
  },
  /**
   * Performs cart clear
   *
   * @param {{int}} - Cart ID
   */
  clear (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.post(`${CART}${id}/clear/`, config)
  },
  /**
   * Performs cart place order
   *
   * @param {{int}} - ID of Cart to delete
   */
  applyDiscount (id, data, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.post(`${CART}${id}/apply-discount/`, data, config)
  },
  /**
   * Performs cart place order
   *
   * @param {{int}} - ID of Cart to delete
   */
  placeOrder (id, data, config = {}) {
    return session.post(`${CART}${id}/place-order/`, data, config)
  }
}
