/**
 * Shortcut fuctions to make calls to API endpoints related to Slider object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { SLIDER } from './_endpoints'

export default {
  /**
   * Performs options request to get slider's schema.
   */
  options (config = {}) {
    return session.options(SLIDER, config)
  },
  /**
   * Performs slider listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(SLIDER, config)
  },
  /**
   * Performs slider creation
   *
   * @param {object} - Slider data
   */
  create (data, config = {}) {
    return session.post(SLIDER, data, config)
  },
  /**
   * Performs slider retrieve
   *
   * @param {{int}} - Slider ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${SLIDER}${id}/`, config)
  },
  /**
   * Performs slider update
   *
   * @param {int}    - Slider ID
   * @param {object} - Slider data
   */
  update (id, data, config = {}) {
    return session.patch(`${SLIDER}${id}/`, data, config)
  },
  /**
   * Performs slider retrieve
   *
   * @param {{int}} - ID of Slider to delete
   */
  delete (id, config = {}) {
    return session.delete(`${SLIDER}${id}/`, config)
  },
  /**
   * Performs slider listing
   */
  homepage (config = {}) {
    return session.get(`${SLIDER}homepage/`, config)
  }
}
