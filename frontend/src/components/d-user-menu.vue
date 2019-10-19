<template>
  <v-menu
    transition="slide-x-transition"
    offset-y
    bottom
    left
    content-class="menuItems">

    <v-btn
      :class="$vuetify.breakpoint.smAndDown? 'hidden-sm-and-down' : '' "
      slot="activator"
      icon>
      <d-icon
        scale="1.65"
        name="b-user"/>
    </v-btn>

    <v-list
      class="pa-0">
      <!--
        Cuenta
      -->
      <v-list-tile
        :to="{ name: 'user-profile::settings' }"
        ripple>
        <v-list-tile-avatar>
          <d-icon
            scale="1.4"
            name="b-user"/>
        </v-list-tile-avatar>
        <v-list-tile-title style="font-size:14px;">
          Mi cuenta
        </v-list-tile-title>
      </v-list-tile>
      <v-divider
        class="mx-2"/>

      <!--
        Pedidos
      -->
      <v-list-tile
        :to="{ name: 'user-profile::orders' }"
        ripple>
        <v-list-tile-avatar>
          <d-icon
            scale="1.4"
            name="b-gift"/>
        </v-list-tile-avatar>
        <v-list-tile-title style="font-size:14px;">
          Mis pedidos
        </v-list-tile-title>
      </v-list-tile>
      <v-divider
        class="mx-2"/>

      <!--
        Reseñas
      -->
      <v-list-tile
        :to="{ name: 'user-profile::bills' }"
        ripple>
        <v-list-tile-avatar>
          <d-icon
            scale="1.4"
            name="b-file-text"/>
        </v-list-tile-avatar>
        <v-list-tile-title style="font-size:14px;">
          Mis facturas
        </v-list-tile-title>
      </v-list-tile>
      <v-divider
        class="mx-2"/>

      <!--
        Cupones
      -->
      <v-list-tile
        :to="{ name: 'user-profile::coupons' }"
        ripple>
        <v-list-tile-avatar>
          <d-icon
            scale="1.4"
            name="b-barcode"/>
        </v-list-tile-avatar>
        <v-list-tile-title style="font-size:14px;">
          Mis cupones
        </v-list-tile-title>
      </v-list-tile>
      <v-divider
        class="mx-2"/>

      <!--
        Panel de control
      -->
      <template
        v-if="user && user.isStaff">
        <v-list-tile
          href="/dashboard/"
          ripple>
          <v-list-tile-avatar>
            <d-icon
              scale="1.4"
              name="b-dashboard"/>
          </v-list-tile-avatar>
          <v-list-tile-title style="font-size:14px;">
            Panel de control
          </v-list-tile-title>
        </v-list-tile>
        <v-divider
          class="mx-2"/>
      </template>

      <!--
        Cerrar Sesión
      -->
      <v-list-tile
        @click="handleLogout"
        ripple>
        <v-list-tile-avatar>
          <d-icon
            scale="1.4"
            name="b-logout"/>
        </v-list-tile-avatar>
        <v-list-tile-title style="font-size:14px;">
          Cerrar sesión
        </v-list-tile-title>
      </v-list-tile>

    </v-list>
  </v-menu>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { ROOT } from '@/router'

export default {
  name: 'DUserMenu',
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
