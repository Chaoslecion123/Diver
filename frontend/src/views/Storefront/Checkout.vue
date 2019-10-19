<template>
  <v-content app :class="['d-page__content', 'd-checkout']">
    <v-container
      grid-list-xl
      :fluid="$vuetify.breakpoint.mdAndDown"
      :class="['mt-3', 'mb-5', 'd-checkout__content']">
      <v-layout row wrap>
        <v-flex
          v-if="this.$route.meta && this.$route.meta.breadcrumbs"
          xs12
          mb-4
          pb-0>
          <v-breadcrumbs :items="this.$route.meta.breadcrumbs" class="pa-0">
            <template v-slot:item="props">
              <li>
                <router-link
                  :to="props.item.href"
                  :class="[
                    'v-breadcrumbs__item',
                    {
                      'v-breadcrumbs__item--disabled': props.item.disabled
                    }
                  ]">
                  {{ props.item.text }}
                </router-link>
              </li>
            </template>
          </v-breadcrumbs>
        </v-flex>

        <v-flex xs12 pt-0>
          <h2
            :class="[
              {
                'd-inline-block': $vuetify.breakpoint.smAndUp
              }
            ]">
            Mi carrito
          </h2>

          <h2
            :class="[
              'green--text',
              'font-weight-regular',
              {
                'd-inline-block': $vuetify.breakpoint.smAndUp
              }
            ]"
            :style="{
              float: $vuetify.breakpoint.smAndUp ? 'right' : 'none'
            }">
            <small>
              <d-icon
                scale="1.25"
                name="b-safety"
                :style="{ verticalAlign: 'text-bottom' }"/>
              Compra Segura
            </small>
          </h2>
        </v-flex>

        <v-flex xs12 md9 :class="['d-checkout__process']">
          <v-stepper
            v-model="step"
            :alt-labels="$vuetify.breakpoint.smAndDown"
            :class="['checkout-process']">
            <v-stepper-header
              :class="['checkout-process__header', 'mb-4', 'grey', 'lighten-4']">
              <v-stepper-step
                step="1"
                :color="isShippingComplete ? 'success' : 'accent'"
                :class="['pa-3']"
                :complete="isShippingComplete">
                Entrega
              </v-stepper-step>
              <v-divider />
              <v-stepper-step
                step="2"
                :color="isBillingComplete ? 'success' : 'accent'"
                :class="['pa-3']"
                :complete="isBillingComplete">
                Facturación
              </v-stepper-step>
              <v-divider />
              <v-stepper-step step="3" color="accent" :class="['pa-3']">
                Pago
              </v-stepper-step>
            </v-stepper-header>

            <v-stepper-items :class="['checkout-process__items']">
              <!--
                Entrega y envío
              -->
              <v-stepper-content
                step="1"
                :class="['pa-0', 'checkout-process__item']">
                <v-card flat color="grey lighten-4">
                  <template v-if="$vuetify.breakpoint.smAndDown">
                    <v-card-title>
                      <h3 class="mb-0">
                        ENTREGA
                      </h3>
                    </v-card-title>
                    <v-divider />
                  </template>

                  <d-shipping-type-selector
                    v-model="purchaseShippingType"
                    class="checkout-process__shipping-type-selector"
                    @change="updatePurchaseShippingType"/>

                  <template
                    v-if="
                      (isForDoorShipping || isForStoreShipping) &&
                        !updatingPurchaseShippingType
                    ">
                    <v-divider />
                    <d-shipping-address-selector
                      v-if="isForDoorShipping"
                      v-model="purchaseShippingAddress"
                      :addresses="purchaseAddresses"
                      class="checkout-process__address-selector"
                      @change="updatePurchaseShippingAddress"/>

                    <d-shipping-store-address-selector
                      v-if="isForStoreShipping"
                      v-model="purchaseShippingAddress"
                      class="checkout-process__address-selector"
                      @change="updatePurchaseShippingAddress"/>
                  </template>

                  <template
                    v-if="
                      isForDoorShipping &&
                        purchaseShippingAddress !== null &&
                        !updatingPurchaseShippingAddress
                    ">
                    <v-divider />

                    <d-shipping-method-selector
                      v-model="purchaseShippingMethod"
                      class="checkout-process__address-selector"/>
                  </template>
                  <v-divider />
                  <v-card-text
                    :class="[
                      'checkout-process__item-actions',
                      {
                        'checkout-process__item-actions--flex':
                          $vuetify.breakpoint.smAndUp,
                        'justify-end': $vuetify.breakpoint.smAndUp
                      }
                    ]">
                    <v-btn
                      depressed
                      color="accent"
                      :disabled="!isShippingComplete"
                      :block="$vuetify.breakpoint.xs"
                      :class="[
                        'ma-0',
                        'd-btn',
                        'd-btn--rounded',
                        'd-btn--bold',
                        'd-btn--no-transform'
                      ]"
                      @click="step++">
                      Siguiente
                    </v-btn>
                  </v-card-text>
                </v-card>
              </v-stepper-content>

              <!--
                Facturación
              -->
              <v-stepper-content
                step="2"
                :class="['pa-0', 'checkout-process__item']">
                <v-card flat color="grey lighten-4">
                  <template v-if="$vuetify.breakpoint.smAndDown">
                    <v-card-title>
                      <h3 class="mb-0">
                        FACTURACIÓN
                      </h3>
                    </v-card-title>
                    <v-divider />
                  </template>

                  <d-billing-type-selector
                    v-model="purchaseBillingType"
                    class="checkout-process__billing-type-selector"
                    @change="updatePurchaseBillingType"/>
                  <template v-if="isForFacture && !updatingPurchaseBillingType">
                    <v-divider />
                    <v-card-text>
                      <v-card-title class="px-0 pt-0">
                        ¿A qué nombre entidad emitimos tu comprobante de pago?
                      </v-card-title>
                      <label>RUC:</label>
                      <v-text-field
                        ref="taxId"
                        v-model="taxId"
                        browser-autocomplete="off"
                        type="text"
                        flat
                        solo
                        required
                        style="width: 100%; max-width: 360px;"
                        :class="[
                          'd-input',
                          'd-input--rounded',
                          'd-input--bordered',
                          'd-input--transparent'
                        ]"/>
                      <label>Razón social:</label>
                      <v-text-field
                        ref="businessName"
                        v-model="businessName"
                        browser-autocomplete="off"
                        type="text"
                        flat
                        solo
                        required
                        style="width: 100%; max-width: 360px;"
                        :class="[
                          'd-input',
                          'd-input--rounded',
                          'd-input--bordered',
                          'd-input--transparent'
                        ]"/>
                    </v-card-text>
                    <v-divider />
                    <d-billing-address-selector
                      v-model="purchaseBillingAddress"
                      class="checkout-process__address-selector"
                      :addresses="purchaseAddresses"
                      @change="updatePurchaseBillingAddress"/>
                  </template>

                  <v-divider />

                  <v-card-text
                    :class="[
                      'checkout-process__item-actions',
                      {
                        'checkout-process__item-actions--flex':
                          $vuetify.breakpoint.smAndUp
                      }
                    ]">
                    <v-btn
                      outline
                      color="accent"
                      :block="$vuetify.breakpoint.xs"
                      :class="[
                        'mx-0',
                        'mt-0',
                        'd-btn',
                        'd-btn--rounded',
                        'd-btn--bold',
                        'd-btn--no-transform',
                        {
                          'mb-0': $vuetify.breakpoint.smAndUp,
                          'mb-3': $vuetify.breakpoint.xs
                        }
                      ]"
                      @click="step--">
                      Anterior
                    </v-btn>
                    <v-btn
                      depressed
                      color="accent"
                      :disabled="!isBillingComplete"
                      :block="$vuetify.breakpoint.xs"
                      :class="[
                        'ma-0',
                        'd-btn',
                        'd-btn--rounded',
                        'd-btn--bold',
                        'd-btn--no-transform'
                      ]"
                      @click="step++">
                      Siguiente
                    </v-btn>
                  </v-card-text>
                </v-card>
              </v-stepper-content>

              <!--
                Pago
              -->
              <v-stepper-content
                step="3"
                :class="['pa-0', 'checkout-process__item']">
                <v-card flat color="grey lighten-4">
                  <template v-if="$vuetify.breakpoint.smAndDown">
                    <v-card-title>
                      <h3 class="mb-0">
                        PAGO
                      </h3>
                    </v-card-title>
                    <v-divider />
                  </template>
                  <d-billing-method-selector
                    class="checkout-process__address-selector"
                    @change="updatePaymentSettings"/>

                  <v-divider />
                  <v-card-text
                    :class="[
                      'checkout-process__item-actions',
                      {
                        'checkout-process__item-actions--flex':
                          $vuetify.breakpoint.smAndUp
                      }
                    ]">
                    <v-btn
                      outline
                      color="accent"
                      :block="$vuetify.breakpoint.xs"
                      :class="[
                        'mx-0',
                        'mt-0',
                        'd-btn',
                        'd-btn--rounded',
                        'd-btn--bold',
                        'd-btn--no-transform',
                        {
                          'mb-0': $vuetify.breakpoint.smAndUp,
                          'mb-3': $vuetify.breakpoint.xs
                        }
                      ]"
                      @click="step--">
                      Anterior
                    </v-btn>
                    <v-btn
                      depressed
                      color="accent"
                      :block="$vuetify.breakpoint.xs"
                      :class="[
                        'ma-0',
                        'd-btn',
                        'd-btn--bold',
                        'd-btn--no-transform'
                      ]"
                      @click="processPayment">
                      Finalizar
                    </v-btn>
                  </v-card-text>
                </v-card>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-flex>

        <v-flex xs12 md3 :class="['d-checkout__summary']">
          <d-checkout-sumary :ordered="true" :showCodeForm="true" />
        </v-flex>
      </v-layout>
    </v-container>
    <d-account-popup v-model="isAccountPopupOpen" :email="emailForValidation" />
    <d-success-popup v-model="isSuccesssPopupOpen" />
  </v-content>
