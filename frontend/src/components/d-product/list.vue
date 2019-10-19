<template>
  <v-container v-if="products" fluid grid-list-lg class="d-product-list">
    <v-layout row wrap>
      <v-flex v-for="(product, i) in products" :key="i" xs6 sm4 md3>
        <d-product-card :product="product" />
      </v-flex>

      <v-flex v-if="pagination" xs12 text-xs-right>
        <div style="margin: 0 0 0 auto;width: fit-contnet;">
          <v-pagination
            color="accent"
            :value="pagination.current"
            :length="pagination.pages"
            :total-visible="4"
            @input="handleInput">
          </v-pagination>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style lang="less">
.d-product-list {
  .v-pagination {
    .v-pagination__navigation,
    .v-pagination__item {
      box-shadow: none;
      border: 1px solid #eee;
      outline: none;

      &:hover {
        box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.2),
          0 8px 10px 1px rgba(0, 0, 0, 0.14), 0 3px 14px 2px rgba(0, 0, 0, 0.12);
      }
    }

    .v-pagination__item--active {
      border: 0 none;
    }
  }
}
</style>

<script>
import ProductCard from './card'

export default {
  name: 'd-product-list',
  component: {
    'd-product-card': ProductCard
  },
  props: {
    products: {
      type: Array,
      defaul: null
    },
    pagination: {
      type: Object,
      defaul: null
    }
  },
  methods: {
    handleInput (value) {
      this.$emit('pagechange', value)
    }
  }
}
</script>
