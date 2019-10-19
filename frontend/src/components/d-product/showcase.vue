<template>
  <v-container
    fluid
    :class="[
      'd-product-showcase',
      {
        'd-product-showcase-large': $vuetify.breakpoint.smAndUp
      }
    ]">
    <v-layout
      v-if="$vuetify.breakpoint.smAndUp"
      column
      class="d-product-showcase__navigator">
      <v-flex
        v-for="({ image }, i) in images"
        :key="i"
        shrink
        class="pa-0 mb-2">
        <v-card
          flat
          hover
          class="d-product-showcase__navigator-item pa-1"
          @click="goToSlide(i)"
          @mouseover="goToSlide(i)">
          <v-img
            contain
            width="100%"
            height="100%"
            class="image-view"
            :src="image.productSmall"/>
        </v-card>
      </v-flex>
      <v-flex v-if="video" shrink class="pa-0">
        <v-card
          flat
          hover
          class="d-product-showcase__navigator-item pa-1"
          @click.stop="goToVideo">
          <v-img contain :src="assets.playProductView" />
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout class="d-product-showcase__carousel">
      <v-flex xs12 class="pa-0">
        <carousel
          v-model="currentSlide"
          :perPage="1"
          :autoplay="false"
          :loop="true"
          :speed="500"
          :paginationEnabled="false"
          :paginationPadding="8"
          :paginationSize="12">
          <slide v-for="({ image }, i) in images" :key="i">
            <v-img
              contain
              height="400px"
              width="100%"
              :src="image.productGallery"/>
          </slide>
          <slide v-if="innerExtraImage">
            <v-img contain height="100%" :src="innerExtraImage" />
          </slide>
        </carousel>
      </v-flex>
    </v-layout>

    <v-layout
      v-if="$vuetify.breakpoint.xs"
      row
      justify-space-around
      class="d-product-showcase__navigator">
      <v-flex
        v-for="({ image }, i) in images"
        :key="i"
        shrink
        class="pa-0 mr-2">
        <v-card
          flat
          hover
          class="d-product-showcase__navigator-item pa-1"
          @click="goToSlide(i)"
          @mouseover="goToSlide(i)">
          <v-img
            contain
            width="100%"
            height="100%"
            class="image-view"
            :src="image.productSmall"/>
        </v-card>
      </v-flex>
      <v-flex v-if="video" shrink class="pa-0">
        <v-card
          flat
          hover
          class="d-product-showcase__navigator-item pa-1"
          @click.stop="goToVideo">
          <v-img contain :src="assets.playProductView" />
        </v-card>
      </v-flex>
    </v-layout>

    <v-dialog
      v-model="isVideoOpen"
      content-class="d-product-showcase__video-wrapper">
      <v-card class="d-product-showcase__video">
        <youtube v-if="isVideoOpen" player-width="100%" :video-id="videoId" />
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style lang="less">
.d-product-showcase {
  margin: 0;
  padding: 0;

  &.d-product-showcase-large {
    .d-product-showcase__navigator {
      width: 64px;
      float: left;
    }

    .d-product-showcase__carousel {
      width: calc(100% - 72px);
      margin: 0 0 0 72px !important;
    }
  }

  .d-product-showcase__navigator {
    padding: 0;
    margin: 0 !important;

    .d-product-showcase__navigator-item {
      width: 64px;
      height: 64px;
      border: 1px solid #d1d1d1;
      border-radius: 4px;
    }
  }

  .d-product-showcase__carousel {
    width: 100%;
  }
}

.d-product-showcase__video-wrapper {
  max-width: 800px;
}

.d-product-showcase__video {
  max-width: 800px;

  iframe {
    display: block;
  }
}
</style>

<script>
import playProductView from '@/assets/images/play-product-view.svg'

export default {
  name: 'd-product-showcase',
  props: {
    images: {
      type: Array,
      default () {
        return []
      }
    },
    video: {
      type: String,
      default: ''
    },
    extraImage: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      assets: {
        playProductView: playProductView
      },
      currentSlide: 0,
      innerExtraImage: '',
      isVideoOpen: false
    }
  },
  computed: {
    videoId () {
      if (this.video) {
        return this.$youtube.getIdFromURL(this.video)
      }
      return null
    }
  },
  watch: {
    images (val, oldVal) {
      if (val && val.length > 0) {
        this.currentView = val[0].image.detail
      }
    },
    extraImage (val, oldVal) {
      if (val) {
        this.innerExtraImage = val
      }
    },
    innerExtraImage (val, oldVal) {
      if (val) {
        this.currentView = val
        this.$nextTick(() => {
          this.currentSlide = this.video
            ? this.images.length + 1
            : this.images.length
        })
      }
    },
    currentSlide (val, oldVal) {
      if (val !== (this.video ? this.images.length + 1 : this.images.length)) {
        this.innerExtraImage = ''
      }
    }
  },
  methods: {
    goToSlide (i) {
      this.currentSlide = i
    },
    goToVideo () {
      this.isVideoOpen = true
    }
  }
}
</script>
