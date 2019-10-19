<template>
  <v-card-text>
    <v-card-title class="px-0 pt-0">
      ¿Cómo quieres pagar tu compra?
    </v-card-title>

    <div class="text-xs-center mb-4">
      <template v-for="paymentMethod in purchasePaymentMethodOptions">
        <v-btn
          v-if="paymentMethod.available"
          :key="paymentMethod.value"
          outline
          depressed
          size="large"
          :block="$vuetify.breakpoint.xs"
          :color="purchasePaymentMethod === paymentMethod.value ? 'accent' : ''"
          :class="[
            'ma-0',
            {
              'mb-2': $vuetify.breakpoint.xs,
              'mr-2': $vuetify.breakpoint.smAndUp
            },
            'd-btn',
            'd-btn--rounded',
            'd-btn--bold',
            'd-btn--no-transform'
          ]"
          @click="handleChange(paymentMethod.value)">{{ paymentMethod.name }}</v-btn>
      </template>
    </div>
    <div>
      <v-window v-model="purchasePaymentMethod">
        <v-window-item :value="paymentType.card">
          <div class="text-xs-center">
            <p>
              Los pagos por tarjeta son procesados por
              <a class="accent--text" href="https://culqi.com/" target="_brank">Culqi</a>.
            </p>
            <p class="mb-4">
              <a class="accent--text" href="https://culqi.com/" target="_brank">
                <img
                  :src="assets.culqiLogo"
                  alt="Culqi"
                  style="height: 25px;"/>
              </a>
            </p>
            <v-form
              ref="paymentForm"
              v-model="isValidPaymentForm"
              lazy-validation
              class="d-form my-3 mx-auto">
              <v-container pa-0 grid-list-xs>
                <v-layout row wrap>
                  <v-flex xs12 pb-0>
                    <v-text-field
                      ref="card_number"
                      v-model="paymentForm.card_number"
                      data-culqi="card[number]"
                      browser-autocomplete="off"
                      prepend-inner-icon="payment"
                      placeholder="Tarjeta de crédito o débito"
                      type="text"
                      flat
                      solo
                      required
                      :rules="creditCardRules"
                      :class="[
                        'd-input',
                        'd-input--rounded',
                        'd-input--bordered'
                      ]"
                      :style="(cardProvider && cardProvider.logo)?{
                        width: 'calc(100% - 72px)',
                        display: 'inline-block'
                      }:''"
                      @input="handleChange"/>

                    <div v-if="cardProvider.logo" style="margin-left: 8px; width: 64px; height:48px; line-height: 48px; display: inline-block; text-align: center; float: right;">
                      <img
                        style="width: auto; height: 100%;"
                        :src="cardProvider.logo"
                        :alt="cardProvider.label"/>
                    </div>
                  </v-flex>

                  <v-flex xs4 pb-0>
                    <v-text-field
                      ref="expiration_month"
                      v-model="paymentForm.expiration_month"
                      data-culqi="card[exp_month]"
                      browser-autocomplete="off"
                      prepend-inner-icon="calendar_today"
                      placeholder="Mes"
                      type="text"
                      flat
                      solo
                      required
                      mask="##"
                      :rules="[v => !!v || 'Campo requerido']"
                      :class="[
                        'd-input',
                        'd-input--rounded',
                        'd-input--bordered'
                      ]"
                      @input="handleChange"/>
                  </v-flex>

                  <v-flex xs4 pb-0>
                    <v-text-field
                      ref="expiration_year"
                      v-model="paymentForm.expiration_year"
                      data-culqi="card[exp_year]"
                      browser-autocomplete="off"
                      prepend-inner-icon="calendar_today"
                      placeholder="Año"
                      type="text"
                      flat
                      solo
                      required
                      mask="####"
                      :rules="[v => !!v || 'Campo requerido']"
                      :class="[
                        'd-input',
                        'd-input--rounded',
                        'd-input--bordered'
                      ]"
                      @input="handleChange"/>
                  </v-flex>

                  <v-flex xs4 pb-0>
                    <v-text-field
                      ref="cvv"
                      v-model="paymentForm.cvv"
                      data-culqi="card[cvv]"
                      browser-autocomplete="off"
                      prepend-inner-icon="lock"
                      placeholder="CVV"
                      type="text"
                      flat
                      solo
                      required
                      mask="###"
                      :rules="[v => !!v || 'Campo requerido']"
                      :class="[
                        'd-input',
                        'd-input--rounded',
                        'd-input--bordered'
                      ]"
                      @input="handleChange"/>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-form>
          </div>
        </v-window-item>

        <v-window-item
          v-if="paymentSettings && paymentSettings.cashPayment.enabled"
          :value="paymentType.cash">
          <div class="d-cash-payment" style="max-width: 400px; margin: 0 auto;">
            <p>
              <strong>
                Código de Pedido
                <br />20012019-01
              </strong>
            </p>
            <p>
              Acercate a cualquier agencia bancaria o agente y realiza tu
              deposito a cualquiera de nuestras cuentas.
            </p>
            <v-data-table
              :headers="[
                {
                  text: 'Banco',
                  align: 'left',
                  value: 'provider',
                  sortable: false
                },
                {
                  text: 'Número de cuenta',
                  value: 'number',
                  sortable: false,
                  align: 'center'
                }
              ]"
              :items="paymentSettings.cashPayment.bankAccounts"
              hide-actions>
              <template slot="items" slot-scope="{ item }">
                <td class="text-xs-left">{{ item.provider }}</td>
                <td>{{ item.number }}</td>
              </template>
            </v-data-table>
          </div>
        </v-window-item>

        <v-window-item
          v-if="paymentSettings && paymentSettings.deliveryPayment.enabled"
          :value="paymentType.delivery">
          <div class="text-xs-center" style="max-width: 400px; margin: 0 auto;">
            <p><strong>1.</strong> Completa tus datos.</p>
            <p><strong>2.</strong> Acercate al local que elegiste.</p>
            <p>
              <strong>3.</strong> Paga en caja indicando el código de pedido que
              te enviaremos a tu correo electronico.
            </p>
            <p><strong>4.</strong> ¡Listo, el producto es tuyo!</p>
          </div>
        </v-window-item>
      </v-window>

      <v-form
        ref="personalForm"
        v-model="isValidPersonalForm"
        lazy-validation
        class="d-form mt-4 mb-2 mx-auto">
        <v-container pa-0 grid-list-xs>
          <v-layout row wrap>
            <v-flex xs12 py-0>
              <v-text-field
                ref="name"
                v-model="personalForm.firstName"
                browser-autocomplete="off"
                prepend-inner-icon="account_circle"
                placeholder="Nombres"
                type="text"
                flat
                solo
                required
                :rules="[v => !!v || 'Campo requerido']"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                @input="handleChange"/>
            </v-flex>

            <v-flex xs12 pb-0>
              <v-text-field
                ref="name"
                v-model="personalForm.lastName"
                browser-autocomplete="off"
                prepend-inner-icon="account_circle"
                placeholder="Apellido"
                type="text"
                flat
                solo
                required
                :rules="[v => !!v || 'Campo requerido']"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                @input="handleChange"/>
            </v-flex>

            <v-flex xs12 pb-0>
              <v-text-field
                ref="email"
                v-model="personalForm.email"
                data-culqi="card[email]"
                browser-autocomplete="off"
                prepend-inner-icon="mail"
                placeholder="Correo electrónico"
                type="email"
                flat
                solo
                required
                :rules="[v => !!v || 'Campo requerido']"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                @input="handleChange"/>
            </v-flex>

            <v-flex xs12 pb-0>
              <v-checkbox
                v-model="personalForm.suscribedToNewsletter"
                required
                class="mt-2">
                <div slot="label">
                  Me gustaría recibir comunicaciones promocionales.
                </div>
              </v-checkbox>
            </v-flex>

            <v-flex xs12 pb-0>
              <v-checkbox
                v-model="personalForm.termsAndConditions"
                required
                class="mt-2">
                <div slot="label">
                  Acepto términos y condiciones de la politíca de privacidad y
                  tratamiento de datos personales.
                </div>
              </v-checkbox>
            </v-flex>
          </v-layout>
        </v-container>
      </v-form>
    </div>
  </v-card-text>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import {
  CARD_PAYMENT,
  CASH_PAYMENT,
  DELIVERY_PAYMENT,
  STORE_SHIPPING
} from './constants'

