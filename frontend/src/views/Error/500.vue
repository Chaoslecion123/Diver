<template>
  <BaseErrorView>
    <v-content
      app
      class="d-view-error-content">
      <v-container>
        <img
          class="d-view-error__image"
          :src="assets.image"
          alt="Error 500"
          title="Error 500">
        <div
          class="d-view-error__message">
          <h1>
            ¡Ups! Nuestros servidores están reportando problemas.
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
import Image500 from '@/assets/images/errors/500.svg'
import { ROOT } from '@/router'
import BaseErrorView from './Base.vue'

export default {
  name: 'ServerErrorView',
  components: {
    'BaseErrorView': BaseErrorView
  },
  data () {
    return {
      assets: {
        image: Image500
      },
      links: {
        index: ROOT
      }
    }
  }
}
</script>
