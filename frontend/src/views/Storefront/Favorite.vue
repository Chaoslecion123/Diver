<template>
  <v-content class="d-page__content d-overide">
    <v-layout id="section__favorite" class="section">
      <v-container fluid pa-0 my-4>
        <v-layout row wrap mb-3>
          <v-flex md2 class="hidden-sm-and-down">
            <v-flex mb-3>
              <h2 class="text-uppercase headline font-weight-bold">FAVORITOS</h2>
            </v-flex>
            <v-card hover @click="openAddCollection"  height="80" flat color="grey lighten-4">
              <v-card-title class="pa-3 fill-height" primary-title>
                <v-layout row justify-space-between>
                  <v-icon class="mr-2">add</v-icon>
                  <v-flex class="body-2 text-xs-center" style="line-height:24px;">Agregar colección</v-flex>
                  <d-popup
                    v-model="addCollectionPopupIsOpen"
                    width="500"
                    :onOk="addCollection">
                    <slot>
                      <div>Agregar colección</div>
                    </slot>
                    <v-container fluid pa-0 grid-list-md slot="content">
                      <v-layout row wrap>
                        <v-flex xs12 pa-0 mx-3>
                          <v-form
                            lazy-validation
                            ref="addCollectionForm">
                            <v-text-field
                              v-model="collectionName"
                              class="pt-4 border-radius"
                              :rules="[rules.required]"
                              placeholder="Escribe el nombre para tu nueva colección"
                              hide-details
                              outline
                              validate-on-blur
                              flat
                              required
                              type="text"/>
                          </v-form>
                        </v-flex>
                      </v-layout>
                    </v-container>
                    <div slot="button">Aceptar</div>
                  </d-popup>
                </v-layout>
              </v-card-title>
            </v-card>
            <v-card hover flat color="grey lighten-4" v-for ="(collection, i) in content.collection" :key="i">
              <v-card-title class="my-2 pa-3" primary-title>
                <v-flex xs12 style="font-weight:600;" class="subheading">{{ collection.name }}</v-flex>
                <v-flex grow class="body-2">{{ collection.items }}</v-flex>
                <v-flex shrink text-xs-right>
                  <v-btn
                    class="ma-0 delete-btn"
                    @click="delCollection(i)"
                    flat
                    icon>
                    <d-icon color="#FF0046" name="b-trash"/>
                  </v-btn>
                </v-flex>
              </v-card-title>
            </v-card>
          </v-flex>
          <v-flex xs12 md10 pl-4 class="remove-padding">
            <v-flex>
              <v-container fluid pa-0 ma-0 grid-list-sm>
                <v-layout row wrap align-center>
                  <h2 class="hidden-sm-and-down headline mb-3 font-weight-600">Colección Uno</h2>
                  <v-flex xs12 class="hidden-md-and-up">
                    <h2 class="text-uppercase headline font-weight-bold">MIS FAVORITOS</h2>
                  </v-flex>
                  <v-layout row wrap align-center class="hidden-md-and-up">
                    <v-flex xs8 md8 v-for="(item, i) in content.favoriteFilter" :key="i">
                      <v-menu
                        offset-y
                        full-width
                        transition="slide-y-transition"
                        bottom>
                        <v-btn
                          depressed
                          outline
                          block
                          class="ma-0"
                          style="border-radius: 4px; height:30px;"
                          slot="activator"
                          color="black">
                          {{item.filter}}
                          <d-icon right class="ml-2" medium name="b-down"/>
                        </v-btn>
                        <v-list>
                          <v-list-tile>
                            <v-list-tile-title>Holi, aquí selecciona tu filtro</v-list-tile-title>
                          </v-list-tile>
                        </v-list>
                      </v-menu>
                    </v-flex>
                    <v-flex xs4>
                      <v-btn style="height:30px;" class="q-orange--background" dark block >
                        <v-icon right class="mr-2">add</v-icon> Colección
                      </v-btn>
                    </v-flex>
                  </v-layout>
                  <v-flex xs12 mb-2>
                    <v-card flat color="grey lighten-4">
                      <v-container pa-2>
                        <v-layout row wrap>
                          <v-spacer class="hidden-md-and-up"/>
                          <v-flex xs12 md6 pa-0 align-self-center>
                            <v-layout row wrap>
                              <v-checkbox v-model="content.allCheck" class="my-0 py-0 mx-2"/>
                              <v-btn flat icon :ripple="false" class="ma-0 delete-btn">
                                <d-icon name="b-trash"/>
                              </v-btn>
                            </v-layout>
                          </v-flex>
                          <v-spacer class="hidden-sm-and-down"/>
                          <v-flex xs2 pa-0 class="hidden-sm-and-down">
                            <v-btn
                              @click="moveCollectionPopupIsOpen = true"
                              style="height:28px;"
                              class="border-radius font-weight-600 ma-0"
                              block
                              depressed
                              dark
                              color="#212121">
                              Mover a
                            </v-btn>
                            <d-popup
                              v-model="moveCollectionPopupIsOpen"
                              width="800"
                              :onOk="moveCollection">
                              <slot>
                                <div>Selecciona tu colección</div>
                              </slot>
                              <v-container fluid pa-0 grid-list-md slot="content">
                                <v-radio-group
                                  class="ma-0"
                                  hide-details
                                  v-model="chooseCollection">
                                  <v-layout row wrap>
                                    <v-flex xs4 align-self-center
                                      v-for="(item,i) in content.collection"
                                      :key="i">
                                      <v-card
                                        flat
                                        class="pa-3 border-radius"
                                        color="grey lighten-3">
                                        <v-layout row wrap>
                                          <v-radio
                                            :value="item.name"
                                            class="ma-0"/>
                                          <v-flex align-self-center>{{item.name}}</v-flex>
                                        </v-layout>
                                      </v-card>
                                    </v-flex>
                                  </v-layout>
                                </v-radio-group>
                              </v-container>
                              <div slot="button">Hecho</div>
                            </d-popup>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-card>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-flex>
            <v-flex class="item-card" mb-2 v-for="(item, i) in content.collectionItem" :key="i">
              <v-card flat color="grey lighten-4">
                <v-container pa-2>
                  <v-layout row wrap fill-height align-center justify-space-between>
                    <v-checkbox :value="item.checked" @check="handleCheck(i)" class="ml-2 my-0 hidden-sm-and-down"/>
                    <v-flex xs4 sm2 md2>
                      <v-img max-height="100" contain :src="item.product"></v-img>
                    </v-flex>
                    <v-divider vertical inset class="mx-2 my-0" style="height: auto; border-color: black; border-width: .5px;"/>
                    <v-flex xs6 sm5 md5 class="set-margin-right-4-600">
                      <v-flex>
                        <span class="product-description">{{item.productDescription}}</span>
                      </v-flex>
                      <v-flex mb-2>
                        <span class="grey--text product-brand">
                          <v-icon style="line-height:15px;" :color="item.brandTagColor" size="14">fiber_manual_record</v-icon>
                          {{item.brand}}
                        </span>
                      </v-flex>
                      <v-flex pa-0>
                        <span class="product-final-price">S/{{item.finalPrice}}</span>
                        <span class="ml-3 grey--text text--darken-1 product-previous-price" v-if="item.discount == true">S/<del>{{item.previousPrice}}</del></span>
                      </v-flex>
                    </v-flex>
                    <v-flex xs12 sm3 md3>
                      <v-container fluid pa-0 grid-list-md>
                        <v-layout row wrap class="card-buttons">
                          <v-flex xs5 sm12>
                            <v-btn block style="background-color: #ffffff!important;" outline>Detalles</v-btn>
                          </v-flex>
                          <!--v-flex xs3 sm5>
                            <v-btn
                              style="background-color: #ffffff!important;"
                              :ripple="false"
                              block
                              outline>
                              <v-text-field
                                class="ma-0 pa-0 input__number"
                                type="number"
                                value="1"
                                hide-details
                                solo
                                flat
                              ></v-text-field>
                            </v-btn>
                          </v-flex-->
                          <v-flex xs5 sm12>
                            <v-btn class="q-orange--background" dark block >
                              Añadir
                              <d-icon
                              class="ml-3"
                              scale="1.5"
                              name="b-shopping-cart"/>
                            </v-btn>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-flex>
                    <v-btn
                      icon
                      @click="delItem(i)"
                      :ripple="false"
                      class="ma-0 close-btn">
                      <d-icon class="d-red--text" name="b-close"/>
                    </v-btn>
                  </v-layout>
                </v-container>
              </v-card>
            </v-flex>
            <!--v-layout class="no--items grey lighten-4" row wrap align-center justify-center>
              <v-card flat color="transparent">
                <v-flex shrink fill-height text-xs-center>
                  <span>¿Aún no tienes productos favoritos?</span> <br>
                  <span>¡Dale click al
                    <d-icon
                     style="vertical-align: sub;"
                     class="q-disabled--text"
                     scale="2"
                     name="b-heart-fill"/>
                      en los productos y añade esos todos los que gustes!
                  </span>
                </v-flex>
              </v-card>
            </v-layout-->
          </v-flex>
        </v-layout>
        <v-layout row wrap id="section__recentproducts">
          <v-flex xs12 mb-3>
            <h2 class="text-uppercase headline font-weight-bold">PRODUCTOS VISTOS RECIENTEMENTE</h2>
          </v-flex>
          <v-flex>
            <v-container fluid grid-list-md pa-0 ma-0>
              <v-layout row wrap>
                <v-flex xs6 sm4 md3 my-1 v-for="(product, i) in content.ourProducts.categoryProduct" :key="i">
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
#section__favorite {
  .delete-btn {
    height: 30px !important;
    width: auto;
    .fa-icon:hover {
      color: red;
    }
  }
  .v-input {
    height: auto !important;
    min-height: auto !important;
    .v-input__slot {
      height: auto !important;
      min-height: auto !important;
    }
  }
  .v-input--checkbox {
    flex: none;
    .v-input__slot {
      margin: 0 !important;
      .v-input--selection-controls__input {
        margin: 0;
      }
    }
    .v-messages {
      display: none;
    }
  }
  .card-buttons {
    .v-input__control {
      min-height: 32px;
      .v-input__slot {
        padding: 0;
        input {
          text-align: center;
        }
      }
    }
  }
}
@media screen and (max-width: 600px) {
  .card-buttons {
    margin-top: 8px;
    margin-bottom: 8px;
    .v-btn {
      height: 30px;
      .v-input__control {
        min-height: 24px !important;
        height: 24px;
      }
    }
  }
  .close-btn,
  .close-btn:hover,
  .close-btn:active {
    top: 0 !important;
    margin-right: 8px !important;
  }
}
</style>

