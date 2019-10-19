<template>
  <v-btn
    flat
    depresed
    class="d-btn d-btn--circle"
    active-class=""
    @click="goToCart">
    <v-badge overlap bottom color="error">
      <span slot="badge">
        {{ cart ? cart.quantity : 0 }}
      </span>
      <d-icon scale="1.5" name="b-shopping-cart" />
    </v-badge>
  </v-btn>
</template>

<style lang="less">
.cart-summary {
  &.popup {
    max-width: 280px;
  }
}
</style>

<script>
import { mapState } from 'vuex'
import { STOREFRONT_CART } from '@/router/storefront'

export default {
  name: 'd-checkout-summary',
  computed: {
    ...mapState('cart', {
      cart: 'object'
    })
  },
  methods: {
    goToCart () {
      this.$router.push({
        name: STOREFRONT_CART
      })
    }
  }
}
</script>
