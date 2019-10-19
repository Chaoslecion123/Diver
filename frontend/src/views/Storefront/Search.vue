<template>
  <v-content app class="d-page__content">
    <!--
      Home product list
    -->
    <v-container :fluid="$vuetify.breakpoint.mdAndDown">
      <v-layout wrap row class="my-4">
        <v-flex xs12 class="text-xs-center">
          <h2 class="text-xs-center text--uppercase mb-4">
            Explora nuestra galería de productos
          </h2>
        </v-flex>

        <v-flex xs12>
          <v-container fluid grid-list-lg>
            <v-layout row wrap>
              <v-flex
                v-for="(product, i) in productList.items"
                :key="i"
                xs6
                sm4
                md3>
                <d-product-card :product="product" />
              </v-flex>

              <v-flex xs12 text-xs-right>
                <div style="margin: 0 0 0 auto;width: fit-contnet;">
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
.d-advantage {
  display: flex;
  padding: 24px;
  flex-direction: row;
  align-items: center;
  justify-content: center;

  .d-advantage--icon {
    margin-right: 24px;
  }

  .d-advantage--text {
    width: 240px;
  }
}
</style>

<script>
import { STOREFRONT_CATEGORY } from '@/router/storefront'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'index',
  data () {
    return {
      links: {
        storefrontCategory: STOREFRONT_CATEGORY
      },
      advantages: [
        {
          class: '',
          icon: 'b-global',
          service: 'Llegamos a todo el país'
        },
        {
          class: 'hidden-sm-and-down',
          icon: 'b-card',
          service: 'Recibimos cualquier forma de pago'
        },
        {
          class: '',
          icon: 'b-clock',
          service: 'Servicio de envío las 24 horas'
        }
      ],
      page: 1,
      search: ''
    }
  },
  computed: {
    ...mapState('product', {
      productList: 'objects'
    }),

    ...mapState('slider', {
      headerSlider: 'object'
    }),

    ...mapState('banner', {
      banner: 'object'
    }),

    ...mapState('scene', {
      sceneList: 'objects'
    }),

    ...mapState('stripe', {
      stripeList: 'objects'
    }),

    ...mapState('brand', {
      featuredBrands: 'featuredObjects'
    }),

    productQuery () {
      return {
        q: this.search,
        page: this.page,
        fields: ['id', 'name', 'slug', 'image', 'availability'].join(',')
      }
    },

    headerPlaceholder () {
      return ''
    },

    stripe () {
      if (this.stripeList && this.stripeList.items) {
        return this.stripeList.items[0] || {}
      }

      return {}
    },

    scenes () {
      if (this.sceneList && this.sceneList.items) {
        return this.sceneList.items || []
      }

      return []
    },

    detailedProduct () {
      if (!this.dialog) return null

      return this.content.ourProducts.categoryProduct[this.$route.params.slug]
    }
  },
  watch: {
    '$route.query.q' (val, oldVal) {
      if (val) {
        this.search = val
        this.getProductList({
          query: this.productQuery
        })
      }
    }
  },
  methods: {
    ...mapActions('slider', {
      getHeaderSlider: 'homepage'
    }),
    ...mapActions('banner', {
      getBanner: 'homepage'
    }),
    ...mapActions('scene', {
      getSceneList: 'list'
    }),
    ...mapActions('product', {
      getProductList: 'list'
    }),

    refreshProductList () {
      this.getProductList({
        query: this.productQuery
      })
    }
  },
  created () {
    if (this.$route.query && this.$route.query.q) {
      this.search = this.$route.query.q

      this.getProductList({
        query: this.productQuery
      })
    }
  }
}
</script>
