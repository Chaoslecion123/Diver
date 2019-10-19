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
                  <h4>ID: {{ order.token }}</h4>
                </v-flex>

                <v-flex xs12 class="grey lighten-4 mb-3">
                  <dl>
                    <dt><strong>Fecha de pedido</strong></dt>
                    <dd class="mb-3">{{ creationDate }}</dd>

                    <dt><strong>Tipo de envío</strong></dt>
                    <dd v-if="shippingType">
                      {{ shippingType }}
                    </dd>
                  </dl>
                </v-flex>

                <v-flex id="tracking-panel" xs12 class="grey lighten-4 mb-3">
                  <div class="mb-3">
                    <strong>Seguimiento del pedido</strong>
                  </div>
                  <div>
                    <v-slider
                      class="mx-5"
                      :step="trackingStep"
                      color="#FCB814"
                      ticks
                      :max="3"
                      readonly></v-slider>
                    <v-layout row wrap text-xs-center justify-space-between>
                      <v-flex xs2 v-for="(item, i) in tackingSteps" :key="i">
                        <!--<v-icon class="tracking-icon mb-2">{{item.icon}}</v-icon>-->
                        <d-icon class="tracking-icon mb-2" :name="item.icon" />
                      </v-flex>
                    </v-layout>
                    <v-layout row wrap text-xs-center justify-space-between>
                      <v-flex
                        xs3
                        sm2
                        md2
                        class="tackingSteps"
                        v-for="(item, i) in tackingSteps"
                        :key="i">
                        {{ item.ticksLabels }}
                      </v-flex>
                    </v-layout>
                  </div>
                </v-flex>
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

<style lang="less">
#tracking-panel {
  .v-slider__track__container {
    height: 8px !important;
    border-radius: 64px;
  }
  .v-slider__track,
  .v-slider__track-fill {
    height: 8px !important;
  }
  .v-slider__thumb {
    border: 1px solid #000 !important;
    width: 32px !important;
    height: 32px !important;
  }
  .v-slider__ticks {
    border-style: none;
  }
  .theme--light.v-input--slider:not(.v-input--is-dirty) .v-slider__thumb {
    background-color: #fcb814;
  }
  .tracking-icon {
    height: 24px !important;
    width: 24px !important;
  }
  .tackingSteps {
    line-height: 1.125rem;
  }
}

@media only screen and (max-width: 600px) {
  .trackingInfo-divider {
    display: none;
  }
  .v-input--slider {
    margin-left: 16px !important;
    margin-right: 16px !important;
  }
  .tackingSteps {
    font-size: 0.875rem;
  }
}
</style>

<script>
import { mapState, mapActions } from 'vuex'
import {
  DOOR_SHIPPING,
  STORE_SHIPPING
} from '@/views/Storefront/d-checkout/constants'

export default {
  name: 'OrderDetail',
  data () {
    return {
      tackingSteps: {
        1: {
          icon: 'b-store',
          ticksLabels: 'En tienda'
        },
        2: {
          icon: 'b-rocket',
          ticksLabels: 'Pedido confirm.'
        },
        3: {
          icon: 'b-car',
          ticksLabels: 'En curso'
        },
        4: {
          icon: 'b-gift',
          ticksLabels: 'Entregado'
        }
      }
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
    }),
    creationDate () {
      let { order } = this
      if (order && order.created) {
        let datetime = new Date(order.created)
        return datetime.toLocaleString()
      }

      return null
    },
    shippingType () {
      let { order } = this
      if (order && order.shippingType) {
        if (order.shippingType === DOOR_SHIPPING) {
          return 'Entrega a domicilio'
        }
        if (order.shippingType === STORE_SHIPPING) {
          return 'Recojo en tienda'
        }
      }
      return null
    },
    trackingStep () {
      return 0
    }
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
        fields: ['token', 'created', 'shipping_type', 'billing_type'].join(',')
      }
    })
  }
}
</script>
