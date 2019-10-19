/**
 * Shortcut fuctions to make calls to API endpoints related to Group object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { GROUP } from './_endpoints'

export default {
  /**
   * Performs options request to get group's schema.
   */
  options (config = {}) {
    return session.options(GROUP, config)
  },
  /**
   * Performs group listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(GROUP, config)
  },
  /**
   * Performs group creation
   *
   * @param {object} - Group data
   */
  create (data, config = {}) {
    return session.post(GROUP, data, config)
  },
  /**
   * Performs group retrieve
   *
   * @param {{int}} - Group ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${GROUP}${id}/`, config)
  },
  /**
   * Performs group update
   *
   * @param {int}    - Group ID
   * @param {object} - Group data
   */
  update (id, data, config = {}) {
    return session.patch(`${GROUP}${id}/`, data, config)
  },
  /**
   * Performs group retrieve
   *
   * @param {{int}} - ID of Group to delete
   */
  delete (id, config = {}) {
    return session.delete(`${GROUP}${id}/`, config)
  }
}
