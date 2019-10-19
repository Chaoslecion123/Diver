/**
 * Shortcut fuctions to make calls to API endpoints related to Country_Area object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { COUNTRY_AREA } from './_endpoints'

export default {
  /**
   * Performs options request to get country_area's schema.
   */
  options (config = {}) {
    return session.options(COUNTRY_AREA, config)
  },
  /**
   * Performs country_area listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(COUNTRY_AREA, config)
  },
  /**
   * Performs country_area creation
   *
   * @param {object} - Country_Area data
   */
  create (data, config = {}) {
    return session.post(COUNTRY_AREA, data, config)
  },
  /**
   * Performs country_area retrieve
   *
   * @param {{int}} - Country_Area ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${COUNTRY_AREA}${id}/`, config)
  },
  /**
   * Performs country_area update
   *
   * @param {int}    - Country_Area ID
   * @param {object} - Country_Area data
   */
  update (id, data, config = {}) {
    return session.patch(`${COUNTRY_AREA}${id}/`, data, config)
  },
  /**
   * Performs country_area retrieve
   *
   * @param {{int}} - ID of Country_Area to delete
   */
  delete (id, config = {}) {
    return session.delete(`${COUNTRY_AREA}${id}/`, config)
  }
}
