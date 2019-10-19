<template>
  <v-form ref="form" class="d-add-comment" v-model="valid">
    <v-rating v-model="rating" class="d-rating mb-2">
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

    <v-textarea
      class="d-input d-input--bordered d-input--rounded mb-2"
      v-model="comment"
      type="text"
      no-resize
      solo
      flat
      hide-details
      required
      placeholder="¿Recomendarías el producto? ¿Fue lo que esperabas? ¿Te gustó o no? ¡Cuéntanos!"/>

    <v-btn
      class="d-btn d-btn--rounded d-btn--bold d-btn--no-transform"
      outline
      block
      :ripple="false"
      :disabled="!valid"
      color="accent"
      @click="postComment">
      Enviar Reseña
    </v-btn>

    <v-snackbar :value="createReviewError" right top :timeout="5000">
      Ya has comentado este producto.
      <v-btn color="accent" flat class="ma-0 px-2">
        <d-icon name="b-close" />
      </v-btn>
    </v-snackbar>
  </v-form>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'd-add-comment',
  data () {
    return {
      valid: false,
      rating: this.rating,
      comment: ''
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('customer-review', {
      createReviewError: 'createError',
      createReviewSuccess: 'createSuccess'
    }),
    userId () {
      if (this.user) {
        return this.user.id
      }
      return null
    },
    productId () {
      return this.$route.params.id
    }
  },
  watch: {
    createReviewSuccess (val, oldVal) {
      if (val) {
        this.getCustomerReviewList({
          query: {
            product: this.productId,
            expand: 'user'
          }
        })
      }
    }
  },
  methods: {
    ...mapActions('customer-review', {
      createReview: 'create'
    }),
    ...mapActions('customer-review', {
      getCustomerReviewList: 'list'
    }),
    postComment () {
      if (this.$refs.form.validate() && this.isAuthenticated) {
        const customerReview = {
          user: this.userId,
          product: this.productId,
          comment: this.comment,
          score: this.rating
        }
        this.createReview({
          data: customerReview
        })

        this.$refs.form.reset()
        this.rating = 0
      } else {
        this.$router.push({ name: this.$route.name, query: { login: true } })
      }
    }
  }
}
</script>
