<template>
  <BaseErrorView>
    <v-content
      app
      class="d-view-error-content">
      <v-container>
        <img
          class="d-view-error__image"
          :src="assets.image"
          alt="Error 403"
          title="Error 403">
        <div
          class="d-view-error__message">
          <h1>
            No tienes permisos para ingresar aquí.
          </h1>
          <v-btn
            :to="{ name: links.index }"
            large
            color="accent"
            class="d-btn d-btn--rounded d-btn--bold d-btn--no-transform">
            <d-icon name="b-store"/>
            Volver a la tienda
          </v-btn>
        </div>
      </v-container>
    </v-content>
  </BaseErrorView>
</template>

<script>
import Image403 from '@/assets/images/errors/403.svg'
import { ROOT } from '@/router'
import BaseErrorView from './Base.vue'

export default {
  name: 'ForbiddenView',
  components: {
    'BaseErrorView': BaseErrorView
  },
  data () {
    return {
      assets: {
        image: Image403
      },
      links: {
        index: ROOT
      }
    }
  }
}
</script>
