<template>
  <v-content app class="d-page__content d-shoping-cart">
    <transition name="fade">
      <v-container
        v-if="cartReading && !refreshCartAfterCartLineDelete"
        class="mt-5 mb-5 d-shoping-cart__content">
        <v-layout align-center justify-center>
          <v-progress-circular
            :size="90"
            :width="5"
            color="accent"
            indeterminate/>
        </v-layout>
      </v-container>

      <v-container
        v-else
        :fluid="$vuetify.breakpoint.mdAndDown"
        :class="['mt-3', 'mb-5', 'd-shoping-cart__content']">
        <v-layout row wrap>
          <v-flex
            v-if="this.$route.meta && this.$route.meta.breadcrumbs"
            xs12
            mb-4>
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

          <v-flex xs12 mb-4>
            <h2 class="font-weight-bold">
              Mi carrito
            </h2>
          </v-flex>

          <v-flex
            v-if="!cart || cart.quantity === 0"
            xs12
            shrink
            text-xs-center
            class="d-shoping-cart__empty-cart-message grey lighten-4">
            <h2 class="mb-3">
              ¿Aún no tienes productos en el carrito?
            </h2>
            <h3 class="mb-4">
              ¡Visita nuestra tienda y en los productos y compra todo lo que
              quieras!
            </h3>
            <v-btn
              large
              depressed
              color="accent"
              :class="[
                'ma-0',
                'd-btn',
                'd-btn--rounded',
                'd-btn--no-transform',
                'd-btn--bold'
              ]"
              :to="{ name: links.home }">
              <d-icon scale="1.5" name="b-shopping-cart" class="mr-2" />
              Quiero comprar
            </v-btn>
          </v-flex>

          <template v-if="cart && cart.quantity > 0">
            <v-flex xs12>
              <v-container fluid grid-list-xl pa-0>
                <v-layout row wrap>
                  <v-flex xs12 md9 class="d-shoping-cart__product-list">
                    <v-container pa-0 fluid>
                      <v-layout
                        row
                        wrap
                        mx-0
                        mt-0
                        mb-4
                        pa-0
                        grey
                        lighten-4
                        class="d-shoping-cart__product-list-header">
                        <v-flex
                          xs5
                          text-xs-left
                          class="d-shoping-cart__product-list--header-item">
                          Producto
                        </v-flex>
                        <v-flex xs7 align-center>
                          <v-layout row wrap>
                            <v-flex
                              v-if="$vuetify.breakpoint.xs"
                              text-xs-right
                              xs12
                              class="d-shoping-cart__product-list--header-item">
                              Detalles
                            </v-flex>
                            <template v-else>
                              <v-flex
                                text-xs-right
                                xs12
                                sm4
                                class="d-shoping-cart__product-list--header-item">
                                Cant.
                              </v-flex>
                              <v-flex
                                text-xs-right
                                xs12
                                sm3
                                class="d-shoping-cart__product-list--header-item">
                                Precio (S/)
                              </v-flex>
                              <v-flex
                                text-xs-right
                                xs12
                                sm3
                                class="d-shoping-cart__product-list--header-item">
                                Total (S/)
                              </v-flex>
                            </template>
                          </v-layout>
                        </v-flex>
                      </v-layout>

                      <template v-for="(line, i) in cart.lines">
                        <v-layout
                          v-if="line.variant"
                          :key="`item-${i}`"
                          row
                          wrap
                          mx-0
                          mb-0
                          pa-0
                          grey
                          lighten-4
                          :align-center="$vuetify.breakpoint.smAndUp"
                          :class="[
                            'd-shoping-cart__item',
                            {
                              'd-shoping-cart__item-deleting':
                                deleting[line.id] || cartClearing
                            }
                          ]">
                          <v-flex xs5>
                            <v-layout row wrap align-center>
                              <v-flex
                                :xs12="$vuetify.breakpoint.xs"
                                :shrink="$vuetify.breakpoint.smAndUp">
                                <v-img
                                  width="64px"
                                  height="64px"
                                  :src="line.variant.image.image.productSmall2x"/>
                              </v-flex>
                              <v-flex
                                text-xs-left
                                :xs12="$vuetify.breakpoint.xs"
                                :grow="$vuetify.breakpoint.smAndUp">
                                <router-link
                                  :to="{
                                    name: links.productDetail,
                                    params: {
                                      id: line.variant.product.id,
                                      slug: line.variant.product.slug
                                    }
                                  }">
                                  {{ line.variant.displayName }}
                                  <d-icon
                                    name="b-export"
                                    class="fa-icon-text"/>
                                </router-link>
                              </v-flex>
                            </v-layout>
                          </v-flex>
                          <v-flex xs7 align-center>
                            <v-layout
                              row
                              wrap
                              :align-center="$vuetify.breakpoint.smAndUp">
                              <v-flex text-xs-right xs12 sm4>
                                <strong
                                  v-if="$vuetify.breakpoint.xs"
                                  class="d-shoping-cart__label">
                                  <small>
                                    Cant.:
                                  </small>
                                </strong>
                                <span class="d-shoping-cart__value">
                                  <v-toolbar dense flat class="pa-0">
                                    <v-btn
                                      block
                                      depressed
                                      color="accent"
                                      :class="[
                                        'ma-0',
                                        'px-3',
                                        'd-btn',
                                        'd-btn--bold',
                                        'd-btn--no-transform'
                                      ]"
                                      @click="removeOneFromLine(line)">-</v-btn>
                                    <v-text-field
                                      name="quantity"
                                      flat
                                      solo
                                      :class="['d-input', 'd-input--bordered']"
                                      :value="line.quantity"
                                      :readonly="cartLineUpdating"
                                      @change="
                                        updateLineQuantity($event, line.id)
                                      ">
                                    </v-text-field>
                                    <v-btn
                                      block
                                      depressed
                                      color="accent"
                                      :class="[
                                        'ma-0',
                                        'px-3',
                                        'd-btn',
                                        'd-btn--bold',
                                        'd-btn--no-transform'
                                      ]"
                                      @click="addOneToLine(line)">+</v-btn>
                                  </v-toolbar>
                                </span>
                              </v-flex>
                              <v-flex text-xs-right xs12 sm3>
                                <strong
                                  v-if="$vuetify.breakpoint.xs"
                                  class="d-shoping-cart__label">
                                  <small>
                                    Precio:
                                  </small>
                                </strong>
                                <span class="d-shoping-cart__value">
                                  <span v-if="$vuetify.breakpoint.xs">
                                    S/
                                  </span>
                                  <template
                                    v-if="
                                      line.variant &&
                                        line.variant.priceDisplay.displayGross
                                    ">
                                    {{
                                      formatPrice(
                                        line.variant.price.gross.amount
                                      )
                                    }}
                                  </template>
                                  <template v-else>
                                    {{
                                      formatPrice(line.variant.price.net.amount)
                                    }}
                                  </template>
                                </span>
                              </v-flex>
                              <v-divider
                                v-if="$vuetify.breakpoint.xs"
                                class="flex xs12 pa-0"/>
                              <v-flex text-xs-right xs12 sm3>
                                <strong
                                  v-if="$vuetify.breakpoint.xs"
                                  class="d-shoping-cart__label">
                                  <small>
                                    Total:
                                  </small>
                                </strong>
                                <span class="d-shoping-cart__value">
                                  <span v-if="$vuetify.breakpoint.xs">
                                    S/
                                  </span>
                                  <template
                                    v-if="
                                      line.variant &&
                                        line.variant.priceDisplay.displayGross
                                    ">
                                    {{
                                      formatPrice(
                                        line.quantity *
                                          line.variant.price.gross.amount
                                      )
                                    }}
                                  </template>
                                  <template v-else>
                                    {{
                                      formatPrice(
                                        line.quantity *
                                          line.variant.price.net.amount
                                      )
                                    }}
                                  </template>
                                </span>
                              </v-flex>
                              <v-divider
                                v-if="$vuetify.breakpoint.xs"
                                class="flex xs12 pa-0"/>
                              <v-flex xs12 sm2 text-xs-right>
                                <v-btn
                                  :disabled="cartLineDeleting || cartReading"
                                  flat
                                  class="ma-0"
                                  @click="deleteCartLine(line.id)">
                                  <d-icon name="b-trash" />
                                </v-btn>
                              </v-flex>
                            </v-layout>
                          </v-flex>
                        </v-layout>
                      </template>

                      <v-layout
                        row
                        wrap
                        mx-0
                        mb-0
                        pa-0
                        grey
                        lighten-4
                        :align-center="$vuetify.breakpoint.smAndUp"
                        :class="['d-shoping-cart__item']">
                        <v-flex
                          text-xs-right
                          xs12
                          class="d-shoping-cart__product-list--header-item">
                          <v-btn
                            :block="$vuetify.breakpoint.xs"
                            depressed
                            color="accent"
                            :class="[
                              'ma-0',
                              'd-btn',
                              'd-btn--no-transform',
                              'd-btn--rounded',
                              'd-btn--bold'
                            ]"
                            @click="handleClearCart">
                            Limpiar carrito
                            <d-icon name="b-trash" class="ml-2" />
                          </v-btn>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-flex>

                  <v-flex xs12 md3 class="d-shoping-cart__summary">
                    <d-checkout-sumary :cart="true" />
                  </v-flex>
                </v-layout>
              </v-container>
            </v-flex>
          </template>
        </v-layout>
      </v-container>
    </transition>
  </v-content>
