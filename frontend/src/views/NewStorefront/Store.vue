<template>
  <v-content>
    <v-layout id="section__storeBanner">
      <carousel
        class="CarouselBanner"
        :perPage="1"
        :autoplay="false"
        :loop="true"
        :paginationEnabled="false">
        <slide
          v-for="(slide, i) in content.banner.carousel.items"
          :key="i">
          <v-img contain :src="slide.background">
            <v-layout row wrap align-center fill-height style="position:absolute; z-index:999; width:100vw;">
              <v-flex xs5 offset-xs1>
                <v-card flat color="transparent">
                  <v-flex class="white--text">
                    <span class="banner-description">{{ slide.description }} "Estilos tiene todos los productos que puedas comprar."</span>
                  </v-flex>
                </v-card>
              </v-flex>
            </v-layout>
          </v-img>
        </slide>
      </carousel>
      <v-flex>
        <img class="mt-2" style="position:absolute; top:0; right:0; margin-right: 90px; max-width:100px; display:none;" :src="assets.storeLogo">
      </v-flex>
    </v-layout>

    <v-layout id="section__category" class="section">
      <v-container fluid px-0>
        <v-flex mb-3>
          <h2>{{brand.name}} <span class="font-weight-medium">(1,250 productos)</span></h2>
        </v-flex>
        <v-layout row wrap>
          <v-flex md2 class="hidden-sm-and-down">
            <d-category-filter></d-category-filter>
          </v-flex>
          <v-flex xs12 md10 pl-5 class="remove-padding">
            <v-container fluid grid-list-md pa-0 ma-0>
              <v-layout row wrap>
                <v-flex xs6 sm4 md3 my-1 v-for="(product, i) in content.ourProducts.categoryProduct" :key="i">
                  <d-product-card :product="product"/>
                </v-flex>
                <v-container my-5 pa-0 fill-height>
                  <v-layout align-center justify-center row fill-height>
                    <v-flex xs3>
                      <v-btn outline block class="border-radius my-2"> Más productos </v-btn>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>

    <v-layout id="section__storeInfo" class="section">
      <v-container class="border-radius" fluid my-5 px-4 grid-list-md grey lighten-3>
        <v-layout row wrap align-center justify-space-around
          v-for="(store, i) in content.storeInfo" :key="i">
          <v-flex md3 d-flex justify-center>
            <v-img contain max-width="130px" :src="assets.storeLogo"></v-img>
          </v-flex>
          <v-flex xs8 md7 class="store-info">
            {{ store.info }} "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magnaaliqua. Ut enim ad minim veniam, quis nostrud exercitationullamco laboris nisi ut aliquip ex ea commodo consequat."
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>
  </v-content>
</template>

<style lang="less">
#section__storeBanner {
  .banner-description {
    font-size: 2rem;
    line-height: 36px;
    font-weight: 600;
  }
}

#section__storeInfo {
  .store-info {
    font-size: 1.25rem;
    line-height: 24px;
  }
}

@media only screen and (max-width: 960px) {
  #section__storeBanner {
    .banner-description {
      font-size: 1.5rem;
      line-height: 1.5rem;
    }
  }

  #section__storeInfo {
    .container {
      margin-top: 24px !important;
      margin-bottom: 24px !important;
      .v-image {
        max-height: 100px;
      }
      .store-info {
        font-size: 1rem;
        line-height: 18px;
      }
    }
  }
}

@media only screen and (max-width: 600px) {
  #section__storeBanner {
    .banner-description {
      font-size: 1rem;
      line-height: 1rem;
    }
  }
}
</style>

<script>
import bannerStore from '../../assets/images/fondo_estilos.jpeg'
import storeLogo from '../../assets/images/logo_estilos.png'

