<template>
  <v-menu
    v-if="!featuredBrandList || ((featuredBrandList && featuredBrandList.items) && featuredBrandList.items.length)"
    offset-y
    content-class="d-store-menu-content"
    class="hidden-sm-and-down d-store-menu"
    v-model="isClose"
    :close-on-content-click="false">
    <v-btn
      round
      depressed
      outline
      slot="activator"
      class="d-store-menu-activator d-btn--no-transform d-btn--bold">
      Marcas
    </v-btn>

    <v-card>
      <v-container
        fluid
        grid-list-xl>
        <v-layout
          row
          wrap
          align-center
          justify-center>
          <v-flex xs12>
            <h3
              class="text-xs-center">
              MARCAS DESTACADAS
            </h3>
          </v-flex>
          <v-flex
            v-for="(brand, i) in featuredBrands"
            :key="i"
            shrink
            fill-height
            class="d-store-menu-item">
            <router-link
              class="d-block pa-1"
              :to="{
                name: 'FeaturedBrandProducts',
                params: {
                  id: brand.id
                }
              }">
              <v-img :src="brand.image"/>
            </router-link>
          </v-flex>
          <v-flex
            xs12
            text-xs-center>
            <v-btn
              depressed
              outline
              color="accent"
              class=""
              :to = "{ name: links.brand }">
              Ver Todo
            </v-btn>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-menu>
</template>

<style lang="less">
.d-store-menu-content {
  top: 92px !important;
  left: 48px !important;
  right: 48px !important;
  position: fixed;
  max-width: initial;

  .d-store-menu-item {
    width: 140px;
  }
}
</style>

<script>
import { mapState, mapActions } from 'vuex'
import { STOREFRONT_BRAND_LIST } from '@/router/storefront'

export default {
  name: 'd-store-menu',
  data () {
    return {
      links: {
        brand: STOREFRONT_BRAND_LIST
      },
      isClose: false
    }
  },
  computed: {
    ...mapState('brand', {
      featuredBrandList: 'objects'
    }),
    featuredBrands () {
      if (this.featuredBrandList && this.featuredBrandList.meta) {
        if (this.featuredBrandList.meta.count >= 1) {
          return this.featuredBrandList.items
        }
      }
      return null
    }
  },
  watch: {
    $route (val, oldVal) {
      this.isClose = false
    },
    '$vuetify.breakpoint' (val, oldVal) {
      this.isClose = false
    }
  },
  methods: {
    ...mapActions('brand', {
      getFeaturedBrand: 'list'
    })
  },
  created () {
    this.getFeaturedBrand({
      query: {
        isFeatured: true
      }
    })
  }
}
</script>
