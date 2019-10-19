<template>
  <v-btn
    v-if="product"
    icon
    absolute
    right
    :ripple="false"
    class="ma-0 d-product-card__favorite-indicator"
    @click.stop="handleClick">
    <d-icon
      scale="1.5"
      :name="isFavorite ? 'b-heart-fill' : 'b-heart'"
      :class="isFavorite ? 'heart-filled__icon' : 'heart__icon'"/>
    <d-login-popup v-model="showLogin" />
    <v-snackbar
      v-model="showSnackbar"
      right
      :top="$vuetify.breakpoint.mdAndUp"
      :bottom="$vuetify.breakpoint.smAndDown"
      :style="{
        textTransform: 'none'
      }"
      @click.stop="() => {}">
      Has agregado "{{ product.name }}" a tus favoritos
      <v-btn color="pink" flat @click="showSnackbar = false">
        <d-icon name="b-close" />
      </v-btn>
    </v-snackbar>
  </v-btn>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'

export default {
  name: 'd-product-favorite-mark',
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      showLogin: false,
      showSnackbar: false,
      clickOnThis: false
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('product', {
      addingToFavorites: 'addingToFavorites',
      addToFavoritesSuccess: 'addToFavoritesSuccess',
      removingFromFavorites: 'removingFromFavorites',
      removeFromFavoritesSuccess: 'removeFromFavoritesSuccess'
    }),
    isFavorite () {
      let { product, user } = this

      if (product && product.id && (user && user.favoriteProducts)) {
        return (
          user.favoriteProducts.includes(product.id) ||
          user.favoriteProducts.find(item => item.id === product.id)
        )
      }

      return false
    }
  },
  watch: {
    isAuthenticated (val, oldVal) {
      if (val && !oldVal && this.clickOnThis) {
        let { product } = this
        this.addToFavorites({
          id: product.id
        })
      }
    },
    addToFavoritesSuccess (val, oldVal) {
      if (val && this.clickOnThis) {
        this.getAutenticatedUser()
        this.showSnackbar = true
      }
    },
    removeFromFavoritesSuccess (val, oldVal) {
      if (val && this.clickOnThis) {
        this.getAutenticatedUser()
      }
    },
    addingToFavorites (val, oldVal) {
      if (!val && oldVal && this.clickOnThis) {
        this.clickOnThis = false
      }
    },
    removingFromFavorites (val, oldVal) {
      if (!val && oldVal && this.clickOnThis) {
        this.clickOnThis = false
      }
    }
  },
  methods: {
    ...mapActions('auth', {
      getAutenticatedUser: 'getAutenticatedUser'
    }),
    ...mapActions('product', {
      addToFavorites: 'addToFavorites',
      removeFromFavorites: 'removeFromFavorites'
    }),
    handleClick () {
      this.clickOnThis = true

      let {
        isAuthenticated,
        isFavorite,
        product,
        addingToFavorites,
        removingFromFavorites
      } = this

      if (!addingToFavorites && !removingFromFavorites) {
        if (isAuthenticated) {
          if (isFavorite) {
            this.removeFromFavorites({
              id: product.id
            })
          } else {
            this.addToFavorites({
              id: product.id
            })
          }
        } else {
          this.showLogin = true
        }
      }
    }
  }
}
</script>
