<template>
  <v-layout
    row
    wrap
    fill-height
    align-center
    justify-center
    class="ma-0">
    <div>
      <v-progress-circular
        :width="2"
        :size="64"
        color="accent"
        indeterminate>
      </v-progress-circular>
    </div>
  </v-layout>
</template>

<script>
export default {
  name: 'd-loader'
}
</script>
