/**
 * Shortcut fuctions to make calls to API endpoints related to Task_Result object
 */
import session from './_session'
import { paramsSerializer } from './_utils'
import { camelToSnake } from '@/_utils'
import { TASK_RESULT } from './_endpoints'

export default {
  /**
   * Performs options request to get task_result's schema.
   */
  options (config = {}) {
    return session.options(TASK_RESULT, config)
  },
  /**
   * Performs task_result listing
   */
  list (query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(TASK_RESULT, config)
  },
  /**
   * Performs task_result creation
   *
   * @param {object} - Task_Result data
   */
  create (data, config = {}) {
    return session.post(TASK_RESULT, data, config)
  },
  /**
   * Performs task_result retrieve
   *
   * @param {{int}} - Task_Result ID
   */
  retrieve (id, query = {}, config = {}) {
    config.params = camelToSnake(query)
    config.paramsSerializer = paramsSerializer
    return session.get(`${TASK_RESULT}${id}/`, config)
  },
  /**
   * Performs task_result update
   *
   * @param {int}    - Task_Result ID
   * @param {object} - Task_Result data
   */
  update (id, data, config = {}) {
    return session.patch(`${TASK_RESULT}${id}/`, data, config)
  },
  /**
   * Performs task_result retrieve
   *
   * @param {{int}} - ID of Task_Result to delete
   */
  delete (id, config = {}) {
    return session.delete(`${TASK_RESULT}${id}/`, config)
  }
}
