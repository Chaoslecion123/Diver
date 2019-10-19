<template>
  <v-menu
    :value="isActive"
    open-on-hover
    offset-y
    left
    :nudge-top="$vuetify.breakpoint.mdAndUp ? -9 : -5">
    <template slot="activator">
      <d-card-indicator />
    </template>

    <v-card class="d-cart-summary-popup">
      <v-card-text class="d-cart-summary-popup--content">
        <v-list two-line class="d-cart-summary-popup--content-list pa-0">
          <template v-for="(line, order) in cart.lines">
            <v-list-tile v-if="line" :key="`item-${order}`">
              <v-list-tile-avatar v-if="line.variant && line.variant.image">
                <img :src="line.variant.image.image.productSmall" />
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title
                  v-if="line.variant && line.variant.displayName">
                  {{ line.variant.displayName }}
                </v-list-tile-title>
                <v-list-tile-sub-title>
                  {{ line.quantity }}
                  {{ line.quantity === 1 ? 'unidad' : 'unidades' }}
                </v-list-tile-sub-title>
              </v-list-tile-content>

              <v-list-tile-action
                v-if="line.variant && line.variant.price"
                class="ml-4">
                S/
                <template
                  v-if="line.variant && line.variant.priceDisplay.displayGross">
                  {{
                    formatPrice(line.quantity * line.variant.price.gross.amount)
                  }}
                </template>
                <template v-else>
                  {{
                    formatPrice(line.quantity * line.variant.price.net.amount)
                  }}
                </template>
              </v-list-tile-action>
            </v-list-tile>
            <v-divider :key="`divider-${order}`" />
          </template>
        </v-list>
        <v-list class="pa-0">
          <v-list-tile>
            <v-list-tile-avatar> </v-list-tile-avatar>
            <v-list-tile-content>
              Total
            </v-list-tile-content>
            <v-list-tile-action class="ml-4">
              S/ {{ subtotalAmount | price }}
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-card-text>
      <v-card-text>
        <v-container grid-list-lg pa-0>
          <v-layout>
            <v-flex xs6>
              <v-btn
                block
                outline
                color="accent"
                :class="[
                  'ma-0',
                  'd-btn',
                  'd-btn--rounded',
                  'd-btn--bold',
                  'd-btn--no-transform'
                ]"
                @click="goToCart">
                Ver mi carrito
              </v-btn>
            </v-flex>
            <v-flex xs6>
              <v-btn
                block
                depressed
                color="accent"
                :class="[
                  'ma-0',
                  'd-btn',
                  'd-btn--rounded',
                  'd-btn--bold',
                  'd-btn--no-transform'
                ]"
                @click="goToCheckout">
                Ir a pagar
              </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<style lang="less">
.d-cart-summary-popup {
  max-width: 380px;
  .d-cart-summary-popup--content {
    .v-list__tile {
      padding: 0;
    }
  }
  .d-cart-summary-popup--content-list {
    max-height: 219px;
    overflow-y: auto;
  }
}
</style>

<script>
import { mapState, mapGetters } from 'vuex'
import { STOREFRONT_CART, STOREFRONT_CART_CHECKOUT } from '@/router/storefront'

import CardIndicator from './indicator'

export default {
  name: 'd-checkout-summary',
  components: {
    'd-card-indicator': CardIndicator
  },
  data () {
    return {
      timer: null,
      isActive: false
    }
  },
  computed: {
    ...mapState('cart', {
      cart: 'object',
      cartReadSuccess: 'readSuccess'
    }),
    ...mapState('product', {
      addToCartSuccess: 'addToCartSuccess'
    }),
    ...mapGetters('cart', {
      totalAmount: 'totalAmount',
      subtotalAmount: 'subtotalAmount'
    })
  },
  watch: {
    cartReadSuccess (val, oldVal) {
      if (val) {
        if (this.addToCartSuccess) {
          this.isActive = true && this.$route.name !== STOREFRONT_CART_CHECKOUT

          if (this.timer === null && this.isActive) {
            this.timer = setTimeout(() => {
              this.timer = null
              this.isActive = false
            }, 2000)
          }
        }
      }
    }
  },
  methods: {
    formatPrice (value) {
      let val = (value / 1).toFixed(2) // .replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
    },

    goToCart () {
      this.$router.push({
        name: STOREFRONT_CART
      })
    },

    goToCheckout () {
      this.$router.push({
        name: STOREFRONT_CART_CHECKOUT
      })
    }
  }
}
</script>
