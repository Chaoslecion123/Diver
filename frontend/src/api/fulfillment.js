/**
 * Shortcut fuctions to make calls to API endpoints related to Fulfillment object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { FULFILLMENT } from './_endpoints'

export default {
  /**
   * Performs options request to get fulfillment's schema.
   */
  options (config = {}) {
    return session.options(FULFILLMENT, config)
  },
  /**
   * Performs fulfillment listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(FULFILLMENT, config)
  },
  /**
   * Performs fulfillment creation
   *
   * @param {object} - Fulfillment data
   */
  create (data, config = {}) {
    return session.post(FULFILLMENT, data, config)
  },
  /**
   * Performs fulfillment retrieve
   *
   * @param {{int}} - Fulfillment ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${FULFILLMENT}${id}/`, config)
  },
  /**
   * Performs fulfillment update
   *
   * @param {int}    - Fulfillment ID
   * @param {object} - Fulfillment data
   */
  update (id, data, config = {}) {
    return session.patch(`${FULFILLMENT}${id}/`, data, config)
  },
  /**
   * Performs fulfillment retrieve
   *
   * @param {{int}} - ID of Fulfillment to delete
   */
  delete (id, config = {}) {
    return session.delete(`${FULFILLMENT}${id}/`, config)
  }
}
