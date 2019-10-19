<template>
  <v-card
    :max-width='200'
    class="pa-2 d-product-minicard">
    <v-container
      fluid
      pa-0
      grid-list-lg>
      <v-layout
        row
        wrap
        align-center>
        <v-flex>
          <v-card-text class="pa-0">
            <div class="d-product__name">
              <strong>
                {{ product.name }}
              </strong>
            </div>
            <div class="d-product__price accent--text">
              <span>
                <template v-if="showFrom">Desde </template>
                <template v-if="prefixCurrency">{{ currency }} </template>
                {{ price.amount|price }}
                <template v-if="!prefixCurrency">{{ currency }}</template>
              </span>
              <small>
                <span v-if="isOnSale" class="d-pin__product-price grey--text lighten-3">
                  <del>
                    <template v-if="prefixCurrency">{{ currency }} </template>
                    {{ undiscountedPrice.amount|price }}
                    <template v-if="!prefixCurrency">{{ currency }}</template>
                  </del>
                </span>
              </small>
            </div>
          </v-card-text>
        </v-flex>
        <v-divider vertical inset class="flex shrink pa-0 ma-0"/>
        <v-flex
          shrink>
          <v-btn
            flat
            icon
            small
            class="ma-0"
            @click.stop="goToProductDetail">
            <d-icon
              name='b-right'/>
          </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<style lang="less">
.d-product-minicard {
  .d-product__name {
    font-size: 0.875rem;
  }

  .d-product__price {
    font-size: 0.785rem;
  }
}
</style>
<script>
import { STOREFRONT_PRODUCT } from '@/router/storefront'

const PEN = 'PEN'

export default {
  name: 'd-product-minicard',
  props: {
    product: {
      type: Object,
      default () {
        return {}
      }
    }
  },
  computed: {
    displayGross () {
      const { product } = this
      if (product && product.availability) {
        const { displayGross } = product.availability.priceDisplay
        return displayGross
      }

      return false
    },
    isOnSale () {
      const { product } = this
      if (product && product.availability) {
        const { onSale } = product.availability
        return onSale
      }

      return false
    },
    showFrom () {
      const { product } = this
      if (product && product.availability) {
        const lowerPrice = product.availability.priceRange.start
        const upperPrice = product.availability.priceRange.stop
        return lowerPrice.amount !== !upperPrice.amount
      }

      return false
    },
    prefixCurrency () {
      const { price } = this
      return price.currency === PEN
    },
    price () {
      const { product, displayGross } = this
      if (product && product.availability) {
        let price = product.availability.priceRange.start
        if (displayGross) {
          return price.gross
        } else {
          return price.net
        }
      }

      return {
        amount: null,
        currency: null
      }
    },
    undiscountedPrice () {
      const { product, displayGross } = this
      if (product && product.availability) {
        let price = product.availability.priceRangeUndiscounted.start
        if (displayGross) {
          return price.gross
        } else {
          return price.net
        }
      }

      return {
        amount: null,
        currency: null
      }
    },
    currency () {
      const { price } = this
      if (price.currency === PEN) {
        return 'S/'
      }

      return price.currency
    }
  },
  methods: {
    goToProductDetail () {
      this.$router.push(
        {
          name: STOREFRONT_PRODUCT,
          params: {
            id: this.product.id,
            slug: this.product.slug
          }
        }
      )
    }
  }
}
</script>
