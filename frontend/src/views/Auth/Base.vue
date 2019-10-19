<template functional>
  <v-content
    class="d-view__auth--content">
    <v-container
      fill-height
      fluid>
      <v-layout
        row
        align-center
        fill-height
        justify-center>
        <slot></slot>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
export default {
  name: 'Auth'
}
</script>
