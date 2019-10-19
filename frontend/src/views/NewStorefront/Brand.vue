<template>
  <v-content>
    <v-layout id="section__brandBanner">
      <carousel
        class="CarouselBanner"
        :perPage="1"
        :autoplay="false"
        :loop="true"
        :paginationEnabled="false">
        <slide
          v-for="(slide, i) in content.banner.carousel.items"
          :key="i">
          <v-layout row wrap align-center fill-height style="position:absolute; z-index:999; width:100vw;">
            <v-flex md6 offset-md1 xs6 offset-xs1>
              <v-card flat color="transparent" v-for="description in content.banner.carousel.items" :key="description.description">
                <v-flex class="black--text banner-description">
                  <span v-html="description.description" />
                </v-flex>
              </v-card>
            </v-flex>
          </v-layout >
          <v-img width="100vw" :src="slide.background"></v-img>
        </slide>
      </carousel>
    </v-layout>
    <v-layout id="section__featuredstores" class="section">
      <d-brand-carousel/>
    </v-layout>
    <v-layout id="section__shoppingfilter" class="section">
      <v-container fluid pa-0 grid-list-lg>
        <h1>TODAS LAS MARCAS</h1>
        <v-layout row wrap>
          <v-flex xs12 md2 order-xs3 order-sm3 order-md1>
            <v-btn
              depressed
              outline
              block
              style="border-radius: 4px; height:42px;"
              class="my-0">
              Ver Todo
            </v-btn>
          </v-flex>
          <v-flex py-0 md10 order-sm2 order-md2 class="hidden-sm-and-down">
            <v-flex d-flex mx-2 py-0 px-0>
              <v-flex xs12 px-0 v-for="(item, i) in content.shoppingFilter.letterFilter" :key="i">
                <v-btn-toggle>
                  <v-btn flat class="btn--letter">
                    <p class="ma-0 black--text">{{item.letter}}</p>
                  </v-btn>
                </v-btn-toggle>
              </v-flex>
            </v-flex>
          </v-flex>
          <!--v-flex xs12 md2 order-xs1 order-sm1 order-md3 align-self-center>
            FILTRAR POR:
          </v-flex>
          <v-flex md2 order-xs2 order-sm2 order-md4 v-for="(item, i) in content.shoppingFilter.filters" :key="i">
            <v-menu
              offset-y
              full-width
              transition="slide-y-transition"
              bottom>
              <v-btn
                depressed
                outline
                block
                class="btn--category ma-0"
                style="border-radius: 4px; height:42px;"
                slot="activator"
                color="black"
              >
                {{item.filter}}
                <d-icon right medium name="b-down"/>
              </v-btn>
              <v-list>
                <v-list-tile>
                  <v-list-tile-title>Holi, aquí selecciona tu filtro</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
          </v-flex-->
        </v-layout>

        <v-container fluid grid-list-lg px-0>
          <v-layout row wrap>
            <v-flex md2 xs4
              v-for="(item,i) in content.shoppingFilter.showFilter"
              :key="i">
                <v-card flat hover class="d-flex justify-center" height="100">
                  <v-img contain height="100%" max-width="180px" :src="item.src"></v-img>
                </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-container>
    </v-layout>
    <v-container class="text-xs-center">
      <d-pagination class="hidden-sm-and-down"/>
        <!--v-flex xs6 offset-xs3>
          <v-btn outline block class="border-radius my-2"> Más tiendas </v-btn>
        </v-flex-->
    </v-container>
  </v-content>
</template>

<style lang="less">
#section__brandBanner {
  .v-tooltip__content {
    width: 96px;
    text-align: center;
  }
  .VueCarousel-wrapper {
    .banner-description {
      font-size: 2rem;
      line-height: 36px;
    }
  }
}

#section__shoppingfilter {
  .v-card {
    box-shadow: none;
    padding: 15px;
    /*border: 1px solid black;*/
    border-radius: 4px;
    .v-img {
      display: flex;
      margin: 0 auto;
    }
  }
}

@media only screen and (max-width: 960px) {
  #section__brandBanner {
    .VueCarousel-wrapper {
      .banner-description {
        font-size: 1.5rem;
        line-height: 1.5rem;
      }
    }
  }
}

@media only screen and (max-width: 600px) {
  #section__brandBanner {
    .VueCarousel-wrapper {
      .banner-description {
        font-size: 1.25rem;
        line-height: 1.25rem;
      }
    }
  }
}
</style>

<script>
import bannerBrand from '@/assets/images/banner_tiendas.jpeg'
import brand01 from '@/assets/images/quimder/brand1.png'
import brand02 from '@/assets/images/quimder/brand2.jpg'
import brand03 from '@/assets/images/quimder/brand3.png'
import brand04 from '@/assets/images/quimder/brand4.png'
import brand05 from '@/assets/images/quimder/brand5.png'

