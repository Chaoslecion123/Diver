<template>
  <v-list-group
    v-if="filterItem && filterItem.values && filterItem.values.length > 0"
    :value="true"
    class="d-product-filter-item grey lighten-3">
    <v-list-tile
      slot="activator">
      <v-list-tile-content>
        <v-list-tile-title>{{ filterItem.name }}</v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>

    <v-list-tile
      v-for="value in filterItem.values"
      :key="value.id">
      <v-list-tile-action>
        <v-checkbox
          hide-details
          @change="handleCahnge({'key': filterItem.slug, 'value': [value.id]}, $event)"/>
      </v-list-tile-action>
      <v-list-tile-content>
        <v-list-tile-title>{{ value.name }}</v-list-tile-title>
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
  methods: {
    handleCahnge (value, $event) {
      this.$emit($event ? 'add' : 'remove', value)
    }
  }
}
</script>
