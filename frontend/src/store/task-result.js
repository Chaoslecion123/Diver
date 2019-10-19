import TASK_RESULT from '@/api/task-result'

import {
  /* Creating task_result flow */
  CREATE_BEGIN,
  CREATE_SUCCESS,
  CREATE_FAILURE,
  CREATE_SET_MESSAGES,
  CREATE_SET_STATUS_CODE,

  /* Reading task_result flow */
  READ_BEGIN,
  READ_SUCCESS,
  READ_FAILURE,
  READ_SET_MESSAGES,
  READ_SET_STATUS_CODE,

  /* Updating task_result flow */
  UPDATE_BEGIN,
  UPDATE_SUCCESS,
  UPDATE_FAILURE,
  UPDATE_SET_MESSAGES,
  UPDATE_SET_STATUS_CODE,

  /* Deleting task_result flow */
  DELETE_BEGIN,
  DELETE_SUCCESS,
  DELETE_FAILURE,
  DELETE_SET_MESSAGES,
  DELETE_SET_STATUS_CODE,

  /* Listing task_result flow */
  LIST_BEGIN,
  LIST_SUCCESS,
  LIST_FAILURE,
  LIST_SET_MESSAGES,
  LIST_SET_STATUS_CODE,

  /* Schemating task_result flow */
  SCHEMA_BEGIN,
  SCHEMA_SUCCESS,
  SCHEMA_FAILURE,
  SCHEMA_SET_MESSAGES,
  SCHEMA_SET_STATUS_CODE,

  /* Handle objects */
  SET_SCHEMA,
  SET_OBJECT,
  SET_OBJECT_LIST
} from './_processes'

const initialState = {
  schema: null,
  object: null,
  objects: [],

  /* Create state variables */
  creating: false,
  createError: false,
  createSuccess: false,
  createMessages: null,
  createStatusCode: null,

  /* Read state variables */
  reading: false,
  readError: false,
  readSuccess: false,
  readMessages: null,
  readStatusCode: null,

  /* Update state variables */
  updating: false,
  updateError: false,
  updateSuccess: false,
  updateMessages: null,
  updateStatusCode: null,

  /* Delete state variables */
  deleting: false,
  deleteError: false,
  deleteSuccess: false,
  deleteMessages: null,
  deleteStatusCode: null,

  /* List state variables */
  listing: false,
  listError: false,
  listSuccess: false,
  listMessages: null,
  listStatusCode: null,

  /* Schema state variables */
  schemating: false,
  schemaError: false,
  schemaSuccess: false,
  schemaMessages: null,
  schemaStatusCode: null
}

const actions = {
  create (
    { commit },
    {
      data,
      config = {}
    } = {}) {
    commit(CREATE_BEGIN)
    commit(CREATE_SET_MESSAGES, null)
    commit(CREATE_SET_STATUS_CODE, null)
    return TASK_RESULT
      .create(data, config)
      .then((response) => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(CREATE_SUCCESS)
      })
      .catch((error) => {
        commit(CREATE_FAILURE)
        commit(CREATE_SET_MESSAGES, error.response.data)
        commit(CREATE_SET_STATUS_CODE, error.response.status)
      })
  },

  read (
    { commit },
    {
      id,
      query = {},
      config = {}
    } = {}) {
    commit(READ_BEGIN)
    commit(READ_SET_MESSAGES, null)
    commit(READ_SET_STATUS_CODE, null)
    return TASK_RESULT
      .retrieve(id, query, config)
      .then((response) => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(READ_SUCCESS)
      })
      .catch((error) => {
        commit(READ_FAILURE)
        commit(READ_SET_MESSAGES, error.response.data)
        commit(READ_SET_STATUS_CODE, error.response.status)
      })
  },

  update (
    { commit },
    {
      id,
      data,
      config = {}
    } = {}) {
    commit(UPDATE_BEGIN)
    commit(UPDATE_SET_MESSAGES, null)
    commit(UPDATE_SET_STATUS_CODE, null)
    return TASK_RESULT
      .update(id, data, config)
      .then((response) => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(UPDATE_SUCCESS)
      })
      .catch((error) => {
        commit(UPDATE_FAILURE)
        commit(UPDATE_SET_MESSAGES, error.response.data)
        commit(UPDATE_SET_STATUS_CODE, error.response.status)
      })
  },

  delete (
    { commit },
    {
      id,
      config = {}
    } = {}) {
    commit(DELETE_BEGIN)
    commit(DELETE_SET_MESSAGES, null)
    commit(DELETE_SET_STATUS_CODE, null)
    return TASK_RESULT
      .delete(id, config)
      .then((response) => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(DELETE_SUCCESS)
      })
      .catch((error) => {
        commit(DELETE_FAILURE)
        commit(DELETE_SET_MESSAGES, error.response.data)
        commit(DELETE_SET_STATUS_CODE, error.response.status)
      })
  },

  list (
    { commit },
    {
      query = {},
      config = {}
    } = {}) {
    commit(LIST_BEGIN)
    commit(LIST_SET_MESSAGES, null)
    commit(LIST_SET_STATUS_CODE, null)
    return TASK_RESULT
      .list(query, config)
      .then((response) => {
        commit(SET_OBJECT_LIST, response.data)
      })
      .then(() => {
        commit(LIST_SUCCESS)
      })
      .catch((error) => {
        commit(LIST_FAILURE)
        commit(LIST_SET_MESSAGES, error.response.data)
        commit(LIST_SET_STATUS_CODE, error.response.status)
      })
  },

  schema (
    { commit },
    {
      config = {}
    } = {}) {
    commit(SCHEMA_BEGIN)
    commit(SCHEMA_SET_MESSAGES, null)
    commit(SCHEMA_SET_STATUS_CODE, null)
    return TASK_RESULT
      .options(config)
      .then((response) => {
        commit(SET_SCHEMA, response.data)
      })
      .then(() => {
        commit(SCHEMA_SUCCESS)
      })
      .catch((error) => {
        commit(SCHEMA_FAILURE)
        commit(SCHEMA_SET_MESSAGES, error.response.data)
        commit(SCHEMA_SET_STATUS_CODE, error.response.status)
      })
  }
}

