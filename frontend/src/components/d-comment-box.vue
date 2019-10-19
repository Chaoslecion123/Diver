<template>
  <div class="d-comment-box mt-3">
    <v-rating v-model="comment.score" class="d-rating">
      <v-icon
        class="pa-0"
        slot="item"
        slot-scope="props"
        color="#ffeb3b"
        large
        @click="props.click">
        {{ props.isFilled ? 'star' : 'star_border' }}
      </v-icon>
    </v-rating>
    <v-flex xs12 my-2>
      {{ comment.comment }}
    </v-flex>
    <v-flex xs12 my-1>
      <em>
        Por {{ username }}
        <template v-if="fomatedDate">
          el {{ fomatedDate }}
        </template>
      </em>
    </v-flex>
  </div>
</template>

<style lang="less">
.d-comment-box {
  .d-rating {
    pointer-events: none;
    .v-icon {
      font-size: 24px !important;
    }
  }
}
</style>

<script>
export default {
  name: 'd-comment-box',
  props: ['comment'],
  data () {
    return {}
  },
  computed: {
    username () {
      const { comment } = this
      if (comment.user.firstName && comment.user.lastName) {
        return `${comment.user.firstName} ${comment.user.lastName}`
      }

      return comment.user.email.split('@')[0]
    },
    fomatedDate () {
      if (this.comment && this.comment.created) {
        let date = new Date(this.comment.created)
        return date.toLocaleDateString()
      }
      return ''
    }
  }
}
</script>
