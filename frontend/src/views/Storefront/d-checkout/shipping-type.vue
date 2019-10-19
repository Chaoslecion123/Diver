<template>
  <v-card-text>
    <v-card-title class="px-0 pt-0">
      ¿Como deseas recibir tu pedido?
    </v-card-title>
    <v-radio-group
      class="ma-0 pa-0"
      :value="shippingType"
      @change="handleChange">
      <v-radio
        v-for="shippingType in shippingTypeOptions"
        :key="shippingType.value"
        :disabled="shippingType.disabled"
        :label="shippingType.name"
        :value="shippingType.value"/>
    </v-radio-group>
  </v-card-text>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { DOOR_SHIPPING, STORE_SHIPPING } from './constants'

export default {
  name: 'd-shipping-type-selector',
  model: {
    prop: 'shippingType',
    event: 'change'
  },
  props: {
    shippingType: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      /* Step 1 */
      shippingTypeOptions: [
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
      ]
    }
  },
  computed: {
    ...mapState('cart', {
      cartToken: 'token'
    }),

    ...mapState('physical-store', {
      physicalStores: 'objects'
    })
  },
  watch: {
    physicalStores (val, oldVal) {
      if (val && val.items && val.items.length > 0) {
        this.shippingTypeOptions[1].disabled = false
      }
    }
  },
  methods: {
    ...mapActions('cart', {
      cartUpdate: 'update'
    }),

    handleChange (value) {
      this.$emit('change', value)

      this.cartUpdate({
        id: this.cartToken,
        data: {
          shippingType: value,
          shippingAddress: null,
          shippingMethod: null
        }
      })
    }
  }
}
</script>
