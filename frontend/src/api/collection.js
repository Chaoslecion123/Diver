/**
 * Shortcut fuctions to make calls to API endpoints related to Collection object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { COLLECTION } from './_endpoints'

export default {
  /**
   * Performs options request to get collection's schema.
   */
  options (config = {}) {
    return session.options(COLLECTION, config)
  },
  /**
   * Performs collection listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(COLLECTION, config)
  },
  /**
   * Performs collection creation
   *
   * @param {object} - Collection data
   */
  create (data, config = {}) {
    return session.post(COLLECTION, data, config)
  },
  /**
   * Performs collection retrieve
   *
   * @param {{int}} - Collection ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${COLLECTION}${id}/`, config)
  },
  /**
   * Performs collection update
   *
   * @param {int}    - Collection ID
   * @param {object} - Collection data
   */
  update (id, data, config = {}) {
    return session.patch(`${COLLECTION}${id}/`, data, config)
  },
  /**
   * Performs collection retrieve
   *
   * @param {{int}} - ID of Collection to delete
   */
  delete (id, config = {}) {
    return session.delete(`${COLLECTION}${id}/`, config)
  }
}
