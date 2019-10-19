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
          Mis Pedidos
        </v-flex>
      </v-layout>
    </v-card>

    <v-card flat>
      <v-container grid-list-md pa-0>
        <v-layout row wrap>
          <v-flex
            xs6 md3
            v-for="(order, i) in order.items"
            :key="i"
            class="settings-card">
            <v-card
              min-height="auto"
              class="pa-3 border-radius fill-height"
              flat
              color="grey lighten-4">
              <v-container
                pa-0
                fluid
                fill-height
                grid-list-md>
                <v-layout row wrap>
                  <v-flex xs8> Pedido N° {{order.id}} </v-flex>
                  <v-spacer/>
                  <v-menu
                    right
                    nudge-right="24"
                    nudge-top="24"
                    offset-x
                    content-class="order-list"
                    :close-on-content-click="false">
                    <d-icon
                      class="ma-2 q-orange--text"
                      slot="activator"
                      scale="1.25"
                      name="b-info-circle-o"/>
                    <v-card style="font-size:0.875rem;" class="d-pin__content">
                      <v-list subheader class="pa-0">
                        <v-subheader>Lista de productos</v-subheader>
                        <v-list-tile
                          avatar
                          :to="{name: 'Favorite'}"
                          ripple>
                          <v-list-tile-avatar size="48">
                            <v-img contain :src="assets.product" />
                          </v-list-tile-avatar>
                          <v-list-tile-content style="font-size:1rem">
                            <v-list-tile-title>Crema hidratante #1</v-list-tile-title>
                          </v-list-tile-content>
                        </v-list-tile>
                        <v-divider class="mx-3"></v-divider>
                        <v-list-tile
                          avatar
                          :to="{name: 'Favorite'}"
                          ripple>
                          <v-list-tile-avatar size="48">
                            <v-img contain :src="assets.product" />
                          </v-list-tile-avatar>
                          <v-list-tile-content style="font-size:1rem">
                            <v-list-tile-title>Crema hidratante #2</v-list-tile-title>
                          </v-list-tile-content>
                        </v-list-tile>
                      </v-list>
                    </v-card>
                  </v-menu>
                  <v-flex xs12> Cant: 12 </v-flex>
                </v-layout>
              </v-container>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-flex>
</template>

<style lang="less">
.order-list {
  width: 28vw !important;
  max-height: 148px;
  overflow-y: scroll;
}
</style>

<script>
import { mapState, mapActions } from 'vuex'

import product from '@/assets/images/quimder/offersale1.png'

export default {
  name: 'UserOrders',
  data () {
    return {
      assets: {
        product: product
      }
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapState('order', {
      order: 'objects'
    })
  },
  methods: {
    ...mapActions('order', {
      getOrder: 'list'
    })
  },
  created () {
    this.getOrder()
  }
}
</script>
