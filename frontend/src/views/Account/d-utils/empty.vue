<template>
  <v-layout
    row
    wrap
    fill-height
    align-center
    justify-center
    class="text-xs-center ma-0 grey lighten-4">
    <div>
      <slot></slot>
    </div>
  </v-layout>
</template>

<script>
export default {
  name: 'd-empty'
}
</script>
