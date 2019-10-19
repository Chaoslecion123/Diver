/**
 * Shortcut fuctions to make calls to API endpoints related to Vat object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { VAT } from './_endpoints'

export default {
  /**
   * Performs options request to get vat's schema.
   */
  options (config = {}) {
    return session.options(VAT, config)
  },
  /**
   * Performs vat listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(VAT, config)
  },
  /**
   * Performs vat creation
   *
   * @param {object} - Vat data
   */
  create (data, config = {}) {
    return session.post(VAT, data, config)
  },
  /**
   * Performs vat retrieve
   *
   * @param {{int}} - Vat ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${VAT}${id}/`, config)
  },
  /**
   * Performs vat update
   *
   * @param {int}    - Vat ID
   * @param {object} - Vat data
   */
  update (id, data, config = {}) {
    return session.patch(`${VAT}${id}/`, data, config)
  },
  /**
   * Performs vat retrieve
   *
   * @param {{int}} - ID of Vat to delete
   */
  delete (id, config = {}) {
    return session.delete(`${VAT}${id}/`, config)
  }
}
