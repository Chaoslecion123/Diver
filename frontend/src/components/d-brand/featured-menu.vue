<template>
  <v-menu
    v-if="brands && brands.items && brands.items.length > 0"
    offset-y
    content-class="d-brand-menu-content"
    class="hidden-sm-and-down d-brand-menu"
    v-model="isClose"
    :close-on-content-click="false">
    <v-btn
      round
      depressed
      outline
      slot="activator"
      class="d-brand-menu-activator d-btn--no-transform d-btn--bold">
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
          <!-- v-flex
            v-for="(brand, i) in featuredBrands"
            :key="i"
            shrink
            fill-height
            class="d-brand-menu-item">
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
          </v-flex -->
          <v-flex
            xs12>
            <d-brand-featured-carousel/>
          </v-flex>
          <v-flex
            xs12
            text-xs-center>
            <v-btn
              depressed
              outline
              color="accent"
              class=""
              :to="{ name: links.brandList }">
              Ver Todo
            </v-btn>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-menu>
</template>

<style lang="less">
.d-brand-menu-content {
  top: 92px !important;
  left: 48px !important;
  right: 48px !important;
  position: fixed;
  max-width: initial;

  .d-brand-menu-item {
    width: 140px;
  }
}
</style>

<script>
import { mapState } from 'vuex'
import { STOREFRONT_BRAND_LIST } from '@/router/storefront'

export default {
  name: 'd-brand-menu',
  data () {
    return {
      links: {
        brandList: STOREFRONT_BRAND_LIST
      },
      isClose: false
    }
  },
  computed: {
    ...mapState('brand', {
      brands: 'featuredObjects'
    })
  },
  watch: {
    $route (val, oldVal) {
      this.isClose = false
    },
    '$vuetify.breakpoint' (val, oldVal) {
      this.isClose = false
    }
  }
}
</script>
