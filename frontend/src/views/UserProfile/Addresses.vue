<template>
  <v-flex
    xs12 md10 pl-3
    style="font-size:14px;"
    class="remove-padding d-overide">
    <v-card
      class="py-2 px-3 mb-3"
      flat
      color="grey lighten-4">
      <v-layout row wrap align-center>
        <v-flex
          xs6
          style="font-size:1.25rem;"
          class="font-weight-600">
          Mis Direcciones
        </v-flex>
        <v-spacer/>
        <v-flex xs5 sm3>
          <v-btn
            style="height:32px;"
            class="my-0 border-radius"
            color="grey darken-4"
            depressed
            block
            dark
            @click="openAddNewAddress">
            Añadir dirección
          </v-btn>
        </v-flex>
      </v-layout>
    </v-card>

    <d-popup
      v-model="addNewAddressPopupIsOpen"
      width="800"
      :onOk="addNewAddress">
      <div>NUEVA DIRECCIÓN</div>
      <v-container fluid pa-0 grid-list-lg slot="content">
        <v-form
          lazy-validation
          ref="addAddressForm">
          <v-layout>
            {{ createAddressMessages }}
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Nombre
              </v-flex>
              <v-text-field
                v-model="firstName"
                class="border-radius"
                :rules="[rules.required]"
                outline
                flat
                required
                type="text"/>
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Apellido
              </v-flex>
              <v-text-field
                v-model="lastName"
                class="border-radius"
                :rules="[rules.required]"
                outline
                flat
                required
                type="text"/>
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Nombre de empresa
              </v-flex>
              <v-text-field
                v-model="companyName"
                class="border-radius"
                :rules="[rules.required]"
                outline
                flat
                required
                type="text"/>
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                País
              </v-flex>
              <v-autocomplete
                v-model="country"
                ref="country"
                :rules="[() => !!country || 'Este campo es requerido.' ]"
                append-icon="expand_more"
                :items="countryList"
                outline
                flat />
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Provincia
              </v-flex>
              <v-autocomplete
                v-model="city"
                ref="city"
                :rules="[() => !!city || 'Este campo es requerido.' ]"
                append-icon="expand_more"
                :items="provinces"
                outline
                flat />
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Dirección
              </v-flex>
              <v-text-field
                v-model="street1"
                class="border-radius"
                :rules="[rules.required]"
                outline
                flat
                required />
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Dirección complementaria / Referencia
              </v-flex>
              <v-text-field
                v-model="street2"
                class="border-radius"
                placeholder="ej: Dpto. 504 / Cerca a tienda X"
                :rules="[rules.required]"
                outline
                flat
                required />
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Distrito
              </v-flex>
              <v-text-field
                v-model="cityArea"
                class="border-radius"
                :rules="[rules.required]"
                outline
                flat
                required />
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Código postal
              </v-flex>
              <v-text-field
                v-model="postalCode"
                class="border-radius"
                mask="############"
                outline
                flat
                type="text" />
            </v-flex>
            <v-flex xs12 sm6 py-0>
              <v-flex px-0 py-1>
                Teléfono
              </v-flex>
              <v-text-field
                v-model="phone"
                class="border-radius"
                placeholder="ej: +51 987654321"
                :rules="[rules.required]"
                outline
                flat
                hide-details
                required
                type="text" />
            </v-flex>
          </v-layout>
        </v-form>
      </v-container>
      <div slot="button">Guardar dirección</div>
    </d-popup>

    <v-card flat>
      <v-container grid-list-md pa-0>
        <v-layout row wrap>
          <v-flex
            xs6 sm4 md3
            class="settings-card">
            <v-card
              v-for="(address, i) in address.items"
              :key="i"
              class="pa-3 border-radius fill-height"
              flat
              color="grey lighten-4">
              <v-container fluid pa-0 grid-list-md>
                <v-layout row wrap>
                  <v-flex xs12>
                    <span v-if="address.firstName"> {{address.firstName}} </span>
                    <span v-if="address.lastName"> {{address.lastName}} </span>
                  </v-flex>
                  <v-flex xs12 v-if="address.companyName">
                    {{address.companyName}}
                  </v-flex>
                  <v-flex xs12>
                    <span v-if="address.streetAddress1"> {{address.streetAddress1}} </span>
                    <span v-if="address.streetAddress2"> {{address.streetAddress2}} </span>
                  </v-flex>
                  <v-flex xs12 v-if="address.cityArea">
                    {{address.cityArea}}
                  </v-flex>
                  <v-flex xs12 v-if="address.city">
                    {{address.city}}
                  </v-flex>
                  <v-flex xs12 v-if="address.postalCode">
                    {{address.postalCode}}
                  </v-flex>
                  <v-flex xs12 v-if="address.phone">
                    {{address.phone}}
                  </v-flex>
                  <v-flex xs12 v-if="address.country">
                    {{address.country}}
                  </v-flex>
                  <v-btn :ripple="false" icon absolute class="close-btn">
                    <d-icon class="q-red--text" scale="1.25" name="b-close"/>
                  </v-btn>
                  <v-btn @click="addNewAddress=!addNewAddress" :ripple="false" icon absolute class="edit-btn">
                    <d-icon
                      name="b-edit"/>
                  </v-btn>
                </v-layout>
              </v-container>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>

    <v-card
      v-if="!address.items"
      flat
      class="pa-3 mb-3"
      color="grey lighten-4">
      <v-container>
        <v-layout  align-center justify-center text-xs-center>
          <v-flex xs8 sm7>
            <d-icon
              class="coupon-icon"
              name="b-flag"
              scale="5"/>
            <v-flex style="font-size: 1.25rem;">
              En cuanto los tengas, aquí podrás consultarlos para
              aplicarlos en tus compras
            </v-flex>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>

  </v-flex>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'UserAdresses',
  data () {
    return {
      addNewAddressPopupIsOpen: false,
      firstName: '',
      lastName: '',
      companyName: '',
      country: '',
      city: '',
      street1: '',
      street2: '',
      cityArea: '',
      postalCode: '',
      phone: '',
      countryList: ['AR', 'BO', 'BR', 'CH', 'CO', 'EC', 'PE'],
      provinces: ['Amazonas', 'Ayacucho', '...'],
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        min: v =>
          (v && v.length >= 8) ||
          'La contraseña debe tener al menos 8 caracteres'
      }
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('address', {
      address: 'objects'
    }),
    ...mapState('address', {
      createAddressSuccess: 'createSuccess',
      createAddressMessages: 'createMessages',
      createAddressError: 'createError'
    }),
    userId () {
      if (this.user) {
        return this.user.id
      }
      return null
    }
  },
  watch: {
    createAddressSuccess (val, oldVal) {
      if (val) {
        this.addNewAddressPopupIsOpen = false
        this.$refs.addAddressForm.reset()
        this.getAddressList()
      }
    },
    createAddressError (val, oldVal) {
      if (val) {
        this.addNewAddressPopupIsOpen = true
      }
    }
  },
  methods: {
    ...mapActions('address', {
      createAddress: 'create'
    }),
    ...mapActions('address', {
      getAddressList: 'list'
    }),
    openAddNewAddress () {
      this.addNewAddressPopupIsOpen = true
    },
    addNewAddress () {
      if (this.$refs.addAddressForm.validate() && this.isAuthenticated) {
        // this.addNewAddressPopupIsOpen = false

        const newAddress = {
          user: this.userId,
          firstName: this.firstName,
          lastName: this.lastName,
          companyName: this.companyName,
          country: this.country,
          city: this.city,
          street1: this.streetAddress1,
          street2: this.streetAddress2,
          // cityArea: this.cityArea,
          postalCode: this.postalCode,
          phone: this.phone
        }

        this.createAddress({
          data: newAddress
        })
      }
    }
  },
  created () {
    this.getAddressList()
  }
  /*   delAddress (i) {
      this.$delete(this.content.collection, i)
    } */
}
</script>
