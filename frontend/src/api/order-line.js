/**
 * Shortcut fuctions to make calls to API endpoints related to Order_Line object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { ORDER_LINE } from './_endpoints'

export default {
  /**
   * Performs options request to get order_line's schema.
   */
  options (config = {}) {
    return session.options(ORDER_LINE, config)
  },
  /**
   * Performs order_line listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(ORDER_LINE, config)
  },
  /**
   * Performs order_line creation
   *
   * @param {object} - Order_Line data
   */
  create (data, config = {}) {
    return session.post(ORDER_LINE, data, config)
  },
  /**
   * Performs order_line retrieve
   *
   * @param {{int}} - Order_Line ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${ORDER_LINE}${id}/`, config)
  },
  /**
   * Performs order_line update
   *
   * @param {int}    - Order_Line ID
   * @param {object} - Order_Line data
   */
  update (id, data, config = {}) {
    return session.patch(`${ORDER_LINE}${id}/`, data, config)
  },
  /**
   * Performs order_line retrieve
   *
   * @param {{int}} - ID of Order_Line to delete
   */
  delete (id, config = {}) {
    return session.delete(`${ORDER_LINE}${id}/`, config)
  }
}