import zapatillas01 from '../../assets/images/zapatillas01.png'
import short01 from '../../assets/images/short01.png'
import polo01 from '../../assets/images/polo01.png'
import zapatillas02 from '../../assets/images/zapatillas02.png'
import mochila01 from '../../assets/images/mochila01.png'
import polera01 from '../../assets/images/polera01.png'
import pantalon01 from '../../assets/images/pantalon01.png'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'Store',
  data () {
    return {
      assets: {
        bannerStore: bannerStore,
        storeLogo: storeLogo,
        zapatillas01: zapatillas01,
        short01: short01,
        polo01: polo01,
        zapatillas02: zapatillas02,
        mochila01: mochila01,
        polera01: polera01,
        pantalon01: pantalon01
      },
      filters: {},
      content: {
        banner: {
          carousel: {
            items: [
              { background: bannerStore, description: 'Estilos tiene todos los productos que puedas comprar.' },
              { background: bannerStore, description: 'Estilos tiene todos los productos que puedas comprar.' },
              { background: bannerStore, description: 'Estilos tiene todos los productos que puedas comprar.' }
            ]
          }
        },
        storeInfo: {
          info: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magnaaliqua. Ut enim ad minim veniam, quis nostrud exercitationullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in'
        },
        ourProducts: {
          categoryProduct: {
            1: {
              product: zapatillas02,
              brandTagColor: 'purple',
              brand: 'Nike Perú',
              productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
              finalPrice: '559.12',
              previousPrice: '420'
            },
            2: {
              product: mochila01,
              brandTagColor: 'pink',
              brand: 'Porta Perú',
              productDescription: 'Mochila negra Porta',
              finalPrice: '75.99',
              previousPrice: ''
            },
            3: {
              product: polera01,
              brandTagColor: 'brown',
              brand: 'Adidas Perú',
              productDescription: 'Polera Gris deportiva damas',
              finalPrice: '85',
              previousPrice: ''
            },
            4: {
              product: pantalon01,
              brand: 'ELLE',
              brandTagColor: 'green',
              productDescription: 'Pantalón azul marino para caballeros',
              finalPrice: '85',
              previousPrice: ''
            },
            5: {
              product: zapatillas02,
              brandTagColor: 'purple',
              brand: 'Nike Perú',
              productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
              finalPrice: '559.12',
              previousPrice: '420'
            },
            6: {
              product: mochila01,
              brandTagColor: 'pink',
              brand: 'Porta Perú',
              productDescription: 'Mochila negra Porta',
              finalPrice: '75.99',
              previousPrice: ''
            },
            7: {
              product: polera01,
              brandTagColor: 'brown',
              brand: 'Adidas Perú',
              productDescription: 'Polera Gris deportiva damas',
              finalPrice: '85',
              previousPrice: ''
            },
            8: {
              product: pantalon01,
              brand: 'ELLE',
              brandTagColor: 'green',
              productDescription: 'Pantalón azul marino para caballeros',
              finalPrice: '85',
              previousPrice: ''
            },
            9: {
              product: zapatillas02,
              brandTagColor: 'purple',
              brand: 'Nike Perú',
              productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
              finalPrice: '559.12',
              previousPrice: '420'
            },
            10: {
              product: mochila01,
              brandTagColor: 'pink',
              brand: 'Porta Perú',
              productDescription: 'Mochila negra Porta',
              finalPrice: '75.99',
              previousPrice: ''
            },
            11: {
              product: polera01,
              brandTagColor: 'brown',
              brand: 'Adidas Perú',
              productDescription: 'Polera Gris deportiva damas',
              finalPrice: '85',
              previousPrice: ''
            },
            12: {
              product: pantalon01,
              brand: 'ELLE',
              brandTagColor: 'green',
              productDescription: 'Pantalón azul marino para caballeros',
              finalPrice: '85',
              previousPrice: ''
            }
          }
        }
      }
    }
  },
  computed: {
    ...mapState('brand', {
      brand: 'object'
    })
  },
  watch: {
    $route (val, oldVal) {
      const brandId = this.$route.params.id

      if (brandId) {
        this.getFeaturedBrand({
          id: brandId
        })
      }
    }
  },
  methods: {
    addToChart () { },
    ...mapActions('brand', {
      getFeaturedBrand: 'read'
    })
  },
  created () {
    const brandId = this.$route.params.id

    if (brandId) {
      this.getFeaturedBrand({
        id: brandId
      })
    }
  }
}
</script>
