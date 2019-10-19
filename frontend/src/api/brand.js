/**
 * Shortcut fuctions to make calls to API endpoints related to Brand object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { BRAND } from './_endpoints'

export default {
  /**
   * Performs options request to get brand's schema.
   */
  options (config = {}) {
    return session.options(BRAND, config)
  },
  /**
   * Performs brand listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(BRAND, config)
  },
  /**
   * Performs brand creation
   *
   * @param {object} - Brand data
   */
  create (data, config = {}) {
    return session.post(BRAND, data, config)
  },
  /**
   * Performs brand retrieve
   *
   * @param {{int}} - Brand ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${BRAND}${id}/`, config)
  },
  /**
   * Performs brand update
   *
   * @param {int}    - Brand ID
   * @param {object} - Brand data
   */
  update (id, data, config = {}) {
    return session.patch(`${BRAND}${id}/`, data, config)
  },
  /**
   * Performs brand retrieve
   *
   * @param {{int}} - ID of Brand to delete
   */
  delete (id, config = {}) {
    return session.delete(`${BRAND}${id}/`, config)
  },
  /**
   * Performs listing of featured brands
   */
  listFeatured (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${BRAND}featured/`, config)
  }
}
