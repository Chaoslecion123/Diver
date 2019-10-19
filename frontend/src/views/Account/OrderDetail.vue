<template>
  <v-container
    :fluid="$vuetify.breakpoint.mdAndDown"
    grid-list-xl
    class="pa-0 ma-0">
    <v-layout row wrap>
      <v-flex v-if="order" xs12 :class="['d-order__detail']">
        <v-container fluid grid-list-xl pa-0>
          <v-layout row wrap>
            <v-flex xs12 class="d-shoping-cart__product-list">
              <v-container pa-0 fluid>
                <v-flex xs12 class="grey lighten-4 mb-3">
                  <h2>
                    Orden
                  </h2>
                  <h4>ID: {{ order && order.token }}</h4>
                </v-flex>

                <v-flex xs12 class="grey lighten-4 mb-3">
                  <h4 class="mb-2">Adjunta tu comprobante de pago</h4>
                  <v-upload-btn
                    depressed
                    title="Adjuntar"
                    color="accent"
                    class="pa-0"
                    labelClass="ma-0">
                    <template slot="icon">
                      <v-icon>add</v-icon>
                    </template>
                  </v-upload-btn>
                </v-flex>
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
                              {{ formatPrice(line.variant.price.gross.amount) }}
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
                                  line.quantity * line.variant.price.net.amount
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
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import UploadButton from 'vuetify-upload-button'

export default {
  name: 'OrderDetail',
  components: {
    'v-upload-btn': UploadButton
  },
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
      order: 'object'
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
