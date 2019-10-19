<template>
  <v-navigation-drawer
    v-model="innerActive"
    app
    fixed
    temporary
    :class="['d-navigation-drawer']"
    :width="240"
    @input="setInnerChange">
    <v-toolbar flat>
      <v-list v-if="isAuthenticated" class="d-navigation-drawer__user-promtp">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <img
              v-if="user && user.picture"
              src="https://randomuser.me/api/portraits/men/85.jpg"/>
            <template v-else>
              {{ user.fullName[0] }}
            </template>
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>{{ user.fullName }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-btn
        v-else
        block
        depressed
        color="accent"
        class="d-btn d-btn--rounded d-btn--bold d-btn--no-transform"
        @click="openLogin">
        Iniciar sesión
      </v-btn>
    </v-toolbar>

    <v-divider />

    <v-list
      v-if="categoryList && categoryList.items && categoryList.items.length > 0"
      class="d-navigation-drawer__user-promtp">
      <v-subheader>Categorías</v-subheader>
      <v-list-tile
        v-for="category in categoryList.items"
        :key="category.id"
        ripple
        :to="{
          name: 'storefront:category',
          params: {
            slug: category.slug,
            id: category.id
          }
        }">
        <v-list-tile-avatar>
          <img v-if="category.iconImage" :src="category.iconImage" />
          <span v-else>
            {{ category.name[0] }}
          </span>
        </v-list-tile-avatar>
        <v-list-tile-title style="font-size:14px;">
          {{ category.name }}
        </v-list-tile-title>
      </v-list-tile>
    </v-list>

    <v-divider />

    <v-list v-if="isAuthenticated" class="d-navigation-drawer__user-promtp">
      <v-subheader>Mi cuenta</v-subheader>

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
        <v-list-tile href="/dashboard/">
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

    <v-divider />

    <v-footer absolute>
      &copy; {{ new Date().getFullYear() }} Quimder
    </v-footer>
  </v-navigation-drawer>
</template>

<style lang="less">
@import './navigation-drawer.less';
</style>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import { ROOT } from '@/router'
import {
  ACCOUNT_ORDERS,
  ACCOUNT_ADDRESSES,
  ACCOUNT_FAVORITES,
  ACCOUNT_SETTINGS
} from '@/router/account'

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
      ],
      innerChange: false
    }
  },
  computed: {
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapState('category', {
      categoryList: 'objects'
    }),

    innerActive: {
      get () {
        if (this.$vuetify.breakpoint.smAndDown) {
          return this.active
        }

        return false
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
    ...mapActions('auth', {
      performLogout: 'logout'
    }),

    openLogin () {
      this.$emit('openlogin')
    },

    closeDrawer () {
      this.$emit('closedrawer')
    },

    setInnerChange () {
      this.innerChange = true
    },

    handleLogout () {
      this.performLogout()
      this.closeDrawer()
    }
  }
}
</script>
