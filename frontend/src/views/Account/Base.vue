<template>
  <v-content class="d-view__account--content">
    <v-container
      :fluid="$vuetify.breakpoint.mdAndDown"
      grid-list-xl
      :class="['mt-3', 'mb-3']">
      <v-layout row wrap>
        <v-flex
          v-if="this.$route.meta && this.$route.meta.breadcrumbs"
          xs12
          mb-4
          pb-0>
          <v-breadcrumbs :items="this.$route.meta.breadcrumbs" class="pa-0">
            <template v-slot:item="props">
              <li>
                <router-link
                  :to="props.item.href"
                  :class="[
                    'v-breadcrumbs__item',
                    {
                      'v-breadcrumbs__item--disabled': props.item.disabled
                    }
                  ]">
                  {{ props.item.text }}
                </router-link>
              </li>
            </template>
          </v-breadcrumbs>
        </v-flex>

        <v-flex xs12 mb-4 py-0>
          <h2 class="font-weight-bold">
            Mi cuenta
          </h2>
        </v-flex>

        <v-flex v-if="$vuetify.breakpoint.mdAndUp" md3 lg2>
          <d-account-menu :items="menuItems" class="transparent" />
        </v-flex>

        <v-flex xs12 md9 lg10>
          <template v-if="contentComponent">
            <component v-bind:is="contentComponent"></component>
          </template>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
import {
  ACCOUNT_ORDERS,
  ACCOUNT_ADDRESSES,
  ACCOUNT_FAVORITES,
  ACCOUNT_SETTINGS
} from '@/router/account'

export default {
  name: 'Account',
  components: {
    'd-account-menu': () => import('./d-account-menu')
  },
  props: {
    contentComponent: null
  },
  data () {
    return {
      menuItems: [
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
  }
}
</script>
