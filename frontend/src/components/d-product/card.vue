<template>
  <v-card
    v-if="product"
    class="d-product-card"
    flat
    hover
    @click.stop="goToProductDetail">
    <!--
      Badge for sale offers
    -->
    <span v-if="isOnSale" class="d-product-card__tag" style="z-index: 1;">
      Oferta
    </span>

    <!--
      Badge for new product
    -->
    <span
      v-else-if="product.is_new"
      class="d-product-card__tag"
      style="z-index: 1;">
      Nuevo
    </span>

    <!--
      Add to favorite
    -->
    <d-favorite-mark :product="product" />

    <!--
      Product image
    -->
    <v-container pa-4 class="d-product-card__image grey lighten-3">
      <v-img
        v-if="product.image"
        contain
        height="100%"
        :src="product.image.image.productList">
      </v-img>
      <!--
        Product geolocation image
      -->
      <!-- v-btn
        small
        icon
        absolute
        right
        color="#8fff8b"
        class="d-location--btn"
        style="z-index: 1;">
        <d-icon
          name="b-location"/>
      </v-btn -->
    </v-container>

    <!--
      Product title
    -->
    <v-card-text class="pb-0">
      <d-brand-badge :brand="product.brand" />

      <strong>
        {{ product.name }}
      </strong>
    </v-card-text>

    <!--
      Product price detail
    -->
    <v-card-text class="pt-1">
      <div v-if="showFrom">
        <small>
          Desde
        </small>
      </div>
      <h4
        :class="{
          'accent--text': isOnSale
        }">
        {{ price | moneyFormat }}
      </h4>
      <div v-if="isOnSale" class="grey--text lighten-3">
        <small>
          <del>
            {{ undiscountedPrice | moneyFormat }}
          </del>
        </small>
      </div>

      <!--
        Shoping cart button
      -->
      <v-btn
        icon
        absolute
        right
        :ripple="false"
        class="ma-0 d-product-card__cart-indicator">
        <d-icon scale="1.5" class="accent--text" name="b-shopping-cart" />
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<style lang="less">
.d-product-card {
  border: 1px solid #eee !important;
  position: relative;
  border-radius: 4px;
  height: 100%;

  .d-product-card__tag {
    height: 24px;
    line-height: 24px;
    position: absolute;
    top: -12px;
    left: 12px;
    color: white;
    background-color: red;
    padding: 0 8px;
    border-radius: 4px !important;
  }

  .d-product-card__image {
    border-radius: 4px 4px 0 0;
    position: relative;
    overflow: hidden;
    height: 200px;
  }

  .d-product-card__cart-indicator {
    position: absolute;
    bottom: 16px;
    right: 16px;
    z-index: 1;
  }

  .d-product-card__favorite-indicator {
    position: absolute;
    z-index: 1;
    right: 16px;
    top: 16px;
  }

  .heart__icon {
    &:hover {
      color: red;
    }
  }

  .heart-filled__icon {
    color: red !important;
  }

  .v-card__title {
    background-color: #ffffff;
  }

  .card-image {
    position: relative;
    height: 200px;
  }
}

.card-image {
  position: relative;
}
</style>

<script>
import { mapGetters } from 'vuex'
import { STOREFRONT_PRODUCT } from '@/router/storefront'
import FavoriteMark from './favorite-mark'
import BrandBadge from './brand-badge'

export default {
  name: 'd-product-card',
  components: {
    'd-favorite-mark': FavoriteMark,
    'd-brand-badge': BrandBadge
  },
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      favoritePopupIsOpen: false,
      isLiked: false
    }
  },
  computed: {
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),

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
    }
  },
  methods: {
    goToProductDetail () {
      this.$router.push({
        name: STOREFRONT_PRODUCT,
        params: {
          id: this.product.id,
          slug: this.product.slug
        }
      })
    },

    makeFavorite () {
      if (!this.isLiked) {
        this.favoritePopupIsOpen = true
      } else {
        this.isLiked = false
      }
    },

    addToFavorites () {
      this.favoritePopupIsOpen = false

      if (this.isAuthenticated) {
        this.isLiked = true
      } else {
        this.$router.push({ name: this.$route.name, query: { login: true } })
      }
    }
  }
}
</script>