import culqiLogo from '@/assets/images/culqi.png'
import visasLogo from '@/assets/images/visa.svg'
import discoversLogo from '@/assets/images/discover.svg'
import americansExpressLogo from '@/assets/images/american-express.svg'
import mastersCardLogo from '@/assets/images/mastercard.svg'

export default {
  name: 'd-shipping-type-selector',
  model: {
    prop: 'shippingMethod',
    event: 'change'
  },
  data () {
    return {
      assets: {
        culqiLogo: culqiLogo,
        americanExpressLogo: americansExpressLogo,
        visaLogo: visasLogo,
        masterCardLogo: mastersCardLogo,
        discoverLogo: discoversLogo
      },
      isValidPaymentForm: false,
      paymentForm: {
        card_number: '',
        cvv: '',
        expiration_month: '',
        expiration_year: ''
      },
      isValidPersonalForm: false,
      personalForm: {
        firstName: '',
        lastName: '',
        email: '',
        suscribedToNewsletter: false,
        termsAndConditions: false
      },
      paymentType: {
        card: CARD_PAYMENT,
        cash: CASH_PAYMENT,
        delivery: DELIVERY_PAYMENT
      },
      paymentSettings: null,
      purchasePaymentMethod: CARD_PAYMENT,
      purchasePaymentMethodOptions: [
        {
          name: 'Con tarjeta',
          available: true,
          value: CARD_PAYMENT
        },
        {
          name: 'Deposito en cuenta',
          available: true,
          value: CASH_PAYMENT
        },
        {
          name: 'Contra entrega',
          available: true,
          value: DELIVERY_PAYMENT
        }
      ]
    }
  },
  computed: {
    ...mapState('cart', {
      cartToken: 'token'
    }),

    ...mapState('cart', {
      cart: 'object'
    }),

    ...mapState('auth', {
      user: 'currentUser'
    }),

    ...mapGetters('auth', {
      userIsAuthenticated: 'isAuthenticated'
    }),
    cardProvider () {
      /* eslint-disable camelcase */
      let { card_number } = this.paymentForm
      if (card_number.startsWith('3')) return { label: 'American Express', logo: americansExpressLogo }
      if (card_number.startsWith('4')) return { label: 'Visa', logo: visasLogo }
      if (card_number.startsWith('5')) return { label: 'MasterCard', logo: mastersCardLogo }
      if (card_number.startsWith('6')) return { label: 'Discover', logo: discoversLogo }
      return { label: 'Desconocido', logo: null }
      /* eslint-enable camelcase */
    },
    creditCardRules () {
      /* eslint-disable camelcase */
      let { card_number } = this.paymentForm
      let rules = [
        v => !!v || 'Campo requerido',
        v => v.startsWith('3') || v.startsWith('4') || v.startsWith('5') || v.startsWith('6') || 'Proveedor desconocido'
      ]
      if (card_number.startsWith('3')) {
        rules.push(v => v.length === 15 || 'El numero de tarjeta debe de tener 15 digitos')
      } else {
        rules.push(v => v.length === 16 || 'El numero de tarjeta debe de tener 16 digitos')
      }
      return rules
      /* eslint-enable camelcase */
    }
  },
  watch: {
    cart (val, oldVal) {
      this.updatePaymentMethodsAvailability()
    }
  },
  methods: {
    ...mapActions('cart', {
      cartUpdate: 'update'
    }),

    updatePaymentMethodsAvailability () {
      let paymentSettingsContianer = document.getElementById('meta-payment')

      if (paymentSettingsContianer) {
        this.paymentSettings = JSON.parse(paymentSettingsContianer.content)

        this.purchasePaymentMethodOptions.forEach(item => {
          if (item.value === CASH_PAYMENT) {
            item.available = this.paymentSettings.cashPayment.enabled
          }
          if (item.value === DELIVERY_PAYMENT) {
            if (this.cart) {
              item.available =
                this.paymentSettings.deliveryPayment.enabled &&
                this.cart.shippingType === STORE_SHIPPING
            }
          }
        })
      }
    },

    handleChange (value) {
      if (
        [CARD_PAYMENT, CASH_PAYMENT, DELIVERY_PAYMENT].indexOf(value) !== -1
      ) {
        this.purchasePaymentMethod = value
      }

      this.$emit('change', {
        paymentMethod: this.purchasePaymentMethod,

        paymentForm: this.paymentForm,
        paymentFormIsValid: this.$refs.paymentForm.validate(),

        personalForm: this.personalForm,
        personalFormIsValid: this.$refs.personalForm.validate()
      })
    }
  },
  created () {
    /**
     * Get payment settings
     */
    this.updatePaymentMethodsAvailability()
  },
  mounted () {
    if (this.userIsAuthenticated) {
      this.personalForm.firstName = this.user.firstName
      this.personalForm.lastName = this.user.lastName
      this.personalForm.email = this.user.email
    }
  }
}
</script>
