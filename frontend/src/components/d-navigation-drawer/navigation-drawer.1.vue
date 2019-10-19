<template>
  <v-navigation-drawer
    v-model="innerActive"
    @input="setInnerChange"
    app
    fixed
    temporary
    class="d-navigation-drawer">
    <v-layout
      column
      wrap>
      <v-list
        v-if="isAuthenticated && user"
        class="q-orange--background px-1 py-2">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <img src="https://randomuser.me/api/portraits/men/85.jpg">
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title class="font-weight-600 white--text">{{user.fullName}}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-list class="pa-0" v-else>
        <v-list-tile class="login-tile">
          <v-layout row wrap fill-height class="q-orange--background">
            <v-btn
              dark
              class="ma-0 btn--nav-drawer"
              :ripple="false"
              flat
              block
              depressed
              @click="openLoginModal">
              Iniciar sesión
            </v-btn>
            <v-divider
              vertical
              style="min-height:0; height:auto; border-color:#fff;"
              class="my-2"/>
            <v-btn
              dark
              class="ma-0 btn--nav-drawer"
              :ripple="false"
              flat
              block
              depressed
              @click="openRegisterModal">
              Regístrate
            </v-btn>

            <d-login-popup v-model="isLoginModalOpen"/>
          </v-layout>
        </v-list-tile>
      </v-list>

      <v-divider/>

      <v-list
        class="pa-0">
        <v-list-tile
          :to="{ name: links.ROOT }">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-home"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Inicio</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        class="pa-0">
        <v-list-tile
          @click="authFirst('user-profile::settings')">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-user"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Mi cuenta</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        v-if="isAuthenticated"
        class="pa-0">
        <v-list-tile
          @click="authFirst('user-profile::addresses')">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-flag"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Mis direcciones</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        v-if="isAuthenticated"
        class="pa-0">
        <v-list-tile
          @click="authFirst('user-profile::bills')">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-file-text"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Mis facturas</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        v-if="isAuthenticated"
        class="pa-0">
        <v-list-tile
          @click="authFirst('user-profile::tracking')">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-location"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Tracking</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        class="pa-0">
        <v-list-tile
          @click="authFirst('user-profile::orders')">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-gift"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Mis pedidos</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        class="pa-0">
        <v-list-tile
          @click="authFirst('user-profile::coupons')">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-barcode"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Mis cupones</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        v-if="user && user.isStaff && isAuthenticated"
        class="pa-0">
        <v-list-tile
          href="/dashboard/">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-dashboard"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Panel de control</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list
        v-if="isAuthenticated"
        class="pa-0">
        <v-list-tile
          @click="handleLogout">
          <v-list-tile-action>
            <d-icon
              scale="1.35"
              color="grey darken-4"
              name="b-logout"/>
          </v-list-tile-action>
          <v-list-tile-title style="font-size:1rem;">Cerrar sesión</v-list-tile-title>
        </v-list-tile>
      </v-list>

      <v-list class="pa-0">
        <template v-for="(item,i) in navPanel">
          <v-list-tile class="grey lighten-3" v-if="item.title" :key="i">
            <v-list-tile-content>
              <v-list-tile-title style="font-size:1rem;">{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <!--<v-icon>arrow_forward</v-icon-->
              <d-icon name="b-arrow-right"/>
            </v-list-tile-action>
          </v-list-tile>
          <v-expansion-panel expand v-else :key="i">
            <v-expansion-panel-content
              class="grey lighten-3">
              <v-icon slot="actions">keyboard_arrow_down</v-icon>
              <div slot="header">{{item.header}}</div>
              <v-card>
                <v-card-text>{{item.options}}</v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </template>
      </v-list>

      <v-list mx-3>
        <v-list-tile>
          <v-layout row wrap text-xs-center>
            <v-flex align-self-center>Nuestras redes</v-flex>
            <v-divider style="border-color:#000" class="mx-2" vertical></v-divider>
            <v-flex>
              <v-icon medium color="#3C5A99">fiber_manual_record</v-icon>
            </v-flex>
            <v-flex>
              <v-icon medium color="red">fiber_manual_record</v-icon>
            </v-flex>
            <v-flex>
              <v-icon medium color="green">fiber_manual_record</v-icon>
            </v-flex>
          </v-layout>
        </v-list-tile>
      </v-list>

      <v-footer absolute color="#fff">
        <v-flex mx-3>
          <v-layout fill-height row wrap>
          <div>&copy; {{ new Date().getFullYear() }} Quimder</div>
          <v-spacer></v-spacer>
          <router-link class="policies" :to="{name: 'Store'}">Política y cookies</router-link>
          </v-layout>
        </v-flex>
      </v-footer>
    </v-layout>
  </v-navigation-drawer>
</template>

<style lang="less">
.d-navigation-drawer {
  &.v-navigation-drawer {
    .v-list {
      &__tile--active {
        color: #f58220 !important;
      }
      .login-tile {
        .v-list__tile {
          padding: 0;
        }
      }
    }
    .v-list:nth-child(2) {
      .v-list__tile:nth-child(1) {
        height: auto;
        padding: 0 !important;
      }
    }
    .v-list__tile__action {
      min-width: 42px;
    }
  }
  .btn--nav-drawer {
    border-radius: 0;
    height: 48px !important;
  }
  .btn--nav-location {
    .v-btn__content {
      justify-content: initial;
    }
  }
  .v-expansion-panel {
    box-shadow: none;
    height: auto;
    .v-expansion-panel__container {
      border: none;
      .v-expansion-panel__header {
        padding-left: 16px;
        padding-right: 16px;
        height: 48px;
        .v-expansion-panel__header__icon {
          i {
            color: #000 !important;
          }
        }
      }
    }
  }
  .v-expansion-panel__body {
    height: auto !important;
  }
  .policies {
    text-decoration: none;
    color: inherit;
  }
}
</style>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import { ROOT } from '@/router'

export default {
  name: 'd-navigation-drawer',
  props: {
    active: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      links: {
        root: ROOT
      },
      isLoginModalOpen: false,
      innerChange: false,
      navButtons: [
        { btn: 'Inicia Sesión' },
        { divider: true },
        { btn: 'Regístrate' }
      ],
      navPanel: [
        { header: 'Help & FAQ', icon: 'add', options: 'Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem' },
        { header: 'Help & FAQ', icon: 'add', options: 'Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem' }
      ]
    }
  },
  computed: {
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('auth', {
      user: 'currentUser'
    }),
    innerActive: {
      get () {
        return this.active
      },
      set (val) {
        if (this.innerChange) {
          this.$emit('closedrawer')
        }
      }
    },
    userFullName () {
      if (this.user) {
        return this.user.fullName
      }
      return null
    }
  },
  watch: {
    active () {
      this.innerChange = false
    }
  },
  methods: {
    setInnerChange () {
      this.innerChange = true
    },
    openLoginModal () {
      this.isLoginModalOpen = true
    },
    openRegisterModal () {
      this.isLoginModalOpen = true
    },
    authFirst (routeName) {
      if (this.isAuthenticated) {
        this.$router.push({ name: routeName })
      } else {
        this.$router.replace({ name: this.$route.name, query: { login: true } })
      }
    },
    ...mapActions('auth', {
      performLogout: 'logout'
    }),
    handleLogout () {
      this.performLogout()
      this.$router.push({ name: ROOT })
    }
  }
}
</script>
