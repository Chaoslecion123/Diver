/**
 * Shortcut fuctions to make calls to API endpoints related to Permission object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { PERMISSION } from './_endpoints'

export default {
  /**
   * Performs options request to get permission's schema.
   */
  options (config = {}) {
    return session.options(PERMISSION, config)
  },
  /**
   * Performs permission listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(PERMISSION, config)
  },
  /**
   * Performs permission creation
   *
   * @param {object} - Permission data
   */
  create (data, config = {}) {
    return session.post(PERMISSION, data, config)
  },
  /**
   * Performs permission retrieve
   *
   * @param {{int}} - Permission ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${PERMISSION}${id}/`, config)
  },
  /**
   * Performs permission update
   *
   * @param {int}    - Permission ID
   * @param {object} - Permission data
   */
  update (id, data, config = {}) {
    return session.patch(`${PERMISSION}${id}/`, data, config)
  },
  /**
   * Performs permission retrieve
   *
   * @param {{int}} - ID of Permission to delete
   */
  delete (id, config = {}) {
    return session.delete(`${PERMISSION}${id}/`, config)
  }
}
