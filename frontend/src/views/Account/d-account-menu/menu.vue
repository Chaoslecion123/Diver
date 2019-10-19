<template>
  <v-list
    subheader
    class="d-account-menu"
    active-class="accent--text">
    <template
      v-for="(item, key) in items">
      <v-divider
        v-if="item.prependDivider"
        :key="`divider-${key}`"/>
      <d-account-menu-item
        :key="key"
        :item="item"/>
    </template>
  </v-list>
</template>

<script>
import Item from './item.vue'

export default {
  name: 'd-account-menu',
  components: {
    'd-account-menu-item': Item
  },
  props: {
    items: {
      type: Array,
      default () {
        return []
      }
    }
  }
}
</script>
