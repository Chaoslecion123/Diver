<template>
  <carousel
    class="d-showcase"
    :autoplay="$vuetify.breakpoint.smAndDown? true : false"
    :paginationEnabled="false"
    :navigationEnabled="false"
    :autoplayHoverPause="true"
    :perPageCustom="[[0,1], [600,2], [960, 3]]"
    :autoplayTimeout="5000"
    :loop="true">
    <slide
      v-for="(scene, i) in scenes"
      :key="i">
      <d-scene
        :scene="scene"/>
    </slide>
  </carousel>
</template>

<style lang="less">
@import "./style.less";
</style>

<script>
import Scene from './scene'

export default {
  name: 'd-showcase',
  components: {
    'd-scene': Scene
  },
  props: {
    scenes: {
      type: Array,
      default () {
        return []
      }
    }
  }
}
</script>
