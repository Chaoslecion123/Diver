/**
 * Shortcut fuctions to make calls to API endpoints related to Session object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SESSION } from './_endpoints'

export default {
  /**
   * Performs options request to get session's schema.
   */
  options (config = {}) {
    return session.options(SESSION, config)
  },
  /**
   * Performs session listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SESSION, config)
  },
  /**
   * Performs session creation
   *
   * @param {object} - Session data
   */
  create (data, config = {}) {
    return session.post(SESSION, data, config)
  },
  /**
   * Performs session retrieve
   *
   * @param {{int}} - Session ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SESSION}${id}/`, config)
  },
  /**
   * Performs session update
   *
   * @param {int}    - Session ID
   * @param {object} - Session data
   */
  update (id, data, config = {}) {
    return session.patch(`${SESSION}${id}/`, data, config)
  },
  /**
   * Performs session retrieve
   *
   * @param {{int}} - ID of Session to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SESSION}${id}/`, config)
  }
}
