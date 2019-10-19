/**
 * Shortcut fuctions to make calls to API endpoints related to Content_Type object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { CONTENT_TYPE } from './_endpoints'

export default {
  /**
   * Performs options request to get content_type's schema.
   */
  options (config = {}) {
    return session.options(CONTENT_TYPE, config)
  },
  /**
   * Performs content_type listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(CONTENT_TYPE, config)
  },
  /**
   * Performs content_type creation
   *
   * @param {object} - Content_Type data
   */
  create (data, config = {}) {
    return session.post(CONTENT_TYPE, data, config)
  },
  /**
   * Performs content_type retrieve
   *
   * @param {{int}} - Content_Type ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${CONTENT_TYPE}${id}/`, config)
  },
  /**
   * Performs content_type update
   *
   * @param {int}    - Content_Type ID
   * @param {object} - Content_Type data
   */
  update (id, data, config = {}) {
    return session.patch(`${CONTENT_TYPE}${id}/`, data, config)
  },
  /**
   * Performs content_type retrieve
   *
   * @param {{int}} - ID of Content_Type to delete
   */
  delete (id, config = {}) {
    return session.delete(`${CONTENT_TYPE}${id}/`, config)
  }
}
