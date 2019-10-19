<template>
  <v-content app :class="['d-page__content', 'd-order']">
    <v-container
      my-5
      :fluid="$vuetify.breakpoint.mdAndDown"
      grid-list-xl
      :class="['d-checkout__content']">
      <v-layout v-if="readOrderSatusCode !== 404" row wrap>
        <!-- <v-flex mb-2 xs12>
          <h1 v-if="readOrderSatusCode === 404">
            Tu orden no existe como el amor de ella :'v
          </h1>
          <h1 v-else>
            Yey! :3
          </h1>
        </v-flex> -->

        <v-flex mb-2 xs12>
          <h1>
            Orden
          </h1>
          <h3>ID: {{ order && order.token }}</h3>
        </v-flex>

        <v-flex v-if="order" xs12 :class="['d-order__detail']">
          <v-container fluid grid-list-xl pa-0>
            <v-layout row wrap>
              <v-flex xs12 class="d-shoping-cart__product-list">
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
                      xs6
                      text-xs-left
                      class="d-shoping-cart__product-list--header-item">
                      Producto
                    </v-flex>
                    <v-flex xs6 align-center>
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
                            sm4
                            class="d-shoping-cart__product-list--header-item">
                            Precio (S/)
                          </v-flex>
                          <v-flex
                            text-xs-right
                            xs12
                            sm4
                            class="d-shoping-cart__product-list--header-item">
                            Total (S/)
                          </v-flex>
                        </template>
                      </v-layout>
                    </v-flex>
                  </v-layout>

                  <template v-for="(line, i) in order.lines">
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
                          'd-shoping-cart__item-deleting': deleting[line.id]
                        }
                      ]">
                      <v-flex xs6>
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
                            {{ line.variant.displayName }}
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs6 align-center>
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
                              {{ line.quantity }}
                            </span>
                          </v-flex>
                          <v-flex text-xs-right xs12 sm4>
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
                                  formatPrice(line.variant.price.gross.amount)
                                }}
                              </template>
                              <template v-else>
                                {{ formatPrice(line.variant.price.net.amount) }}
                              </template>
                            </span>
                          </v-flex>
                          <v-divider
                            v-if="$vuetify.breakpoint.xs"
                            class="flex xs12 pa-0"/>
                          <v-flex text-xs-right xs12 sm4>
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
                        </v-layout>
                      </v-flex>
                    </v-layout>
                  </template>
                </v-container>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>

        <v-flex xs12 :class="['d-order__detail']" v-if="order">
          {{ order.user_email }}
        </v-flex>
      </v-layout>
      <v-container v-else >
      <div class="layout text-xs-center ma-0 grey lighten-4 row wrap fill-height align-center justify-center"><div>
        <h2 class="mb-4 mt-4">
        Número de orden incorrecto
        </h2><a href="/" class="mb-4 v-btn--active v-btn v-btn--large v-btn--router theme--light accent d-btn d-btn--no-transform d-btn--bold d-btn--rounded"><div class="v-btn__content"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 1024 1024" focusable="false" class="mr-2 fa-icon" style="font-size: 1.25em;"><path d="M922.9 701.9H327.4l29.9-60.9 496.8-0.9c16.8 0 31.2-12 34.2-28.6l68.8-385.1c1.8-10.1-0.9-20.5-7.5-28.4-6.5-7.8-16.2-12.4-26.6-12.5l-632-2.1-5.4-25.4c-3.4-16.2-18-28-34.6-28H96.5c-19.4 0-35.3 15.8-35.3 35.3 0 19.5 15.8 35.3 35.3 35.3h125.9L246 312.8l58.1 281.3-74.8 122.1c-7.9 10.7-9.1 24.8-3 36.8 6 11.9 18.1 19.4 31.5 19.4h62.8C307.3 790 300 811.7 300 834.1c0 56.6 46 102.6 102.6 102.6s102.6-46 102.6-102.6c0-22.3-7.4-44-20.6-61.7h161.1c-13.3 17.6-20.6 39.3-20.6 61.7 0 56.6 46 102.6 102.6 102.6s102.6-46 102.6-102.6c0-22.3-7.4-44-20.6-61.7H923c19.4 0 35.3-15.8 35.3-35.3-0.1-19.4-15.9-35.2-35.4-35.2zM305.7 253l575.8 1.9-56.4 315.8-452.3 0.8L305.7 253z m96.9 612.7c-17.4 0-31.6-14.2-31.6-31.6 0-17.4 14.2-31.6 31.6-31.6s31.6 14.2 31.6 31.6c0 17.5-14.2 31.6-31.6 31.6z m325.1 0c-17.4 0-31.6-14.2-31.6-31.6 0-17.4 14.2-31.6 31.6-31.6s31.6 14.2 31.6 31.6c0 17.5-14.2 31.6-31.6 31.6z"></path></svg>
        Volver a la tienda
      </div></a></div></div>
      </v-container>
    </v-container>
  </v-content>
</template>

<style lang="less"></style>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Order',
  data () {
    return {
      deleting: {}
    }
  },
  props: {
    thanks: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    ...mapState('order', {
      order: 'object',
      readOrderSatusCode: 'readStatusCode'
    })
  },
  watch: {
    order (val, oldVal) {
      console.log(val)
    }
  },
  methods: {
    ...mapActions('order', {
      getOrder: 'read'
    }),

    formatPrice (value) {
      let val = (value / 1).toFixed(2) // .replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
    }
  },
  created () {
    let token = this.$route.params.id
    this.getOrder({
      id: token,
      query: {
        expand: 'lines.variant.image',
        fields: ['token', 'lines'].join(',')
      }
    })
  }
}
</script>
