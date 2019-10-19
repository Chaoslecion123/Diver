/**
 * Shortcut fuctions to make calls to API endpoints related to Physical_Store object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { PHYSICAL_STORE } from './_endpoints'

export default {
  /**
   * Performs options request to get physical_store's schema.
   */
  options (config = {}) {
    return session.options(PHYSICAL_STORE, config)
  },
  /**
   * Performs physical_store listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(PHYSICAL_STORE, config)
  },
  /**
   * Performs physical_store creation
   *
   * @param {object} - Physical_Store data
   */
  create (data, config = {}) {
    return session.post(PHYSICAL_STORE, data, config)
  },
  /**
   * Performs physical_store retrieve
   *
   * @param {{int}} - Physical_Store ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${PHYSICAL_STORE}${id}/`, config)
  },
  /**
   * Performs physical_store update
   *
   * @param {int}    - Physical_Store ID
   * @param {object} - Physical_Store data
   */
  update (id, data, config = {}) {
    return session.patch(`${PHYSICAL_STORE}${id}/`, data, config)
  },
  /**
   * Performs physical_store retrieve
   *
   * @param {{int}} - ID of Physical_Store to delete
   */
  delete (id, config = {}) {
    return session.delete(`${PHYSICAL_STORE}${id}/`, config)
  }
}