</template>

<style lang="less">
.d-shoping-cart {
  .d-shoping-cart__content {
    .d-shoping-cart__empty-cart-message {
      min-height: 300px;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    }
  }

  .d-shoping-cart__product-list {
    .v-btn {
      min-width: auto;
    }

    .d-shoping-cart__product-list--header-item {
      text-transform: uppercase;
      font-weight: bold;
    }

    .d-shoping-cart__item {
      border-radius: 4px;
    }

    .v-toolbar__content {
      padding: 0;
    }
    .d-shoping-cart__item ~ .d-shoping-cart__item {
      margin-top: 1.5rem !important;
    }

    .d-shoping-cart__item-deleting {
      * {
        color: #646464;
      }

      background-image: repeating-linear-gradient(
        -45deg,
        transparent,
        transparent 10px,
        #dedede 10px,
        #dedede 11px
      );
      animation: deleting-cart-line 2s linear infinite;
      background-size: 150% 100%;
    }

    .d-shoping-cart__value {
      min-width: 64px;
      display: inline-block;

      .d-btn {
        &:first-of-type {
          border-radius: 8px 0px 0px 8px !important;
        }

        &:last-of-type {
          border-radius: 0px 8px 8px 0px !important;
        }
      }
      .v-input {
        .v-input__control {
          min-height: auto;
        }
        .v-input__slot {
          border-radius: 0;
          border-left: 0 none;
          border-right: 0 none;
          margin: 0;
          padding: 0 8px !important;
          height: 36px !important;
          background: transparent;

          input {
            text-align: center;
          }
        }
      }
    }
  }
}

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
import { mapState, mapActions } from 'vuex'
import { ROOT } from '@/router'
import { STOREFRONT_PRODUCT } from '@/router/storefront'

