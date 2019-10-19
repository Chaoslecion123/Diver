/**
 * Shortcut fuctions to make calls to API endpoints related to Payment object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { PAYMENT } from './_endpoints'

export default {
  /**
   * Performs options request to get payment's schema.
   */
  options (config = {}) {
    return session.options(PAYMENT, config)
  },
  /**
   * Performs payment listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(PAYMENT, config)
  },
  /**
   * Performs payment creation
   *
   * @param {object} - Payment data
   */
  create (data, config = {}) {
    return session.post(PAYMENT, data, config)
  },
  /**
   * Performs payment retrieve
   *
   * @param {{int}} - Payment ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${PAYMENT}${id}/`, config)
  },
  /**
   * Performs payment update
   *
   * @param {int}    - Payment ID
   * @param {object} - Payment data
   */
  update (id, data, config = {}) {
    return session.patch(`${PAYMENT}${id}/`, data, config)
  },
  /**
   * Performs payment retrieve
   *
   * @param {{int}} - ID of Payment to delete
   */
  delete (id, config = {}) {
    return session.delete(`${PAYMENT}${id}/`, config)
  }
}
