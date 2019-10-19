/**
 * Shortcut fuctions to make calls to API endpoints related to Customer_Note object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CUSTOMER_NOTE } from './_endpoints'

export default {
  /**
   * Performs options request to get customer_note's schema.
   */
  options (config = {}) {
    return session.options(CUSTOMER_NOTE, config)
  },
  /**
   * Performs customer_note listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CUSTOMER_NOTE, config)
  },
  /**
   * Performs customer_note creation
   *
   * @param {object} - Customer_Note data
   */
  create (data, config = {}) {
    return session.post(CUSTOMER_NOTE, data, config)
  },
  /**
   * Performs customer_note retrieve
   *
   * @param {{int}} - Customer_Note ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CUSTOMER_NOTE}${id}/`, config)
  },
  /**
   * Performs customer_note update
   *
   * @param {int}    - Customer_Note ID
   * @param {object} - Customer_Note data
   */
  update (id, data, config = {}) {
    return session.patch(`${CUSTOMER_NOTE}${id}/`, data, config)
  },
  /**
   * Performs customer_note retrieve
   *
   * @param {{int}} - ID of Customer_Note to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CUSTOMER_NOTE}${id}/`, config)
  }
}
