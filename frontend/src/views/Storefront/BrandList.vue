<template>
  <v-content
    app
    class="d-brand-view">
    <v-layout id="section__brandBanner">
      <carousel
        class="CarouselBanner"
        :perPage="1"
        :autoplay="false"
        :loop="true"
        :paginationEnabled="false">
        <slide>
          <v-layout row wrap align-center fill-height style="position:absolute; z-index:999; width:100vw;">
            <v-flex md6 offset-md1 xs6 offset-xs1>
              <v-card flat color="transparent">
                <v-flex class="black--text banner-description">
                  <strong>Lo mejor para tu piel</strong>
                  de las marcas más prestigiosas a nivel mundial.
                </v-flex>
              </v-card>
            </v-flex>
          </v-layout >
          <v-img width="100vw" :src="assets.bannerBrand"></v-img>
        </slide>
      </carousel>
    </v-layout>

    <v-container
      fluid
      class="d-container d-container--full-fluid d-container--full-width">
      <v-layout
        class="d-header grey lighten-2"
        align-center
        justify-center>
        <h1>
          Los mejores productos de las mejores marcas
        </h1>
      </v-layout>
    </v-container>

    <v-container
      v-if="featuredBrands && featuredBrands.items && featuredBrands.items.length > 0"
      grid-list-lg>
      <v-layout
        row
        wrap
        align-content-center>
        <v-flex
          xs12>
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

        <v-flex
          xs12>
          <h2
            class="text-xs-center text--uppercase mb-4">
            Marcas destacadas
          </h2>
        </v-flex>
        <v-flex
          xs12>
          <d-brand-featured-carousel/>
        </v-flex>
      </v-layout>
    </v-container>

    <v-container
      v-if="brands && brands.items && brands.items.length > 0"
      grid-list-lg
      align-center>
      <v-layout
        row
        wrap>
        <v-flex
          xs12>
          <h2
            class="text-xs-center text--uppercase mb-4">
            Todas las marcas
          </h2>
        </v-flex>
        <v-flex
          v-for="brand in brands.items"
          :key="brand.id"
          xs2
          sm4
          md4
          lg2
          text-xs-center>
          <v-card flat hover class="d-flex justify-center" height="100">
            <v-img contain height="100%" max-width="180px" :src="brand.image"></v-img>
          </v-card>
        </v-flex>
        <v-flex
          xs12
          text-xs-center>
          <v-pagination
            v-if="brands && brands.meta"
            v-model="page"
            color="accent"
            :length="brands.meta.pages"
            :total-visible="4"
            @input="refreshBrands"/>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<style lang="less">
.d-brand-view {
  .d-header {
    min-height: 100px;
  }
}
</style>

<script>
import { mapState, mapActions } from 'vuex'
import bannerBrand from '@/assets/images/banner_tiendas.jpeg'
import { STOREFRONT_BRAND } from '@/router/storefront'

export default {
  name: 'Brand',
  data () {
    return {
      links: {
        brandDetail: STOREFRONT_BRAND
      },
      assets: {
        bannerBrand: bannerBrand
      },
      page: 1
    }
  },
  computed: {
    ...mapState('brand', {
      brands: 'objects',
      featuredBrands: 'featuredObjects'
    }),
    brandQuery () {
      return {
        page: this.page,
        fields: [
          'id',
          'name',
          'slug',
          'image'
        ].join(',')
      }
    }
  },
  methods: {
    ...mapActions('brand', {
      getBrandList: 'list'
    }),
    refreshBrands () {
      this.getBrandList({
        query: this.brandQuery
      })
    }
  },
  created () {
    this.getBrandList({
      query: this.brandQuery
    })
  }
}
</script>
