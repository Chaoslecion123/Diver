<template>
  <v-container fluid fill-height class="pa-0 ma-0">
    <transition mode="out-in" name="fade">
      <d-loader v-if="listingFavorites" key="loading" />
      <d-empty
        v-else-if="!listingFavorites && userHasNoFavorites"
        key="userHasNoFavorites">
        <h2 class="mb-4">
          Aún no tienes favoritos
        </h2>
        <v-btn
          :to="{ name: links.root }"
          large
          color="accent"
          :class="[
            'd-btn',
            'd-btn--no-transform',
            'd-btn--bold',
            'd-btn--rounded'
          ]">
          <d-icon :scale="1.25" class="mr-2" name="b-shopping-cart" />
          ¡Quiero comprar mis productos favoritos!
        </v-btn>
      </d-empty>

      <v-layout v-else key="order-list" row wrap class="ma-0">
        <v-flex xs12 class="pa-0">
          <v-layout row wrap>
            <v-flex xs12>
              <h2 style="font-weight: normal;">
                <d-icon name="b-enviroment-o" />
                Mis favoritos
              </h2>
              <v-divider />
            </v-flex>
            <v-flex v-for="(product, i) in favorites" :key="i" xs6 sm4 md3>
              <d-product-card :product="product" />
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </transition>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { ROOT } from '@/router'
import Loader from './d-utils/loader'
import Empty from './d-utils/empty'
// import OrderList from './d-order/list'

export default {
  name: 'AccountFavorite',
  components: {
    'd-loader': Loader,
    'd-empty': Empty
    // 'd-order-list': OrderList
  },
  data () {
    return {
      links: {
        root: ROOT
      },
      listingFavorites: false,
      query: {
        expand: 'favorite_products.brand'
      }
    }
  },
  computed: {
    ...mapState('auth', {
      currentUser: 'currentUser'
    }),
    ...mapState('product', {
      addingToFavorites: 'addingToFavorites',
      addToFavoritesSuccess: 'addToFavoritesSuccess',
      removingFromFavorites: 'removingFromFavorites',
      removeFromFavoritesSuccess: 'removeFromFavoritesSuccess'
    }),
    favorites () {
      if (
        this.currentUser &&
        this.currentUser.favoriteProducts &&
        this.currentUser.favoriteProducts.every(value => {
          return typeof value === 'object' && value !== null
        })
      ) {
        return this.currentUser.favoriteProducts
      }
      return []
    },
    userHasNoFavorites () {
      return this.favorites.length === 0
    }
  },
  methods: {
    ...mapActions('auth', {
      getAutenticatedUser: 'getAutenticatedUser'
    }),
    ...mapActions('product', {
      addToFavorites: 'addToFavorites',
      removeFromFavorites: 'removeFromFavorites'
    })
  },
  created () {
    this.getAutenticatedUser({ query: this.query })
  }
}
</script>
