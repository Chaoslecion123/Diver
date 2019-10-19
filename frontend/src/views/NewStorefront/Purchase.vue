<template>
  <v-content>
    <v-layout
      id="section__purchase"
      class="section remove-margin-600">
      <v-container
        fluid
        px-0
        class="remove-padding-600">
        <v-layout
          row
          wrap>
          <v-flex
            xs12 md9>
            <v-stepper
              v-model="step"
              vertical>
              <v-stepper-step
                :complete="step > 1"
                step="01">
                <span
                  class="font-weight-bold">
                  Elija una dirección de entrega
                </span>
                <small>
                  Texto de ayuda
                </small>
              </v-stepper-step>

              <v-stepper-content
                step="1">
                <v-card
                  color="grey lighten-4"
                  class="border-radius">
                  <v-container>
                    <v-flex
                      style="font-size:1.125rem;"
                      class="mb-3 font-weight-600">
                      Datos personales
                    </v-flex>
                    <v-divider/>
                    <v-radio-group
                      hide-details
                      v-model="radio">
                      <v-layout
                        v-for="(address, i) in address.items"
                        :key="i"
                        row
                        wrap
                        fill-height
                        align-center
                        justify-space-between
                        class="mt-4">
                        <v-radio
                          class="ml-2 my-0"
                          :value="address.streetAddress1"/>
                        <v-flex
                          xs6 sm5 md6>
                          <v-flex
                            mb-2
                            class="font-weight-600">
                            <!-- No renderiza la vista cuando estás deslogeado porque no hay current user -->
                            <span v-if="address.firstName"> {{address.firstName}} </span>
                            <span v-if="address.lastName"> {{address.lastName}} </span>
                          </v-flex>
                          <v-flex>
                            <span v-if="address.streetAddress1"> {{address.streetAddress1}} </span>
                            <span v-if="address.streetAddress2"> {{address.streetAddress2}} </span>
                          </v-flex>
                        </v-flex>
                        <v-spacer/>
                        <v-flex
                          offset-xs2 xs8 sm3 md2>
                          <v-btn
                            outline
                            block
                            class="d-blue--background border-radius"
                            @click="editAddress=!editAddress">
                            <span
                              class="font-weight-600">
                              Editar
                            </span>
                          </v-btn>
                          <d-new-address-popup
                            v-model="editAddress"/>
                        </v-flex>
                      </v-layout>
                    </v-radio-group>
                    <v-btn
                      class="q-orange--text title font-weight-600 pa-0 my-3"
                      @click="addAddressPopupIsOpen = true"
                      :ripple="false"
                      flat>
                      <v-icon
                        class="mr-4"
                        left>
                        add
                      </v-icon>
                      Crear nueva dirección
                    </v-btn>
                    <d-new-address-popup
                      v-model="addAddressPopupIsOpen"
                      :onOk="addAddress"/>
                    <v-divider
                      class="mb-4"/>
                    <v-layout
                      row
                      wrap
                      justify-end>
                      <v-flex
                        xs6 sm5 md4>
                        <v-btn
                          style="font-size:1.125rem;"
                          class="q-red--background ma-0 font-weight-600"
                          dark
                          block
                          @click="nextStep">
                          Siguiente
                        </v-btn>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-stepper-content>

              <v-stepper-step
                :complete="step > 2"
                step="02">
                <span
                  class="font-weight-bold">
                  Elija un método de envío
                </span>
              </v-stepper-step>

              <v-stepper-content
                step="2">
                <v-card
                  color="grey lighten-4"
                  class="border-radius">
                  <v-container
                    grid-list-lg>
                    <v-flex
                      style="font-size:1.125rem;"
                      class="mb-3 font-weight-600">
                      Métodos de envío
                    </v-flex>
                    <v-divider/>
                    <v-layout
                      class="my-4"
                      row
                      wrap
                      fill-height
                      align-center>
                      <v-flex
                        v-for="(item,i) in content.shipment"
                        :key="i"
                        xs6
                        sm4
                        md3 >
                        <v-btn
                          outline
                          block
                          @click="shipingType = i+1"
                          :class="[
                            {
                              'active': shipingType == i+1
                            },
                            'border-radius',
                            'btn--payment'
                          ]">
                          <d-icon
                            class="card-icon"
                            dark
                            name="b-shopping-cart"/>
                          <span class="font-weight-600">
                            {{ item.method }}
                          </span>
                        </v-btn>
                      </v-flex>
                    </v-layout>
                    <v-flex style="font-size:1.125rem;" class="mb-3 font-weight-600">
                      {{ currentShipment }}
                    </v-flex>
                    <v-divider/>
                    <v-window
                      v-model="shipingType">
                      <v-window-item
                        :value="1">
                        <v-layout
                          row
                          wrap>
                          <v-flex
                            my-3>
                            {{content.firstShipment}}
                          </v-flex>
                        </v-layout>
                      </v-window-item>

                      <v-window-item
                        :value="2">
                        <v-layout
                          row
                          wrap>
                          <v-flex
                            my-3>
                            {{content.secondShipment}}
                          </v-flex>
                        </v-layout>
                      </v-window-item>

                      <v-window-item
                        :value="3">
                        <v-layout
                          row
                          wrap>
                          <v-flex
                            my-3>
                            {{content.thirdShipment}}
                          </v-flex>
                        </v-layout>
                      </v-window-item>
                    </v-window>

                    <v-divider class="mb-4"/>
                    <v-layout
                      row
                      wrap
                      justify-space-between>
                      <v-flex
                        xs6
                        sm5
                        md4>
                        <v-btn
                          style="font-size:1.125rem;"
                          class="q-red--background ma-0 font-weight-600"
                          dark
                          block
                          @click="prevStep">
                          Atrás
                        </v-btn>
                      </v-flex>
                      <v-flex
                        xs6
                        sm5
                        md4>
                        <v-btn
                          style="font-size:1.125rem;"
                          class="q-red--background ma-0 font-weight-600"
                          dark
                          block
                          @click="nextStep">
                          Siguiente
                        </v-btn>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-stepper-content>

              <v-stepper-step
                step="03"
                :complete="step > 3">
                <span
                  class="font-weight-bold">
                  Elija un método de pago
                </span>
              </v-stepper-step>

              <v-stepper-content
                step="3">
                <v-card
                  color="grey lighten-4"
                  class="border-radius">
                  <v-container
                    grid-list-lg>
                    <v-flex
                      style="font-size:1.125rem;"
                      class="mb-3 font-weight-600">
                      Métodos de pago
                    </v-flex>
                    <v-divider/>
                    <v-layout class="my-2" row wrap fill-height align-center>
                      <v-flex
                        xs6
                        sm4
                        md3
                        v-for="(item,i) in content.payment"
                        :key="i">
                        <v-btn
                          outline
                          block
                          @click="paymentType = i+1"
                          :class="[
                            {
                              'active': paymentType == i+1
                            },
                            'border-radius',
                            'btn--payment'
                          ]">
                          <d-icon
                            dark class="card-icon"
                            name="b-card"/>
                          <span class="font-weight-600">
                            {{ item.method }}
                          </span>
                        </v-btn>
                      </v-flex>
                    </v-layout>

                    <v-flex style="font-size:1.125rem;" class="mb-3 font-weight-600">
                      {{ currentPayment }}
                    </v-flex>
                    <v-divider/>
                    <v-window v-model="paymentType">
                      <v-window-item :value="1">
                        <v-flex xs8 sm7 md6 my-4>
                          <v-btn
                            style="font-size:1.125rem;"
                            color="#2e2e2e"
                            class="border-radius font-weight-600"
                            dark
                            block
                            @click="makePayment">
                            Realizar pago con Culqi
                          </v-btn>
                        </v-flex>
                        <!--v-flex xs8 sm7 md7 my-2>
                          <div class="delivery-info">
                            <span class="font-weight-600 mr-2">Código de Pedido:</span>
                            {{content.purchaseCode}}
                          </div>
                        </v-flex>
                        <v-flex>
                          <span>{{content.purchaseDescription}}</span>
                        </v-flex>
                        <v-flex xs12 md9>
                          <form>
                            <v-layout class="mt-3" row wrap>
                              <v-flex xs12 sm3>
                                Nombre del Usuario
                              </v-flex>
                              <v-flex xs12 sm9>
                                <v-text-field
                                  value="Martin"
                                  class="border-radius"
                                  :rules="[rules.required]"
                                  solo
                                  flat
                                  required
                                  type="text"/>
                              </v-flex>
                              <v-flex xs12 sm3>
                                # de tarjeta
                              </v-flex>
                              <v-flex xs12 sm9>
                                <v-text-field
                                  data-culqi="card[number]"
                                  id="card[number]"
                                  :value="card.card_number"
                                  :rules="[rules.required]"
                                  solo
                                  flat
                                  required/>
                              </v-flex>
                              <v-flex xs12 sm3>
                                Fecha de caducidad
                              </v-flex>
                              <v-flex xs6 sm2>
                                <v-text-field
                                  data-culqi="card[exp_month]"
                                  :value="card.expiration_month"
                                  id="card[exp_month]"
                                  mask="##"
                                  :rules="[rules.required]"
                                  placeholder="Mes"
                                  solo
                                  flat
                                  required
                                  maxlength="2"
                                ></v-text-field>
                              </v-flex>
                              <v-flex xs6 sm2>
                                <v-text-field
                                  data-culqi="card[exp_year]"
                                  id="card[exp_year]"
                                  :value="card.expiration_year"
                                  mask="####"
                                  :rules="[rules.required]"
                                  placeholder="Año"
                                  solo
                                  flat
                                  required
                                  maxlength="4"
                                ></v-text-field>
                              </v-flex>
                              <v-spacer/>
                              <v-flex xs12 sm2>
                                CVV
                              </v-flex>
                              <v-flex xs12 sm2>
                                <v-text-field
                                  data-culqi="card[cvv]"
                                  id="card[cvv]"
                                  :value="card.cvv"
                                  mask="###"
                                  :rules="[rules.required]"
                                  solo
                                  flat
                                  required
                                  maxlength="3"/>
                              </v-flex>
                            </v-layout>

                            <input
                              type="text"
                              class="form-control"
                              placeholder="Correo electrónico"
                              v-model="user.email"
                              data-culqi="card[email]"
                              id="card[email]">
                          </form>
                        </v-flex -->
                      </v-window-item>

                      <v-window-item :value="2">
                        <v-layout row wrap>
                          <v-flex xs8 sm7 md7 my-2>
                            <div class="delivery-info">
                              <span class="font-weight-600 mr-2">Código de Pedido:</span>
                              {{content.purchaseCode}}
                            </div>
                          </v-flex>
                          <v-flex>
                            <span>{{content.purchaseDescription}}</span>
                          </v-flex>
                          <v-flex class="my-2">
                            <span class="font-weight-600 mr-2">Nº de Cuenta Corriente:</span>
                            {{content.accountNumber}}
                          </v-flex>
                        </v-layout>
                      </v-window-item>

                      <v-window-item :value="3">
                        <v-layout row wrap>
                          <v-flex xs8 sm7 md7 my-2>
                            <div class="delivery-info">
                              <span class="font-weight-600 mr-2">Código de Pedido:</span>
                              {{content.purchaseCode}}
                            </div>
                          </v-flex>
                          <v-flex>
                            <span>{{content.purchaseDescription}}</span>
                          </v-flex>
                          <v-flex class="my-2">
                            <span class="font-weight-600 mr-2">Nº de Cuenta Corriente:</span>
                            {{content.accountNumber}}
                          </v-flex>
                        </v-layout>
                      </v-window-item>
                    </v-window>

                    <v-divider class="mb-4"/>
                    <v-layout row wrap justify-space-between>
                      <v-flex xs6 sm5 md4>
                        <v-btn
                          style="font-size:1.125rem;"
                          class="q-red--background ma-0 font-weight-600"
                          dark
                          block
                          @click="prevStep">
                          Atrás
                        </v-btn>
                      </v-flex>

                      <v-flex xs6 sm5 md4>
                        <v-btn
                          style="font-size:1.125rem;"
                          class="q-red--background ma-0 font-weight-600"
                          dark
                          block
                          :to="{name: 'Tracking'}">
                          Finalizar compra
                        </v-btn>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card>
              </v-stepper-content>
            </v-stepper>
          </v-flex>
          <v-flex xs12 offset-sm2 offset-md0 sm8 md3 class="set-margin-4-600">
            <d-checkout-sumary :code="true"/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>
  </v-content>
