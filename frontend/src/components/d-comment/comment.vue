<template>
  <div
    class="d-comment mt-3">
    <v-rating
      v-model="comment.score"
      class="d-rating">
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
      {{ comment.comment}}
    </v-flex>
    <v-flex xs12 my-1>
      <em>Por {{ username }} el {{comment.createDate}}</em>
    </v-flex>
  </div>
</template>

<style lang="less">
.d-comment {
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
  name: 'd-comment',
  props: [
    'comment'
  ],
  data () {
    return {
      upvoted: false
    }
  },
  methods: {
    upvote () {
      this.upvoted = !this.upvoted
    }
  },
  computed: {
    votes () {
      if (this.upvoted) {
        return this.comment.votes + 1
      } else {
        return this.comment.votes
      }
    },
    username () {
      const { comment } = this
      if (comment.user.firstName && comment.user.lastName) {
        return `${comment.user.firstName} ${comment.user.lastName}`
      }

      return comment.user.email.split('@')[0]
    }
  }
}
</script>
