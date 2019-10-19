<template>
  <div
    class="d-brand-carousel-wrapper">
    <carousel
      v-if="brands"
      v-model="carouselIndex"
      :class="[
        'd-brand-carousel',
        {
          'd-brand-carousel--centered': !navigationEnabled
        }
      ]"
      :autoplay="true"
      :autoplayTimeout="2500"
      :loop="true"
      :paginationEnabled="false"
      :paginationPadding="10"
      :paginationSize="10"
      :perPageCustom="[[0,2], [450,3], [600, 4], [900, 5]]">
      <slide
        v-for="(brand, i) in brands"
        :key="i">
        <v-img
          contain
          height="100%"
          max-width="120"
          style="margin: 0 auto;"
          :alt="brand.mame"
          :src="brand.image"/>
      </slide>
    </carousel>
    <v-btn
      v-if="navigationEnabled"
      class="ma-0 pa-0 d-brand-carousel-btn d-brand-carousel-btn--prev"
      icon
      flat
      @click="prevSlide">
      <d-icon
        name="b-left"/>
    </v-btn>
    <v-btn
      v-if="navigationEnabled"
      class="ma-0 pa-0 d-brand-carousel-btn d-brand-carousel-btn--next"
      icon
      flat
      @click="nextSlide">
      <d-icon
        name="b-right"/>
    </v-btn>
  </div>
</template>

<style lang="less">
.d-brand-carousel-wrapper {
  position: relative;
  padding: 0 36px;

  .d-brand-carousel {
    &.d-brand-carousel--centered {
      .VueCarousel-inner {
        justify-content: center;
      }
    }

    .VueCarousel-slide {
      padding: 0 16px;
    }
  }

  .d-brand-carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);

    &.d-brand-carousel-btn--prev {
      left: 0;
    }

    &.d-brand-carousel-btn--next {
      right: 0;
    }
  }
}
</style>

<script>
export default {
  name: 'd-brand-carousel',
  props: {
    brands: {
      type: Array,
      default () {
        return []
      }
    }
  },
  data () {
    return {
      carouselIndex: 1
    }
  },
  computed: {
    itemsPerSlide () {
      // https://ssense.github.io/vue-carousel/api/#perPageCustom
      // :perPageCustom="[[0,2], [450,3], [600, 4], [900, 5]]"
      const { $vuetify } = this

      if ($vuetify.breakpoint.width >= 900) {
        return 5
      } else if ($vuetify.breakpoint.width >= 600) {
        return 4
      } else if ($vuetify.breakpoint.width >= 450) {
        return 3
      }
      return 2
    },
    navigationEnabled () {
      // https://ssense.github.io/vue-carousel/api/#perPageCustom
      // :perPageCustom="[[0,2], [450,3], [600, 4], [900, 5]]"
      const { brands, itemsPerSlide } = this

      if (brands) {
        return brands.length >= itemsPerSlide
      }

      return true
    }
  },
  methods: {
    prevSlide (e) {
      // const { brands, itemsPerSlide } = this
      // const nBrands = brands.length
      // const nSlides = Math.ceil(nBrands / itemsPerSlide)
      // let prevIndex = (nSlides + this.carouselIndex - 1) % nSlides
      let prevIndex = Math.max(this.carouselIndex - 1, 0)
      this.carouselIndex = prevIndex
    },
    nextSlide (e) {
      const { brands, itemsPerSlide } = this
      const nBrands = brands.length
      const nSlides = Math.ceil(nBrands / itemsPerSlide)
      // let nextIndex = (this.carouselIndex + 1) % nSlides
      let nextIndex = Math.min(this.carouselIndex + 1, nSlides - 1)
      this.carouselIndex = nextIndex
    }
  }
}
</script>
