/**
 * Shortcut fuctions to make calls to API endpoints related to Slider object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { STOREFRONT_SLIDER } from './_endpoints'

export default {
  /**
   * Performs options request to get slider's schema.
   */
  options (config = {}) {
    return session.options(STOREFRONT_SLIDER, config)
  },
  /**
   * Performs slider listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(STOREFRONT_SLIDER, config)
  },
  /**
   * Performs slider creation
   *
   * @param {object} - Slider data
   */
  create (data, config = {}) {
    return session.post(STOREFRONT_SLIDER, data, config)
  },
  /**
   * Performs slider retrieve
   *
   * @param {{int}} - Slider ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${STOREFRONT_SLIDER}${id}/`, config)
  },
  /**
   * Performs slider update
   *
   * @param {int}    - Slider ID
   * @param {object} - Slider data
   */
  update (id, data, config = {}) {
    return session.patch(`${STOREFRONT_SLIDER}${id}/`, data, config)
  },
  /**
   * Performs slider retrieve
   *
   * @param {{int}} - ID of Slider to delete
   */
  delete (id, config = {}) {
    return session.delete(`${STOREFRONT_SLIDER}${id}/`, config)
  },
  /**
   * Get active slider
   *
   */
  active (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(STOREFRONT_SLIDER, config)
  }
}
