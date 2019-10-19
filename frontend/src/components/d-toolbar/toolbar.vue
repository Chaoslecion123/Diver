<template>
  <v-toolbar app flat fixed class="d-toolbar elevation-1">
    <v-toolbar-side-icon
      v-if="$vuetify.breakpoint.smAndDown"
      @click.stop="openDrawer"/>

    <v-toolbar-title v-if="!computedActiveSearch" class="logo">
      <router-link
        :to="{
          name: links.root
        }">
        <img :src="assets.logoQuimder" />
      </router-link>
    </v-toolbar-title>
    <v-spacer v-if="!computedActiveSearch" />

    <v-toolbar-items class="d-overide">
      <d-brand-featured-menu class="mr-2" />
      <d-category-menu />
      <d-search-field @chageactive="handleActiveSearch" />
    </v-toolbar-items>

    <v-spacer
      :class="$vuetify.breakpoint.smAndDown ? 'hidden-sm-and-down' : ''"/>

    <v-toolbar-items>
      <d-cart-sumary
        v-if="$vuetify.breakpoint.mdAndUp && cart && cart.quantity > 0"
        class="mr-3"/>
      <d-cart-indicator v-else />

      <template v-if="$vuetify.breakpoint.mdAndUp">
        <d-user-menu v-if="isAuthenticated" />

        <v-btn
          v-else
          depressed
          color="accent"
          class="d-btn d-btn--rounded d-btn--no-transform d-btn--bold"
          @click.stop="openLogin">
          Iniciar sesión
        </v-btn>
      </template>
    </v-toolbar-items>
  </v-toolbar>
</template>

<style lang="less">
@import './toolbar.less';
</style>

<script>
import { mapState, mapGetters } from 'vuex'

import { STOREFRONT_CART } from '@/router/storefront'
import { ROOT } from '@/router'
import logoQuimder from '@/assets/images/quimder/logo_quimder.png'
import CartSumary from '@/components/d-cart/summary'
import CartIndicator from '@/components/d-cart/indicator'
import FeaturedMenu from '@/components/d-brand/featured-menu'

import UserMenu from './user-menu'

export default {
  name: 'd-toolbar',
  components: {
    'd-user-menu': UserMenu,
    'd-cart-sumary': CartSumary,
    'd-cart-indicator': CartIndicator,
    'd-brand-featured-menu': FeaturedMenu
  },
  data () {
    return {
      assets: {
        logoQuimder: logoQuimder
      },
      links: {
        root: ROOT,
        storefrontCart: STOREFRONT_CART
      },
      isSearchActive: false
    }
  },
  computed: {
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('cart', {
      cart: 'object'
    }),
    computedActiveSearch () {
      if (this.$vuetify.breakpoint.smAndDown) {
        return this.isSearchActive
      }
      return false
    }
  },
  methods: {
    openLogin () {
      this.$emit('openlogin')
    },
    openDrawer () {
      this.$emit('opendrawer')
    },
    handleActiveSearch (e) {
      this.isSearchActive = e
      console.log(e)
    }
  }
}
</script>
