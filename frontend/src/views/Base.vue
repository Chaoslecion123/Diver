<template>
  <v-app app id="app" class="d-page d-view">
    <d-navigation-drawer
      :active="$vuetify.breakpoint.smAndDown ? isDrawerOpen : false"
      @closedrawer="handleCloseDrawer"
      @openlogin="handleOpenLogin"/>

    <d-system-bar />

    <d-toolbar @openlogin="handleOpenLogin" @opendrawer="handleOpenDrawer" />

    <transition name="fade">
      <router-view class="d-page__content" />
    </transition>

    <d-footer />

    <d-login-popup v-model="isLoginOpen" />
    <v-snackbar
      v-model="showWelcomeSnackbar"
      right
      :top="$vuetify.breakpoint.mdAndUp"
      :bottom="$vuetify.breakpoint.smAndDown">
      Bienvenido a Quimder
      <v-btn color="pink" flat @click="showWelcomeSnackbar = false">
        <d-icon name="b-close" />
      </v-btn>
    </v-snackbar>

    <d-order-glove />
  </v-app>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import { setInterval, clearInterval } from 'timers'
import { ROOT } from '@/router'
import DOrderGlove from '@/components/d-order/glove'

export default {
  name: 'StorefrontView',
  components: {
    'd-order-glove': DOrderGlove
  },
  data () {
    return {
      isLoginOpen: false,
      isDrawerOpen: false,

      isLiked: false,
      sharePopup: false,
      favoritePopupIsOpen: false,
      showWelcomeSnackbar: false
    }
  },
  computed: {
    ...mapState('auth', ['sessionPersistence', 'tokenRefreshInterval']),
    ...mapGetters('auth', ['isAuthenticated']),
    classes () {
      return [
        {
          'd-view-error':
            this.$route.name && this.$route.name.includes('error'),
          'd-view-error--not-found':
            this.$route.name && this.$route.name === 'error:not-found',
          'd-view-error--forbidden':
            this.$route.name && this.$route.name === 'error:forbidden',
          'd-view-error--server-error':
            this.$route.name && this.$route.name === 'error:server-error'
        }
      ]
    },
    isErrorView () {
      return this.$route.name && this.$route.name.includes('error')
    },
    isProductDetailView () {
      return this.$route.name === 'ProductDetails'
    }
  },
  watch: {
    isAuthenticated (val, oldVal) {
      if (val) {
        this.getAutenticatedUser()
        this.showWelcomeSnackbar = true
        if (!this.refrehsTimer) {
          this.refrehsTimer = setInterval(
            this.refreshToken,
            this.tokenRefreshInterval
          )
        }
      } else {
        clearInterval(this.refrehsTimer)
        this.refrehsTimer = null
      }
    }
  },
  methods: {
    ...mapActions('auth', [
      'logout',
      'refreshToken',
      'initialize',
      'getAutenticatedUser'
    ]),

    ...mapActions('brand', {
      getFeaturedBrands: 'listFeatured'
    }),

    ...mapActions('category', {
      getCategoryList: 'list'
    }),

    /**
     * Open login pop-up
     */
    handleOpenLogin () {
      if (this.isDrawerOpen) {
        this.handleCloseDrawer()
      }

      this.isLoginOpen = true
    },
    /**
     * Open drawer
     */
    handleOpenDrawer () {
      this.isDrawerOpen = true
    },
    /**
     * Close drawer
     */
    handleCloseDrawer () {
      this.isDrawerOpen = false
    },

    handleLeaving () {
      if (!this.sessionPersistence && this.isAuthenticated) {
        this.logout()
      }
    },
    closeProductDetails () {
      try {
        this.$router.go(-1)
      } catch (error) {
        this.$router.push({ name: ROOT })
      }
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
      this.isLiked = true
    }
  },
  created () {
    /**
     * TODO:
     * If persistence session is false, make logout on browser / tab close
     * not on reload
     */
    this.initialize()

    window.addEventListener(
      'beforeunload',
      e => {
        e.preventDefault()
        this.handleLeaving()
      },
      false
    )

    console.log('getting featured brands')
    this.getCategoryList({
      query: {}
    })

    this.getFeaturedBrands({
      query: {
        fields: ['id', 'name', 'slug', 'image'].join(','),
        pageSize: 100
      }
    })
  },
  mounted () {
    if (!this.refrehsTimer) {
      this.refrehsTimer = setInterval(
        this.refreshToken,
        this.tokenRefreshInterval
      )
    }
  },
  beforeDestroy () {
    clearInterval(this.refrehsTimer)
    this.refrehsTimer = null
  }
}
</script>
