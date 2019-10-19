/**
 * Shortcut fuctions to make calls to API endpoints related to Code object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CODE } from './_endpoints'

export default {
  /**
   * Performs options request to get code's schema.
   */
  options (config = {}) {
    return session.options(CODE, config)
  },
  /**
   * Performs code listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CODE, config)
  },
  /**
   * Performs code creation
   *
   * @param {object} - Code data
   */
  create (data, config = {}) {
    return session.post(CODE, data, config)
  },
  /**
   * Performs code retrieve
   *
   * @param {{int}} - Code ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CODE}${id}/`, config)
  },
  /**
   * Performs code update
   *
   * @param {int}    - Code ID
   * @param {object} - Code data
   */
  update (id, data, config = {}) {
    return session.patch(`${CODE}${id}/`, data, config)
  },
  /**
   * Performs code retrieve
   *
   * @param {{int}} - ID of Code to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CODE}${id}/`, config)
  }
}