export default {
  name: 'Cart',
  data () {
    return {
      refreshCartAfterCartLineDelete: false,
      links: {
        home: ROOT,
        productDetail: STOREFRONT_PRODUCT
      },
      deleting: {}
    }
  },
  computed: {
    ...mapState('cart', {
      cart: 'object',
      cartReading: 'reading',
      cartReadSuccess: 'readSuccess',
      cartToken: 'token',
      cartClearing: 'clear'
    }),
    ...mapState('cart-line', {
      cartLineUpdating: 'updating',
      cartLineUpdateSuccess: 'updateSuccess',
      cartLineDeleting: 'deleting',
      cartLineDeleteSuccess: 'deleteSuccess'
    })
  },
  watch: {
    cartReadSuccess (val, oldVal) {
      if (val) {
        this.refreshCartAfterCartLineDelete = false
      }
    },
    cartLineDeleteSuccess (val, oldVal) {
      if (val) {
        this.refreshCartAfterCartLineDelete = true
        this.refreshCart()
      }
    },
    cartLineUpdateSuccess (val, oldVal) {
      if (val) {
        this.refreshCartAfterCartLineDelete = true
        this.refreshCart()
      }
    }
  },
  methods: {
    ...mapActions('cart', {
      cartRead: 'read',
      cartClear: 'clear'
    }),
    ...mapActions('cart-line', {
      cartLineUpdate: 'update',
      cartLineDelete: 'delete'
    }),

    formatPrice (value) {
      let val = (value / 1).toFixed(2) // .replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
    },

    deleteCartLine (lineId) {
      this.deleting[lineId] = true
      this.cartLineDelete({
        id: lineId
      })
    },
    handleClearCart () {
      this.cartClear({
        id: this.cartToken,
        query: {
          expand: ['lines.variant.image', 'lines.variant.product'].join(','),
          fields: ['token', 'quantity', 'lines'].join(',')
        }
      })
    },
    refreshCart () {
      if (this.cartToken) {
        this.cartRead({
          id: this.cartToken,
          query: {
            expand: ['lines.variant.image', 'lines.variant.product'].join(','),
            fields: ['token', 'quantity', 'lines'].join(',')
          }
        })
      }
    },
    removeOneFromLine (line) {
      if (line.quantity > 1) {
        this.updateLineQuantity(line.quantity - 1, line.id)
      }
    },
    addOneToLine (line) {
      this.updateLineQuantity(line.quantity + 1, line.id)
    },
    updateLineQuantity (value, lineId) {
      if (value && lineId) {
        this.cartLineUpdate({
          id: lineId,
          data: {
            quantity: value
          }
        })
      }
    }
  },
  created () {
    this.refreshCart()
  }
}
</script>