export default {
  name: 'Brand',
  data () {
    return {
      featuredStoresCarouselIndex: 0,
      assets: {
        bannerBrand: bannerBrand,
        brand01: brand01,
        brand02: brand02,
        brand03: brand03,
        brand04: brand04,
        brand05: brand05
      },
      content: {
        banner: {
          carousel: {
            items: [
              {
                background: bannerBrand,
                description: 'Descubre todo lo que puedes comprar en la <b>mejor tienda del país</b>.'
              },
              {
                background: bannerBrand
              },
              {
                background: bannerBrand
              }
            ]
          }
        },
        featuredStores: [
          { src: brand01, name: 'marca01' },
          { src: brand02, name: 'marca02' },
          { src: brand03, name: 'marca03' },
          { src: brand04, name: 'marca04' },
          { src: brand05, name: 'marca05' },
          { src: brand01, name: 'marca01' },
          { src: brand02, name: 'marca02' },
          { src: brand03, name: 'marca03' },
          { src: brand04, name: 'marca04' },
          { src: brand05, name: 'marca05' }
        ],
        shoppingFilter: {
          letterFilter: [
            { letter: 'A' },
            { letter: 'B' },
            { letter: 'C' },
            { letter: 'D' },
            { letter: 'E' },
            { letter: 'F' },
            { letter: 'G' },
            { letter: 'H' },
            { letter: 'I' },
            { letter: 'J' },
            { letter: 'K' },
            { letter: 'L' },
            { letter: 'M' },
            { letter: 'N' },
            { letter: 'Ñ' },
            { letter: 'O' },
            { letter: 'P' },
            { letter: 'Q' },
            { letter: 'R' },
            { letter: 'S' },
            { letter: 'T' },
            { letter: 'U' },
            { letter: 'V' },
            { letter: 'W' },
            { letter: 'X' },
            { letter: 'Y' },
            { letter: 'Z' }
          ],
          filters: {
            1: {
              filter: 'Categoría'
            },
            2: {
              filter: 'Producto'
            }
          },
          showFilter: [
            { src: brand01 },
            { src: brand02 },
            { src: brand03 },
            { src: brand04 },
            { src: brand05 },
            { src: brand01 },
            { src: brand02 },
            { src: brand03 },
            { src: brand04 },
            { src: brand05 },
            { src: brand01 },
            { src: brand02 },
            { src: brand03 },
            { src: brand04 },
            { src: brand05 },
            { src: brand01 },
            { src: brand02 },
            { src: brand03 },
            { src: brand04 },
            { src: brand05 },
            { src: brand01 },
            { src: brand02 },
            { src: brand03 }
          ]
        }
      }
    }
  },
  methods: {
    // ...mapActions('product', {
    // getProductList: 'list'
    // }),
    featuredStoresPrevSlide (e) {
      // https://ssense.github.io/vue-carousel/api/#perPageCustom
      // :perPageCustom="[[0,2], [450,3], [600, 4], [900, 5]]"
      const nStores = this.content.featuredStores.length
      let nPages = 0

      if (this.$vuetify.breakpoint.width >= 900) {
        nPages = Math.ceil(nStores / 5)
      } else if (this.$vuetify.breakpoint.width >= 600) {
        nPages = Math.ceil(nStores / 4)
      } else if (this.$vuetify.breakpoint.width >= 450) {
        nPages = Math.ceil(nStores / 3)
      } else {
        nPages = Math.ceil(nStores / 2)
      }

      let currentIndex = (nPages + this.featuredStoresCarouselIndex - 1) % nPages
      this.featuredStoresCarouselIndex = currentIndex
    },
    featuredStoresNextSlide (e) {
      // https://ssense.github.io/vue-carousel/api/#perPageCustom
      // :perPageCustom="[[0,2], [450,3], [600, 4], [900, 5]]"
      const nStores = this.content.featuredStores.length
      let nPages = 0

      if (this.$vuetify.breakpoint.width >= 900) {
        nPages = Math.ceil(nStores / 5)
      } else if (this.$vuetify.breakpoint.width >= 600) {
        nPages = Math.ceil(nStores / 4)
      } else if (this.$vuetify.breakpoint.width >= 450) {
        nPages = Math.ceil(nStores / 3)
      } else {
        nPages = Math.ceil(nStores / 2)
      }

      let currentIndex = (this.featuredStoresCarouselIndex + 1) % nPages
      this.featuredStoresCarouselIndex = currentIndex
    }
  }
}
</script>
