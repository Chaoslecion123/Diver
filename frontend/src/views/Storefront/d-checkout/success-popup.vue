<template>
  <v-dialog
    v-model="innerValue"
    width="fit-content"
    lazy
    persistent
    color="q-orange--background"
    content-class="d-login-popup">
    <div class="d-form d-form__auth">
      <v-card>
        <v-card-title
          :class="['title', 'font-weight-regular', 'justify-center']">
          <span>Gracias por tu compra</span>
        </v-card-title>
        <v-divider />
        <v-card-text class="text-xs-center">
          Tu compra se ha realizado con exito.
        </v-card-text>
        <v-card-text class="text-xs-center pt-0">
          Hemos enviado los detalles de tu orden a tu correo electrónico .
        </v-card-text>
        <v-card-text class="text-xs-center pt-0">
          <v-btn
            large
            depressed
            color="accent"
            :class="[
              'ma-0',
              'd-btn',
              'd-btn--no-transform',
              'd-btn--bold',
              'd-btn--rounded'
            ]"
            @click="close">
            <d-icon scale="1.5" name="b-shopping-cart" class="mr-2" />
            Seguir comprando
          </v-btn>
        </v-card-text>
      </v-card>
    </div>
  </v-dialog>
</template>

<script>
import { mapState } from 'vuex'
import { ROOT } from '@/router'

export default {
  name: 'd-login-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    },
    closeAction: null
  },
  data () {
    return {
      step: 1
    }
  },
  computed: {
    ...mapState('order', {
      order: 'order'
    }),

    innerValue: {
      get () {
        return this.value
      },
      set (newVal) {
        this.$emit('input', newVal)
      }
    }
  },
  methods: {
    close () {
      this.$router.push({
        name: ROOT
      })
    }
  }
}
</script>
