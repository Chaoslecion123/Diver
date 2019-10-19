<template>
  <v-content
    app
    class="d-page-detail">
    <v-container
      v-if="page"
      class="mt-5 mb-5 d-page-detail__content"
      grid-list-md>
      <v-layout
        row
        wrap>
        <v-flex
          xs12>
          <h1>{{ page.title }}</h1>
        </v-flex>
        <v-divider class="flex xs12"/>
        <v-flex
          v-html="page.content">
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<style lang="less">
.d-page-detail {
  .d-page-detail__content {
    width: 100%;
    max-width: 800px;

    h2 {
      margin-bottom: 0.75rem;
    }

    h3 {
      margin-bottom: 0.5rem;
    }
  }
}
</style>
<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'Page',
  computed: {
    ...mapState('page', {
      page: 'object'
    })
  },
  methods: {
    ...mapActions('page', {
      pageRead: 'read'
    })
  },
  created () {
    const slug = this.$route.params.slug
    this.pageRead({
      id: slug
    })
  }
}
</script>
