<template>
  <v-form
    ref="form"
    v-model="isValidForm"
    lazy-validation
    class="d-address-form d-address-tabs-form">
    <v-card
      :flat="flat"
      :class="{
        transparent: transparent
      }">
      <v-progress-linear
        v-if="addressCreating || addressUpdating"
        height="3"
        color="accent"
        :indeterminate="true"
        class="ma-0"/>

      <!--
        TITLE
      -->
      <v-card-title
        :class="[
          'title',
          'font-weight-regular'
          // {
          //   'justify-center': !closeAction,
          //   'justify-space-between': !!closeAction
          // }
        ]">
        {{ editMode ? 'Editar' : 'Nueva' }} dirección
      </v-card-title>
      <v-divider />

      <!--
        FORM
      -->
      <v-card-text class="pa-0">
        <v-tabs color="white" light grow slider-color="accent" v-model="tab">
          <!-- Map -->
          <v-tab ripple>
            Mapa
          </v-tab>
          <v-tab-item class="d-address-map-wrapper">
            <v-alert :value="true" type="info" class="ma-0">
              Busca tu direccion en el mapa y completa los detalles en la
              pestaña de <code>Dirección</code>.
            </v-alert>
            <d-address-map :address="address" @change="handleMapChange" />
          </v-tab-item>

          <!--
            ADDRESS
          -->
          <v-tab ripple>
            Dirección
          </v-tab>
          <v-tab-item>
            <v-alert :value="true" type="info" class="ma-0">
              Completa los detalles de tu dirección de entrega, también puedes
              buscarla la pestaña <code>Mapa</code>. En la pestaña
              <code>Contacto</code> completa los datos del receptor tú pedido.
            </v-alert>
            <v-container class="pb-0">
              <v-layout row wrap>
                <v-flex v-if="nonFieldErrors" xs12>
                  <div
                    class="v-input v-text-field v-text-field--solo v-text-field--enclosed theme--light">
                    <div class="v-input__control">
                      <div class="v-text-field__details">
                        <div class="v-messages theme--light error--text ">
                          <div
                            v-for="(message, index) in nonFieldErrors"
                            :key="index"
                            class="v-messages__wrapper">
                            {{ message }}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </v-flex>

                <!--
                  STREET1 FIELD
                -->
                <v-flex xs12>
                  <div>
                    Tipo de dirección
                  </div>
                  <v-select
                    v-if="locationTypes"
                    ref="locationType"
                    v-model="form.locationType"
                    :items="locationTypes"
                    item-text="text"
                    item-value="value"
                    flat
                    solo
                    required
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]">
                  </v-select>
                </v-flex>

                <!--
                  STREET1 FIELD
                -->
                <v-flex xs12>
                  <div>
                    Dirección
                  </div>
                  <v-text-field
                    ref="streetAddress1"
                    v-model="form.streetAddress1"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    hint="Ingresa una dirección para encontrarte. Calle, Av., Dpto, Int., Mz-Lt, ..."
                    persistent-hint
                    :error-messages="getErrors('streetAddress1')"/>
                </v-flex>

                <!--
                  STREET2 FIELD
                -->
                <v-flex xs12>
                  <div>
                    Referencia
                    <small>(Opcional)</small>
                  </div>
                  <v-text-field
                    ref="streetAddress2"
                    v-model="form.streetAddress2"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    :rules="[]"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    hint="Ingresa una referencia: Edificio, Urbanización, ..."
                    persistent-hint
                    :error-messages="getErrors('streetAddress2')"/>
                </v-flex>

                <!--
                <v-flex xs12>
                  <div>
                    Distrito
                  </div>
                  <d-autocomplete-world />
                </v-flex>
                -->

                <!--
                  CITYAREA FIELD
                -->
                <v-flex xs12>
                  <div>
                    Distrito
                  </div>
                  <v-text-field
                    ref="cityArea"
                    v-model="form.cityArea"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('cityArea')"/>
                </v-flex>

                <!--
                  CITY FIELD
                -->
                <v-flex xs12>
                  <div>
                    Provincia
                  </div>
                  <v-text-field
                    ref="city"
                    v-model="form.city"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('city')"/>
                </v-flex>

                <!--
                  COUNTRYAREA FIELD
                -->
                <v-flex xs12>
                  <div>
                    Departamento
                  </div>
                  <v-text-field
                    ref="countryArea"
                    v-model="form.countryArea"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('countryArea')"/>
                </v-flex>

                <!--
                  COUNTRY FIELD
                -->
                <v-flex xs12>
                  <div>
                    País
                  </div>
                  <v-select
                    v-if="countryList"
                    ref="country"
                    v-model="form.country"
                    :items="countryList"
                    item-text="name"
                    item-value="code"
                    flat
                    solo
                    readonly
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('country')"
                    @change="clearGeographicalData">
                  </v-select>
                  <v-text-field
                    v-else
                    ref="country"
                    v-model="form.country"
                    browser-autocomplete="off"
                    type="text"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('country')"/>
                </v-flex>

                <!--
                  POSTALCODE FIELD
                -->
                <v-flex xs12>
                  <div>
                    Código postal
                    <small>(Opcional)</small>
                  </div>
                  <v-text-field
                    ref="postalCode"
                    v-model="form.postalCode"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    :rules="[]"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('postalCode')"/>
                </v-flex>
              </v-layout>
            </v-container>
          </v-tab-item>

          <!-- Contact -->
          <v-tab ripple>
            Contacto
          </v-tab>
          <v-tab-item>
            <v-alert :value="true" type="info" class="ma-0">
              Completa aquí datos de la persona que recepcionará el pedido.
            </v-alert>
            <v-container class="pb-0">
              <v-layout row wrap>
                <v-flex v-if="nonFieldErrors" xs12>
                  <div
                    class="v-input v-text-field v-text-field--solo v-text-field--enclosed theme--light">
                    <div class="v-input__control">
                      <div class="v-text-field__details">
                        <div class="v-messages theme--light error--text ">
                          <div
                            v-for="(message, index) in nonFieldErrors"
                            :key="index"
                            class="v-messages__wrapper">
                            {{ message }}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </v-flex>

                <!--
                  FIRSTNAME FIELD
                -->
                <v-flex xs12>
                  <div>
                    Nombres
                  </div>
                  <v-text-field
                    ref="firstName"
                    v-model="form.firstName"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('firstName')"/>
                </v-flex>

                <!--
                  LASTNAME FIELD
                -->
                <v-flex xs12>
                  <div>
                    Apellidos
                  </div>
                  <v-text-field
                    ref="lastName"
                    v-model="form.lastName"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    required
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('lastName')"/>
                </v-flex>

                <!--
                  COMPANYNAME FIELD
                -->
                <v-flex xs12 v-if="false">
                  <div>
                    Nombre de empresa
                    <small>(Opcional)</small>
                  </div>
                  <v-text-field
                    ref="companyName"
                    v-model="form.companyName"
                    browser-autocomplete="off"
                    type="text"
                    flat
                    solo
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('companyName')"/>
                </v-flex>

                <!--
                  PHONE FIELD
                -->
                <v-flex xs12>
                  <div>
                    Teléfono
                  </div>
                  <v-select
                    style="display: inline-block; width: 25%;"
                    v-model="form.phoneCode"
                    :items="phoneCodes"
                    flat
                    solo
                    required
                    readonly
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"/>
                  <v-text-field
                    style="display: inline-block; width: 75%;"
                    ref="phone"
                    v-model="form.phone"
                    browser-autocomplete="off"
                    placeholder="999999999999"
                    type="text"
                    flat
                    solo
                    required
                    item-text="text"
                    item-value="value"
                    :rules="[v => !!v || 'Campo requerido']"
                    :class="[
                      'd-input',
                      'd-input--rounded',
                      'd-input--bordered'
                    ]"
                    :error-messages="getErrors('phone')"/>
                </v-flex>
              </v-layout>
            </v-container>
          </v-tab-item>
        </v-tabs>
      </v-card-text>
      <v-divider />

      <!--
        ACCIONES
      -->
      <v-card-actions class="pa-0">
        <v-container grid-list-lg>
          <v-layout row wrap justify-center>
            <v-flex xs6 class="py-0">
              <v-btn
                block
                flat
                :class="[
                  'd-btn',
                  'd-btn--bold',
                  'd-btn--no-transform',
                  'error--text'
                ]"
                @click="handleDiscard">
                Descartar
              </v-btn>
            </v-flex>

            <v-flex xs6 class="py-0">
              <v-btn
                block
                dark
                depressed
                color="accent"
                :class="['d-btn', 'd-btn--bold', 'd-btn--no-transform']"
                @click="handleCreateOrUpdate">
                {{ tab === 2 ? 'Guardar' : 'Agregar' }}
              </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<style lang="less">
