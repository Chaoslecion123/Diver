<template>
  <v-menu left bottom offset-y transition="slide-y-transition">
    <v-btn icon slot="activator" class="d-btn d-btn--circle">
      <d-icon scale="1.5" name="b-user" />
    </v-btn>

    <v-list subheader class="pa-0" active-class="accent--text">
      <template v-for="(item, key) in userMenuItems">
        <v-divider v-if="item.prependDivider" :key="`divider-${key}`" />
        <v-list-tile v-if="item" :key="key" :to="item.to">
          <v-list-tile-avatar>
            <d-icon :name="item.icon" />
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
              {{ item.title }}
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>

      <template v-if="user && user.isStaff">
        <v-divider />
        <v-list-tile href="/dashboard/" target="_blank">
          <v-list-tile-avatar>
            <d-icon name="b-dashboard" />
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
              Panel de control
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>

      <v-divider />
      <v-list-tile @click="handleLogout" ripple>
        <v-list-tile-avatar>
          <d-icon name="b-logout" />
        </v-list-tile-avatar>
        <v-list-tile-title>
          Cerrar sesión
        </v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { ROOT } from '@/router'
import {
  ACCOUNT_ORDERS,
  ACCOUNT_ADDRESSES,
  ACCOUNT_FAVORITES,
  ACCOUNT_SETTINGS
} from '@/router/account'

export default {
  name: 'DUserMenu',
  data () {
    return {
      userMenuItems: [
        {
          icon: 'b-file-text',
          title: 'Pedidos',
          to: {
            name: ACCOUNT_ORDERS
          }
        },
        {
          icon: 'b-location',
          title: 'Direcciones',
          to: {
            name: ACCOUNT_ADDRESSES
          }
        },
        {
          icon: 'b-heart',
          title: 'Favoritos',
          to: {
            name: ACCOUNT_FAVORITES
          }
        },
        {
          icon: 'b-cog',
          title: 'Ajustes',
          to: {
            name: ACCOUNT_SETTINGS
          },
          prependDivider: true
        }
      ]
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser',
      isAuthenticated: 'isAuthenticated'
    })
  },
  methods: {
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
