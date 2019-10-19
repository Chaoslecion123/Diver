/**
 * Shortcut fuctions to make calls to API endpoints related to Fulfillment_Line object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { FULFILLMENT_LINE } from './_endpoints'

export default {
  /**
   * Performs options request to get fulfillment_line's schema.
   */
  options (config = {}) {
    return session.options(FULFILLMENT_LINE, config)
  },
  /**
   * Performs fulfillment_line listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(FULFILLMENT_LINE, config)
  },
  /**
   * Performs fulfillment_line creation
   *
   * @param {object} - Fulfillment_Line data
   */
  create (data, config = {}) {
    return session.post(FULFILLMENT_LINE, data, config)
  },
  /**
   * Performs fulfillment_line retrieve
   *
   * @param {{int}} - Fulfillment_Line ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${FULFILLMENT_LINE}${id}/`, config)
  },
  /**
   * Performs fulfillment_line update
   *
   * @param {int}    - Fulfillment_Line ID
   * @param {object} - Fulfillment_Line data
   */
  update (id, data, config = {}) {
    return session.patch(`${FULFILLMENT_LINE}${id}/`, data, config)
  },
  /**
   * Performs fulfillment_line retrieve
   *
   * @param {{int}} - ID of Fulfillment_Line to delete
   */
  delete (id, config = {}) {
    return session.delete(`${FULFILLMENT_LINE}${id}/`, config)
  }
}