</template>

<style lang="less">
#section__purchase {
  .v-stepper {
    box-shadow: none;
    margin-top: -24px;
    .v-stepper__step {
      &--complete {
        .v-stepper__step__step {
          background-color: #f58220 !important;
          border-color: #f58220 !important;
        }
      }
    }
    .v-stepper__content {
      .v-input--selection-controls.v-input--radio-group {
        margin-top: 0;
        padding-top: 0;
      }
    }
    .v-card {
      box-shadow: none;
      .v-input__slot {
        border-radius: 5px;
        input {
          font-size: 0.875rem;
        }
      }
      .btn--payment {
        padding: 0 8px !important;
        border-width: 2px !important;
        height: 72px !important;
        color: rgba(0, 0, 0, 0.6) !important;
        .card-icon {
          margin: 0 8px;
          height: 24px;
          width: 36px;
        }
        @media only screen and (max-width: 600px) {
          .card-icon {
            width: 48px;
          }
        }
        &:hover,
        &:active,
        &:focus,
        &:before,
        &.active {
          color: #f58220 !important;
        }
        span {
          white-space: normal;
        }
      }
    }
  }
  .delivery-info {
    height: 36px;
    border-radius: 5px;
    background-color: #2e2e2e;
    line-height: 36px;
    text-align: center;
    color: #fff;
  }
}
.v-input__append-inner {
  margin: auto !important;
}
</style>