</template>

<style lang="less">
.checkout-process {
  box-shadow: none;

  .v-input__slot {
    margin: 0;
  }

  // .v-messages {
  //   display: none;
  // }

  .checkout-process__header {
    box-shadow: none;
    // background-color:
    border-radius: 4px;
  }

  .checkout-process__item {
    .v-card {
      border-radius: 4px;
      overflow: hidden;
    }

    .checkout-process__item-actions--flex {
      display: flex;
      flex-direction: row;
      justify-content: space-between;

      &.justify-end {
        justify-content: flex-end !important;
      }
    }
    .checkout-process__shipping-type-selector,
    .checkout-process__billing-type-selector {
      .v-input__slot {
        margin: 0;
      }

      .v-messages {
        display: none;
      }
    }

    .checkout-process__address-selector {
      .v-radio {
        align-items: flex-start;
      }

      .address-selector__item {
        height: 100%;
        background-color: transparent;
        cursor: pointer;
        display: flex;
        flex-direction: column;

        &.active {
          border-color: var(--v-accent-base);

          .address-selector__item-name {
            color: var(--v-accent-base);
          }
        }
      }
    }
  }
}
</style>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

import session from '@/api/_session'
import { BASE } from '@/api/_endpoints'
// import { camelToSnake } from '@/_utils'
import Culqi from '@/_utils/culqi'
// import { paramsSerializer } from '@/api/_utils'
// import axios from 'axios'
// import cuilqiLogo from '@/assets/images/culqi.png'

