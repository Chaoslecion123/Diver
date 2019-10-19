<template>
  <v-card
    tile
    flat
    max-height="650"
    class="d-scene">
    <v-img
      width="100%"
      :src="scene.image.original">
      <d-scene-pin
        v-for="spotlight in scene.spotlights"
        :key="spotlight.id"
        :top="parseFloat(spotlight.pointY)"
        :left="parseFloat(spotlight.pointX)"
        :product="spotlight.product"/>
    </v-img>
  </v-card>
</template>

<script>
import Pin from './pin'

export default {
  name: 'd-scene',
  components: {
    'd-scene-pin': Pin
  },
  props: {
    scene: {
      type: Object,
      default () {
        return {}
      }
    }
  }
}
</script>
