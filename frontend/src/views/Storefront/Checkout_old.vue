<template>
  <v-content app class="d-page__content d-checkout">
    <v-container class="mt-5 mb-5 d-shoping-cart__content" grid-list-md>
      <v-layout row wrap>
        <v-flex xs12 mb-4>
          <h2 class="text-uppercase">Proceso de pago</h2>
        </v-flex>

        <v-flex xs12 md9 shrink text-xs-center>
          <v-stepper v-model="step" vertical>
            <!--
              Tipo de envío
            -->
            <v-stepper-step :complete="purchaseShippingType !== null" step="01">
              <strong>Forma de entrega</strong>
            </v-stepper-step>

            <v-stepper-content step="1">
            </v-stepper-content>
          </v-stepper>
        </v-flex>
        <!-- v-if="cart && cart.quantity > 0" -->
        <v-flex xs12 md9 shrink text-xs-center>
          <v-stepper v-model="step" vertical>
            <!--
              Tipo de envío
            -->
            <v-stepper-step :complete="purchaseShippingType !== null" step="01">
              <strong>Forma de entrega</strong>
            </v-stepper-step>

            <v-stepper-content step="1">
              <v-card flat class="d-shipping-type grey lighten-4 text-xs-left">
                <v-card-text>
                  <v-radio-group class="ma-0 pa-0" v-model="purchaseShippingType">
                    <v-radio
                      v-for="shippingType in purchaseShippingTypeOptions"
                      :key="shippingType.value"
                      :disabled="shippingType.disabled"
                      :label="shippingType.name"
                      :value="shippingType.value"/>
                  </v-radio-group>
                </v-card-text>
                <v-divider/>
                <v-card-text>
                  <v-btn
                    depressed
                    color="accent"
                    class="ma-0 d-btn d-btn--rounded d-btn--bold d-btn--no-transform"
                    :block="$vuetify.breakpoint.xs"
                    :disabled="purchaseShippingType === null"
                    @click="completePurchaseShippingType">Siguiente</v-btn>
                </v-card-text>
              </v-card>
            </v-stepper-content>

            <!--
              Dirección de entrega
            -->
            <v-stepper-step :complete="purchaseShippingAddress !== null" step="02">
              <strong v-if="isForStoreShipping">Punto de recojo</strong>
              <strong v-else>Dirección de entrega</strong>
            </v-stepper-step>

            <v-stepper-content step="2">
              <v-card flat class="d-shipping-address grey lighten-4 text-xs-left">
                <template v-if="isForStoreShipping">
                  <v-card-text>Elije nuestra tienda más cercana a ti para recoger tu pedido.</v-card-text>
                  <v-divider/>
                  <v-card-text>
                    <div
                      v-if="physicalStores && physicalStores.items && physicalStores.items.length > 0"
                      class="mb-4">
                      <v-radio-group v-model="purchaseShippingAddress">
                        <v-radio
                          v-for="{name, address} in physicalStores.items"
                          :key="address.id"
                          :value="address.id">
                          <template slot="label">
                            <div>
                              <div>
                                <strong>{{ name }}</strong>
                              </div>
                              <div>{{ address.streetAddress1 }}</div>
                              <div>{{ address.streetAddress2 }}</div>
                              <div v-if="address.cityArea || address.city">
                                <template v-if="address.cityArea">{{ address.cityArea }},</template>
                                {{ address.city }}
                              </div>
                              <div
                                v-if="address.countryArea || address.countryName || address.country">
                                <template v-if="address.countryArea">{{ address.countryArea }},</template>
                                {{ address.countryName || address.country }}
                              </div>
                              <div v-if="address.postalCode">{{ address.postalCode }}</div>
                              {{ address.countryName }}
                            </div>
                          </template>
                        </v-radio>
                      </v-radio-group>
                    </div>
                    <div v-else class="mb-4">
                      Lo sentimos, por el momento no disponemos de una tienda fisica.
                      Por favor, selecione la opcion de envío a domicilio.
                    </div>
                  </v-card-text>
                </template>

                <template v-else>
                  <v-card-text>
                    <div
                      v-if="purchaseShippingAddresses && purchaseShippingAddresses.length > 0"
                      class="mb-4">
                      <v-radio-group v-model="purchaseShippingAddress">
                        <v-radio
                          v-for="address in purchaseShippingAddresses"
                          :key="address.id"
                          :value="address.id">
                          <template slot="label">
                            <div>
                              <div>
                                <strong>{{ address.firstName }} {{ address.lastName }}</strong>
                              </div>
                              <div v-if="address.companyName || address.phone">
                                <template v-if="address.companyName">{{ address.companyName }},</template>
                                {{ address.phone }}
                              </div>
                              <div>{{ address.streetAddress1 }}</div>
                              <div>{{ address.streetAddress2 }}</div>
                              <div v-if="address.cityArea || address.city">
                                <template v-if="address.cityArea">{{ address.cityArea }},</template>
                                {{ address.city }}
                              </div>
                              <div
                                v-if="address.countryArea || address.countryName || address.country">
                                <template v-if="address.countryArea">{{ address.countryArea }},</template>
                                {{ address.countryName || address.country }}
                              </div>
                              <div v-if="address.postalCode">{{ address.postalCode }}</div>
                            </div>
                          </template>
                        </v-radio>
                      </v-radio-group>
                    </div>
                    <div v-else class="mb-4">No tienes registrada ninguna dirección</div>

                    <v-btn
                      outline
                      depressed
                      color="accent"
                      :block="$vuetify.breakpoint.xs"
                      :class="[
                        'ma-0',
                        'd-btn',
                        'd-btn--rounded',
                        'd-btn--bold',
                        'd-btn--no-transform',
                      ]"
                      @click="openAddressPopup">
                      <d-icon class="mr-2" name="b-plus-circle-o"/>Añadir dirección
                    </v-btn>
                  </v-card-text>
                </template>

                <v-divider/>

                <v-card-text>
                  <v-btn
                    outline
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      {
                        'mb-2': $vuetify.breakpoint.xs,
                        'mr-2': $vuetify.breakpoint.smAndUp,
                      },
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="prevStep">Anterior</v-btn>

                  <v-btn
                    :disabled="purchaseShippingAddress === null"
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="completePurchaseShippingAddress">Siguiente</v-btn>
                </v-card-text>
              </v-card>
            </v-stepper-content>

            <!--
              Metodo de envio
            -->
            <v-stepper-step :complete="purchaseShippingMethod !== null" step="03">
              <strong>Método de envío</strong>
            </v-stepper-step>

            <v-stepper-content step="3">
              <v-card flat class="d-shipping-method grey lighten-4 text-xs-left">
                <v-card-text>
                  <v-radio-group class="ma-0 pa-0" v-model="purchaseShippingMethod">
                    <v-radio
                      v-for="shippingMethod in purchaseShippingMethodOptions.items"
                      :key="shippingMethod.id"
                      :value="shippingMethod.id">
                      <template slot="label">
                        <strong>{{ shippingMethod.name }}</strong> (
                        <template v-if="shippingMethod.price.currency ==='PEN'">S/ </template>{{ formatPrice(shippingMethod.price.amount) }}<template v-if="shippingMethod.price.currency !=='PEN'"> {{ shippingMethod.price.currency }}</template>)
                      </template>
                    </v-radio>
                  </v-radio-group>
                </v-card-text>
                <v-divider/>

                <v-card-text>
                  <v-btn
                    outline
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      {
                        'mb-2': $vuetify.breakpoint.xs,
                        'mr-2': $vuetify.breakpoint.smAndUp,
                      },
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="prevStep">Anterior</v-btn>

                  <v-btn
                    depressed
                    color="accent"
                    class="ma-0 d-btn d-btn--rounded d-btn--bold d-btn--no-transform"
                    :block="$vuetify.breakpoint.xs"
                    :disabled="purchaseShippingMethod === null"
                    @click="completePurchaseShippingMethod">Siguiente</v-btn>
                </v-card-text>
              </v-card>
            </v-stepper-content>

            <!--
              Dirección de facturación
            -->
            <v-stepper-step :complete="purchaseBillingAddress !== null" step="04">
              <strong>Dirección de facturación</strong>
            </v-stepper-step>

            <v-stepper-content step="4">
              <v-card flat class="d-billing-address grey lighten-4 text-xs-left">
                <v-card-text>Crea o elije una dirección para registrar tu comprobante de pago.</v-card-text>
                <v-divider/>
                <v-card-text>
                  <div
                    v-if="purchaseBillingAddresses && purchaseBillingAddresses.length > 0"
                    class="mb-4">
                    <v-radio-group v-model="purchaseBillingAddress">
                      <v-radio
                        v-for="address in purchaseBillingAddresses"
                        :key="address.id"
                        :value="address.id">
                        <template slot="label">
                          <div>
                            <div>
                              <strong>{{ address.firstName }} {{ address.lastName }}</strong>
                            </div>
                            <div v-if="address.companyName || address.phone">
                              <template v-if="address.companyName">{{ address.companyName }},</template>
                              {{ address.phone }}
                            </div>
                            <div>{{ address.streetAddress1 }}</div>
                            <div>{{ address.streetAddress2 }}</div>
                            <div v-if="address.cityArea || address.city">
                              <template v-if="address.cityArea">{{ address.cityArea }},</template>
                              {{ address.city }}
                            </div>
                            <div
                              v-if="address.countryArea || address.countryName || address.country">
                              <template v-if="address.countryArea">{{ address.countryArea }},</template>
                              {{ address.countryName || address.country }}
                            </div>
                            <div v-if="address.postalCode">{{ address.postalCode }}</div>
                          </div>
                        </template>
                      </v-radio>
                    </v-radio-group>
                  </div>
                  <div v-else class="mb-4">No tienes registrada ninguna dirección</div>

                  <v-btn
                    outline
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                    'ma-0',
                    'd-btn',
                    'd-btn--rounded',
                    'd-btn--bold',
                    'd-btn--no-transform',
                    ]"
                    @click="openAddressPopup">
                    <d-icon class="mr-2" name="b-plus-circle-o"/>Añadir dirección
                  </v-btn>
                </v-card-text>

                <v-divider/>

                <v-card-text>
                  <v-btn
                    outline
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      {
                        'mb-2': $vuetify.breakpoint.xs,
                        'mr-2': $vuetify.breakpoint.smAndUp,
                      },
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="prevStep">Anterior</v-btn>

                  <v-btn
                    :disabled="purchaseBillingAddress === null"
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="completePurchaseBillingAddress">Siguiente</v-btn>
                </v-card-text>
              </v-card>
            </v-stepper-content>

            <!--
              Tipo de comprobante
            -->
            <!--
            <v-stepper-step :complete="purchasePaymentInvoiceType !== null" step="05">
              <strong>Comprobante de Pago</strong>
            </v-stepper-step>

            <v-stepper-content step="5">
              <v-card flat class="d-shipping-type grey lighten-4 text-xs-left">
                <v-card-text>
                  <v-radio-group class="ma-0 pa-0" v-model="paymentInvoiceType">
                    <v-radio
                      v-for="paymentInvoiceType in paymentInvoiceTypeOptions"
                      :key="paymentInvoiceType.value"
                      :disabled="paymentInvoiceType.disabled"
                      :label="paymentInvoiceType.name"
                      :value="paymentInvoiceType.value"
                    />
                  </v-radio-group>
                </v-card-text>
                <v-divider/>
                <v-card-text>
                  <v-btn
                    outline
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      {
                        'mb-2': $vuetify.breakpoint.xs,
                        'mr-2': $vuetify.breakpoint.smAndUp,
                      },
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="prevStep">
                    Anterior
                  </v-btn>

                  <v-btn
                    depressed
                    color="accent"
                    class="ma-0 d-btn d-btn--rounded d-btn--bold d-btn--no-transform"
                    :block="$vuetify.breakpoint.xs"
                    :disabled="paymentInvoiceType === null"
                    @click="completePurchasePaymentInvoiceType"
                  >Siguiente</v-btn>
                </v-card-text>
              </v-card>
            </v-stepper-content>
            -->

            <!--
              Pago de pedido
            -->
            <v-stepper-step step="05" :complete="step > 6">
              <span class="font-weight-bold">Elija un método de pago</span>
            </v-stepper-step>

            <v-stepper-content step="5">
              <v-card flat class="d-billing-address grey lighten-4 text-xs-center mb-4">
                <v-card-text>Elije un método de pago</v-card-text>
                <v-divider/>
                <v-card-text>
                  <template v-for="paymentMethod in purchasePaymentMethodOptions">
                    <v-btn
                      v-if="paymentMethod.available"
                      :key="paymentMethod.value"
                      outline
                      depressed
                      size="large"
                      :block="$vuetify.breakpoint.xs"
                      :color="purchasePaymentMethod === paymentMethod.value ? 'accent': ''"
                      :class="[
                        'ma-0',
                        {
                          'mb-2': $vuetify.breakpoint.xs,
                          'mr-2': $vuetify.breakpoint.smAndUp,
                        },
                        'd-btn',
                        'd-btn--rounded',
                        'd-btn--bold',
                        'd-btn--no-transform',
                      ]"
                      @click="purchasePaymentMethod = paymentMethod.value">{{ paymentMethod.name }}</v-btn>
                  </template>
                </v-card-text>
                <v-card-text>
                  <v-window v-model="purchasePaymentMethod">
                    <v-window-item :value="paymentType.card">
                      <div>
                        <p>
                          Los pagos por tarjeta son procesados por
                          <a
                            class="accent--text"
                            href="https://culqi.com/"
                            target="_brank">Culqi</a>.
                        </p>
                        <p>
                          <a class="accent--text" href="https://culqi.com/" target="_brank">
                            <img :src="assets.culqiLogo" alt="Culqi" style="height: 25px;">
                          </a>
                        </p>
                        <v-form
                          ref="paymentForm"
                          v-model="isValidForm"
                          lazy-validation
                          class="d-form"
                          style="margin: 0 auto;">
                          <v-container pa-0>
                            <v-layout row wrap>
                              <v-flex xs12>
                                <v-text-field
                                  ref="name"
                                  v-model="paymentForm.name"
                                  browser-autocomplete="off"
                                  prepend-inner-icon="account_circle"
                                  placeholder="Nombres y apellidos"
                                  type="text"
                                  flat
                                  solo
                                  :class="[
                                    'd-input',
                                    'd-input--rounded',
                                    'd-input--bordered',
                                  ]"/>
                              </v-flex>

                              <v-flex xs12>
                                <v-text-field
                                  ref="email"
                                  v-model="paymentForm.email"
                                  data-culqi="card[email]"
                                  browser-autocomplete="off"
                                  prepend-inner-icon="mail"
                                  placeholder="Correo electrónico"
                                  type="email"
                                  flat
                                  solo
                                  :class="[
                                    'd-input',
                                    'd-input--rounded',
                                    'd-input--bordered',
                                  ]"/>
                              </v-flex>

                              <v-flex xs12>
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
                                  :class="[
                                    'd-input',
                                    'd-input--rounded',
                                    'd-input--bordered',
                                  ]"/>
                              </v-flex>

                              <v-flex xs4>
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
                                  :class="[
                                    'd-input',
                                    'd-input--rounded',
                                    'd-input--bordered',
                                  ]"/>
                              </v-flex>

                              <v-flex xs4>
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
                                  :class="[
                                    'd-input',
                                    'd-input--rounded',
                                    'd-input--bordered',
                                  ]"/>
                              </v-flex>

                              <v-flex xs4>
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
                                  :class="[
                                    'd-input',
                                    'd-input--rounded',
                                    'd-input--bordered',
                                  ]"/>
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
                            <br>20012019-01
                          </strong>
                        </p>
                        <p>
                          Acercate a cualquier agencia bancaria o agente y
                          realiza tu deposito a cualquiera de nuestras cuentas.
                        </p>
                        <v-data-table
                          :headers="[
                            {
                              text: 'Banco',
                              align: 'left',
                              value: 'provider',
                              sortable: false,
                            },
                            {
                              text: 'Número de cuenta',
                              value: 'number',
                              sortable: false,
                              align: 'center',
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
                      <div style="max-width: 400px; margin: 0 auto;">
                        <p>
                          <strong>
                            Código de Pedido
                            <br>20012019-01
                          </strong>
                        </p>
                        <p>
                          <strong>1.</strong> Acercate al local que elegiste.
                        </p>
                        <p>
                          <strong>2.</strong> Paga en caja indicando el código de tu pedido.
                        </p>
                        <p>
                          <strong>3.</strong> ¡Listo, el producto es tuyo!
                        </p>
                      </div>
                    </v-window-item>
                  </v-window>
                </v-card-text>
                <v-divider/>
                <v-card-text>
                  <!--
                    :disabled="purchaseBillingAddress === null"
                  -->
                  <v-btn
                    depressed
                    color="accent"
                    :block="$vuetify.breakpoint.xs"
                    :class="[
                      'ma-0',
                      'd-btn',
                      'd-btn--rounded',
                      'd-btn--bold',
                      'd-btn--no-transform',
                    ]"
                    @click="makePayment">Finalizar compra</v-btn>
                </v-card-text>
              </v-card>
            </v-stepper-content>
          </v-stepper>
        </v-flex>

        <v-flex xs12 md3 shrink text-xs-center class="d-shoping-cart__summary">
          <d-checkout-sumary :ordered="true"/>
        </v-flex>
      </v-layout>
      <d-address-popup v-model="addressPopupIsOpen"/>
    </v-container>
  </v-content>
