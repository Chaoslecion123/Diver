<template>
  <BaseErrorView>
    <v-content
      app
      class="d-view-error-content">
      <v-container>
        <img
          class="d-view-error__image"
          :src="assets.image"
          alt="Error 400"
          title="Error 400">
        <div
          class="d-view-error__message">
          <h1>
            Lo sentimos, hubo un problema con tu solicitud.
          </h1>
          <h1>
            Por favor intentalo nuevamente.
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
import Image400 from '@/assets/images/errors/400.svg'
import { ROOT } from '@/router'
import BaseErrorView from './Base.vue'

export default {
  name: 'BadRequestView',
  components: {
    'BaseErrorView': BaseErrorView
  },
  data () {
    return {
      assets: {
        image: Image400
      },
      links: {
        index: ROOT
      }
    }
  }
}
</script>
