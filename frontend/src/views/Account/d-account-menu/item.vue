<template>
  <v-list-tile
    v-if="item"
    :to="item.to"
    class="d-account-menu-item grey lighten-4">
    <v-list-tile-avatar>
      <!-- v-icon>{{ item.icon }}</v-icon -->
      <d-icon :name="item.icon" />
    </v-list-tile-avatar>
    <v-list-tile-content>
      <v-list-tile-title>{{ item.title }}</v-list-tile-title>
    </v-list-tile-content>
  </v-list-tile>
</template>

<script>
export default {
  name: 'd-account-menu-item',
  props: {
    item: {
      type: Object,
      default () {
        return {}
      }
    }
  }
}
</script>
