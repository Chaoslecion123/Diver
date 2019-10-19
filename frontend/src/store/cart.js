import CART from '@/api/cart'

import {
  /* Creating cart flow */
  CREATE_BEGIN,
  CREATE_SUCCESS,
  CREATE_FAILURE,
  CREATE_SET_MESSAGES,
  CREATE_SET_STATUS_CODE,

  /* Reading cart flow */
  READ_BEGIN,
  READ_SUCCESS,
  READ_FAILURE,
  READ_SET_MESSAGES,
  READ_SET_STATUS_CODE,

  /* Updating cart flow */
  UPDATE_BEGIN,
  UPDATE_SUCCESS,
  UPDATE_FAILURE,
  UPDATE_SET_MESSAGES,
  UPDATE_SET_STATUS_CODE,

  /* Deleting cart flow */
  DELETE_BEGIN,
  DELETE_SUCCESS,
  DELETE_FAILURE,
  DELETE_SET_MESSAGES,
  DELETE_SET_STATUS_CODE,

  /* Listing cart flow */
  LIST_BEGIN,
  LIST_SUCCESS,
  LIST_FAILURE,
  LIST_SET_MESSAGES,
  LIST_SET_STATUS_CODE,

  /* Schemating cart flow */
  SCHEMA_BEGIN,
  SCHEMA_SUCCESS,
  SCHEMA_FAILURE,
  SCHEMA_SET_MESSAGES,
  SCHEMA_SET_STATUS_CODE,

  /* Handle objects */
  SET_SCHEMA,
  SET_OBJECT,
  REMOVE_OBJECT,
  SET_OBJECT_LIST,
  REMOVE_OBJECT_LIST
} from './_processes'

const CLEAR_BEGIN = 'CLEAR_BEGIN'
const CLEAR_SUCCESS = 'CLEAR_SUCCESS'
const CLEAR_FAILURE = 'CLEAR_FAILURE'
const CLEAR_SET_MESSAGES = 'CLEAR_SET_MESSAGES'
const CLEAR_SET_STATUS_CODE = 'CLEAR_SET_STATUS_CODE'

const PLACE_ORDER_BEGIN = 'PLACE_ORDER_BEGIN'
const PLACE_ORDER_SUCCESS = 'PLACE_ORDER_SUCCESS'
const PLACE_ORDER_FAILURE = 'PLACE_ORDER_FAILURE'
const PLACE_ORDER_SET_MESSAGES = 'PLACE_ORDER_SET_MESSAGES'
const PLACE_ORDER_SET_STATUS_CODE = 'PLACE_ORDER_SET_STATUS_CODE'

const DISCOUNT_BEGIN = 'DISCOUNT_BEGIN'
const DISCOUNT_SUCCESS = 'DISCOUNT_SUCCESS'
const DISCOUNT_FAILURE = 'DISCOUNT_FAILURE'
const DISCOUNT_SET_MESSAGES = 'DISCOUNT_SET_MESSAGES'
const DISCOUNT_SET_STATUS_CODE = 'DISCOUNT_SET_STATUS_CODE'

const ADD_TO_CART = 'ADD_TO_CART'
const REMOVE_FROM_CART = 'REMOVE_FROM_CART'
const SET_TOKEN = 'SET_TOKEN'
const SET_ORDER_TOKEN = 'SET_ORDER_TOKEN'
const REMOVE_TOKEN = 'REMOVE_TOKEN'
const TOKEN_STORAGE_KEY = 'CartToken'
const NULL_TOKEN = null

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
  schemaStatusCode: null,

  /* Schema state variables */
  placingOrder: false,
  placeOrderError: false,
  placeOrderSuccess: false,
  placeOrderMessages: null,
  placeOrderStatusCode: null,

  /* List state variables */
  discounting: false,
  discountError: false,
  discountSuccess: false,
  discountMessages: null,
  discountStatusCode: null,

  /* Create state variables */
  clearing: false,
  clearError: false,
  clearSuccess: false,
  clearMessages: null,
  clearStatusCode: null,

  /* Other processes */
  token: NULL_TOKEN,
  orderToken: NULL_TOKEN,

  /**
   * Dummy Cart
   *
   * items must be in the form of
   *
   *  item: {
   *    product: { ... },
   *    variant: { ... },
   *    quantity: integer
   *  }
   *
   */
  cart: {
    data: {},
    items: []
  }
}

