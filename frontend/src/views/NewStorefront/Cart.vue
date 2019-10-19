<template>
  <v-content>
    <v-layout id="section__cart" class="section">
      <v-container fluid pa-0 my-4>
        <v-layout row wrap mb-3>
          <v-flex xs12 md9>
            <v-flex mb-3>
              <h2 class="text-uppercase headline font-weight-bold" >MI CARRITO</h2>
            </v-flex>
            <v-flex class="hidden-sm-and-up mb-2">PRODUCTOS:</v-flex>
            <v-container
              pa-2
              class="hidden-xs-only"
              v-if="cartProductsCount !== 0">
              <v-layout style="font-size:0.875rem" row wrap fill-height align-center justify-space-between text-xs-center mb-2 mr-5>
                <v-flex class="font-weight-600" xs4 sm2 md2>PRODUCTO</v-flex>
                <v-flex class="font-weight-600" sm4 md4></v-flex>
                <v-flex class="font-weight-600" sm1 md1>PRECIO</v-flex>
                <v-flex class="font-weight-600" sm1 md1>CANT.</v-flex>
                <v-flex class="font-weight-600" sm1 md1>TOTAL</v-flex>
              </v-layout>
            </v-container>
            <v-flex class="item-card" mb-2 v-for="(line, i) in cart.items" :key="i">
              <v-card flat color="grey lighten-4">
                <v-container pa-2>
                  <v-layout row wrap fill-height align-center justify-space-between text-xs-center mr-5>
                    <v-flex xs4 sm2 md2>
                      <v-img max-height="100" contain :src="line.product.image.image.thumbnail"></v-img>
                    </v-flex>
                    <v-divider vertical class="mx-2" style="height:auto; border-color:#000"></v-divider>
                    <v-flex xs7 sm3 md3 class="product-description text-xs-left">
                      <span class="my-2 font-weight">{{line.product.name}}</span>
                    </v-flex>
                    <v-flex sm1 md1 my-2>
                      <v-flex class="hidden-sm-and-up mt-2">Precio unit:</v-flex>
                      <span class="my-2 font-weight">S/{{ line.variant.priceRange.start.net.amount }}</span>
                    </v-flex>
                    <v-flex sm1 md1 my-2>
                      <!--v-text-field
                        class="input__number ma-0 pa-0"
                        type="number"
                        :value="line.quantity"
                        hide-details
                        solo
                        flat/-->
                        <v-flex class="mt-2 hidden-sm-and-up">Cant.</v-flex>
                        <span class="my-2 font-weight">{{line.quantity}}</span>
                    </v-flex>
                    <v-flex sm1 md1 my-2>
                      <v-flex class="hidden-sm-and-up mt-2">Total:</v-flex>
                        <span class="font-weight"> S/{{ line.variant.priceRange.start.net.amount * line.quantity }} </span>
                    </v-flex>
                    <v-btn
                      @click="removeFromCart"
                      icon
                      absolute
                      right
                      class="ma-0 close-btn">
                      <!--v-icon class="d-red--text">close</v-icon-->
                      <d-icon class="d-red--text" name="b-close"/>
                    </v-btn>
                  </v-layout>
                </v-container>
              </v-card>
            </v-flex>
            <v-layout v-if="cartProductsCount == 0" class="no--items grey lighten-4" row wrap align-center justify-center>
              <v-card flat color="transparent">
                <v-flex shrink fill-height text-xs-center>
                  <span>¿Aún no tienes productos en el carrito?</span> <br>
                  <span>¡Dale click al
                    <d-icon
                     style="vertical-align: sub;"
                     class="q-disabled--text"
                     scale="2"
                     name="b-shopping-cart"/>
                      en los productos y compra todo lo que quieras!
                  </span>
                </v-flex>
              </v-card>
            </v-layout>
          </v-flex>
          <v-flex class="remove-padding set-margin-y-3" pl-3 md3>
            <d-checkout-sumary :cart="true"/>
          </v-flex>
        </v-layout>
        <v-layout row wrap id="section__recentproducts" v-if="relatedProducts">
          <v-flex xs12 mb-3>
            <h2 class="text-uppercase headline font-weight-bold">PRODUCTOS VISTOS RECIENTEMENTE</h2>
          </v-flex>
          <v-flex>
            <v-container fluid grid-list-md pa-0 ma-0>
              <v-layout row wrap>
                <v-flex xs6 sm4 md3 my-1 v-for="(product, i) in relatedProducts" :key="i">
                  <d-product-card :product="product"/>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>
  </v-content>