<script>
import { mapGetters } from 'vuex'

import product01 from '@/assets/images/quimder/producto1.png'
import product02 from '@/assets/images/quimder/producto2.png'
import product03 from '@/assets/images/quimder/producto3.png'
import product04 from '@/assets/images/quimder/producto4.png'
import product05 from '@/assets/images/quimder/producto5.png'
import product06 from '@/assets/images/quimder/producto6.png'
import product07 from '@/assets/images/quimder/producto7.png'

export default {
  name: 'Favorite',
  data () {
    return {
      rules: {
        required: value => !!value || 'Este campo es requerido.'
      },
      chooseCollection: null,
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
        allCheck: false,
        collection: [
          {
            name: 'Collección Uno',
            items: '11 productos'
          },
          {
            name: 'Collección Dos',
            items: '8 productos'
          },
          {
            name: 'Collección Tres',
            items: '20 productos'
          },
          {
            name: 'Collección Cuatro',
            items: '5 productos'
          },
          {
            name: 'Collección Cinco',
            items: '12 productos'
          }
        ],
        favoriteFilter: {
          1: {
            filter: 'Colección uno'
          }
        },
        collectionItem: {
          1: {
            checked: false,
            product: product01,
            brandTagColor: 'purple',
            brand: 'Nike Perú',
            productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
            finalPrice: '559.12',
            discount: true,
            previousPrice: '420'
          },
          2: {
            checked: false,
            product: product02,
            brandTagColor: 'pink',
            brand: 'Porta Perú',
            productDescription: 'Mochila negra Porta',
            finalPrice: '75.99',
            previousPrice: ''
          },
          3: {
            checked: false,
            product: product03,
            brandTagColor: 'brown',
            brand: 'Adidas Perú',
            productDescription: 'Polera Gris deportiva damas',
            finalPrice: '85',
            discount: true,
            previousPrice: '120'
          },
          4: {
            checked: false,
            product: product04,
            brand: 'ELLE',
            brandTagColor: 'green',
            productDescription: 'Pantalón azul marino para caballeros',
            finalPrice: '85',
            discount: true,
            previousPrice: '100'
          },
          5: {
            checked: false,
            product: product05,
            brandTagColor: 'purple',
            brand: 'Nike Perú',
            productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
            finalPrice: '559.12',
            discount: true,
            previousPrice: '420'
          }
        },
        ourProducts: {
          categoryProduct: {
            1: {
              product: product06,
              brandTagColor: 'purple',
              brand: 'Nike Perú',
              productDescription: 'Quiksilver-zapatillas azul blanca Hombre',
              finalPrice: '559.12',
              discount: true,
              previousPrice: '420'
            },
            2: {
              product: product07,
              brandTagColor: 'pink',
              brand: 'Porta Perú',
              productDescription: 'Mochila negra Porta',
              finalPrice: '75.99',
              previousPrice: ''
            },
            3: {
              product: product01,
              brandTagColor: 'brown',
              brand: 'Adidas Perú',
              productDescription: 'Polera Gris deportiva damas',
              finalPrice: '85',
              previousPrice: ''
            },
            4: {
              product: product02,
              brand: 'ELLE',
              brandTagColor: 'green',
              productDescription: 'Pantalón azul marino para caballeros',
              finalPrice: '85',
              previousPrice: ''
            }
          }
        }
      },
      addCollectionPopupIsOpen: false,
      moveCollectionPopupIsOpen: false,
      activate: false
    }
  },
  computed: {
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    })
  },
  watch: {
    'content.allCheck' (val, oldVal) {
      for (let i in this.content.collectionItem) {
        this.content.collectionItem[i].checked = val
      }
    }
  },
  methods: {
    addToChart () {
      alert('Has agregado un producto al carrito :D')
    },
    addCollection () {
      if (this.$refs.addCollectionForm.validate()) {
        this.addCollectionPopupIsOpen = false
        this.content.collection.push({
          name: this.collectionName,
          items: '0 productos'
        })
      }

      this.$refs.addCollectionForm.reset()
    },
    openAddCollection () {
      if (this.isAuthenticated) {
        this.addCollectionPopupIsOpen = true
      } else {
        this.$router.replace({ name: this.$route.name, query: { login: true } })
      }
    },
    moveCollection () {
      this.moveCollectionPopupIsOpen = false
    },
    handleCheck (i) {
      this.content.collectionItem[i].checked = this.content.collectionItem[i].checked
      if (this.content.allCheck && this.content.collectionItem[i].checked) {
        this.content.allCheck = false
      }
    },
    delCollection (i) {
      this.$delete(this.content.collection, i)
    },
    delItem (i) {
      this.$delete(this.content.collectionItem, i)
    }
  }
}
</script>
