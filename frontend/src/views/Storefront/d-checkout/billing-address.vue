<template>
  <v-card-text>
    <v-card-title class="px-0 pt-0">
      ¿A qué dirección consignamos tu comprobante de pago?
    </v-card-title>

    <v-layout row wrap fill-height>
      <v-flex
        v-for="address in addresses"
        :key="address.id"
        :value="address.id"
        xs12
        sm6
        md4
        lg4
        xl3>
        <d-address-card
          :class="[
            'd-card',
            'd-card--outline',
            'd-card--rounded',
            'address-selector__item',
            {
              active: billingAddress === address.id
            }
          ]"
          allowEdit
          :address="address"
          @click="handleChange(address.id)"/>
      </v-flex>

      <v-flex pt-0 xs12>
        <v-btn
          outline
          color="accent"
          :block="$vuetify.breakpoint.xs"
          :class="[
            'ma-0',
            'd-btn',
            'd-btn--rounded',
            'd-btn--bold',
            'd-btn--no-transform'
          ]"
          @click="openPopup">
          <d-icon class="mr-2" name="b-plus-circle-o" />
          Nueva dirección
        </v-btn>
      </v-flex>

      <d-address-popup v-model="addressPopupIsOpen" />
    </v-layout>
  </v-card-text>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'd-billing-type-selector',
  components: {
    'd-address-card': () => import('@/components/d-address/card'),
    'd-address-popup': () => import('@/components/d-address/popup')
  },
  model: {
    prop: 'billingAddress',
    event: 'change'
  },
  props: {
    addresses: {
      type: Array,
      default () {
        return []
      }
    },
    billingAddress: {
      type: Number,
      default: null
    }
  },
  data () {
    return {
      addressPopupIsOpen: false
    }
  },
  computed: {
    ...mapState('cart', {
      cartToken: 'token'
    })
  },
  methods: {
    ...mapActions('cart', {
      cartUpdate: 'update'
    }),

    openPopup () {
      this.addressPopupIsOpen = true
    },

    handleChange (value) {
      this.$emit('change', value)
      this.cartUpdate({
        id: this.cartToken,
        data: {
          billingAddress: value,
          billingMethod: null
        }
      })
    }
  }
}
</script>
