<template>
  <v-list-group
    :value="true"
    class="d-product-filter-item grey lighten-3 pb-2">
    <v-list-tile
      slot="activator">
      <v-list-tile-content>
        <v-list-tile-title>Precio</v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>

    <v-list-tile>
      <v-list-tile-content
        class="layout row wrap px-2">
        <v-range-slider
          class="mt-0 xs12 flex"
          v-model="price"
          :max="1000"
          :min="0"
          :step="0.01"/>
      </v-list-tile-content>
    </v-list-tile>

    <v-list-tile>
      <v-list-tile-content
        class="layout row wrap align-center justify-center">
        <v-text-field
          v-model="price[0]"
          class="mt-0 py-0 pr-1 flex xs6 shrink d-input d-input--rounded d-input--bordered d-input--small"
          hide-details
          single-line
          flat
          solo
          type="text"/>
        <v-text-field
          v-model="price[1]"
          class="mt-0 py-0 pl-1 flex xs6 shrink d-input d-input--rounded d-input--bordered d-input--small"
          hide-details
          single-line
          flat
          solo
          type="text"/>
      </v-list-tile-content>
    </v-list-tile>

    <v-list-tile>
      <v-list-tile-content>
        <v-btn
          block
          color="accent"
          depressed
          class="d-btn d-btn--no-transform"
          @click="updatePrice">
          Filtrar precios
        </v-btn>
      </v-list-tile-content>
    </v-list-tile>

  </v-list-group>
</template>

<style lang="less">
</style>

<script>
export default {
  name: 'd-product-filter-item',
  props: {
    filterItem: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      price: [0, 1000]
    }
  },
  // watch: {
  //   price (val, oldVal) {
  //     this.$emit('change', { priceMin: this.price[0], priceMax: this.price[1] })
  //   }
  // }
  methods: {
    updatePrice () {
      this.$emit('change', { priceMin: this.price[0], priceMax: this.price[1] })
    }
  }
}
</script>
