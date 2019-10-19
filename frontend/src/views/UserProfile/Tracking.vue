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
          Seguimiento
        </v-flex>
      </v-layout>
    </v-card>

    <v-card flat>
      <v-container grid-list-md pa-0>
        <v-layout row wrap>
          <v-flex
            v-for="(order, i) in order.items"
            :key="i"
            xs6 md3
            class="settings-card">
            <v-card min-height="auto" class="pa-3 border-radius fill-height" flat color="grey lighten-4">
              <v-container
                pa-0
                fluid
                fill-height
                grid-list-md>
                <v-layout row wrap>
                  <v-flex xs8> Pedido N° {{order.id}} </v-flex>
                  <v-spacer/>
                  <router-link :to="{ name: 'Tracking' }">
                  <d-icon
                    class="ma-2 q-orange--text"
                    scale="1.25"
                    name="b-info-circle-o"/>
                  </router-link>
                  <v-flex xs12> Código de Seguimiento: PE123456789LI </v-flex>
                  <v-flex xs12> Método de envío: <span> {{order.shippingMethodName}} </span> </v-flex>
                </v-layout>
              </v-container>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-flex>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'UserTracking',
  data () {
    return {
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
