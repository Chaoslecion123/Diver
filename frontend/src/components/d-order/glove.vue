<template>
  <v-menu
    v-model="openMenu"
    offset-y
    top
    right
    nudge-top="16"
    :close-on-click="false"
    :close-on-content-click="false">
    <template v-slot:activator="{ on }">
      <v-btn color="accent" dark v-on="on" fixed bottom right fab>
        <d-icon name="b-bell"></d-icon>
      </v-btn>
    </template>
    <v-card
      :style="{
        borderRadius: '8px',
        overflow: 'hidden'
      }">
      <v-btn
        color="accent"
        flat
        icon
        class="ma-0 pa-0"
        style="float: right; min-width: initial; border-radius: 0;"
        @click="openMenu = false">
        <d-icon name="b-close" />
      </v-btn>
      <v-card-title class="pb-0">
        <strong>¿Búscas el detalle de tu pedido?</strong>
      </v-card-title>
      <v-card-text>
        <v-text-field
          ref="streetAddress2"
          v-model="orderNumber"
          browser-autocomplete="off"
          type="text"
          flat
          solo
          style="min-width: auto; width: calc(100% - 56px); display: inline-block;"
          :rules="[v => !!v || 'Este campo es requerido']"
          :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
          hint="Ingresa tu número de pedido."
          persistent-hint/>
        <v-btn
          color="accent"
          dark
          :class="[
            'ma-0',
            'ml-2',
            'pa-0',
            'd-btn',
            'd-btn--bold',
            'd-btn--no-transform'
          ]"
          :style="{
            minWidth: 'auto',
            width: '48px',
            height: '48px',
            textAlign: 'center',
            top: '-1px'
          }"
          @click="handleClick">
          <d-icon name="b-search" class="fa-fw"></d-icon>
        </v-btn>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<script>
import { STOREFRONT_ORDER_DETAIL } from '@/router/storefront'

export default {
  name: 'order-globe',
  data () {
    return {
      openMenu: true,
      orderNumber: ''
    }
  },
  methods: {
    handleClick () {
      this.$router.push({
        name: STOREFRONT_ORDER_DETAIL,
        params: {
          id: this.orderNumber.replace(/ /g, '')
        }
      })
    }
  }
}
</script>