const mutations = {
  /**
   * Creating task_result flow
   */
  [CREATE_BEGIN] (state) {
    state.creating = true
    state.createError = false
    state.createSuccess = false
  },
  [CREATE_SUCCESS] (state) {
    state.creating = false
    state.createError = false
    state.createSuccess = true
  },
  [CREATE_FAILURE] (state) {
    state.creating = false
    state.createError = true
    state.createSuccess = false
  },
  [CREATE_SET_MESSAGES] (state, messages) {
    state.createMessages = messages
  },
  [CREATE_SET_STATUS_CODE] (state, statusCode) {
    state.createStatusCode = statusCode
  },
  /**
   * Reading task_result flow
   */
  [READ_BEGIN] (state) {
    state.reading = true
    state.readError = false
    state.readSuccess = false
  },
  [READ_SUCCESS] (state) {
    state.reading = false
    state.readError = false
    state.readSuccess = true
  },
  [READ_FAILURE] (state) {
    state.reading = false
    state.readError = true
    state.readSuccess = false
  },
  [READ_SET_MESSAGES] (state, messages) {
    state.readMessages = messages
  },
  [READ_SET_STATUS_CODE] (state, statusCode) {
    state.readStatusCode = statusCode
  },
  /**
   * Updating task_result flow
   */
  [UPDATE_BEGIN] (state) {
    state.updating = true
    state.updateError = false
    state.updateSuccess = false
  },
  [UPDATE_SUCCESS] (state) {
    state.updating = false
    state.updateError = false
    state.updateSuccess = true
  },
  [UPDATE_FAILURE] (state) {
    state.updating = false
    state.updateError = true
    state.updateSuccess = false
  },
  [UPDATE_SET_MESSAGES] (state, messages) {
    state.updateMessages = messages
  },
  [UPDATE_SET_STATUS_CODE] (state, statusCode) {
    state.updateStatusCode = statusCode
  },
  /**
   * Deleting task_result flow
   */
  [DELETE_BEGIN] (state) {
    state.deleting = true
    state.deleteError = false
    state.deleteSuccess = false
  },
  [DELETE_SUCCESS] (state) {
    state.deleting = false
    state.deleteError = false
    state.deleteSuccess = true
  },
  [DELETE_FAILURE] (state) {
    state.deleting = false
    state.deleteError = true
    state.deleteSuccess = false
  },
  [DELETE_SET_MESSAGES] (state, messages) {
    state.deleteMessages = messages
  },
  [DELETE_SET_STATUS_CODE] (state, statusCode) {
    state.deleteStatusCode = statusCode
  },
  /**
   * Listing task_result flow
   */
  [LIST_BEGIN] (state) {
    state.listing = true
    state.listError = false
    state.listSuccess = false
  },
  [LIST_SUCCESS] (state) {
    state.listing = false
    state.listError = false
    state.listSuccess = true
  },
  [LIST_FAILURE] (state) {
    state.listing = false
    state.listError = true
    state.listSuccess = false
  },
  [LIST_SET_MESSAGES] (state, messages) {
    state.listMessages = messages
  },
  [LIST_SET_STATUS_CODE] (state, statusCode) {
    state.listStatusCode = statusCode
  },
  /**
   * Schemating task_result flow
   */
  [SCHEMA_BEGIN] (state) {
    state.schemaing = true
    state.schemaError = false
    state.schemaSuccess = false
  },
  [SCHEMA_SUCCESS] (state) {
    state.schemaing = false
    state.schemaError = false
    state.schemaSuccess = true
  },
  [SCHEMA_FAILURE] (state) {
    state.schemaing = false
    state.schemaError = true
    state.schemaSuccess = false
  },
  [SCHEMA_SET_MESSAGES] (state, messages) {
    state.schemaMessages = messages
  },
  [SCHEMA_SET_STATUS_CODE] (state, statusCode) {
    state.schemaStatusCode = statusCode
  },
  /**
    * Handle objects
    */
  [SET_SCHEMA] (state, schema) {
    state.schema = schema
  },
  [SET_OBJECT] (state, object) {
    state.object = object
  },
  [SET_OBJECT_LIST] (state, objects) {
    state.objects = objects
  }
}

export default {
  namespaced: true,
  state: initialState,
  actions,
  mutations
}
