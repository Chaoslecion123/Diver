<template>
  <v-content app :class="['d-page__content', 'd-order']">
    <v-container my-5 :fluid="$vuetify.breakpoint.mdAndDown" grid-list-xl>
      <v-layout row wrap class="text-xs-center">
        <v-flex mb-2 xs12>
          <h1>
            ¿Buscas tu pedido?
          </h1>

          <p>
            Ingresa el codigo de tu pedido para ver los detalles
          </p>
        </v-flex>

        <v-flex mb-2 xs12>
          <v-text-field
            v-model="orderCode"
            append-icon="search"
            name="code"
            label="Codigo de pedido"
            single-line
            @click:append="goToOrder"/>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<style lang="less"></style>

<script>
import { STOREFRONT_ORDER_DETAIL } from '@/router/storefront'

export default {
  name: 'Order',
  data () {
    return {
      orderCode: ''
    }
  },
  methods: {
    goToOrder () {
      this.$router.push({
        name: STOREFRONT_ORDER_DETAIL,
        params: {
          id: this.orderCode
        }
      })
    }
  }
}
</script>
