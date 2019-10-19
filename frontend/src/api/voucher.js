/**
 * Shortcut fuctions to make calls to API endpoints related to Voucher object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { VOUCHER } from './_endpoints'

export default {
  /**
   * Performs options request to get voucher's schema.
   */
  options (config = {}) {
    return session.options(VOUCHER, config)
  },
  /**
   * Performs voucher listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(VOUCHER, config)
  },
  /**
   * Performs voucher creation
   *
   * @param {object} - Voucher data
   */
  create (data, config = {}) {
    return session.post(VOUCHER, data, config)
  },
  /**
   * Performs voucher retrieve
   *
   * @param {{int}} - Voucher ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${VOUCHER}${id}/`, config)
  },
  /**
   * Performs voucher update
   *
   * @param {int}    - Voucher ID
   * @param {object} - Voucher data
   */
  update (id, data, config = {}) {
    return session.patch(`${VOUCHER}${id}/`, data, config)
  },
  /**
   * Performs voucher retrieve
   *
   * @param {{int}} - ID of Voucher to delete
   */
  delete (id, config = {}) {
    return session.delete(`${VOUCHER}${id}/`, config)
  }
}
