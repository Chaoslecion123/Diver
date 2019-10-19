<template>
  <carousel
    v-if="$vuetify.breakpoint.smAndDown"
    class="mt-2 mb-4"
    :autoplay="true"
    :perPageCustom="[
      [0,3],
      [375,4],
      [500,5],
      [600,6],
      [800,8]
    ]"
    :paginationEnabled="false"
    :autoplayTimeout="5000"
    :loop="true">
    <slide
      v-for="(category, i) in categoryList.items"
      :key="i">
      <v-card
        class="category-img"
        flat
        :to="{
          name: 'storefront:category',
          params: {
            slug: category.slug,
            id: category.id
          }
        }">
        <v-avatar
          color="grey lighten-3"
          :size="avatarSize"
          :style="{
            'min-width': avatarSize + 'px',
            'border-radius': '50%'
          }">
          <img
            v-if="category.iconImage"
            :src="category.iconImage">
          <span
            v-else
            class="headline">
            {{ category.name[0] }}
          </span>
        </v-avatar>
        <v-flex mx-2 my-1 class="text-xs-center">{{ category.name }}</v-flex>
      </v-card>
    </slide>
  </carousel>
  <div
    v-else>
    <v-card
      :class="desktopClass"
      v-for ="(category, i) in categoryList.items"
      :key="i"
      flat
      @mouseover="changeCollection(category)"
      :to="{
        name: 'storefront:category',
        params: {
          slug: category.slug,
          id: category.id
        }
      }"
      :height="cardHeight">
      <v-container
        px-0
        fill-height
        class="text-on-hover">
        <v-avatar
          color="grey lighten-3"
          :size="avatarSize"
          :style="{
            'min-width': avatarSize + 'px'
          }">
          <img
            v-if="category.iconImage"
            :src="category.iconImage">
          <span
            v-else
            class="headline">
            {{ category.name[0] }}
          </span>
        </v-avatar>
        <v-flex ml-2>
          <v-card-title
            style="height: auto !important;"
            class="fill-height py-0"
            primary-title>
            <span>{{ category.name }}</span>
          </v-card-title>
        </v-flex>
      </v-container>
    </v-card>
  </div>
</template>

<style lang="less">
.category-img {
  font-size: 0.85rem;
  &:hover {
    color: #fcb814;
  }
  text-align: center;
}
</style>

<script>
import { mapState } from 'vuex'

export default {
  name: 'd-categories',
  props: {
    cardHeight: {
      type: String,
      default: ''
    },
    avatarSize: {
      type: String,
      default: ''
    },
    desktopClass: {
      type: String,
      default: ''
    }
  },
  data () {
    return {}
  },
  computed: {
    ...mapState('category', {
      categoryList: 'objects'
    })
  },
  watch: {
    categoryList (val, oldVal) {
      if (val) {
        this.changeCollection(val[0])
      }
    }
  },
  methods: {
    changeCollection (category) {
      this.$emit('changecollection', category)
    }
  }
}
</script>
