<template>
  <v-dialog
    v-model="innerValue"
    scrollable
    persistent
    :width="$vuetify.breakpoint.smAndUp ? 'fit-content' : null"
    :fullscreen="$vuetify.breakpoint.xs">
    <d-address-form v-if="value" :closeAction="close" :address="address" />
  </v-dialog>
</template>

<script>
import { mapState } from 'vuex'
import Form from './form'

export default {
  name: 'd-address-popup',
  components: {
    'd-address-form': Form
  },
  props: {
    value: {
      type: Boolean,
      default: false
    },
    address: {
      type: Object,
      default: null
    },
    closeAction: null
  },
  data () {
    return {
      step: 1
    }
  },
  computed: {
    ...mapState('auth', {
      loginSuccess: 'loginSuccess'
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
  watch: {
    value () {
      this.login = this.value
    },
    loginSuccess (val, oldVal) {
      if (val) {
        this.innerValue = false

        let route = {
          name: this.$route.name,
          params: { ...this.$route.params },
          query: { ...this.$route.query }
        }

        delete route.query['login']
        this.$router.replace(route)
      }
    }
  },
  methods: {
    goToSignUp () {
      this.step = 2
    },
    goToLogIn () {
      this.step = 1
    },
    close () {
      this.innerValue = false

      if (this.closeAction) {
        this.closeAction()
      }
    }
  }
}
</script>