<script>
import { mapActions, mapState } from 'vuex'
import Culqi from '@/_utils/culqi'

export default {
  name: 'Purchase',
  data () {
    return {
      culqi: null,
      showNewAddress: false,
      editAddress: false,
      step: 1,
      paymentType: 1,
      shipingType: 1,
      radio: null,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        min: v =>
          (v && v.length >= 8) ||
          'La contraseña debe tener al menos 8 caracteres'
      },
      card: {
        // card_number: '4111111111111111',
        // cvv: '123',
        // expiration_month: '09',
        // expiration_year: '2020'
        cvv: '039',
        card_number: '5111111111111118',
        expiration_month: '06',
        expiration_year: '2020'
      },
      addAddressPopupIsOpen: false,
      content: {
        addresses: [
          {
            number: 1,
            contactName: 'Sheyla Breña',
            contactFullAdress: 'Huertos de Manchay, MZ C Lt 19, PACHACAMAC'
          },
          {
            number: 2,
            contactName: 'Sheyla Breña',
            contactFullAdress: 'Huertos de Manchay, MZ C Lt 19, PACHACAMAC'
          }
        ],
        payment: [
          { method: 'Tarjetas de crédito' },
          { method: 'Pago contra entrega' },
          { method: 'Pago efectivo' }
        ],
        shipment: [
          { method: 'Envío Standar' },
          { method: 'Envío Express' },
          { method: 'Recoger en tienda' }
        ],
        purchaseCode: '20012019-01',
        purchaseDescription:
          '!Los envíos a centros de trabajo tienen 95% de entregas a tiempo! ¿Por qué no eliges la dirección de tu trabajo para la entrega? Para este medio de pago, el peso de los productos no debe exceder los 20 kg (peso volumétrico). Si tu compra es de un monto superior, por favor, debes elegir entre los otros medios de pago que tenemos disponibles. Este método de pago está disponible sólo para ciudades principales.',
        accountNumber: '191-2516207-0-31',
        orderDetails: {
          1: {
            productsQuantity: '03',
            orderPrice: '635.11',
            orderDiscount: '10%',
            shippingPrice: 'Gratis',
            finalOrderPrice: '571.99'
          }
        },
        firstShipment:
          'El envío Standar es un servicio regular, con código de seguimiento y un tiempo reparto entre 5 a 10 días.',
        secondShipment:
          'El envío Express es un servicio exclusivo, con código de seguimiento, atención las 24 hrs y un tiempo reparto entre 30 minutos a 2 días a nivel nacional.',
        thirdShipment:
          'El cliente se acerca previa cita a recoger su orden. Horario de atención de 9:00 AM a 10:00 PM.'
      }
    }
  },
  computed: {
    ...mapState('cart', {
      cart: 'cart'
    }),
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapState('address', {
      address: 'objects'
    }),
    totalAmount () {
      return this.cart.items.reduce((count, item) => {
        return count + item.variant.priceRange.start.net.amount * item.quantity
      }, 0)
    },
    currentShipment () {
      switch (this.shipingType) {
        case 1:
          return 'Envío Standar'
        case 2:
          return 'Envío Express'
        default:
          return 'Recoger en tienda'
      }
    },
    currentPayment () {
      switch (this.paymentType) {
        case 1:
          return 'Pago con Culqi' // return 'Datos de la tarjeta'
        case 2:
          return 'Pago contra entrega'
        default:
          return 'Pago efectivo'
      }
    }
  },
  watch: {
    culqi (val, oldVal) {
      console.log('*****')
      console.log(this.culqui)
      console.log('*****')
    }
  },
  methods: {
    ...mapActions('address', {
      getAddress: 'list'
    }),
    prevStep () {
      const { step } = this
      this.step = Math.max(step - 1, 1)
    },
    nextStep () {
      const { step } = this
      this.step = Math.min(step + 1, 3)
    },
    addAddress () {
      this.addAddressPopupIsOpen = false

      this.content.addresses.push({})

      this.$refs.addressForm.reset()
    },
    makePayment () {
      this.culqi.settings({
        title: 'Quimder Store',
        currency: 'PEN',
        description: 'Compras en Quimder',
        amount: this.formatPrice(this.totalAmount).replace('.', '')
      })
      this.culqi.open()
    },
    formatPrice (value) {
      let val = (value / 1).toFixed(2) // .replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
    }
  },
  created () {
    this.culqi = new Culqi('pk_test_Etkt4aRO0nZDB1pG')

    this.getAddress()
  }
}
</script>
