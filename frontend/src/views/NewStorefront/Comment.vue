<template>
<div>
  <!--div v-for="(comment,i) in customerReviewSetList.items" :key="i"-->
  <v-container fluid class="d-comment set-padding-4">
    <d-rating/>
    <h3>{{ comment.titleMessage }}</h3>
    <v-flex xs12 my-1>
      <span>From {{comment.user}} </span>, <span> {{comment.place}} </span> <span> {{comment.date}} </span>
    </v-flex>
    <v-flex xs12 my-2>
      <span>{{ comment.comment}}</span>
    </v-flex>
    <v-btn class="border-radius mx-0 q-orange--background" dark>Comentar</v-btn>
    <v-btn v-on:click="counter += 1" :ripple="false" class="comment-buttons like border-radius" outline>
      <!--v-icon class="mr-2" size="16" light right >thumb_up</v-icon-->
      <d-icon class="mr-2" scale="1" light right name="b-like-o"/>
      <span>{{ counter }}</span>
    </v-btn>
  </v-container>
</div>
</template>

<style lang="less">
.d-comment {
  border-bottom: 10px solid #eee;
  @media screen and (max-width: 960px) {
    background: #fff;
    border: none;
  }
  .comment-buttons {
    width: 60px;
    border-color: #c5c5c5 !important;
    &.like {
      &:hover {
        .fa-icon {
          color: #f58220;
        }
      }
    }
  }
}
</style>

<script>
// import { mapActions, mapState } from 'vuex'

export default {
  name: 'DComment',
  props: {
    comment: {
      type: Object,
      default () {
        return {}
      }
    }
  },
  data () {
    return {
      counter: 5
    }
  },
  computed: {
    // ...mapState('comment', {
    //   customerReviewSetList: 'objects'
    // })
  },
  methods: {
    // ...mapActions('comment', {
    //   getCustomerReviewSetList: 'list'
    // })
  },
  created () {
    // this.getCustomerReviewSetList({ query: { product: 'id' } })
  }
}
</script>
