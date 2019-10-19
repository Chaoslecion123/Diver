<template>
  <v-data-table :headers="headers" :items="orders.items" transparent>
    <template slot="items" slot-scope="{ item }">
      <td class="text-xs-center">#{{ item.id }}</td>
      <td class="text-xs-center">{{ formatDate(item.created) }}</td>
      <td class="text-xs-right">S/ {{ item.total.gross.amount }}</td>
      <td class="text-xs-center">
        {{ formatPaymentStatus(item.paymentStatus) }}
      </td>
      <td class="text-xs-center">
        {{ formatStatus(item.status) }}
      </td>
      <td class="text-xs-action">
        <v-btn
          flat
          class="d-btn d-btn--no-transform accent--text"
          @click="goToDetails(item.token)">Detalles</v-btn>

        <v-btn
          flat
          class="d-btn d-btn--no-transform accent--text"
          @click="goToTracking(item.token)">Seguimiento</v-btn>
      </td>
    </template>
  </v-data-table>
</template>

<script>
import { ACCOUNT_ORDER_DETAIL, ACCOUNT_ORDER_TRACKING } from '@/router/account'

export default {
  name: 'd-order-list',
  props: {
    orders: {
      type: Object,
      default () {
        return {
          meta: {},
          items: []
        }
      }
    }
  },
  data () {
    return {
      headers: [
        {
          text: 'Pedido',
          value: 'id',
          align: 'center',
          sortable: false
        },
        {
          text: 'Fecha',
          value: 'created',
          align: 'center',
          sortable: false
        },
        {
          text: 'Resumen',
          value: 'total',
          align: 'center',
          sortable: false
        },
        {
          text: 'Estado de pago',
          value: 'paymentStatus',
          align: 'center',
          sortable: false
        },
        {
          text: 'Estado de pedido',
          value: 'status',
          align: 'center',
          sortable: false
        },
        {
          text: 'Acciones',
          align: 'center',
          sortable: false
        }
      ]
    }
  },
  methods: {
    formatDate (date) {
      const fmtDate = new Date(date)
      return fmtDate.toLocaleString()
    },
    formatStatus (status) {
      if (status === 'draft') return 'Borrador'
      if (status === 'unfulfilled') return 'Sin pagar'
      if (status === 'partially fulfilled') return 'Parcialmente pagado'
      if (status === 'fulfilled') return 'Pagado'
      if (status === 'canceled') return 'Cancelado'
    },
    formatChargeStatus (paymentStatus) {
      if (paymentStatus === 'charged') return 'Cargado'
      if (paymentStatus === 'not-charged') return 'No cargado'
      if (paymentStatus === 'fully-refunded') return 'Reembolsado'
    },
    formatPaymentStatus (paymentStatus) {
      if (paymentStatus === 'not-charged') return 'Sin cargo'
      if (paymentStatus === 'partially-charged') return 'Cargo parcial'
      if (paymentStatus === 'fully-charged') return 'Cargado'
      if (paymentStatus === 'partially-refunded') return 'Reembolso parcial'
      if (paymentStatus === 'fully-refunded') return 'Reembolso'
    },
    goToDetails (id) {
      this.$router.push({
        name: ACCOUNT_ORDER_DETAIL,
        params: {
          id: id
        }
      })
    },
    goToTracking (id) {
      this.$router.push({
        name: ACCOUNT_ORDER_TRACKING,
        params: {
          id: id
        }
      })
    }
  }
}
</script>