</template>

<style lang="less">
.d-checkout {
  a {
    text-decoration: none;
  }
  .v-stepper {
    box-shadow: none;
  }

  .v-input__slot {
    margin: 0;
  }

  .v-messages {
    display: none;
  }

  .d-shipping-address,
  .d-billing-address {
    .v-radio {
      align-items: flex-start;
    }
  }

  .d-cash-payment {
    .v-table {
      background: transparent;
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
import cuilqiLogo from '@/assets/images/culqi.png'

const DOOR_SHIPPING = 'door-shipping'
const STORE_SHIPPING = 'store-shipping'

const BALLOT = 'ballot'
const FACTURE = 'facture'

const CARD_PAYMENT = 'card-payment'
const CASH_PAYMENT = 'cash-payment'
const DELIVERY_PAYMENT = 'delivery-payment'

export default {
  name: 'Checkout',
  data () {
    return {
      /**
       * Globals
       */
      assets: {
        culqiLogo: cuilqiLogo
      },
      isValidForm: false,
      cartQuery: {
        expand: 'lines.variant.image',
        fields: [
          'billingAddress',
          'created',
          'discountAmount',
          'discountName',
          'email',
          'lines',
          'quantity',
          'shippingAddress',
          'shippingMethod',
          'shippingType',
          'token',
          'user',
          'voucherCode'
        ].join(',')
      },

      /* Stepper */
      step: 1,
      purchaseAddresses: [],

      /* Step 1 */
      purchaseShippingType: null,
      purchaseShippingTypeOptions: [
        {
          name: 'Quiero que me lo envíen.',
          disabled: false,
          value: DOOR_SHIPPING
        },
        {
          name: 'Lo iré a recoger en tienda.',
          disabled: true,
          value: STORE_SHIPPING
        }
      ],

      /* Step 2 */
      purchaseShippingAddress: null,
      /* Computed: purchaseShippingAddresses: [], */

      /* Step 3 */
      purchaseShippingMethod: null,
      /* Computed: purchaseShippingMethodOptions: [
        {
          name: 'DHL',
          price: 'S/ 65.00',
          value: 1
        },
        {
          name: 'FedEx',
          price: 'S/ 20.00',
          value: 2
        },
        {
          name: 'Glovo',
          price: 'S/ 25.00',
          value: 3
        }
      ],
      */

      /* Step 4 */
      purchaseBillingAddress: null,
      /* Computed: purchaseBillingAddresses: [], */
      /* Step 5 */
      purchasePaymentInvoiceType: null,
      paymentInvoiceTypeOptions: [
        {
          name: 'Boleta.',
          disabled: false,
          value: BALLOT
        },
        {
          name: 'Factura.',
          disabled: false,
          value: FACTURE
        }
      ],
      /* Step 6 */
      paymentForm: {
        name: '',
        email: '',
        card_number: '',
        cvv: '',
        expiration_month: '',
        expiration_year: ''
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
      ],

      /* Global */
      addressPopupIsOpen: false,
      culqi: null,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        min: v =>
          (v && v.length >= 8) ||
          'La contraseña debe tener al menos 8 caracteres'
      },
      addAddressPopupIsOpen: false
    }
  },
  computed: {
    /**
     * Autenticated User
     */
    ...mapState('auth', {
      user: 'currentUser'
    }),

    /**
     * User addresses
     */
    ...mapState('address', {
      address: 'object',
      addresses: 'objects',
      addressListSuccess: 'listSuccess',
      addressCreateSuccess: 'createSuccess',
      addressUpdateSuccess: 'updateSuccess'
    }),

    /**
     * Cart
     */
    ...mapState('cart', {
      cart: 'object',
      cartToken: 'token',
      cartReadSuccess: 'readSuccess',
      cartUpdateSuccess: 'updateSuccess'
    }),

    /**
     * Physical stores
     */
    ...mapState('physical-store', {
      physicalStores: 'objects',
      physicalStoresListSuccess: 'listSuccess'
    }),

    ...mapGetters('cart', {
      totalAmount: 'totalAmount'
    }),

    /**
     * Shipping Methods
     */
    ...mapState('shipping-method', {
      purchaseShippingMethodOptions: 'objects'
    }),
    /* Global */

    /* Step 1 */
    isForDoorShipping () {
      if (this.purchaseShippingType !== null) {
        return this.purchaseShippingType === DOOR_SHIPPING
      }

      return false
    },

    isForStoreShipping () {
      if (this.purchaseShippingType !== null) {
        return this.purchaseShippingType === STORE_SHIPPING
      }

      return false
    },

    /* Step 2 */
    purchaseShippingAddresses () {
      return this.purchaseAddresses
    },

    /* Step 4 */
    purchaseBillingAddresses () {
      return this.purchaseAddresses
    }
  },
  watch: {
    cartUpdateSuccess (val, oldVal) {
      if (val) {
        const { step, purchaseShippingType } = this
        this.nextStep()
        this.refreshCart()

        if (step === 2 && purchaseShippingType === STORE_SHIPPING) {
          this.nextStep()
          this.purchaseShippingMethod = -1
        }

        // if (purchaseShippingType !== null && ) {
        //   this.nextStep()
        // }
      }
    },

    physicalStoresListSuccess (val, oldVal) {
      if (val) {
        const { physicalStores } = this
        this.purchaseShippingTypeOptions[1].disabled =
          physicalStores &&
          physicalStores.items &&
          physicalStores.items.length === 0
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
        this.purchaseShippingAddress = this.address.id
      }
    },

    addressUpdateSuccess (val, oldVal) {
      if (val) {
        let index = this.purchaseAddresses.findIndex(
          item => item.id === this.address.id
        )
        if (index) {
          this.purchaseAddresses[index] = { ...this.address }
        } else {
          this.purchaseAddresses.push(this.address)
        }

        this.purchaseShippingAddress = this.address.id
      }
    },
    culqi (val, oldVal) {
      console.log('*****')
      console.log(this.culqui)
      console.log('*****')
    }
  },
  methods: {
    /**
     * Cart operations
     */
    ...mapActions('cart', {
      cartRead: 'read',
      cartUpdate: 'update'
    }),

    /**
     * User addresses
     */
    ...mapActions('address', {
      getAddress: 'list'
    }),

    /**
     * Physical stores
     */
    ...mapActions('physical-store', {
      getPhysicalStores: 'list'
    }),

    /**
     * User addresses
     */
    ...mapActions('shipping-method', {
      getShippingMethods: 'list'
    }),

    formatPrice (value) {
      let val = (value / 1).toFixed(2) // .replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
    },

    /**
     * Step 1
     */
    completePurchaseShippingType () {
      if (this.purchaseShippingType) {
        this.cartUpdate({
          id: this.cartToken,
          data: {
            shippingType: this.purchaseShippingType,
            shippingAddress: null
          }
        })
      }
    },

    /**
     * Step 2
     */
    completePurchaseShippingAddress () {
      if (this.purchaseShippingAddress) {
        this.cartUpdate({
          id: this.cartToken,
          data: {
            shippingAddress: this.purchaseShippingAddress
          }
        })
      }

      if (
        this.purchaseShippingAddress &&
        this.purchaseShippingType === DOOR_SHIPPING
      ) {
        let purchaseShippingAddress = this.purchaseShippingAddresses.find(
          item => item.id === this.purchaseShippingAddress
        )
        this.getShippingMethods({
          query: {
            shipping_zone__countries__contains: purchaseShippingAddress.country
          }
        })
      }
    },

    /**
     *  Step 3
     */
    completePurchaseShippingMethod () {
      this.nextStep()
    },

    /**
     * Step 4
     */
    completePurchaseBillingAddress () {
      if (this.purchaseBillingAddress) {
        this.cartUpdate({
          id: this.cartToken,
          data: {
            billingAddress: this.purchaseBillingAddress
          }
        })
      }
    },

    /**
     * Step 5
     */
    completePurchasePaymentInvoiceType () {
      this.nextStep()
    },

    /**
     * Global
     */
    openAddressPopup () {
      this.addressPopupIsOpen = true
    },

    prevStep () {
      const { step, purchaseShippingType } = this
      this.step = Math.max(step - 1, 1)
      if (step === 4 && purchaseShippingType === STORE_SHIPPING) {
        this.prevStep()
      }
    },
    nextStep () {
      const { step } = this
      this.step = Math.min(step + 1, 5)
    },
    addAddress () {
      this.addAddressPopupIsOpen = false
      this.content.addresses.push({})
    },
    createToken () {
      this.culqi.createToken().then(token => {
        console.log('resultado ' + token)
      })
    },
    makePayment () {
      this.culqi.settings({
        title: 'Quimder Store',
        currency: 'PEN',
        description: 'Compras en Quimder',
        amount: this.formatPrice(this.totalAmount).replace('.', '')
      })
      this.createToken()
      // this.culqi.open()
    },

    refreshCart () {
      if (this.cartToken) {
        this.cartRead({
          id: this.cartToken,
          query: this.cartQuery
        })
      }
    }
  },
  created () {
    /**
     * Get payment settings
     */
    let paymentSettingsContianer = document.getElementById('meta-payment')
    if (paymentSettingsContianer) {
      this.paymentSettings = JSON.parse(paymentSettingsContianer.content)
      this.purchasePaymentMethodOptions.forEach(item => {
        if (item.value === CASH_PAYMENT) {
          item.available = this.paymentSettings.cashPayment.enabled
        }
        if (item.value === DELIVERY_PAYMENT) {
          item.available = this.paymentSettings.deliveryPayment.enabled
        }
      })
    }
    /**
     * Handle cart operations
     */
    this.refreshCart()
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
          culqi_token: window.Culqi.token.id,
          // culqi_installments: window.Culqi.token.metadata.installments
          // userId: this.user.id,
          extra: JSON.stringify(this.cart)
        }

        const serializedData = Object.keys(data)
          .map(key => {
            return encodeURIComponent(key) + '=' + encodeURIComponent(data[key])
          })
          .join('&')

        session
          .post(BASE + 'culqi/checkout/', serializedData)
          .then(function (response) {
            console.log(response)
          })
      }
    }

    this.culqi = new Culqi('pk_test_0fKy1wOS9SwjchPN')
    this.getAddress()
  }
}
</script>
