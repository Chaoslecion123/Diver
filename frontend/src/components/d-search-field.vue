<template>
  <v-menu
    v-model="openMenu"
    offset-y
    class="d-search-menu"
    content-class="search-menu"
    :close-on-click="false"
    :close-on-content-click="false">
    <v-autocomplete
      class="search-field"
      solo
      flat
      clearable
      hide-no-data
      return-object
      slot="activator"
      color="#F58220"
      :class="[
        {
          active: inputIsActive,
          'v-select--is-menu-active': inputIsActive,
          'v-input--is-focused': inputIsActive
        }
      ]"
      :loading="isLoading"
      :append-icon="$vuetify.breakpoint.mdAndUp ? 'search' : 'search'"
      :search-input.sync="search"
      :append-outer-icon="$vuetify.breakpoint.smAndDown ? '' : ''"
      :placeholder="
        $vuetify.breakpoint.mdAndUp ? 'Encuentra lo que buscas aquí :D' : ''
      "
      @click:append="expandInput"
      @click:clear="clearMessage"/>
    <v-list v-if="productList.length > 0 || isLoading || notFound">
      <v-list-tile v-if="isLoading">
        Buscando productos ...
      </v-list-tile>
      <v-list-tile v-else-if="!isLoading && notFound">
        No se encontraron productos
      </v-list-tile>
      <template v-else>
        <v-list-tile
          v-for="(product, i) in productList"
          :key="i"
          @click="goToProductDetail(product)">
          <v-list-tile-avatar>
            <img
              contain
              max-height="160"
              :src="product.image.image.productSmall"/>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
              {{ product.name }}
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
      <v-list-tile v-if="!isLoading && !notFound" @click="goToSearchPage">
        <v-btn
          outline
          block
          color="accent"
          :class="[
            'ma-0',
            'd-btn',
            'd-btn--rounded',
            'd-btn--bold',
            'd-btn--no-transform'
          ]">
          Ver más productos
        </v-btn>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<style lang="less">
.search-menu {
  position: fixed;
  top: 80px !important;

  &.v-menu__content {
    @media (max-width: 480px) {
      left: 0px;
      max-width: initial!important;
      width: 100%;
    }
  }
}

.search-field {
  caret-color: var(--v-accent-base) !important;
  height: inherit;
  transition: all 0.8s ease-in;
  .v-input__control {
    min-height: 36px !important;
    height: 36px;
    margin: auto;
    .v-input__slot {
      border: 1px solid var(--v-accent-base);
      margin: 0;
      border-radius: 0 28px 28px 0 !important;
      .v-select__slot {
        input {
          cursor: text !important;
          width: 30vw;
          -webkit-transition: width 0.35s ease-in-out;
          transition: width 0.35s ease-in-out;
          margin-right: 24px;
        }
        .v-input__append-inner {
          display: flex;
          position: absolute;
          right: 0;
          cursor: pointer;
        }
      }
    }
  }
  &.v-input--is-dirty {
    .v-input__icon--append {
      display: none;
    }
  }
  @media only screen and (max-width: 960px) {
    width: 32px;
    -webkit-transition: all 0.7s ease-in-out;
    -moz-transition: all 0.7s ease-in-out;
    transition: all 0.7s ease-in-out;
    caret-color: transparent;
    .v-input__control {
      .v-input__slot {
        border: none !important;
        background: none !important;
        padding: 0 !important;
        border-radius: 28px !important;
        .v-select__slot {
          margin: 0 16px !important;
          input {
            width: 0 !important;
            max-width: calc(100% - 24px);
          }
          .v-input__append-inner {
            display: flex;
            position: absolute;
            right: 0;
            i {
              font-size: 28px;
            }
          }
        }
      }
    }
    &.v-input--is-dirty {
      .v-input__append-outer {
        display: none;
      }
    }
    .v-input__append-outer {
      align-items: center;
      position: absolute;
      height: inherit;
      right: 0px;
      margin: auto !important;
      i {
        font-size: 28px;
        color: rgba(0, 0, 0, 0.87) !important;
      }
    }
    &.active {
      caret-color: var(--v-accent-base) !important;
      width: calc(100vw - 288px) !important;
      .v-input__control {
        .v-input__slot {
          border: 1px solid var(--v-accent-base) !important;
          background: #fff !important;
        }
      }
    }
  }
  .v-progress-linear {
    width: calc(100% - 13px);
    @media only screen and (max-width: 960px) {
      width: calc(100% - 26px);
      margin-left: 13px !important;
    }
  }
  &.v-select.v-select--is-menu-active .v-input__icon--append .v-icon {
    transform: none !important;
    transition-duration: 0.1s;
    color: var(--v-accent-base) !important;
  }
}
</style>

<script>
import { STOREFRONT_SEARCH, STOREFRONT_PRODUCT } from '@/router/storefront'
import PRODUCT from '@/api/product'

export default {
  name: 'd-search-field',
  data () {
    return {
      links: {
        storefrontSearch: STOREFRONT_SEARCH
      },
      productList: [],
      isLoading: false,
      search: '',
      notFound: false,
      inputIsActive: false,
      openMenu: false
    }
  },
  watch: {
    inputIsActive (val, oldVal) {
      this.$emit('chageactive', val)
    },
    search (val, oldVal) {
      if (!val || val.length <= 2) {
        this.isLoading = false
        this.openMenu = false
        this.productList = []
        this.notFound = false
        return
      }

      if (this.isLoading) return

      if (val && val.length > 2) {
        this.isLoading = true
        this.openMenu = true

        const query = {
          fields: 'id,name,slug,price_range,image',
          q: val
        }

        PRODUCT.list(query)
          .then(response => {
            this.productList = response.data.items.slice(0, 4)
            this.notFound = this.productList.length === 0
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoading = false))
      } else {
        this.openMenu = false
      }
    }
  },
  methods: {
    // expandInput () {
    //  this.inputIsActive = !this.inputIsActive
    // },
    expandInput () {
      if (this.$vuetify.breakpoint.smAndDown) {
        this.inputIsActive = !this.inputIsActive
      }
    },
    clearMessage () {},
    goToProductDetail (product) {
      this.$router.push({
        name: STOREFRONT_PRODUCT,
        params: {
          id: product.id,
          slug: product.slug
        }
      })
    },
    goToSearchPage () {
      console.log('goToSearchPage')
      this.$router.push({
        name: STOREFRONT_SEARCH,
        query: {
          q: this.search
        }
      })
    }
  }
}
</script>
