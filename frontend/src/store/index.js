/* global process */
/**
 * Vue libraries
 */
import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger'

/**
 * Custom State Modules
 */
// Authentication process
import auth from './auth'
import culqi from './culqi'

import city from './city'
import cityArea from './city-area'
import countryArea from './country-area'
import address from './address'
import association from './association'
import authorizationKey from './authorization-key'
import cart from './cart'
import cartLine from './cart-line'
import category from './category'
import code from './code'
import collection from './collection'
import contentType from './content-type'
import conversionRate from './conversion-rate'
import customerNote from './customer-note'
import customerReview from './customer-review'
import brand from './brand'
import fulfillment from './fulfillment'
import fulfillmentLine from './fulfillment-line'
import group from './group'
import impersonationLog from './impersonation-log'
import logEntry from './log-entry'
import menu from './menu'
import menuItem from './menu-item'
import nonce from './nonce'
import order from './order'
import orderEvent from './order-event'
import orderLine from './order-line'
import page from './page'
import partial from './partial'
import payment from './payment'
import permission from './permission'
import product from './product'
import rateTypes from './rate-types'
import sale from './sale'
import scene from './scene'
import session from './session'
import shippingMethod from './shipping-method'
import shippingZone from './shipping-zone'
import site from './site'
import siteSettings from './site-settings'
import taskResult from './task-result'
import token from './token'
import transaction from './transaction'
import user from './user'
import userSocialAuth from './user-social-auth'
import vat from './vat'
import variantImage from './variant-image'
import voucher from './voucher'
import physicalStore from './physical-store'

import banner from './banner'
import slider from './slider'

const debug = process.env.NODE_ENV !== 'production'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    /* Auth process */
    auth,
    culqi,

    /* Common objects */
    banner,
    slider,
    scene,

    brand: brand,
    'log-entry': logEntry,

    city: city,
    'city-area': cityArea,
    'country-area': countryArea,

    address,
    association,
    'authorization-key': authorizationKey,
    cart,
    'cart-line': cartLine,
    category,
    code,
    collection,
    'content-type': contentType,
    'conversion-rate': conversionRate,
    'customer-note': customerNote,
    'customer-review': customerReview,
    fulfillment,
    'fulfillment-line': fulfillmentLine,
    group,
    'impersonation-log': impersonationLog,
    menu,
    'menu-item': menuItem,
    nonce,
    order,
    'order-event': orderEvent,
    'order-line': orderLine,
    page,
    partial,
    payment,
    permission,
    product,
    'rate-types': rateTypes,
    sale,
    session,
    'shipping-method': shippingMethod,
    'shipping-zone': shippingZone,
    site,
    'site-settings': siteSettings,
    'task-result': taskResult,
    token,
    transaction,
    user,
    'user-social-auth': userSocialAuth,
    vat,
    'variant-image': variantImage,
    voucher,
    'physical-store': physicalStore
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