const getters = {
  isCartAvailable: state => {
    return (
      state.object !== null &&
      state.object.quantity !== 0 &&
      state.object.token !== NULL_TOKEN &&
      state.object.token === state.token
    )
  },
  subtotalAmount: state => {
    return state.object && state.object.lines
      ? state.object.lines.reduce((amount, line) => {
        if (line.variant && line.variant.priceDisplay) {
          if (line.variant.priceDisplay.displayGross) {
            return amount + line.quantity * line.variant.price.gross.amount
          }

          return amount + line.quantity * line.variant.price.net.amount
        }

        return 0
      }, 0)
      : 0
  },
  totalAmount: state => {
    let subtotal =
      state.object && state.object.lines
        ? state.object.lines.reduce((amount, line) => {
          if (line.variant && line.variant.priceDisplay) {
            if (line.variant.priceDisplay.displayGross) {
              return amount + line.quantity * line.variant.price.gross.amount
            }

            return amount + line.quantity * line.variant.price.net.amount
          }

          return 0
        }, 0)
        : 0

    let shipping =
      state.object &&
      state.object.shippingMethod &&
      state.object.shippingMethod.price
        ? state.object.shippingMethod.price
          ? state.object.shippingMethod.price.amount
          : 0
        : 0

    let discount =
      state.object && state.object.discountAmount
        ? state.object.discountAmount.amount
        : 0

    return subtotal + shipping - discount
  }
}

const actions = {
  /**
   * Initialize the authentication process.
   */
  initialize ({ commit, dispatch }) {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY)

    if (token) {
      commit(SET_TOKEN, token)
      return dispatch('read', {
        id: token,
        query: {
          expand: ['lines.variant.image', 'lines.variant.product'].join(','),
          fields: ['token', 'quantity', 'lines'].join(',')
        }
      })
    } else {
      commit(REMOVE_TOKEN)
      commit(REMOVE_OBJECT)
    }
  },

  addToCart ({ commit }, { item } = {}) {
    commit(ADD_TO_CART, item)
  },

  removeFromCart ({ commit }, { item } = {}) {
    commit(REMOVE_FROM_CART, item)
  },

  create ({ commit }, { data, config = {} } = {}) {
    commit(CREATE_BEGIN)
    commit(CREATE_SET_MESSAGES, null)
    commit(CREATE_SET_STATUS_CODE, null)
    return CART.create(data, config)
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
    return CART.retrieve(id, query, config)
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
        commit(REMOVE_TOKEN)
        commit(REMOVE_OBJECT)
      })
  },

  update ({ commit }, { id, data, config = {} } = {}) {
    commit(UPDATE_BEGIN)
    commit(UPDATE_SET_MESSAGES, null)
    commit(UPDATE_SET_STATUS_CODE, null)
    return CART.update(id, data, config)
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
    return CART.delete(id, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(DELETE_SUCCESS)
        commit(REMOVE_OBJECT)
        commit(REMOVE_TOKEN)
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
    return CART.list(query, config)
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

  schema ({ commit }, { config = {} } = {}) {
    commit(SCHEMA_BEGIN)
    commit(SCHEMA_SET_MESSAGES, null)
    commit(SCHEMA_SET_STATUS_CODE, null)
    return CART.options(config)
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
  },

  placeOrder ({ commit, dispatch }, { id, data = {}, config = {} } = {}) {
    commit(PLACE_ORDER_BEGIN)
    commit(PLACE_ORDER_SET_MESSAGES, null)
    commit(PLACE_ORDER_SET_STATUS_CODE, null)
    return CART.placeOrder(id, data, config)
      .then(response => {
        if (response.data && response.data.orderToken) {
          commit(SET_ORDER_TOKEN, response.data.orderToken)
          dispatch(
            'order/read',
            { id: response.data.orderToken },
            { root: true }
          )
        }
        // commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(PLACE_ORDER_SUCCESS)
        commit(REMOVE_OBJECT)
        commit(REMOVE_TOKEN)
      })
      .catch(error => {
        commit(PLACE_ORDER_FAILURE)
        commit(DELETE_SET_MESSAGES, error.response.data)
        commit(DELETE_SET_STATUS_CODE, error.response.status)
      })
  },

  applyDiscount ({ commit }, { id, data, query = {}, config = {} } = {}) {
    commit(DISCOUNT_BEGIN)
    commit(DISCOUNT_SET_MESSAGES, null)
    commit(DISCOUNT_SET_STATUS_CODE, null)
    return CART.applyDiscount(id, data, query, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(DISCOUNT_SUCCESS)
      })
      .catch(error => {
        commit(DISCOUNT_FAILURE)
        commit(DISCOUNT_SET_MESSAGES, error.response.data)
        commit(DISCOUNT_SET_STATUS_CODE, error.response.status)
      })
  },

  clear ({ commit }, { id, query = {}, config = {} } = {}) {
    commit(CLEAR_BEGIN)
    commit(CLEAR_SET_MESSAGES, null)
    commit(CLEAR_SET_STATUS_CODE, null)
    return CART.clear(id, query, config)
      .then(response => {
        commit(SET_OBJECT, response.data)
      })
      .then(() => {
        commit(CLEAR_SUCCESS)
      })
      .catch(error => {
        commit(CLEAR_FAILURE)
        commit(CLEAR_SET_MESSAGES, error.response.data)
        commit(CLEAR_SET_STATUS_CODE, error.response.status)
        commit(REMOVE_TOKEN)
        commit(REMOVE_OBJECT)
      })
  }
}

