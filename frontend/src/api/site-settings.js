/**
 * Shortcut fuctions to make calls to API endpoints related to Site_Settings object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SITE_SETTINGS } from './_endpoints'

export default {
  /**
   * Performs options request to get site_settings's schema.
   */
  options (config = {}) {
    return session.options(SITE_SETTINGS, config)
  },
  /**
   * Performs site_settings listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SITE_SETTINGS, config)
  },
  /**
   * Performs site_settings creation
   *
   * @param {object} - Site_Settings data
   */
  create (data, config = {}) {
    return session.post(SITE_SETTINGS, data, config)
  },
  /**
   * Performs site_settings retrieve
   *
   * @param {{int}} - Site_Settings ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SITE_SETTINGS}${id}/`, config)
  },
  /**
   * Performs site_settings update
   *
   * @param {int}    - Site_Settings ID
   * @param {object} - Site_Settings data
   */
  update (id, data, config = {}) {
    return session.patch(`${SITE_SETTINGS}${id}/`, data, config)
  },
  /**
   * Performs site_settings retrieve
   *
   * @param {{int}} - ID of Site_Settings to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SITE_SETTINGS}${id}/`, config)
  }
}
