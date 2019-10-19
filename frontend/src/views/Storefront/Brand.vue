<template>
  <v-content
    app
    class="d-brand-view">
    <v-container
      v-if="brand && (brand.slider || brand.backgroundImage)"
      fluid
      class="d-brand-view__content d-container d-container--full-fluid d-container--full-width">
      <d-header-carousel
        :slider="brand.slider"
        :placeholder="brand.backgroundImage"/>
    </v-container>

    <v-container
      v-if="brand"
      fluid
      class="d-container d-container--full-fluid d-container--full-width">
      <v-layout
        class="d-header grey lighten-2"
        align-center
        justify-center>
        <h1>
          {{ brand.name }}
        </h1>
      </v-layout>
    </v-container>

    <v-container
      v-if="brand"
      grid-list-xl
      class="my-4"
      :fluid="$vuetify.breakpoint.mdAndDown">
      <v-layout
        wrap
        row>
        <v-flex
          xs12>
          <v-breadcrumbs v-if="breadcrumbs" :items="breadcrumbs" class="pa-0">
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

        <v-flex
          xs12
          md3
          lg2>
          <d-product-filter
            :filterData="brand.filterData"
            @filter="handleFilter"/>
        </v-flex>

        <v-flex
          xs12
          md9
          lg10>
          <v-container
            fluid
            class="pa-0">
            <v-layout
              row
              wrap>
              <v-flex
                v-for="(product, i) in productList.items"
                :key="i"
                xs6
                sm4
                md4
                lg3>
                <d-product-card
                  :product="product"/>
              </v-flex>

              <v-flex
                xs12
                text-xs-right>
                <div
                  style="margin: 0 0 0 auto;width: fit-contnet;">
                  <v-pagination
                    v-if="productList && productList.meta"
                    v-model="page"
                    color="accent"
                    :length="productList.meta.pages"
                    :total-visible="4"
                    @input="refreshProductList">
                  </v-pagination>
                </div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<style lang="less">
.d-brand-view {
  .d-header {
    height: 100px;
  }
}
</style>

<script>
import { mapState, mapActions } from 'vuex'
import { STOREFRONT_BRAND } from '@/router/storefront'

export default {
  name: 'Brand',
  data () {
    return {
      brandDrawer: null,
      page: 1
    }
  },
  computed: {
    ...mapState('product', {
      productList: 'objects'
    }),
    ...mapState('brand', {
      brand: 'object'
    }),
    breadcrumbs () {
      return [
        ...this.$route.meta.breadcrumbs,
        {
          text: this.brand.name,
          disabled: true,
          href: {
            name: STOREFRONT_BRAND,
            params: { ...this.$route.params }
          }
        }
      ]
    },
    brandId () {
      if (this.$route && this.$route.params) {
        return this.$route.params.id
      }
      return null
    },
    productQuery () {
      return {
        brand: this.brandId,
        page: this.page,
        fields: ['id', 'name', 'slug', 'image', 'availability'].join(',')
      }
    }
  },
  watch: {
    brandId (val, oldVal) {
      if (val) {
        this.getBrand({
          id: val
        })

        this.getProductList({
          query: this.productQuery
        })
      }
    }
  },
  methods: {
    ...mapActions('product', {
      getProductList: 'list'
    }),
    ...mapActions('brand', {
      getBrand: 'read'
    }),

    refreshProductList () {
      this.getProductList({
        query: this.productQuery
      })
    },

    handleFilter (filters) {
      this.getProductList({
        query: { ...this.productQuery, ...filters }
      })
    }
  },
  created () {
    if (this.brandId) {
      this.getBrand({
        id: this.brandId
      })

      this.getProductList({
        query: this.productQuery
      })
    }
  }
}
</script>
