/**
 * Shortcut fuctions to make calls to API endpoints related to City_Area object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CITY_AREA } from './_endpoints'

export default {
  /**
   * Performs options request to get city_area's schema.
   */
  options (config = {}) {
    return session.options(CITY_AREA, config)
  },
  /**
   * Performs city_area listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CITY_AREA, config)
  },
  /**
   * Performs city_area creation
   *
   * @param {object} - City_Area data
   */
  create (data, config = {}) {
    return session.post(CITY_AREA, data, config)
  },
  /**
   * Performs city_area retrieve
   *
   * @param {{int}} - City_Area ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CITY_AREA}${id}/`, config)
  },
  /**
   * Performs city_area update
   *
   * @param {int}    - City_Area ID
   * @param {object} - City_Area data
   */
  update (id, data, config = {}) {
    return session.patch(`${CITY_AREA}${id}/`, data, config)
  },
  /**
   * Performs city_area retrieve
   *
   * @param {{int}} - ID of City_Area to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CITY_AREA}${id}/`, config)
  }
}
