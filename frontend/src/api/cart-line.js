/**
 * Shortcut fuctions to make calls to API endpoints related to Cart_Line object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CART_LINE } from './_endpoints'

export default {
  /**
   * Performs options request to get cart_line's schema.
   */
  options (config = {}) {
    return session.options(CART_LINE, config)
  },
  /**
   * Performs cart_line listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CART_LINE, config)
  },
  /**
   * Performs cart_line creation
   *
   * @param {object} - Cart_Line data
   */
  create (data, config = {}) {
    return session.post(CART_LINE, data, config)
  },
  /**
   * Performs cart_line retrieve
   *
   * @param {{int}} - Cart_Line ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CART_LINE}${id}/`, config)
  },
  /**
   * Performs cart_line update
   *
   * @param {int}    - Cart_Line ID
   * @param {object} - Cart_Line data
   */
  update (id, data, config = {}) {
    return session.patch(`${CART_LINE}${id}/`, data, config)
  },
  /**
   * Performs cart_line retrieve
   *
   * @param {{int}} - ID of Cart_Line to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CART_LINE}${id}/`, config)
  }
}
