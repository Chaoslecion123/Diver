<template>
  <carousel
    v-if="slider && slider.slides"
    class="d-header-carousel"
    :perPage="1"
    :autoplay="true"
    :loop="true"
    :autoplayTimeout="6000"
    :paginationPadding="10"
    :paginationSize="10">
    <slide
      v-for="(slide, i) in slider.slides"
      :key="i">
      <v-img
        :src="slide.image.fullsize"/>
    </slide>
  </carousel>
  <v-img
    class="d-header-carousel"
    v-else
    :src="placeholder"/>
</template>

<style lang="less">
@import "./header-carousel.less";
</style>

<script>
export default {
  name: 'd-header-carousel',
  props: {
    slider: {
      type: Object,
      default () {
        return {}
      }
    },
    placeholder: {
      type: String,
      default: ''
    }
  }
}
</script>
