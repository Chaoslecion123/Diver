/**
 * Shortcut fuctions to make calls to API endpoints related to Order object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { ORDER } from './_endpoints'

export default {
  /**
   * Performs options request to get order's schema.
   */
  options (config = {}) {
    return session.options(ORDER, config)
  },
  /**
   * Performs order listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(ORDER, config)
  },
  /**
   * Performs order creation
   *
   * @param {object} - Order data
   */
  create (data, config = {}) {
    return session.post(ORDER, data, config)
  },
  /**
   * Performs order retrieve
   *
   * @param {{int}} - Order ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${ORDER}${id}/`, config)
  },
  /**
   * Performs order update
   *
   * @param {int}    - Order ID
   * @param {object} - Order data
   */
  update (id, data, config = {}) {
    return session.patch(`${ORDER}${id}/`, data, config)
  },
  /**
   * Performs order retrieve
   *
   * @param {{int}} - ID of Order to delete
   */
  delete (id, config = {}) {
    return session.delete(`${ORDER}${id}/`, config)
  }
}
