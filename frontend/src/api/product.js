/**
 * Shortcut fuctions to make calls to API endpoints related to Product object
 */
import session from './_session'
import { paramsSerializer, serializeJsonData } from './_utils'
import { camelToSnake } from '@/_utils'
import { PRODUCT } from './_endpoints'

export default {
  /**
   * Performs options request to get product's schema.
   */
  options (config = {}) {
    return session.options(PRODUCT, config)
  },
  /**
   * Performs product listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(PRODUCT, config)
  },
  /**
   * Performs product creation
   *
   * @param {object} - Product data
   */
  create (data, config = {}) {
    return session.post(PRODUCT, data, config)
  },
  /**
   * Performs product retrieve
   *
   * @param {{int}} - Product ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${PRODUCT}${id}/`, config)
  },
  /**
   * Performs product update
   *
   * @param {int}    - Product ID
   * @param {object} - Product data
   */
  update (id, data, config = {}) {
    return session.patch(`${PRODUCT}${id}/`, data, config)
  },
  /**
   * Performs product retrieve
   *
   * @param {{int}} - ID of Product to delete
   */
  delete (id, config = {}) {
    return session.delete(`${PRODUCT}${id}/`, config)
  },
  /**
   * Performs product adition to cart
   *
   * @param {object} - Product data
   */
  addToCart (id, data, config = {}) {
    return session.post(`${PRODUCT}${id}/add-to-checkout/`, serializeJsonData(data), config)
  },
  /**
   * Performs product adition to cart
   *
   * @param {object} - Product data
   */
  addToFavorites (id, data = {}, config = {}) {
    return session.post(`${PRODUCT}${id}/add-to-favorites/`, serializeJsonData(data), config)
  },
  /**
   * Performs product adition to cart
   *
   * @param {object} - Product data
   */
  removeFromFavorites (id, data = {}, config = {}) {
    return session.post(`${PRODUCT}${id}/remove-from-favorites/`, serializeJsonData(data), config)
  }
}
