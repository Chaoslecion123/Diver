/**
 * Shortcut fuctions to make calls to API endpoints related to Variant_Image object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { VARIANT_IMAGE } from './_endpoints'

export default {
  /**
   * Performs options request to get variant_image's schema.
   */
  options (config = {}) {
    return session.options(VARIANT_IMAGE, config)
  },
  /**
   * Performs variant_image listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(VARIANT_IMAGE, config)
  },
  /**
   * Performs variant_image creation
   *
   * @param {object} - Variant_Image data
   */
  create (data, config = {}) {
    return session.post(VARIANT_IMAGE, data, config)
  },
  /**
   * Performs variant_image retrieve
   *
   * @param {{int}} - Variant_Image ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${VARIANT_IMAGE}${id}/`, config)
  },
  /**
   * Performs variant_image update
   *
   * @param {int}    - Variant_Image ID
   * @param {object} - Variant_Image data
   */
  update (id, data, config = {}) {
    return session.patch(`${VARIANT_IMAGE}${id}/`, data, config)
  },
  /**
   * Performs variant_image retrieve
   *
   * @param {{int}} - ID of Variant_Image to delete
   */
  delete (id, config = {}) {
    return session.delete(`${VARIANT_IMAGE}${id}/`, config)
  }
}
