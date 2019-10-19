<template>
  <v-card-text>
    <v-card-title class="px-0 pt-0">
      ¿Cómo quieres que te envíemos el pedido?
    </v-card-title>
    <v-layout row wrap fill-height>
      <template
        v-if="applicableShippingMethods && applicableShippingMethods.length">
        <v-flex
          v-for="applicableShippingMethod in applicableShippingMethods"
          :key="applicableShippingMethod.id"
          :value="applicableShippingMethod.id"
          xs12
          sm6
          md4
          lg4
          xl3>
          <v-card
            flat
            :class="[
              'd-card',
              'd-card--outline',
              'd-card--rounded',
              'd-card--fill-height',
              'address-selector__item',
              {
                active: shippingMethod === applicableShippingMethod.id
              }
            ]"
            @click="handleChange(applicableShippingMethod.id)">
            <v-card-text>
              <div :class="['address-selector__item-name']">
                <strong>{{ applicableShippingMethod.name }}</strong>
              </div>
              <template v-if="applicableShippingMethod.price.currency === 'PEN'">S/
              </template>
              {{ applicableShippingMethod.price.amount | price }}
              <template
                v-if="applicableShippingMethod.price.currency !== 'PEN'">
                {{ applicableShippingMethod.price.currency }}</template>
            </v-card-text>
          </v-card>
        </v-flex>
      </template>
      <v-flex v-else>
        No podemos repartir a tu zona de entrega :(
      </v-flex>
    </v-layout>
  </v-card-text>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'd-shipping-type-selector',
  model: {
    prop: 'shippingMethod',
    event: 'change'
  },
  props: {
    shippingMethod: {
      type: Number,
      default: null
    }
  },
  data () {
    return {}
  },
  computed: {
    ...mapState('cart', {
      cartToken: 'token'
    }),

    ...mapState('cart', {
      cart: 'object'
    }),

    applicableShippingMethods () {
      if (this.cart && this.cart.applicableShippingMethods) {
        return this.cart.applicableShippingMethods
      }

      return []
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
          shippingMethod: value
        }
      })
    }
  }
}
</script>
