<template>
  <div
    class="d-scene-pin"
    :style="{
      'top': `${top}%`,
      'left': `${left}%`
    }">
    <v-menu
      open-on-hover
      :close-on-content-click="false"
      auto
      offset-y>
      <v-btn
        class="d-scene-pin__marker ma-0"
        slot="activator"
        color="accent"
        small
        flat
        icon>
        <d-icon
          scale="1.25"
          name='b-star'/>
      </v-btn>
      <d-product-minicard
        :product="product"
        class="d-pin__content"/>
    </v-menu>
  </div>
</template>

<script>
import MiniCard from '../d-product/minicard'
export default {
  name: 'd-scene-pin',
  components: {
    'd-product-minicard': MiniCard
  },
  props: {
    top: {
      type: Number,
      default: 50
    },
    left: {
      type: Number,
      default: 50
    },
    product: {
      type: Object,
      default () {
        return {}
      }
    }
  }
}
</script>