import { STOREFRONT_ORDER } from '@/router/storefront'

import ShippingTypeSelector from './d-checkout/shipping-type'
import ShippingAddressSelector from './d-checkout/shipping-address'
import ShippingStoreAddressSelector from './d-checkout/shipping-store-address'
import ShippingStoreMethodSelector from './d-checkout/shipping-method'

import BillingTypeSelector from './d-checkout/billing-type'
import BillingAddressSelector from './d-checkout/billing-address'
import BillingStoreMethodSelector from './d-checkout/billing-method'

import AccountPopup from './d-checkout/account-popup'
import SuccessPopup from './d-checkout/success-popup'

import {
  DOOR_SHIPPING,
  STORE_SHIPPING,
  BALLOT,
  FACTURE,
  CARD_PAYMENT,
  CASH_PAYMENT,
  DELIVERY_PAYMENT
} from './d-checkout/constants'

export default {
  name: 'Checkout',
  components: {
    'd-shipping-type-selector': ShippingTypeSelector,
    'd-shipping-address-selector': ShippingAddressSelector,
    'd-shipping-store-address-selector': ShippingStoreAddressSelector,
    'd-shipping-method-selector': ShippingStoreMethodSelector,

    'd-billing-type-selector': BillingTypeSelector,
    'd-billing-address-selector': BillingAddressSelector,
    'd-billing-method-selector': BillingStoreMethodSelector,

    'd-account-popup': AccountPopup,
    'd-success-popup': SuccessPopup
  },
  data () {
    return {
      /**
       * Globals
       */
      // assets: {
      //   culqiLogo: cuilqiLogo
      // },
      isValidForm: false,
      cartQuery: {
        expand: ['lines.variant.image', 'shipping_method'].join(','),
        fields: [
          'token',
          'user',
          'created',
          'lines',
          'email',
          'quantity',
          'shipping_address',
          'shipping_method',
          'shipping_type',

          'billing_address',
          'billing_type',

          'discount_amount',
          'discount_name',
          'voucher_code',

          'applicable_shipping_methods'
        ].join(',')
      },
      /**
       * Global details
       */
      step: 0,
      purchaseAddresses: [],
      taxId: '',
      businessName: '',
      isAccountPopupOpen: false,
      isSuccesssPopupOpen: false,

      /* Step 1 */
      purchaseShippingType: null,
      updatingPurchaseShippingType: null,

      purchaseShippingAddress: null,
      updatingPurchaseShippingAddress: null,

      purchaseShippingMethod: null,
      updatingpurchaseShippingMethod: null,

      /* Step 2 */
      purchaseBillingType: null,
      updatingPurchaseBillingType: null,

      purchaseBillingAddress: null,
      updatingPurchaseBillingAddress: null,

      /* Step 3 */
      purchasePaymentMethod: null,
      purchasePaymentForm: null,
      purchasePaymentFormIsValid: null,
      purchasePersonalForm: null,
      purchasePersonalFormIsValid: null
    }
  },
  computed: {
    /**
     * Autenticated User
     */
    ...mapState('auth', {
      user: 'currentUser'
    }),

    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    /**
     * User verification
     */
    ...mapState('user', {
      verifyUser: 'verify'
    }),

    /**
     * User addresses
     */
    ...mapState('address', {
      address: 'object',
      addresses: 'objects',
      addressListSuccess: 'listSuccess',
      addressCreateSuccess: 'createSuccess',
      addressUpdateSuccess: 'updateSuccess',
      addressDeleteSuccess: 'deleteSuccess'
    }),

    /**
     * Cart
     */
    ...mapState('cart', {
      cart: 'object',
      cartToken: 'token',
      orderToken: 'orderToken',
      cartUpdating: 'updating',
      cartReadSuccess: 'readSuccess',
      cartUpdateSuccess: 'updateSuccess',
      placeOrderSuccess: 'placeOrderSuccess',
      discountSuccess: 'discountSuccess'
    }),

    ...mapGetters('cart', {
      totalAmount: 'totalAmount'
    }),

    ...mapState('order', {
      order: 'object'
    }),

    /**
     * Physical stores
     */
    ...mapState('physical-store', {
      physicalStores: 'objects',
      physicalStoresListSuccess: 'listSuccess'
    }),

    /**
     * Shipping Methods
     */
    ...mapState('shipping-method', {
      purchaseShippingMethodOptions: 'objects'
    }),

    /**
     * Global
     */
    emailForValidation () {
      if (this.purchasePersonalForm) {
        return this.purchasePersonalForm.email
      }
      return null
    },
    /**
     * Step 1
     */
    isForDoorShipping () {
      return this.purchaseShippingType === DOOR_SHIPPING
    },

    isForStoreShipping () {
      return this.purchaseShippingType === STORE_SHIPPING
    },

    isForBallot () {
      return this.purchaseBillingType === BALLOT
    },

    isForFacture () {
      return this.purchaseBillingType === FACTURE
    },

    isShippingComplete () {
      if (this.isForStoreShipping) {
        return this.purchaseShippingAddress !== null
      }
      if (this.isForDoorShipping) {
        return (
          this.purchaseShippingAddress !== null &&
          this.purchaseShippingMethod !== null
        )
      }
      return false
    },

    isBillingComplete () {
      if (this.isForFacture) {
        return (
          this.purchaseBillingAddress !== null &&
          this.taxId !== '' &&
          this.businessName !== ''
        )
      }

      return this.isForBallot
    }
  },
  watch: {
    isAccountPopupOpen (val, oldVal) {
      if (!val) {
        this.makePayment()
      }
    },
    cartUpdating (val, oldVal) {
      if (!val) {
        this.updatingPurchaseShippingType = false
        this.updatingPurchaseShippingAddress = false
        this.updatingpurchaseShippingMethod = false
        this.updatingPurchaseBillingType = false
      }
    },

    discountSuccess (val, oldval) {
      if (val) {
        this.refreshCart()
      }
    },
    cartUpdateSuccess (val, oldVal) {
      if (val) {
        this.refreshCart()
      }
    },
    addressListSuccess (val, oldVal) {
      if (val) {
        if (this.addresses && this.addresses.items) {
          this.purchaseAddresses = [...this.addresses.items]
        }
      }
    },
    addressCreateSuccess (val, oldVal) {
      if (val) {
        this.purchaseAddresses.push(this.address)

        if (this.step === '1') {
          this.purchaseShippingAddress = this.address.id
          if (this.isForDoorShipping) {
            this.purchaseBillingAddress = this.address.id
          }
        } else if (this.step === '2') {
          this.purchaseBillingAddress = this.address.id
        }
      }
    },
    addressUpdateSuccess (val, oldVal) {
      if (val) {
        let index = this.purchaseAddresses.findIndex(item => {
          return item.id === this.address.id
        })

        if (index >= 0) {
          let addresses = [...this.purchaseAddresses]
          addresses[index] = { ...this.address }
          this.purchaseAddresses = [...addresses]
        } else {
          this.purchaseAddresses.push(this.address)
        }

        if (this.step === '1') {
          this.purchaseShippingAddress = this.address.id
          if (this.isForDoorShipping) {
            this.purchaseBillingAddress = this.address.id
          }
        } else if (this.step === '2') {
          this.purchaseBillingAddress = this.address.id
        }
      }
    },
    addressDeleteSuccess (val, oldVal) {
      if (val) {
        let index = this.purchaseAddresses.findIndex(
          item => item.id === this.address.id
        )

        if (index) {
          this.purchaseAddresses.splice(index, 1)
        }

        if (this.purchaseShippingAddress === this.address.id) {
          this.purchaseShippingAddress = null
        }

        if (this.purchaseBillingAddress === this.address.id) {
          this.purchaseShippingAddress = null
        }
      }
    },
    purchaseShippingType (val, oldVal) {
      this.purchaseShippingAddress = null
      this.purchaseShippingMethod = null
    },
    purchaseShippingAddress (val, oldVal) {
      this.purchaseShippingMethod = null
    },

    placeOrderSuccess (val, oldVal) {
      if (val) {
        if (this.purchasePaymentMethod === DELIVERY_PAYMENT) {
          this.makeDeliveryPayment()
        } else if (this.purchasePaymentMethod === CASH_PAYMENT) {
          this.makeCashPayment()
        } else if (this.purchasePaymentMethod === CARD_PAYMENT) {
          this.makeCardPayment()
        }
      }
    }
  },
  methods: {
    /**
     * Cart operations
     */
    ...mapActions('cart', {
      cartRead: 'read',
      cartUpdate: 'update',
      placeCartOrder: 'placeOrder'
    }),

    /**
     * User addresses
     */
    ...mapActions('address', {
      getAddresses: 'list'
    }),

    /**
     * Physical stores
     */
    ...mapActions('physical-store', {
      getPhysicalStores: 'list'
    }),

    /**
     * Global
     */
    refreshCart () {
      if (this.cartToken) {
        this.cartRead({
          id: this.cartToken,
          query: this.cartQuery
        })
      }
    },

    /**
     * Step 1
     */
    updatePurchaseShippingType () {
      this.updatingPurchaseShippingType = true
      this.purchaseShippingAddress = null
    },

    updatePurchaseShippingAddress () {
      this.updatingPurchaseShippingAddress = true
    },

    updatePurchaseBillingType () {
      this.updatingPurchaseBillingType = true
      this.purchaseBillingAddress = null
    },

    updatePurchaseBillingAddress () {
      this.updatingPurchaseBillingAddress = true
    },
    /**
     * Step 2
     */
    updatePaymentSettings (value) {
      this.purchasePaymentMethod = value.paymentMethod

      this.purchasePaymentFormIsValid = value.paymentFormIsValid
      this.purchasePaymentForm = value.paymentFormIsValid
        ? { ...value.paymentForm }
        : null

      this.purchasePersonalFormIsValid = value.personalFormIsValid
      this.purchasePersonalForm = value.personalFormIsValid
        ? { ...value.personalForm }
        : null
    },

    /**
     * Step 3
     */
    placeOrderForCardPayment () {
      if (this.purchasePersonalFormIsValid && this.purchasePaymentFormIsValid) {
        this.placeCartOrder({
          id: this.cartToken,
          data: this.purchasePersonalForm
        })
      }
    },

    makeCardPayment () {
      this.culqi.settings({
        title: 'Quimder Store',
        currency: 'PEN',
        description: 'Compras en Quimder',
        amount: this.totalAmount.toFixed(2) * 100
      })

      this.culqi.createToken().then(token => {
        console.log('resultado ' + token)
      })
    },

    placeOrderForCashPayment () {
      if (this.purchasePersonalFormIsValid) {
        this.placeCartOrder({
          id: this.cartToken,
          data: this.purchasePersonalForm
        })
      }
    },
    makeCashPayment () {
      // this.redirectToOrderDetail()
      this.isSuccesssPopupOpen = true
    },

    placeOrderForDeliveryPayment () {
      if (this.purchasePersonalFormIsValid) {
        this.placeCartOrder({
          id: this.cartToken,
          data: this.purchasePersonalForm
        })
      }
    },

    makeDeliveryPayment () {
      // this.redirectToOrderDetail()
      this.isSuccesssPopupOpen = true
    },

    redirectToOrderDetail () {
      this.$router.push({
        name: STOREFRONT_ORDER,
        params: {
          // id: this.order.token
          id: this.orderToken
        },
        props: {
          thanks: true
        }
      })
    },

    makePayment () {
      if (this.purchasePaymentMethod === DELIVERY_PAYMENT) {
        this.placeOrderForDeliveryPayment()
      } else if (this.purchasePaymentMethod === CASH_PAYMENT) {
        this.placeOrderForCashPayment()
      } else if (this.purchasePaymentMethod === CARD_PAYMENT) {
        this.placeOrderForCardPayment()
      }
    },

    processPayment () {
      if (this.isAuthenticated) {
        this.makePayment()
      } else {
        this.isAccountPopupOpen = true
      }
    }
  },
  created () {
    /**
     * Handle cart operations
     */
    this.refreshCart()

    this.getAddresses()

    this.getPhysicalStores({
      query: {
        expand: 'address'
      }
    })

    /**
     * Handle checkout process
     */
    window.culqi = () => {
      if (window.Culqi.token) {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')
          .value

        const data = {
          csrfmiddlewaretoken: csrfToken,
          culqi_payment_id: window.Culqi.token.id,
          order: this.order.token
          // extra: JSON.stringify(this.order)
        }

        const serializedData = Object.keys(data)
          .map(key => {
            return encodeURIComponent(key) + '=' + encodeURIComponent(data[key])
          })
          .join('&')

        session
          .post(BASE + 'culqi/checkout/', serializedData)
          .then((response) => {
            console.log(response)
            this.isSuccesssPopupOpen = true
          })
      }
    }

    this.culqi = new Culqi('pk_live_CiOu87Autl9zZphs')
  }
}
</script>
