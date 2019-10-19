<template>
  <v-content app class="d-page__content">
    <!--
      Home carousel
    -->
    <v-container
      fluid
      class="d-container d-container--full-fluid d-container--full-width">
      <d-header-carousel
        v-if="headerSlider && headerSlider.slides"
        :slider="headerSlider"
        :placeholder="headerPlaceholder"/>
    </v-container>

    <!--
      Home advantages
    -->
    <v-container
      fluid
      class="d-container d-container--full-fluid d-container--full-width grey lighten-3 pa-4">
      <v-layout row wrap align-center justify-space-around>
        <v-flex v-for="(advantage, i) in advantages" :key="i" md4 sm4 xs12>
          <div class="d-advantage">
            <d-icon
              :scale="3"
              :name="advantage.icon"
              class="d-advantage--icon"/>
            <span class="d-advantage--text">
              {{ advantage.service }}
            </span>
          </div>
        </v-flex>
      </v-layout>
    </v-container>

    <!--
      Home banner
    -->
    <v-container
      v-if="
        featuredBrands &&
          featuredBrands.items &&
          featuredBrands.items.length > 0
      "
      fluid>
      <v-layout row wrap>
        <v-flex xs12>
          <h2 class="text-xs-center text--uppercase mb-4">
            Marcas destacadas
          </h2>
        </v-flex>
        <v-flex xs12>
          <d-brand-featured-carousel />
        </v-flex>
      </v-layout>
    </v-container>

    <!--
      Home banner
    -->
    <v-container
      fluid
      class="d-container d-container--full-fluid d-container--full-width">
      <v-layout wrap row>
        <v-flex v-if="banner" xs12>
          <v-img contain :src="banner.image.original" />
        </v-flex>
      </v-layout>
    </v-container>

    <!--
      Home scenes
    -->
    <v-container
      fluid
      class="d-container d-container--full-fluid d-container--full-width">
      <d-showcase :scenes="scenes" />
    </v-container>

    <!--
      Home special offers
    -->
    <!-- v-layout id="section__offersales" class="section">
      <v-container fluid px-0>
        <h1>OFERTAS ÚNICAS</h1>
        <carousel :autoplay="true" :perPageCustom="[[0,1], [600, 2], [960, 3]]" :paginationEnabled="false" :autoplayTimeout="5000" :loop="true">
          <slide v-for="(offerSales, i) in content.offerSales" :key="i">
            <v-layout mx-2 row class="offersales__card">
              <v-flex xs6>
                <v-card flat class="fill-height" color="grey lighten-3">
                  <span class="white--text wlb--price-tag">{{ offerSales.discount }}%</span>
                  <v-container px-2 fill-height>
                    <v-img
                      max-height="160"
                      :src="offerSales.product"
                      contain>
                    </v-img>
                  </v-container>
                </v-card>
              </v-flex>
              <v-flex xs6 pa-3 class="product-details__card">
                <v-layout column fill-height>
                  <v-flex offset-xs6 offset-sm5>
                    <v-img
                      max-height="20"
                      contain
                      :src="offerSales.brand">
                    </v-img>
                  </v-flex>
                  <v-flex my-2>
                    {{ offerSales.productDescription }}
                  </v-flex>
                  <v-flex mb-2 class="product-final-price">
                    S/{{ offerSales.finalPrice }}
                  </v-flex>
                  <v-flex class="product-previous-price d-red--text">
                    <del>S/{{ offerSales.previousPrice }}</del>
                  </v-flex>
                  <v-flex>
                    <countdown :time="time" :interval="100" tag="div">
                      <template slot-scope="props">
                        <v-layout align-center justify-center row fill-height>
                          <v-flex>
                            <v-card max-width="50" flat color="grey lighten-3" class="border-radius" style="margin:auto;">
                              <v-layout column fill-height>
                                <v-flex align-center justify-center class="d-flex font-weight-bold">{{ props.hours }}</v-flex>
                                <v-flex align-center justify-center style="font-size:0.75rem" class="d-flex">Hor</v-flex>
                              </v-layout>
                            </v-card>
                          </v-flex>
                          <v-flex d-flex justify-center align-center class="font-weight-bold">:</v-flex>
                          <v-flex>
                            <v-card max-width="50" flat color="grey lighten-3" class="border-radius" style="margin:auto;">
                              <v-layout column fill-height>
                                <v-flex align-center justify-center class="d-flex font-weight-bold">{{ props.minutes }}</v-flex>
                                <v-flex align-center justify-center style="font-size:0.75rem" class="d-flex">Min</v-flex>
                              </v-layout>
                            </v-card>
                          </v-flex>
                          <v-flex d-flex justify-center align-center class="font-weight-bold">:</v-flex>
                          <v-flex>
                            <v-card max-width="50" flat color="grey lighten-3" class="border-radius" style="margin:auto;">
                              <v-layout column fill-height>
                                <v-flex align-center justify-center class="d-flex font-weight-bold">{{ props.seconds }}</v-flex>
                                <v-flex align-center justify-center style="font-size:0.75rem" class="d-flex">Seg</v-flex>
                              </v-layout>
                            </v-card>
                          </v-flex>
                        </v-layout>
                      </template>
                    </countdown>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </slide>
        </carousel>
      </v-container>
    </v-layout -->

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

        <v-flex xs12 md2>
          <h2
            v-if="$vuetify.breakpoint.mdAndUp"
            class="text-xs-left text--uppercase mb-4">
            Categorías
          </h2>
          <d-categories
            desktopClass="hidden-sm-and-down"
            cardHeight="70"
            avatarSize="60"/>
        </v-flex>

        <v-flex xs12 md10>
          <d-product-list
            v-if="productList"
            :products="productList.items"
            :pagination="productList.meta"
            @pagechange="refreshProductList"/>
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
import DProductList from '@/components/d-product/list'

export default {
  name: 'index',
  components: {
    'd-product-list': DProductList
  },
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
      page: 1
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
        page: this.page,
        fields: ['id', 'name', 'slug', 'image', 'availability', 'brand'].join(
          ','
        ),
        expand: ['brand'].join(',')
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

    refreshProductList (value) {
      this.page = value

      this.getProductList({
        query: this.productQuery
      })
    }
  },
  created () {
    this.getHeaderSlider()
    this.getBanner()

    // this.getBrandList({
    //   query: {
    //     isFeatured: true,
    //     fields: [
    //       'id',
    //       'name',
    //       'slug',
    //       'image'
    //     ].join(',')
    //   }
    // })

    this.getSceneList({
      query: {
        isActive: true,
        expand: 'spotlights'
      }
    })

    this.getProductList({
      query: this.productQuery
    })
  }
}
</script>
