import PRODUCT from '@/api/product'

import {
  /* Creating product flow */
  CREATE_BEGIN,
  CREATE_SUCCESS,
  CREATE_FAILURE,
  CREATE_SET_MESSAGES,
  CREATE_SET_STATUS_CODE,

  /* Reading product flow */
  READ_BEGIN,
  READ_SUCCESS,
  READ_FAILURE,
  READ_SET_MESSAGES,
  READ_SET_STATUS_CODE,

  /* Updating product flow */
  UPDATE_BEGIN,
  UPDATE_SUCCESS,
  UPDATE_FAILURE,
  UPDATE_SET_MESSAGES,
  UPDATE_SET_STATUS_CODE,

  /* Deleting product flow */
  DELETE_BEGIN,
  DELETE_SUCCESS,
  DELETE_FAILURE,
  DELETE_SET_MESSAGES,
  DELETE_SET_STATUS_CODE,

  /* Listing product flow */
  LIST_BEGIN,
  LIST_SUCCESS,
  LIST_FAILURE,
  LIST_SET_MESSAGES,
  LIST_SET_STATUS_CODE,

  /* Schemating product flow */
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

/* Adding to cart flow */
const ADD_TO_CART_BEGIN = 'ADD_TO_CART_BEGIN'
const ADD_TO_CART_SUCCESS = 'ADD_TO_CART_SUCCESS'
const ADD_TO_CART_FAILURE = 'ADD_TO_CART_FAILURE'
const ADD_TO_CART_SET_MESSAGES = 'ADD_TO_CART_SET_MESSAGES'
const ADD_TO_CART_SET_STATUS_CODE = 'ADD_TO_CART_SET_STATUS_CODE'

const ADD_TO_FAVORITES_BEGIN = 'ADD_TO_FAVORITES_BEGIN'
const ADD_TO_FAVORITES_SUCCESS = 'ADD_TO_FAVORITES_SUCCESS'
const ADD_TO_FAVORITES_FAILURE = 'ADD_TO_FAVORITES_FAILURE'
const ADD_TO_FAVORITES_SET_MESSAGES = 'ADD_TO_FAVORITES_SET_MESSAGES'
const ADD_TO_FAVORITES_SET_STATUS_CODE = 'ADD_TO_FAVORITES_SET_STATUS_CODE'

const REMOVE_FROM_FAVORITES_BEGIN = 'REMOVE_FROM_FAVORITES_BEGIN'
const REMOVE_FROM_FAVORITES_SUCCESS = 'REMOVE_FROM_FAVORITES_SUCCESS'
const REMOVE_FROM_FAVORITES_FAILURE = 'REMOVE_FROM_FAVORITES_FAILURE'
const REMOVE_FROM_FAVORITES_SET_MESSAGES = 'REMOVE_FROM_FAVORITES_SET_MESSAGES'
const REMOVE_FROM_FAVORITES_SET_STATUS_CODE = 'REMOVE_FROM_FAVORITES_SET_STATUS_CODE'

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

  /* Add to cart state variables */
  addingToCart: false,
  addToCartError: false,
  addToCartSuccess: false,
  addToCartMessages: null,
  addToCartStatusCode: null,

  /* Add to cart state variables */
  addingToFavorites: false,
  addToFavoritesError: false,
  addToFavoritesSuccess: false,
  addToFavoritesMessages: null,
  addToFavoritesStatusCode: null,

  /* Add to cart state variables */
  removingFromFavorites: false,
  removeFromFavoritesError: false,
  removeFromFavoritesSuccess: false,
  removeFromFavoritesMessages: null,
  removeFromFavoritesStatusCode: null,

  /* Schema state variables */
  schemating: false,
  schemaError: false,
  schemaSuccess: false,
  schemaMessages: null,
  schemaStatusCode: null
}

