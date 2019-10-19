/**
 * Shortcut fuctions to make calls to API endpoints related to Transaction object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { TRANSACTION } from './_endpoints'

export default {
  /**
   * Performs options request to get transaction's schema.
   */
  options (config = {}) {
    return session.options(TRANSACTION, config)
  },
  /**
   * Performs transaction listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(TRANSACTION, config)
  },
  /**
   * Performs transaction creation
   *
   * @param {object} - Transaction data
   */
  create (data, config = {}) {
    return session.post(TRANSACTION, data, config)
  },
  /**
   * Performs transaction retrieve
   *
   * @param {{int}} - Transaction ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${TRANSACTION}${id}/`, config)
  },
  /**
   * Performs transaction update
   *
   * @param {int}    - Transaction ID
   * @param {object} - Transaction data
   */
  update (id, data, config = {}) {
    return session.patch(`${TRANSACTION}${id}/`, data, config)
  },
  /**
   * Performs transaction retrieve
   *
   * @param {{int}} - ID of Transaction to delete
   */
  delete (id, config = {}) {
    return session.delete(`${TRANSACTION}${id}/`, config)
  }
}
