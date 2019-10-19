<template>
  <div>
    <carousel
      v-if="activeSlider"
      class="CarouselBanner"
      :perPage="1"
      :autoplay="true"
      :loop="true"
      :paginationPadding="15"
      :autoplayTimeout="6000"
      :paginationSize="15">
        <slide v-for="(slide, i) in activeSlider.slides"
          :key="i">
          <v-img width="100vw" :src="slide.image"></v-img>
        </slide>
    </carousel>
    <carousel
      v-else
      class="CarouselBanner"
      :perPage="1"
      :autoplay="true"
      :loop="true"
      :paginationPadding="15"
      :paginationSize="15">
        <slide>
          <v-img width="100vw" :src="assets.slide01"></v-img>
        </slide>
    </carousel>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import slide01 from '@/assets/images/quimder/portada01.png'

export default {
  name: 'd-home-carousel',
  data () {
    return {
      assets: {
        slide01: slide01
      }
    }
  },
  computed: {
    ...mapState('slider', {
      sliderList: 'objects'
    }),
    activeSlider () {
      if (this.sliderList && this.sliderList.items) {
        return this.sliderList.items[0] || []
      }

      return []
    },
    featuredBrands () {
      if (this.featuredBrandList && this.featuredBrandList.meta) {
        if (this.featuredBrandList.meta.count >= 1) {
          return this.featuredBrandList.items
        }
      }
      return null
    }
  },
  methods: {
    ...mapActions('slider', {
      getSliderList: 'list'
    })
  },
  created () {
    this.getSliderList({ query: { active: true, expand: 'slides' } })
  }
}
</script>
