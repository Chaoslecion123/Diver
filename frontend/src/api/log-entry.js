/**
 * Shortcut fuctions to make calls to API endpoints related to Log_Entry object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { LOG_ENTRY } from './_endpoints'

export default {
  /**
   * Performs options request to get log_entry's schema.
   */
  options (config = {}) {
    return session.options(LOG_ENTRY, config)
  },
  /**
   * Performs log_entry listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(LOG_ENTRY, config)
  },
  /**
   * Performs log_entry creation
   *
   * @param {object} - Log_Entry data
   */
  create (data, config = {}) {
    return session.post(LOG_ENTRY, data, config)
  },
  /**
   * Performs log_entry retrieve
   *
   * @param {{int}} - Log_Entry ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${LOG_ENTRY}${id}/`, config)
  },
  /**
   * Performs log_entry update
   *
   * @param {int}    - Log_Entry ID
   * @param {object} - Log_Entry data
   */
  update (id, data, config = {}) {
    return session.patch(`${LOG_ENTRY}${id}/`, data, config)
  },
  /**
   * Performs log_entry retrieve
   *
   * @param {{int}} - ID of Log_Entry to delete
   */
  delete (id, config = {}) {
    return session.delete(`${LOG_ENTRY}${id}/`, config)
  }
}