const actions = {
  create ({ commit }, { data, config = {} } = {}) {
    commit(CREATE_BEGIN)
    commit(CREATE_SET_MESSAGES, null)
    commit(CREATE_SET_STATUS_CODE, null)
    return PRODUCT.create(data, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(CREATE_SUCCESS)
      })
      .catch(error => {
        commit(CREATE_FAILURE)
        commit(CREATE_SET_MESSAGES, error.response.data)
        commit(CREATE_SET_STATUS_CODE, error.response.status)
      })
  },

  read ({ commit }, { id, query = {}, config = {} } = {}) {
    commit(READ_BEGIN)
    commit(READ_SET_MESSAGES, null)
    commit(READ_SET_STATUS_CODE, null)
    return PRODUCT.retrieve(id, query, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(READ_SUCCESS)
      })
      .catch(error => {
        commit(READ_FAILURE)
        commit(READ_SET_MESSAGES, error.response.data)
        commit(READ_SET_STATUS_CODE, error.response.status)
      })
  },

  update ({ commit }, { id, data, config = {} } = {}) {
    commit(UPDATE_BEGIN)
    commit(UPDATE_SET_MESSAGES, null)
    commit(UPDATE_SET_STATUS_CODE, null)
    return PRODUCT.update(id, data, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(UPDATE_SUCCESS)
      })
      .catch(error => {
        commit(UPDATE_FAILURE)
        commit(UPDATE_SET_MESSAGES, error.response.data)
        commit(UPDATE_SET_STATUS_CODE, error.response.status)
      })
  },

  delete ({ commit }, { id, config = {} } = {}) {
    commit(DELETE_BEGIN)
    commit(DELETE_SET_MESSAGES, null)
    commit(DELETE_SET_STATUS_CODE, null)
    return PRODUCT.delete(id, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(DELETE_SUCCESS)
      })
      .catch(error => {
        commit(DELETE_FAILURE)
        commit(DELETE_SET_MESSAGES, error.response.data)
        commit(DELETE_SET_STATUS_CODE, error.response.status)
      })
  },

  list ({ commit }, { query = {}, config = {} } = {}) {
    commit(LIST_BEGIN)
    commit(LIST_SET_MESSAGES, null)
    commit(LIST_SET_STATUS_CODE, null)
    return PRODUCT.list(query, config)
      .then(response => {
        commit(SET_OBJECT_LIST, response.data)
      })
      .then(() => {
        commit(LIST_SUCCESS)
      })
      .catch(error => {
        commit(LIST_FAILURE)
        commit(LIST_SET_MESSAGES, error.response.data)
        commit(LIST_SET_STATUS_CODE, error.response.status)
      })
  },

  addToCart ({ commit }, { id, data, config = {} } = {}) {
    commit(ADD_TO_CART_BEGIN)
    commit(ADD_TO_CART_SET_MESSAGES, null)
    commit(ADD_TO_CART_SET_STATUS_CODE, null)
    return PRODUCT.addToCart(id, data, config)
      .then(response => {
        commit('cart/SET_TOKEN', response.data.token, { root: true })
        commit(ADD_TO_CART_SUCCESS)
      })
      .catch(error => {
        commit(ADD_TO_CART_FAILURE)
        commit(ADD_TO_CART_SET_MESSAGES, error.response.data)
        commit(ADD_TO_CART_SET_STATUS_CODE, error.response.status)
      })
  },

  addToFavorites ({ commit }, { id, data, config = {} } = {}) {
    commit(ADD_TO_FAVORITES_BEGIN)
    commit(ADD_TO_FAVORITES_SET_MESSAGES, null)
    commit(ADD_TO_FAVORITES_SET_STATUS_CODE, null)
    return PRODUCT.addToFavorites(id, data, config)
      .then(response => {
        commit(ADD_TO_FAVORITES_SUCCESS)
      })
      .catch(error => {
        commit(ADD_TO_FAVORITES_FAILURE)
        commit(ADD_TO_FAVORITES_SET_MESSAGES, error.response.data)
        commit(ADD_TO_FAVORITES_SET_STATUS_CODE, error.response.status)
      })
  },

  removeFromFavorites ({ commit }, { id, data, config = {} } = {}) {
    commit(REMOVE_FROM_FAVORITES_BEGIN)
    commit(REMOVE_FROM_FAVORITES_SET_MESSAGES, null)
    commit(REMOVE_FROM_FAVORITES_SET_STATUS_CODE, null)
    return PRODUCT.removeFromFavorites(id, data, config)
      .then(response => {
        commit(REMOVE_FROM_FAVORITES_SUCCESS)
      })
      .catch(error => {
        commit(REMOVE_FROM_FAVORITES_FAILURE)
        commit(REMOVE_FROM_FAVORITES_SET_MESSAGES, error.response.data)
        commit(REMOVE_FROM_FAVORITES_SET_STATUS_CODE, error.response.status)
      })
  },

  schema ({ commit }, { config = {} } = {}) {
    commit(SCHEMA_BEGIN)
    commit(SCHEMA_SET_MESSAGES, null)
    commit(SCHEMA_SET_STATUS_CODE, null)
    return PRODUCT.options(config)
      .then(response => {
        commit(SET_SCHEMA, response.data)
      })
      .then(() => {
        commit(SCHEMA_SUCCESS)
      })
      .catch(error => {
        commit(SCHEMA_FAILURE)
        commit(SCHEMA_SET_MESSAGES, error.response.data)
        commit(SCHEMA_SET_STATUS_CODE, error.response.status)
      })
  }
}