</template>

<style lang="less">
#section__cart {
  .input__number {
    .v-input__control {
      align-items: center;
      .v-input__slot {
        width: 48px;
        padding: 0 8px;
        border: 1px solid black !important;
        border-radius: 5px;
      }
    }
  }
}

@media screen and (max-width: 600px) {
  .close-btn {
    position: absolute;
    top: 0;
    right: 0;
    i {
      font-size: 1.5rem;
    }
  }
  .font-weight {
    font-weight: 600;
  }
  .card-buttons {
    margin-top: 8px;
    margin-bottom: 8px;
    .v-btn {
      height: 30px;
    }
  }
}
</style>

<script>
import product01 from '@/assets/images/quimder/producto1.png'
import product02 from '@/assets/images/quimder/producto2.png'
import product03 from '@/assets/images/quimder/producto3.png'
import product04 from '@/assets/images/quimder/producto4.png'
import product05 from '@/assets/images/quimder/producto5.png'
import product06 from '@/assets/images/quimder/producto6.png'
import product07 from '@/assets/images/quimder/producto7.png'

import { mapState, mapGetters } from 'vuex'

export default {
  name: 'Cart',
  data () {
    return {
      assets: {
        product01: product01,
        product02: product02,
        product03: product03,
        product04: product04,
        product05: product05,
        product06: product06,
        product07: product07
      },
      content: {
        collectionItem: {
          1: {
            product: product01,
            productDescription: 'Quiksilver-zapatillas azul/blancas Hombre',
            productSize: '41',
            productColor: 'blue',
            finalPrice: '559.12',
            finalTotalPrice: '559.12'
          },
          2: {
            product: product02,
            productDescription: 'Mochila negra Porta',
            productSize: 'Grande',
            productColor: 'black',
            finalPrice: '100',
            finalTotalPrice: '100'
          },
          3: {
            product: product03,
            productDescription: 'Polera Gris deportiva damas',
            productSize: 'XL',
            productColor: 'gray',
            finalPrice: '89.90',
            finalTotalPrice: '89.90'
          },
          4: {
            product: product04,
            productDescription: 'Pantalón azul marino para caballeros',
            productSize: '28',
            productColor: '#000080',
            finalPrice: '160',
            finalTotalPrice: '160'
          }
        },
        orderDetails: {
          1: {
            productsQuantity: '03',
            orderPrice: '635.11',
            orderDiscount: '10%',
            shippingPrice: 'Gratis',
            finalOrderPrice: '571.99'
          }
        },
        ourProducts: {
          categoryProduct: {
            1: {
              product: product05,
              brandTagColor: 'purple',
              brand: 'Nike Perú',
              productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
              finalPrice: '559.12',
              discount: true,
              previousPrice: '420'
            },
            2: {
              product: product06,
              brandTagColor: 'pink',
              brand: 'Porta Perú',
              productDescription: 'Mochila negra Porta',
              finalPrice: '75.99',
              previousPrice: ''
            },
            3: {
              product: product07,
              brandTagColor: 'brown',
              brand: 'Adidas Perú',
              productDescription: 'Polera Gris deportiva damas',
              finalPrice: '85',
              previousPrice: ''
            },
            4: {
              product: product01,
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
    ...mapState('cart', {
      'cart': 'cart'
    }),
    ...mapGetters('cart', {
      cartProductsCount: 'productsCount'
    }),
    relatedProducts () {
      const { cart } = this
      let products = []

      for (let i in cart.items) {
        const product = cart.items[i].product

        for (let j in product.relatedProducts) {
          const relatedProduct = product.relatedProducts[j]
          const index = products.findIndex(item => item.id === relatedProduct.id)

          if (index < 0) {
            products.push(relatedProduct)
          }
        }
      }

      return products
    }
  },
  methods: {
    addToChart () {
      alert('Has agregado un producto al carrito :D')
    },
    removeFromCart (i) {
      // this.$delete(this.content.collectionItem, i)
    }
  }
}
</script>
