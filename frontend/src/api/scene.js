/**
 * Shortcut fuctions to make calls to API endpoints related to Scene object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SCENE } from './_endpoints'

export default {
  /**
   * Performs options request to get scene's schema.
   */
  options (config = {}) {
    return session.options(SCENE, config)
  },
  /**
   * Performs scene listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SCENE, config)
  },
  /**
   * Performs scene creation
   *
   * @param {object} - Scene data
   */
  create (data, config = {}) {
    return session.post(SCENE, data, config)
  },
  /**
   * Performs scene retrieve
   *
   * @param {{int}} - Scene ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SCENE}${id}/`, config)
  },
  /**
   * Performs scene update
   *
   * @param {int}    - Scene ID
   * @param {object} - Scene data
   */
  update (id, data, config = {}) {
    return session.patch(`${SCENE}${id}/`, data, config)
  },
  /**
   * Performs scene retrieve
   *
   * @param {{int}} - ID of Scene to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SCENE}${id}/`, config)
  }
}