const mutations = {
  /**
   * Creating cart flow
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
   * Reading cart flow
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
   * Updating cart flow
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
   * Deleting cart flow
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
   * Listing cart flow
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
   * Schemating cart flow
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
  [REMOVE_OBJECT] (state) {
    state.object = null
  },
  [SET_OBJECT_LIST] (state, objects) {
    state.objects = objects
  },
  [REMOVE_OBJECT_LIST] (state) {
    state.objects = []
  },

  /**
   * Sets the session token and save it to the localStorage
   *
   * @param {object} state - State
   * @param {string} token - Session token
   */
  [SET_TOKEN] (state, token) {
    localStorage.setItem(TOKEN_STORAGE_KEY, token)
    state.token = token
  },

  /**
   * Sets the session token and save it to the localStorage
   *
   * @param {object} state - State
   * @param {string} token - Session token
   */
  [SET_ORDER_TOKEN] (state, token) {
    state.orderToken = token
  },

  /**
   * Remove the session token
   *
   * @param {object} state - State
   */
  [REMOVE_TOKEN] (state) {
    localStorage.removeItem(TOKEN_STORAGE_KEY)
    state.token = NULL_TOKEN
  },

  /**
   *
   * @param {*} state
   * @param {*} newItem
   */
  [ADD_TO_CART] (state, newItem) {
    const index = state.cart.items.findIndex(
      item =>
        item.product.id === newItem.product.id &&
        item.variant.id === newItem.variant.id
    )

    if (index < 0) {
      state.cart.items.push(newItem)
    } else {
      state.cart.items[index].quantity += newItem.quantity
    }
  },
  [REMOVE_FROM_CART] (state, removedItem) {
    const index = state.cart.items.findIndex(
      item =>
        item.product.id === removedItem.product.id &&
        item.variant.id === removedItem.variant.id
    )

    if (index >= 0) {
      state.cart.items.splice(index, 1)
    }
  },

  /**
   *
   */
  [PLACE_ORDER_BEGIN] (state) {
    state.placingOrder = true
    state.placeOrderError = false
    state.placeOrderSuccess = false
  },
  [PLACE_ORDER_SUCCESS] (state) {
    state.placingOrder = false
    state.placeOrderError = false
    state.placeOrderSuccess = true
  },
  [PLACE_ORDER_FAILURE] (state) {
    state.placingOrder = false
    state.placeOrderError = true
    state.placeOrderSuccess = false
  },
  [PLACE_ORDER_SET_MESSAGES] (state, message) {
    state.placeOrderMessages = message
  },
  [PLACE_ORDER_SET_STATUS_CODE] (state, statusCode) {
    state.placeOrderStatusCode = statusCode
  },
  /**
   * Listing cart flow
   */
  [DISCOUNT_BEGIN] (state) {
    state.discounting = true
    state.discountError = false
    state.discountSuccess = false
  },
  [DISCOUNT_SUCCESS] (state) {
    state.discounting = false
    state.discountError = false
    state.discountSuccess = true
  },
  [DISCOUNT_FAILURE] (state) {
    state.discounting = false
    state.discountError = true
    state.discountSuccess = false
  },
  [DISCOUNT_SET_MESSAGES] (state, messages) {
    state.discountMessages = messages
  },
  [DISCOUNT_SET_STATUS_CODE] (state, statusCode) {
    state.discountStatusCode = statusCode
  },

  /**
   *
   */
  [CLEAR_BEGIN] (state) {
    state.clearing = true
    state.clearError = false
    state.clearSuccess = false
  },
  [CLEAR_SUCCESS] (state) {
    state.clearing = false
    state.clearError = false
    state.clearSuccess = true
  },
  [CLEAR_FAILURE] (state) {
    state.clearing = false
    state.clearError = true
    state.clearSuccess = false
  },
  [CLEAR_SET_MESSAGES] (state, message) {
    state.clearMessages = message
  },
  [CLEAR_SET_STATUS_CODE] (state, statusCode) {
    state.clearStatusCode = statusCode
  }
}

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations
}
