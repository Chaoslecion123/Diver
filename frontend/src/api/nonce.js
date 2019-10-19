/**
 * Shortcut fuctions to make calls to API endpoints related to Nonce object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { NONCE } from './_endpoints'

export default {
  /**
   * Performs options request to get nonce's schema.
   */
  options (config = {}) {
    return session.options(NONCE, config)
  },
  /**
   * Performs nonce listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(NONCE, config)
  },
  /**
   * Performs nonce creation
   *
   * @param {object} - Nonce data
   */
  create (data, config = {}) {
    return session.post(NONCE, data, config)
  },
  /**
   * Performs nonce retrieve
   *
   * @param {{int}} - Nonce ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${NONCE}${id}/`, config)
  },
  /**
   * Performs nonce update
   *
   * @param {int}    - Nonce ID
   * @param {object} - Nonce data
   */
  update (id, data, config = {}) {
    return session.patch(`${NONCE}${id}/`, data, config)
  },
  /**
   * Performs nonce retrieve
   *
   * @param {{int}} - ID of Nonce to delete
   */
  delete (id, config = {}) {
    return session.delete(`${NONCE}${id}/`, config)
  }
}
