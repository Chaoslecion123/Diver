<template>
  <v-menu
    offset-y
    content-class="d-category-menu-content"
    class="hidden-sm-and-down d-category-menu"
    v-model="closeMenu"
    :close-on-content-click="false">
    <v-btn
      round
      depressed
      slot="activator"
      style="border-bottom-right-radius: 0; border-top-right-radius: 0;"
      class="d-store-menu-activator accent d-btn d-btn--no-transform d-btn--bold">
      Categorías
      <d-icon
        class="ml-1"
        name="b-down"/>
    </v-btn>
    <v-card>
      <v-content
        fluid
        class="ma-0 pa-0">
        <v-layout>
          <v-flex
            xs12
            class="d-category-menu__colum">
            <div
              class="ma-2">
              <d-categories
                cardHeight="60"
                avatarSize="48"
                @changecollection="changeCollection"/>
            </div>
          </v-flex>
          <!--
          <v-divider
            vertical
            inset/>

          <v-flex
            xs5
            class="d-category-menu__colum">
            <div
              class="ma-2">
              <h2
                class="mb-2">
                {{ category && category.name }}
              </h2>
              <div
                v-for="(item, i) in categoryMenu.categoryList"
                :key="i"
                class="mb-2">
                <p>
                  {{ item.title }}
                </p>
                <div
                  v-for="(item, i) in item.list"
                  :key="i">
                  <a
                    class="black--text text-on-hover">
                    {{ item.item }}
                  </a>
                </div>
              </div>
            </div>
          </v-flex>

          <v-divider vertical inset class="q-red--border"/>

          <v-flex xs5>
            <img style="width:100%;" :src="assets.categoryPromoBanner">
            <v-layout row wrap>
              <v-flex xs6 pa-2 mt-2 v-for="(product, i) in categoryMenu.categoryOfferSales" :key="i">
                <d-product-card class="category-menu--card" :product="product"/>
              </v-flex>
            </v-layout>
          </v-flex>

          -->
        </v-layout>
      </v-content>
      <v-flex px-3 py-2>
        <v-layout row>
        </v-layout>
      </v-flex>
    </v-card>
  </v-menu>
</template>

<style lang="less">
.d-category-menu-content {
  top: 92px !important;
  // left: 48px !important;
  // right: 48px !important;
  position: fixed;
  // max-width: initial;
  max-height: 60vh;
  overflow: hidden;

  .d-category-menu__colum {
    max-height: 60vh;
    overflow: auto;
  }
}

/*
.category-menu--card {
  box-shadow: none !important;
  .card-image {
    height: auto;
    .v-image {
      max-height: 120px !important;
    }
  }
  .v-card__title {
    max-height: 100px;
  }
}
.category-menu.v-menu__content {
  position: fixed;
  top: 92px !important;
  left: 0 !important;
  margin: 0px 48px;
  max-width: none;
  right: 0;
}
.text-on-hover {
  text-decoration: none;
  &:hover {
    color: #f58220 !important;
  }
}
.btn--category {
  .v-btn__content {
    padding-left: 8px;
  }
}
*/
</style>

<script>
import categoryPromoBanner from '../assets/images/category_promo_banner.jpeg'
import product01 from '@/assets/images/quimder/producto1.png'
import product02 from '@/assets/images/quimder/producto2.png'

export default {
  name: 'd-category-menu',
  data () {
    return {
      closeMenu: false,
      category: '',
      assets: {
        categoryPromoBanner: categoryPromoBanner,
        product01: product01,
        product02: product02
      },
      categoryMenu: {
        categoryList: {
          1: {
            title: 'Moda mujer',
            list: [
              { item: 'Vestidos' },
              { item: 'Blusas' },
              { item: 'Tops' },
              { item: 'Chompas' },
              { item: 'Poleras' },
              { item: 'Jeans' },
              { item: 'Pantalones' },
              { item: 'Ropa deportiva' },
              { item: 'Ropa interior' },
              { item: 'Trajes de baño' }
            ]
          },
          2: {
            title: 'Moda Hombre',
            list: [
              { item: 'Terno' },
              { item: 'Camisa' },
              { item: 'Polos' },
              { item: 'Chompas' },
              { item: 'Poleras' },
              { item: 'Jeans' },
              { item: 'Pantalones' },
              { item: 'Ropa deportiva' },
              { item: 'Ropa interior' },
              { item: 'Trajes de baño' }
            ]
          },
          3: {
            title: 'Zapatos Mujer',
            list: [
              { item: 'Urbanos' },
              { item: 'Tacos' },
              { item: 'Zapatillas' },
              { item: 'Balerinas' },
              { item: 'Sandalias' },
              { item: 'Botas y botines' },
              { item: 'Deportivos' }
            ]
          },
          4: {
            title: 'Zapatos Hombre  ',
            list: [
              { item: 'Urbanos' },
              { item: 'Tacos' },
              { item: 'Zapatillas' },
              { item: 'Balerinas' },
              { item: 'Sandalias' },
              { item: 'Botas y botines' },
              { item: 'Deportivos' }
            ]
          }
        },
        categoryOfferSales: {
          1: {
            id: 1,
            new: false,
            discount: null,
            product: product01,
            brandTagColor: null,
            brand: null,
            productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
            finalPrice: '273.12',
            previousPrice: '320'
          },
          2: {
            id: 2,
            new: false,
            discount: null,
            product: product02,
            brandTagColor: null,
            brand: null,
            productDescription: 'Short casual-style deportivo Hombre',
            finalPrice: '76.00',
            previousPrice: '80.00'
          }
        }
      }
    }
  },
  watch: {
    $route (val, oldVal) {
      this.closeMenu = false
    }
  },
  methods: {
    changeCollection (category) {
      this.category = category
    }
  }
}
</script>
