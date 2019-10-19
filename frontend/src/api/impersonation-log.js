/**
 * Shortcut fuctions to make calls to API endpoints related to Impersonation_Log object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { IMPERSONATION_LOG } from './_endpoints'

export default {
  /**
   * Performs options request to get impersonation_log's schema.
   */
  options (config = {}) {
    return session.options(IMPERSONATION_LOG, config)
  },
  /**
   * Performs impersonation_log listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(IMPERSONATION_LOG, config)
  },
  /**
   * Performs impersonation_log creation
   *
   * @param {object} - Impersonation_Log data
   */
  create (data, config = {}) {
    return session.post(IMPERSONATION_LOG, data, config)
  },
  /**
   * Performs impersonation_log retrieve
   *
   * @param {{int}} - Impersonation_Log ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${IMPERSONATION_LOG}${id}/`, config)
  },
  /**
   * Performs impersonation_log update
   *
   * @param {int}    - Impersonation_Log ID
   * @param {object} - Impersonation_Log data
   */
  update (id, data, config = {}) {
    return session.patch(`${IMPERSONATION_LOG}${id}/`, data, config)
  },
  /**
   * Performs impersonation_log retrieve
   *
   * @param {{int}} - ID of Impersonation_Log to delete
   */
  delete (id, config = {}) {
    return session.delete(`${IMPERSONATION_LOG}${id}/`, config)
  }
}
