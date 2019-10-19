<template>
  <v-card class="pa-3 d-shoping-cart-summary" flat color="grey lighten-4">
    <template v-if="cart == true">
      <v-btn
        block
        depressed
        dark
        large
        class="mb-3"
        color="accent"
        :disabled="cartLineDeleting || cartReading"
        @click="makePurchase">
        <strong>
          Comprar
        </strong>
        <v-spacer></v-spacer>
        <d-icon icon right name="b-arrow-right" />
      </v-btn>
    </template>

    <h3 class="mb-3">
      RESUMEN DEL PEDIDO:
    </h3>

    <v-card class="pa-3" flat>
      <v-layout row wrap>
        <v-flex shrink>
          # de productos:
        </v-flex>
        <v-spacer />
        <v-flex shrink>
          {{ shopingCart ? shopingCart.quantity : 0 }}
        </v-flex>
      </v-layout>
      <v-divider class="my-2" />
      <v-layout row wrap>
        <v-flex shrink>
          Precio inicial:
        </v-flex>
        <v-spacer />
        <v-flex shrink> S/ {{ subtotalAmount | price }} </v-flex>
      </v-layout>
      <v-layout
        v-if="
          shopingCart &&
            shopingCart.shippingMethod &&
            shopingCart.shippingMethod.price
        "
        row
        wrap>
        <v-flex shrink>
          Envío:
        </v-flex>
        <v-spacer />
        <v-flex shrink>
          S/ {{ shopingCart.shippingMethod.price.amount | price }}
        </v-flex>
      </v-layout>

      <v-layout
        v-if="
          shopingCart &&
            shopingCart.discountAmount &&
            shopingCart.discountAmount.amount > 0 &&
            shopingCart.discountName !== ''
        "
        row
        wrap>
        <v-flex shrink>
          <div>Descuento:</div>
          <div>({{ shopingCart.discountName }})</div>
        </v-flex>
        <v-spacer />
        <v-flex shrink>
          S/ -{{ shopingCart.discountAmount.amount | price }}
        </v-flex>
      </v-layout>

      <v-layout row wrap>
        <v-flex shrink>
          <strong>
            TOTAL:
          </strong>
        </v-flex>
        <v-spacer />
        <v-flex shrink> S/ {{ totalAmount | price }} </v-flex>
      </v-layout>
    </v-card>
    <template v-if="showCodeForm">
      <v-layout row wrap>
        <v-flex xs12>
          <v-text-field
            v-model="voucherCode"
            placeholder="Código promocional"
            solo
            flat
            :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
            hide-details/>
        </v-flex>
        <v-flex xs12 pt-0>
          <v-btn
            block
            depressed
            large
            color="accent"
            :class="[
              'ma-0',
              'px-3',
              'd-btn',
              'd-btn--rounded',
              'd-btn--bold',
              'd-btn--no-transform'
            ]"
            :style="{ 'min-width': 'auto' }"
            @click="makeDiscount">
            Aplicar codigo
          </v-btn>
        </v-flex>
      </v-layout>
    </template>
  </v-card>
</template>

<style lang="less"></style>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'
import { STOREFRONT_CART_CHECKOUT } from '@/router/storefront'

export default {
  name: 'd-checkout-sumary',
  props: {
    cart: {
      type: Boolean,
      default: false
    },
    ordered: {
      type: Boolean,
      default: false
    },
    showCodeForm: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      voucherCode: '',
      cartQuery: {
        expand: ['lines.variant.image', 'shipping_method'].join(','),
        fields: [
          'token',
          'user',
          'created',
          'lines',
          'email',
          'quantity',
          'shipping_address',
          'shipping_method',
          'shipping_type',

          'billing_address',
          'billing_type',

          'discount_amount',
          'discount_name',
          'voucher_code',

          'applicable_shipping_methods'
        ].join(',')
      }
    }
  },
  computed: {
    ...mapState('cart', {
      shopingCart: 'object',
      cartReading: 'reading',
      discountSuccess: 'discountSuccess'
    }),
    ...mapState('cart-line', {
      cartLineDeleting: 'deleting'
    }),
    ...mapGetters('cart', {
      totalAmount: 'totalAmount',
      subtotalAmount: 'subtotalAmount'
    })
  },
  watch: {
    discountSuccess (val, oldVal) {
      console.log(val)
    }
  },
  methods: {
    ...mapActions('cart', {
      readCart: 'read',
      applyDiscount: 'applyDiscount'
    }),

    makePurchase () {
      this.$router.push({
        name: STOREFRONT_CART_CHECKOUT
      })
    },
    makeDiscount () {
      this.applyDiscount({
        id: this.shopingCart.token,
        data: {
          voucher: this.voucherCode
        }
      })
    }
  }
}
</script>
