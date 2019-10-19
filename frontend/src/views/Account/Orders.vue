<template>
  <v-container fluid fill-height class="pa-0 ma-0">
    <transition mode="out-in" name="fade">
      <d-loader v-if="listingOrders" key="loading" />
      <d-empty
        v-else-if="!listingOrders && userHasNoOrders"
        key="userHasNoOrders">
        <h2 class="mb-4">
          Aún no tienes pedidos
        </h2>
        <v-btn
          :to="{ name: links.root }"
          large
          color="accent"
          :class="[
            'd-btn',
            'd-btn--no-transform',
            'd-btn--bold',
            'd-btn--rounded'
          ]">
          <d-icon :scale="1.25" class="mr-2" name="b-shopping-cart" />
          ¡Quiero ir de compras!
        </v-btn>
      </d-empty>

      <v-layout v-else key="order-list" row wrap c                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      lass="ma-0">
        <v-flex xs12 class="pa-0">
          <v-layout row wrap>
            <v-flex xs12>
              <h2 style="font-weight: normal;">
                <d-icon name="b-enviroment-o" />
                Mis pedidos
              </h2>
              <v-divider />
            </v-flex>
            <v-flex xs12>
              <d-order-list :orders="orders" />
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </transition>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { ROOT } from '@/router'

import Loader from './d-utils/loader'
import Empty from './d-utils/empty'
import OrderList from './d-order/list'

export default {
  name: 'AccountOrders',
  components: {
    'd-loader': Loader,
    'd-empty': Empty,
    'd-order-list': OrderList
  },
  data () {
    return {
      links: {
        root: ROOT
      }
    }
  },
  computed: {
    ...mapState('order', {
      orders: 'objects',
      listingOrders: 'listing'
    }),
    userHasNoOrders () {
      const { orders } = this

      if (orders && orders.meta) {
        return orders.meta.count === 0
      }

      return true
    }
  },
  methods: {
    ...mapActions('order', {
      getOrderList: 'list'
    })
  },
  created () {
    this.getOrderList()
  }
}
</script>
