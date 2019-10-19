<template>
  <v-content app class="d-page__content">
    <v-container id="section__profile" class="mt-5 mb-5 d-overide" grid-list-md>
      <v-layout row wrap>
        <v-flex xs12 mb-4>
          <h2 class="text-uppercase">
            Mi cuenta
          </h2>
        </v-flex>

        <v-flex xs12 md2 class="hidden-sm-and-down">
          <v-container fluid ma-0 pa-0>
            <v-layout
              row
              wrap
              align-center
              v-for="(item, i) in content.profile"
              :key="i">
              <v-flex xs12 my-2>
                <router-link
                  style="font-size: 0.875rem;"
                  class="profile_tabs"
                  :to="item.to">
                  <d-icon class="profile-icon mr-2" :name="item.icon" />
                  {{ item.name }}
                </router-link>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>

        <router-view name="helper" />
      </v-layout>
    </v-container>
  </v-content>
</template>

<style lang="less">
#section__profile {
  .profile-icon {
    vertical-align: bottom;
    height: 20px;
    width: 20px;
  }
  .d-divider--right {
    border-right: 1px solid;
  }
  .profile_tabs {
    text-decoration: none;
    color: #000;
    &:hover {
      color: #f58220 !important;
    }
  }
  .v-text-field {
    .v-input__slot {
      min-height: auto;
      border-radius: 5px;
      border: 1px solid #000;
    }
  }
  .v-text-field.v-text-field--enclosed .v-text-field__details {
    margin-bottom: 4px;
  }
  .v-label {
    font-size: 14px;
    color: black;
  }
  .v-input {
    margin: 0 !important;
    padding: 0;
  }
  input {
    font-size: 14px !important;
  }
  .v-input--checkbox {
    .v-input__slot {
      margin: 0;
    }
    .v-messages {
      display: none;
    }
  }
}

@media only screen and (max-width: 600px) {
  #section__profile {
    .d-divider--right {
      border-right: none;
    }
  }
}
</style>

<script>
import { mapState } from 'vuex'
import {
  PROFILE_SETTINGS,
  PROFILE_ADDRESSES,
  PROFILE_BILLS,
  PROFILE_TRACKING,
  PROFILE_ORDERS,
  PROFILE_COUPONS
} from '@/router/user-profile'
import zapatillas02 from '../../assets/images/zapatillas02.png'
import mochila01 from '../../assets/images/mochila01.png'
import polera01 from '../../assets/images/polera01.png'
import pantalon01 from '../../assets/images/pantalon01.png'

export default {
  name: 'UserProfile',
  data () {
    return {
      assets: {
        zapatillas02: zapatillas02,
        mochila01: mochila01,
        polera01: polera01,
        pantalon01: pantalon01
      },
      /* email: '',
      show: false,
      password: 'Contraseña',

      rules: {
        required: value => !!value || 'Este campo es requerido.',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Email inválido'
        },
        min: v => v.length >= 8 || 'La contraseña debe tener al menos 8 caracteres',
        ruc: v => v.length >= 11 || 'EL RUC debe tener al 11 caracteres'
      },

      date: new Date().toISOString().substr(0, 10),
      modal: false,
      gender: "null", */
      content: {
        // items: [
        //   {
        //     text: 'Mi cuenta',
        //     disabled: false,
        //     to: ''
        //   },
        //   {
        //     text: 'Datos personales',
        //     disabled: true,
        //     to: ''
        //   },
        //   {
        //     text: 'Mi cuenta',
        //     disabled: true,
        //     to: ''
        //   }
        // ],
        profile: {
          1: {
            icon: 'b-user',
            name: 'Datos personales',
            to: { name: PROFILE_SETTINGS }
          },
          2: {
            icon: 'b-flag',
            name: 'Mis Direcciones',
            to: { name: PROFILE_ADDRESSES }
          },
          3: {
            icon: 'b-file-text',
            name: 'Mis Facturas',
            to: { name: PROFILE_BILLS }
          },
          4: {
            icon: 'b-card',
            name: 'Mis Tarjetas',
            to: ''
          },
          5: {
            icon: 'b-location',
            name: 'Tracking',
            to: { name: PROFILE_TRACKING }
          },
          6: {
            icon: 'b-gift',
            name: 'Mis Pedidos',
            to: { name: PROFILE_ORDERS }
          },
          7: {
            icon: 'b-barcode',
            name: 'Mis cupones',
            to: { name: PROFILE_COUPONS }
          }
        }
        /* addresses: {
          1: {
            contactName: "Sheyla Breña",
            addressHome: "Huertos de Manchay, MZ C Lt 19",
            addressProvince: "Lima",
            addressPostCode: "12123",
            addressCountry: "Perú",
            contactNumber: "963353141"
          },
          2: {
            contactName: "Sheyla Breña",
            addressHome: "Huertos de Manchay, MZ C Lt 19",
            addressProvince: "Lima",
            addressPostCode: "12123",
            addressCountry: "Perú",
            contactNumber: "963353141"
          }
        }, */
        /*         ourProducts: {
          categoryProduct: {
            1: {
              product: zapatillas02,
              brandTagColor: 'purple',
              brand: 'Nike Perú',
              productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
              finalPrice: '559.12',
              discount: true,
              previousPrice: '420'
            },
            2: {
              product: mochila01,
              brandTagColor: 'pink',
              brand: 'Porta Perú',
              productDescription: 'Mochila negra Porta',
              finalPrice: '75.99',
              previousPrice: ''
            },
            3: {
              product: polera01,
              brandTagColor: 'brown',
              brand: 'Adidas Perú',
              productDescription: 'Polera Gris deportiva damas',
              finalPrice: '85',
              previousPrice: ''
            },
            4: {
              product: pantalon01,
              brand: 'ELLE',
              brandTagColor: 'green',
              productDescription: 'Pantalón azul marino para caballeros',
              finalPrice: '85',
              previousPrice: ''
            }
          }
        } */
      }
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser',
      isAuthenticated: 'isAuthenticated'
    })
  },
  methods: {
    addToChart () {
      alert('Has agregado un producto al carrito :D')
    }
  }
}
</script>