.d-address-form {
  width: 100%;

  @media screen and (min-width: 600px) {
    width: 500px;
  }

  &.d-address-tabs-form {
    > .v-card {
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: auto;
      max-height: initial;
      width: 100%;

      @media screen and (min-width: 600px) {
        height: 80vh;
        max-height: 700px;
      }

      > .v-card__text {
        flex: 1 1 auto;
        overflow: auto;
        display: flex;

        > .v-tabs {
          flex: 1 1 auto;
          display: flex;
          flex-direction: column;

          > .v-window {
            flex: 1 1 auto;
            display: flex;
            flex-direction: column;

            > .v-window__container {
              flex: 1 1 auto;
              display: flex;
              flex-direction: column;

              .v-window-item {
                flex: 1 1 auto;

                &.d-address-map-wrapper {
                  display: flex;
                  flex-direction: column;
                }
              }
            }
          }
        }
      }

      > .v-card__title,
      > .v-card__actions {
        flex-grow: 0;
      }

      .v-alert {
        border: 0 none !important;
      }
    }

    .v-tabs__item {
      text-transform: none;
      font-weight: normal;
    }
  }
}
</style>

<script>
import { mapActions, mapState, mapGetters, mapMutations } from 'vuex'
import { CREATE_SET_MESSAGES, UPDATE_SET_MESSAGES } from '@/store/_processes'
import { EMAIL } from '@/views/Auth/_utils'
// import AutocompleteWorld from './autocomplete-world'
import Map from './map'

