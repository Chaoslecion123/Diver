<template>
  <v-list
    v-if="filterData"
    expand
    class="d-product-filter pa-0">
    <d-product-filter-item
      v-for="filterItem in filterData"
      :key="filterItem.id"
      :filterItem="filterItem"
      @add="handleAdd"
      @remove="handleRemove"/>
    <d-product-filter-price
      @change="handlePriceChange"/>
  </v-list>
</template>

<style lang="less">
.d-product-filter {
  .d-product-filter-item:not(:last-child) {
    margin-bottom: 1rem;
  }

  .d-product-filter-item {
    border-radius: 4px;
    overflow: hidden;
  }

  .v-list__group:after,
  .v-list__group:before {
    content: none;
  }

  .v-list__tile__action,
  .v-list__tile__avatar {
    min-width: auto;
  }

  .v-list__group__items {
    overflow-y: auto;
    max-height: 250px;
  }
}
</style>

<script>
import FilterItem from './filter-item'
import FilterPrice from './filter-price'

export default {
  name: 'd-product-filter',
  components: {
    'd-product-filter-item': FilterItem,
    'd-product-filter-price': FilterPrice
  },
  props: {
    filterData: {
      type: Array,
      default: null
    }
  },
  data () {
    return {
      filterQuery: {}
    }
  },
  watch: {
    filterQuery (val, oldVal) {
      this.$emit('filter', val)
    }
  },
  methods: {
    handleAdd (e) {
      let { filterQuery } = this
      if (!(e.key in filterQuery)) {
        filterQuery[e.key] = e.value
      } else {
        filterQuery[e.key] = [...filterQuery[e.key], ...e.value]
      }
      this.filterQuery = { ...filterQuery }
    },
    handleRemove (e) {
      let { filterQuery } = this
      if (e.key in filterQuery) {
        filterQuery[e.key].pop(e.value)
        if (filterQuery[e.key].length === 0) {
          delete filterQuery[e.key]
        }
      }
      this.filterQuery = { ...filterQuery }
    },
    handlePriceChange (e) {
      let { filterQuery } = this
      this.filterQuery = { ...filterQuery, ...e }
    }
  }
}
</script>
