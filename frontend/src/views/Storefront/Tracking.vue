<template>
  <v-content class="d-page__content d-overide">
    <v-layout id="section__tracking" class="section">
      <v-container fluid px-0>
        <v-layout row wrap>
          <v-flex xs12 md9 pr-3 class="remove-padding">
            <h2 class="headline q-orange--text font-weight-600 text-uppercase">¡GRACIAS SHEYLA!</h2>
            <v-divider style="border-color: black;" class="my-3"></v-divider>
            <v-flex style="font-size:1.125rem;" class="font-size-600">¡GRACIAS POR CONFIAR EN QUIMDER!</v-flex>
            <v-flex my-2>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore
              magnaaliqua. Ut enim ad minim veniam, quis nostrud exercitationullamco laboris nisi ut aliquip.
            </v-flex>
            <v-flex xs12>
              <v-card flat class="pa-3" color="grey lighten-4">
                <v-container fluid px-0 grid-list-sm>
                  <v-layout style="line-height:1rem;" mx-2 row wrap align-center>
                    <v-flex pa-2 xs3 sm2 md2>Fecha de compra:</v-flex>
                    <v-flex pa-2 offset-xs1 xs8 offset-sm0 sm2 md2>12/01/2019</v-flex>
                    <v-divider class="mx-2 trackingInfo-divider" vertical style="border-color: black"></v-divider>
                    <v-flex pa-2 xs3 sm2 md2>Dirección registrada:</v-flex>
                    <v-flex pa-2 offset-xs1 xs8 offset-sm0 sm4 md3>Huertos de Manchay Mz C Lt 19, Pachacamac</v-flex>
                  </v-layout>
                </v-container>
                <v-card-title class="mx-2 font-weight-bold px-0">BARRA DE PROGRESO DEL PEDIDO</v-card-title>
                <v-card-text class="pa-0">
                  <v-slider
                    class="mx-5"
                    v-model="content.tracking"
                    color= "#FCB814"
                    ticks
                    :max="3"
                    step="1"></v-slider>
                  <v-layout row wrap text-xs-center justify-space-between>
                    <v-flex xs2 v-for="(item,i) in content.trackingTicks" :key="i">
                      <!--<v-icon class="tracking-icon mb-2">{{item.icon}}</v-icon>-->
                      <d-icon
                      class="tracking-icon mb-2"
                      :name="item.icon"/>
                    </v-flex>
                  </v-layout>
                  <v-layout row wrap text-xs-center justify-space-between>
                    <v-flex xs3 sm2 md2 class="trackingTicks" v-for="(item,i) in content.trackingTicks" :key="i">
                      {{item.ticksLabels}}
                    </v-flex>
                  </v-layout>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-flex>
          <v-flex xs12 offset-sm2 offset-md0 sm8 md3 class="set-margin-top-4">
            <d-checkout-sumary :ordered="true"/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>
  </v-content>
</template>

<style lang="less">
#section__tracking {
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
  .trackingTicks {
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
  .trackingTicks {
    font-size: 0.875rem;
  }
}
</style>

<script>
export default {
  name: 'Tracking',
  data () {
    return {
      content: {
        tracking: 0,
        trackingTicks: {
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
        },
        orderDetails: {
          1: {
            productsQuantity: '03',
            orderPrice: '635.11',
            orderDiscount: '10%',
            shippingPrice: 'Gratis',
            finalOrderPrice: '571.99'
          }
        }
      }
    }
  }
}
</script>
