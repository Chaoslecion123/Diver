/**
 * Shortcut fuctions to make calls to API endpoints related to Token object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { TOKEN } from './_endpoints'

export default {
  /**
   * Performs options request to get token's schema.
   */
  options (config = {}) {
    return session.options(TOKEN, config)
  },
  /**
   * Performs token listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(TOKEN, config)
  },
  /**
   * Performs token creation
   *
   * @param {object} - Token data
   */
  create (data, config = {}) {
    return session.post(TOKEN, data, config)
  },
  /**
   * Performs token retrieve
   *
   * @param {{int}} - Token ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${TOKEN}${id}/`, config)
  },
  /**
   * Performs token update
   *
   * @param {int}    - Token ID
   * @param {object} - Token data
   */
  update (id, data, config = {}) {
    return session.patch(`${TOKEN}${id}/`, data, config)
  },
  /**
   * Performs token retrieve
   *
   * @param {{int}} - ID of Token to delete
   */
  delete (id, config = {}) {
    return session.delete(`${TOKEN}${id}/`, config)
  }
}