const PE = 'PE'
const LOCATION_TYPES = [
  { text: 'Casa', value: 'home' },
  { text: 'Oficina', value: 'office' },
  { text: 'Edificio', value: 'building' },
  { text: 'Condominio', value: 'condominium' },
  { text: 'Quinta', value: 'country-house' },
  { text: 'Negocio', value: 'businesses' },
  { text: 'Otro', value: 'other' }
]

export default {
  name: 'd-address-form',
  components: {
    'd-address-map': Map
    // 'd-autocomplete-world': AutocompleteWorld
  },
  props: {
    address: {
      type: Object,
      default: null
    },
    closeAction: null,
    secondaryAction: null,
    flat: null,
    transparent: null
  },
  data () {
    return {
      tab: 0,
      isValidForm: false,
      locationTypes: LOCATION_TYPES,
      default: {
        countryCode: PE
      },
      form: {
        firstName: '',
        lastName: '',
        companyName: '',
        phone: '',
        phoneCode: { text: '+51', value: '+51' },

        streetAddress1: '',
        streetAddress2: '',
        cityArea: '',
        city: '',
        countryArea: '',
        country: '',
        postalCode: '',
        position: null,
        locationType: 'home'
      },
      formAddressList: [],
      rules: {
        email: v => EMAIL.test(v) || 'Email inválido',
        required: {
          email: v => !!v || 'Ingresa tu correo electrónico.',
          password: v => !!v || 'Ingresa tu contraseña.'
        }
      },
      countryList: null,
      phoneCodes: [{ text: '+51', value: '+51' }]
    }
  },
  computed: {
    ...mapState('address', {
      // address: 'object',
      addressList: 'objects',

      addressCreating: 'creating',
      addressCreateSuccess: 'createSuccess',
      addressCreateMessages: 'createMessages',

      addressUpdating: 'updating',
      addressUpdateSuccess: 'updateSuccess',
      addressUpdateMessages: 'updateMessages'
    }),

    ...mapState('auth', {
      user: 'currentUser'
    }),

    ...mapGetters('auth', {
      userIsAuthenticated: 'isAuthenticated'
    }),

    editMode () {
      return this.address !== null
    },

    nonFieldErrors () {
      const { addressUpdateMessages, addressCreateMessages } = this
      let nonFieldErrors = null

      if (this.editMode) {
        if (addressUpdateMessages && addressUpdateMessages.nonFieldErrors) {
          nonFieldErrors = [...addressUpdateMessages.nonFieldErrors]
        }
        return nonFieldErrors
      }

      if (addressCreateMessages && addressCreateMessages.nonFieldErrors) {
        nonFieldErrors = [...addressCreateMessages.nonFieldErrors]
      }
      return nonFieldErrors
    }
  },
  watch: {
    addressCreateSuccess (val, oldVal) {
      if (val) {
        this.handleCloseAction()
      }
    },
    addressUpdateSuccess (val, oldVal) {
      if (val) {
        this.handleCloseAction()
      }
    }
  },
  methods: {
    ...mapActions('address', {
      createAddress: 'create',
      updateAddress: 'update'
    }),

    ...mapMutations('address', {
      setCreateMessages: CREATE_SET_MESSAGES,
      setUpdateMessages: UPDATE_SET_MESSAGES
    }),

    ...mapActions('auth', {
      login: 'login'
    }),

    loadData () {
      if (this.address) {
        this.form.firstName = this.address.firstName
        this.form.lastName = this.address.lastName
        this.form.companyName = this.address.companyName
        if (this.address.phone) {
          this.form.phone = this.address.phone.replace('+51', '')
        } else {
          this.form.phone = this.address.phone
        }
        this.form.streetAddress1 = this.address.streetAddress1
        this.form.streetAddress2 = this.address.streetAddress2
        this.form.cityArea = this.address.cityArea
        this.form.city = this.address.city
        this.form.countryArea = this.address.countryArea
        this.form.country = this.address.country
        this.form.postalCode = this.address.postalCode
        this.form.position = this.address.position
      }
    },

    getErrors (fieldname) {
      const { editMode, addressCreateMessages, addressUpdateMessages } = this
      let messages = addressCreateMessages
      if (editMode) {
        messages = addressUpdateMessages
      }
      if (messages && messages[fieldname]) {
        return [...messages[fieldname]]
      }
      return []
    },

    clearMessages () {
      if (this.editMode) {
        this.setUpdateMessages(null)
      } else {
        this.setCreateMessages(null)
      }
    },

    clearGeographicalData () {
      this.form.cityArea = ''
      this.form.city = ''
      this.form.countryArea = ''
    },

    handleMapChange (value) {
      this.form.streetAddress1 = value.streetAddress1
      this.form.streetAddress2 = value.streetAddress2
      this.form.cityArea = value.cityArea
      this.form.city = value.city
      this.form.countryArea = value.countryArea
      this.form.country = value.country
      this.form.postalCode = value.postalCode
      this.form.position = value.position
    },
    handleCreateOrUpdate () {
      if (this.tab === 2) {
        this.clearMessages()

        const { form } = this.$refs
        form.validate()

        let isValidForm = this.form.firstName !== ''
        isValidForm = isValidForm && this.form.lastName !== ''
        isValidForm = isValidForm && this.form.streetAddress1 !== ''
        isValidForm = isValidForm && this.form.cityArea !== ''
        isValidForm = isValidForm && this.form.city !== ''
        isValidForm = isValidForm && this.form.countryArea !== ''
        isValidForm = isValidForm && this.form.country !== ''
        isValidForm = isValidForm && this.form.position !== null

        if (isValidForm) {
          let form = { ...this.form }
          form.phone = form.phoneCode.value + form.phone
          delete form.phoneCode

          if (form.position) {
            form.position = JSON.stringify(form.position)
          }
          if (this.editMode) {
            this.updateAddress({ id: this.address.id, data: { ...form } })
          } else {
            this.createAddress({ data: { ...form } })
          }
        } else {
          if (this.form.firstName === '' || this.form.lastName === '') {
            this.tab = 2
          } else {
            this.tab = 1
          }
        }
      } else {
        this.tab += 1
      }
    },

    handleDiscard () {
      const { form } = this.$refs
      form.reset()

      if (this.closeAction) {
        this.closeAction()
      }
    },

    handleCloseAction () {
      const { form } = this.$refs
      form.reset()

      if (this.closeAction) {
        this.closeAction()
      }
    }
  },
  created () {
    this.loadData()

    let countryList = document.querySelector('[name="meta-countries"]')

    if (countryList) {
      this.countryList = JSON.parse(countryList.content)
      if (!this.form.country) {
        this.form.country = this.countryList.find(
          item => item.code === 'PE'
        ).code
      }
    }
  },
  mounted () {
    if (
      this.userIsAuthenticated &&
      (!this.form.firstName || !this.form.lastName)
    ) {
      this.form.firstName = this.user.firstName
      this.form.lastName = this.user.lastName
    }
  }
}
</script>
