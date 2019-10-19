<template>
  <v-content app class="d-product-detail">
    <v-container class="mt-5 mb-5 d-product-detail__content" grid-list-md>
    <v-flex
          xs12>
          <v-breadcrumbs v-if="breadcrumbs" :items="breadcrumbs" class="pa-0 mb-4">
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

      <transition name="fade">
        <v-layout v-if="productReading" align-center justify-center>
          <v-progress-circular
            :size="90"
            :width="5"
            color="accent"
            indeterminate>
          </v-progress-circular>
        </v-layout>
        <v-layout v-else row wrap>
          <v-flex xs12 md6>
            <d-product-showcase
              :images="product.images"
              :video="product.video"
              :extraImage="view"/>
          </v-flex>
          <v-flex xs12 md6>
            <v-card flat>
              <v-card-title class="pb-0">
                <h1>
                  {{ product.name }}

                </h1>
              </v-card-title>

              <v-card-text class="pb-0">
                <v-rating :value="product.score" class="d-rating">
                  <v-icon
                    class="pa-0"
                    slot="item"
                    slot-scope="props"
                    color="#ffeb3b"
                    large
                    @click="props.click">
                    {{ props.isFilled ? 'star' : 'star_border' }}
                  </v-icon>
                </v-rating>
              </v-card-text>

              <v-card-text class="pb-0">
                <d-product-attributes
                  :variantPickerData="product.variantPickerData"
                  @changeview="handleViewChange"
                  @change="handleVariantChange"/>
              </v-card-text>

              <v-divider light />

              <v-card-text v-if="price" class="pb-0 text-xs-right">
                <strong style="float: left;">
                  Precio
                </strong>

                <div
                  class="product-final-price headline font-weight-bold text-xs-right">
                  <span v-if="price.currency === 'PEN'">S/ </span>
                  <span>{{ formatPrice(price.gross) }}</span>
                  <span v-if="price.currency !== 'PEN'">{{
                    price.currency
                  }}</span>
                </div>
                <div
                  v-if="
                    priceUndiscounted && priceUndiscounted.gross !== price.gross
                  "
                  class="text-xs-right">
                  <del>
                    <span v-if="priceUndiscounted.currency === 'PEN'">S/ </span>
                    {{ formatPrice(priceUndiscounted.gross) }}
                    <span v-if="priceUndiscounted.currency !== 'PEN'">{{
                      priceUndiscounted.currency
                    }}</span>
                  </del>
                </div>
              </v-card-text>

              <v-card-text class="d-overide">
                <d-product-quantity @change="handleUpdateQuantity" />
              </v-card-text>

              <v-card-text class="py-0">
                <v-btn
                  block
                  outline
                  color="accent"
                  :loading="addingToCart"
                  :disabled="variantNotAvailable || addingToCart"
                  class="border-radius"
                  @click.stop="handleAddToCart">
                  Añadir al carrito
                </v-btn>
              </v-card-text>
            </v-card>
          </v-flex>

          <v-flex xs12 v-if="$vuetify.breakpoint.smAndUp">
            <v-tabs fixed-tabs v-model="tab">
              <v-tab key="details">
                ¿Es para mí?
              </v-tab>
              <v-tab key="specs">
                Conoce el producto
              </v-tab>
              <v-tab key="comments">
                Comentarios
              </v-tab>
            </v-tabs>

            <v-divider />

            <v-tabs-items v-model="tab">
              <v-tab-item key="details">
                <v-container>
                  <div v-html="product.description" />
                </v-container>
              </v-tab-item>

              <v-tab-item key="specs">
                <v-container>
                  <div v-html="product.specs" />
                </v-container>
              </v-tab-item>

              <v-tab-item key="comments">
                <v-container>
                  <h3
                    v-if="
                      customerReviewList.items &&
                        customerReviewList.items.length === 0
                    "
                    xs12
                    class="d-product--be-fisrt-commnet">
                    Se el primero en comentar
                  </h3>

                  <d-add-comment @review="appendReview" />

                  <d-comment-box
                    v-for="(comment, i) in customerReviewList.items"
                    :key="i"
                    :comment="comment"/>
                </v-container>
              </v-tab-item>
            </v-tabs-items>
          </v-flex>

          <v-flex xs12 v-else>
            <v-expansion-panel class="elevation-0">
              <v-expansion-panel-content key="details">
                <template v-slot:header>
                  <div>¿Es para mí?</div>
                </template>
                <v-container>
                  <div v-html="product.description" />
                </v-container>
              </v-expansion-panel-content>
              <v-expansion-panel-content key="specs">
                <template v-slot:header>
                  <div>Conoce el producto</div>
                </template>
                <v-container>
                  <div v-html="product.specs" />
                </v-container>
              </v-expansion-panel-content>
              <v-expansion-panel-content key="comments">
                <template v-slot:header>
                  <div>Comentarios</div>
                </template>
                <v-container>
                  <h3
                    v-if="
                      customerReviewList.items &&
                        customerReviewList.items.length === 0
                    "
                    xs12
                    class="d-product--be-fisrt-commnet">
                    Se el primero en comentar
                  </h3>

                  <d-add-comment @review="appendReview" />

                  <d-comment-box
                    v-for="(comment, i) in customerReviewList.items"
                    :key="i"
                    :comment="comment"/>
                </v-container>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-flex>

          <v-layout
            v-if="product.relatedProducts && product.relatedProducts.length > 0"
            row
            wrap
            justify-center>
            <v-flex xs12 mb-3>
              <h3 class="text-xs-center">
                También te puede interesar estos productos
              </h3>
            </v-flex>
            <v-flex
              xs6
              sm4
              md3
              pa-2
              my-1
              v-for="(product, i) in product.relatedProducts"
              :key="i">
              <d-product-card :product="product" />
            </v-flex>
          </v-layout>
        </v-layout>
      </transition>
    </v-container>
  </v-content>
