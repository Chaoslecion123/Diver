<template>
  <v-card-text>
    <v-card-title
      class="px-0 pt-0">
      ¿Que tipo de comprobante de pago necesita?
    </v-card-title>
    <v-radio-group
      class="ma-0 pa-0"
      :value="billingType"
      @change="handleChange">
      <v-radio
        v-for="billingType in billingTypeOptions"
        :key="billingType.value"
        :disabled="billingType.disabled"
        :label="billingType.name"
        :value="billingType.value"/>
    </v-radio-group>
  </v-card-text>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { BALLOT, FACTURE } from './constants'

export default {
  name: 'd-billing-type-selector',
  model: {
    prop: 'billingType',
    event: 'change'
  },
  props: {
    billingType: {
      type: String,
      default: null
    }
  },
  data () {
    return {
      /* Step 1 */
      billingTypeOptions: [
        {
          name: 'Una boleta está bien.',
          disabled: false,
          value: BALLOT
        },
        {
          name: 'Requiero una factura.',
          disabled: false,
          value: FACTURE
        }
      ]
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

    handleChange (value) {
      this.$emit('change', value)

      this.cartUpdate({
        id: this.cartToken,
        data: {
          billingType: value,
          billingAddress: null
        }
      })
    }
  }
}
</script>