const mutations = {
  /**
   * Creating product flow
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
   * Reading product flow
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
   * Updating product flow
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
   * Deleting product flow
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
   * Listing product flow
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
   * Add product to cart flow
   */
  [ADD_TO_CART_BEGIN] (state) {
    state.addingToCart = true
    state.addToCartError = false
    state.addToCartSuccess = false
  },
  [ADD_TO_CART_SUCCESS] (state) {
    state.addingToCart = false
    state.addToCartError = false
    state.addToCartSuccess = true
  },
  [ADD_TO_CART_FAILURE] (state) {
    state.addingToCart = false
    state.addToCartError = true
    state.addToCartSuccess = false
  },
  [ADD_TO_CART_SET_MESSAGES] (state, messages) {
    state.addToCartMessages = messages
  },
  [ADD_TO_CART_SET_STATUS_CODE] (state, statusCode) {
    state.addToCartStatusCode = statusCode
  },
  /**
   * Add product to favorites flow
   */
  [ADD_TO_FAVORITES_BEGIN] (state) {
    state.addingToFavorites = true
    state.addToFavoritesError = false
    state.addToFavoritesSuccess = false
  },
  [ADD_TO_FAVORITES_SUCCESS] (state) {
    state.addingToFavorites = false
    state.addToFavoritesError = false
    state.addToFavoritesSuccess = true
  },
  [ADD_TO_FAVORITES_FAILURE] (state) {
    state.addingToFavorites = false
    state.addToFavoritesError = true
    state.addToFavoritesSuccess = false
  },
  [ADD_TO_FAVORITES_SET_MESSAGES] (state, messages) {
    state.addToFavoritesMessages = messages
  },
  [ADD_TO_FAVORITES_SET_STATUS_CODE] (state, statusCode) {
    state.addToFavoritesStatusCode = statusCode
  },
  /**
   * Remove product from favorites flow
   */
  [REMOVE_FROM_FAVORITES_BEGIN] (state) {
    state.removingFromFavorites = true
    state.removeFromFavoritesError = false
    state.removeFromFavoritesSuccess = false
  },
  [REMOVE_FROM_FAVORITES_SUCCESS] (state) {
    state.removingFromFavorites = false
    state.removeFromFavoritesError = false
    state.removeFromFavoritesSuccess = true
  },
  [REMOVE_FROM_FAVORITES_FAILURE] (state) {
    state.removingFromFavorites = false
    state.removeFromFavoritesError = true
    state.removeFromFavoritesSuccess = false
  },
  [REMOVE_FROM_FAVORITES_SET_MESSAGES] (state, messages) {
    state.removeFromFavoritesMessages = messages
  },
  [REMOVE_FROM_FAVORITES_SET_STATUS_CODE] (state, statusCode) {
    state.removeFromFavoritesStatusCode = statusCode
  },
  /**
   * Schemating product flow
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