</template>

<style lang="less">
.d-product-detail {
  .d-product-detail__content {
    max-width: 900px;
  }
  .d-product--be-fisrt-commnet {
    font-size: 1rem;
    font-weight: 600;
    padding: 56px;
    text-align: center;
  }
}

#section__product {
  input[type='number']::-webkit-outer-spin-button,
  input[type='number']::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  input[type='number'] {
    -moz-appearance: textfield;
  }

  .v-input {
    .v-input__slot {
      background: #eee;
      @media screen and (max-width: 960px) {
        background: #fff !important;
      }
    }
    label {
      font-size: 0.875rem;
    }
  }

  .product-card {
    .d-rating {
      pointer-events: none;
      white-space: pre;
      .v-icon {
        font-size: 32px !important;
      }
    }
  }

  .image-view-card {
    height: 60px;
    width: 60px;
    border: 1px #d1d1d1 solid;
    margin: 0 auto;
    cursor: pointer;
    .image-view {
      width: 100%;
      height: 100%;
      object-fit: contain;
      &-video {
        padding: 4px;
      }
    }
  }
  @media screen and (max-width: 960px) {
    .product-card {
      background-color: #fff !important;
      border-color: #fff !important;
      .product-card__content {
        min-height: 500px;
        border-color: #fff !important;
        background-color: #fff !important;
      }
    }
    .recent-products {
      background-color: #fff;
    }
  }

  .v-menu {
    .v-btn__content {
      justify-content: left;
      i {
        position: absolute;
        right: 0;
      }
    }
  }
  .product-sale {
    position: absolute;
    bottom: 0;
    right: 0;
    left: 0;
  }
}
</style>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import { STOREFRONT_PRODUCT } from '@/router/storefront'

export default {
  name: 'Product',
  props: {
    makefavorite: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      quantity: 1,
      view: '',
      review: '',
      rating: 5,
      active: false,
      tab: null,
      content: {
        tabs: [
          {
            type: 'details',
            title: 'DETALLES'
          },
          {
            type: 'comments',
            title: 'COMENTARIOS'
          }
        ]
      },
      variant: {},
      variantNotAvailable: false
    }
  },
  computed: {
    ...mapState('product', {
      product: 'object',
      productReadSuccess: 'readSuccess',
      productReading: 'reading',
      addToCartSuccess: 'addToCartSuccess',
      addingToCart: 'addingToCart'
    }),

    ...mapState('customer-review', {
      customerReviewList: 'objects'
    }),
    breadcrumbs () {
      if (!this.product) {
        return [
          ...this.$route.meta.breadcrumbs
        ]
      }

      return [
        ...this.$route.meta.breadcrumbs,
        {
          text: this.product.name,
          disabled: true,
          href: {
            name: STOREFRONT_PRODUCT,
            params: { ...this.$route.params }
          }
        }
      ]
    },

    ...mapState('cart', {
      cartToken: 'token'
    }),

    ...mapGetters('cart', {
      isCartAvailable: 'isCartAvailable'
    }),

    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),

    price () {
      const { variant } = this

      if (variant) {
        return variant.price
      }

      return null
    },

    priceUndiscounted () {
      const { variant } = this

      if (variant) {
        return variant.priceUndiscounted
      }

      return null
    }
  },
  watch: {
    productReadSuccess (val, oldVal) {
      if (val) {
        this.variant = this.product.variantPickerData.variants[0]
      }
    },
    addToCartSuccess (val, oldVal) {
      if (val && this.cartToken) {
        this.getCart({
          id: this.cartToken,
          query: {
            expand: ['lines.variant.image', 'lines.variant.product'].join(','),
            fields: ['token', 'quantity', 'lines'].join(',')
          }
        })
      }
    },
    '$route.path' () {
      let productId = this.$route.params.id

      if (productId) {
        this.getProduct({
          id: productId,
          query: {
            expand: 'related_products,images'
          }
        })

        this.getCustomerReviewList({
          query: {
            product: productId,
            expand: 'user'
          }
        })
      }
    }
  },
  methods: {
    ...mapActions('product', {
      getProduct: 'read',
      addToCart: 'addToCart'
    }),

    ...mapActions('customer-review', {
      getCustomerReviewList: 'list'
    }),

    ...mapActions('cart', {
      getCart: 'read'
    }),

    formatPrice (value) {
      let val = (value / 1).toFixed(2) // .replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
    },

    handleUpdateQuantity (e) {
      this.quantity = e
    },

    handleAddToCart (e) {
      const { addToCart, cartToken, product, variant, quantity } = this

      const data = {
        token: cartToken,
        variant: variant.id,
        quantity: quantity
      }

      addToCart({
        id: product.id,
        data: data
      })
    },

    handleVariantChange (e) {
      if (e) {
        this.variantNotAvailable = false
        this.variant = e
      } else {
        this.variantNotAvailable = true
      }
    },

    handleViewChange (view) {
      this.view = view
    },

    appendReview (review) {
      this.content.tabs[2].comments.unshift({
        user: review.userId,
        place: 'A place',
        date: 'A date',
        comment: review.comment,
        rating: review.rating,
        votes: '5'
      })
    }
  },
  created () {
    let productId = this.$route.params.id

    if (productId) {
      this.getProduct({
        id: productId,
        query: {
          expand: 'related_products,images'
        }
      })

      this.getCustomerReviewList({
        query: {
          product: productId,
          expand: 'user'
        }
      })
    }
  }
}
</script>
