<template>
  <v-flex
    xs12 md10 pl-3
    style="font-size:14px;"
    class="remove-padding">
    <v-card
      class="py-2 px-3 mb-3"
      flat
      color="grey lighten-4">
      <v-layout row wrap align-center>
        <v-flex
          xs8
          style="font-size:1.25rem;"
          class="font-weight-600">
          Mis Cupones
        </v-flex>
      </v-layout>
    </v-card>

    <v-card
      flat>
      <v-container pa-0 fluid grid-list-lg>
        <v-layout row wrap>
          <v-flex xs6 sm4 md3>
            <v-card
              flat
              :class="isActive? '' : 'q-disabled--text q-disabled--border'"
              class="coupons-card border-radius">
              <v-card-title
                class="text-xs-center pa-2 pb-0">
                <v-flex
                  shrink
                  text-xs-left>
                  <div>Cupón:</div>
                  <div>2401201901</div>
                </v-flex>
                <v-spacer></v-spacer>
                <v-menu
                  right
                  :nudge-right="$vuetify.breakpoint.xs? 24 : 40"
                  nudge-top="28"
                  :max-width="$vuetify.breakpoint.xs? 192 : 280"
                  open-on-hover
                  :close-on-content-click="false">
                    <d-icon
                      class="ma-2"
                      :class="isActive? 'q-orange--text' : 'q-disabled--text'"
                      slot="activator"
                      scale="1.25"
                      name="b-info-circle-o"/>
                  <v-card style="font-size:0.875rem;" class="pa-3 d-pin__content">
                    <v-container pa-0 grid-list-md>
                      <v-layout row wrap>
                        <v-flex xs6>Puede ser utilizado en:</v-flex>
                        <v-flex xs6>Todos los artículos</v-flex>
                        <v-flex xs6>Restricciones:</v-flex>
                        <v-flex xs6>NO reembolsable</v-flex>
                        <v-flex xs6>Válido:</v-flex>
                        <v-flex xs6>18/01/19 - 18/12/19</v-flex>
                        <v-flex xs6>Detalles:</v-flex>
                        <v-flex xs6>Lorem ipsum dolor sit amet, consectetur </v-flex>
                      </v-layout>
                    </v-container>
                  </v-card>
                </v-menu>
              </v-card-title>
              <v-card-text class="pa-0 mb-4">
                <v-flex
                  text-xs-center
                  shrink>
                  <div class="display-1">$5.00</div>
                  <div class="headline">Dscto.</div>
                  <div :class="isActive? 'q-red--text' : 'q-disabled--text'">ACTIVO</div>
                </v-flex>
              </v-card-text>
              <v-card-actions
                class="justify-center pa-0">
                <v-btn
                  style="z-index:1"
                  class="border-radius"
                  dark
                  depressed
                  :class="isActive? 'q-white--text q-orange--background' : 'q-disabled--background'"
                  :ripple="false"
                  absolute>
                  APLICAR
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
    <!--v-card
      flat
      class="pa-3 mb-3"
      color="grey lighten-4">
      <v-container>
        <v-layout  align-center justify-center text-xs-center>
          <v-flex xs8 sm7>
            <d-icon
              class="coupon-icon"
              name="b-barcode"
              scale="5"
            />
            <v-flex>
              En cuanto los tengas, aquí podrás consultarlos para
              aplicarlos en tus compras
            </v-flex>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-->

  </v-flex>
</template>

<style lang="less">
.q-disabled{
  &--text {
    color: #d1d1d1 !important;
  }
  &--background {
    background-color: #d1d1d1 !important;
  }
  &--border {
    border-color: #d1d1d1 !important;
  }
}

.coupons-card {
  &.theme--light.v-sheet{
    border: 1px solid #F58220;
  }
  cursor: pointer;
  .v-btn:hover {
    background-color: #F58220 !important;
  }
}
</style>

<script>
export default {
  name: 'UserCoupons',
  props: {
    isActive: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {

    }
  }
}
</script>
