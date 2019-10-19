import { Facebook } from './_social'

export const AuthMixin = {
  props: {
    closeAction: null,
    secondaryAction: null,
    flat: null,
    transparent: null
  },
  data () {
    return {
      isValidForm: true,
      facebookLoginEnabled: false,
      googleLoginEnabled: false,
      facebookProvider: null
    }
  },
  computed: {
    isSocialLoginEnabled () {
      const { facebookLoginEnabled, googleLoginEnabled } = this
      return facebookLoginEnabled || googleLoginEnabled
    }
  },
  created () {
    this.facebookLoginEnabled =
      document.querySelector('meta#facebook-key') !== null
    this.googleLoginEnabled = document.querySelector('meta#google-key') !== null

    const redirectUri = window.location.origin + '/auth/login/facebook'
    const clientId = 341058629833643
    this.facebookProvider = new Facebook(clientId, redirectUri)
  }
}
