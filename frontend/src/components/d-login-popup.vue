<template>
  <v-dialog
    v-model="innerValue"
    width="fit-content"
    lazy
    persistent
    color="q-orange--background"
    content-class="d-login-popup">
    <v-window v-model="step">
      <v-window-item :value="1">
        <d-login-form :secondaryAction="goToSignUp" :closeAction="close" />
      </v-window-item>

      <v-window-item :value="2">
        <d-signup-form :secondaryAction="goToLogIn" :closeAction="close" />
      </v-window-item>
    </v-window>
  </v-dialog>
</template>

<script>
import { mapState } from 'vuex'
import LogIn from '@/views/Auth/d-login'
import SignUp from '@/views/Auth/d-signup'

export default {
  name: 'd-login-popup',
  components: {
    'd-login-form': LogIn.Form,
    'd-signup-form': SignUp.Form
  },
  props: {
    value: {
      type: Boolean,
      default: false
    }
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
      let route = {
        name: this.$route.name,
        params: { ...this.$route.params },
        query: { ...this.$route.query }
      }
      delete route.query['login']
      this.innerValue = false
      this.$router.replace(route)
    }
  }
}
</script>
