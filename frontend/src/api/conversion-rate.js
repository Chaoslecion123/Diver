/**
 * Shortcut fuctions to make calls to API endpoints related to Conversion_Rate object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CONVERSION_RATE } from './_endpoints'

export default {
  /**
   * Performs options request to get conversion_rate's schema.
   */
  options (config = {}) {
    return session.options(CONVERSION_RATE, config)
  },
  /**
   * Performs conversion_rate listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CONVERSION_RATE, config)
  },
  /**
   * Performs conversion_rate creation
   *
   * @param {object} - Conversion_Rate data
   */
  create (data, config = {}) {
    return session.post(CONVERSION_RATE, data, config)
  },
  /**
   * Performs conversion_rate retrieve
   *
   * @param {{int}} - Conversion_Rate ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CONVERSION_RATE}${id}/`, config)
  },
  /**
   * Performs conversion_rate update
   *
   * @param {int}    - Conversion_Rate ID
   * @param {object} - Conversion_Rate data
   */
  update (id, data, config = {}) {
    return session.patch(`${CONVERSION_RATE}${id}/`, data, config)
  },
  /**
   * Performs conversion_rate retrieve
   *
   * @param {{int}} - ID of Conversion_Rate to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CONVERSION_RATE}${id}/`, config)
  }
}
