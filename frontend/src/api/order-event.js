/**
 * Shortcut fuctions to make calls to API endpoints related to Order_Event object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { ORDER_EVENT } from './_endpoints'

export default {
  /**
   * Performs options request to get order_event's schema.
   */
  options (config = {}) {
    return session.options(ORDER_EVENT, config)
  },
  /**
   * Performs order_event listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(ORDER_EVENT, config)
  },
  /**
   * Performs order_event creation
   *
   * @param {object} - Order_Event data
   */
  create (data, config = {}) {
    return session.post(ORDER_EVENT, data, config)
  },
  /**
   * Performs order_event retrieve
   *
   * @param {{int}} - Order_Event ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${ORDER_EVENT}${id}/`, config)
  },
  /**
   * Performs order_event update
   *
   * @param {int}    - Order_Event ID
   * @param {object} - Order_Event data
   */
  update (id, data, config = {}) {
    return session.patch(`${ORDER_EVENT}${id}/`, data, config)
  },
  /**
   * Performs order_event retrieve
   *
   * @param {{int}} - ID of Order_Event to delete
   */
  delete (id, config = {}) {
    return session.delete(`${ORDER_EVENT}${id}/`, config)
  }
}
