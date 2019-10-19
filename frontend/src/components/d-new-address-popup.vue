<template>
  <d-popup
    v-model="newAddress"
    width="800"
    :onOk="onOk">
    <div>NUEVA DIRECCIÓN</div>
    <v-container fluid pa-0 grid-list-lg slot="content" class="d-overide">
      <v-form ref="addressForm" lazy-validation >
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
              type="text"></v-text-field>
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
              type="text"></v-text-field>
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
              type="text"></v-text-field>
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
              required
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
              dpto./ int/ referencia (opcional)
            </v-flex>
            <v-text-field
              v-model="street2"
              class="border-radius"
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
              mask="##################"
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
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'd-new-address-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    },
    onOk: {
      default: () => { }
    }
  },
  data () {
    return {
      newAddress: this.value,
      firstName: '',
      lastName: '',
      companyName: '',
      city: '',
      street1: '',
      street2: '',
      cityArea: '',
      postalCode: '',
      phone: '',
      provinces: [
        'Amazonas',
        'Áncash',
        'Apurímac',
        'Arequipa',
        'Ayacucho',
        'Cajamarca',
        'Cusco',
        'Huancavelica',
        'Huánuco',
        'Ica',
        'Junín',
        'La Libertad',
        'Lambayeque',
        'Lima',
        'Loreto',
        'Madre de Dios',
        'Moquegua',
        'Pasco',
        'Piura',
        'Puno',
        'San Martín',
        'Tacna',
        'Tumbes',
        'Ucayali'
      ],
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        min: v => (v && v.length >= 8) || 'La contraseña debe tener al menos 8 caracteres'
      }
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapState('address', {
      createAddressSuccess: 'createSuccess'
    }),
    userId () {
      if (this.user) {
        return this.user.id
      }
      return null
    }
  },
  watch: {
    value () {
      this.newAddress = this.value
    },
    newAddress () {
      this.$emit('input', this.newAddress)
    }
  }
}
</script>
