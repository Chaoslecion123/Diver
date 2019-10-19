<template>
  <v-form
    ref="form"
    v-model="isValidForm"
    class="d-form d-form__auth"
    onSubmit="return false;"
    @submit="handleSignup">
    <v-card
      :flat="flat"
      :class="{
        transparent: transparent
      }">
      <v-progress-linear
        v-if="signingup"
        height="2"
        color="accent"
        :indeterminate="true"/>

      <!--
        TITLE
      -->
      <v-card-title
        :class="[
          'title',
          'font-weight-regular',
          {
            'justify-center': !closeAction,
            'justify-space-between': !!closeAction
          }
        ]">
        <span>Únete a Quimder</span>
        <template v-if="closeAction">
          <v-avatar
            size="24"
            style="cursor: pointer;"
            @click="handleCloseAction">
            <d-icon name="b-close" style="color: red;" />
          </v-avatar>
        </template>
      </v-card-title>
      <v-divider />
      <!--
        SOCIAL REGISTRATION
      -->
      <template v-if="isSocialLoginEnabled">
        <v-card-title class="justify-center pb-0">
          <span>Registrate con tus redes sociales</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-lg class="pa-0">
            <v-layout row wrap justify-center>
              <v-flex v-if="facebookLoginEnabled" xs6 class="py-0">
                <v-btn
                  :href="facebookProvider && facebookProvider.getUrl()"
                  block
                  dark
                  color="#415A99"
                  class="d-btn d-btn--bold d-btn--no-transform">
                  <d-icon name="b-facebook-fill" class="mr-1" />
                  Facebook
                </v-btn>
              </v-flex>

              <v-flex v-if="googleLoginEnabled" xs6 class="py-0">
                <v-btn
                  dark
                  block
                  color="#E63A3A"
                  class="d-btn d-btn--bold d-btn--no-transform">
                  <d-icon name="b-google" class="mr-1" />
                  Gmail
                </v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-text class="text-xs-center d-form__auth--separator">
          O
        </v-card-text>
      </template>

      <!--
        EMAIL REGISTRATION
      -->
      <v-card-title class="justify-center pb-0">
        <span>Registrate con tu correo electrónico</span>
      </v-card-title>

      <v-card-text class="pb-0">
        <v-container class="pa-0">
          <v-layout row wrap>
            <v-flex v-if="nonFieldErrors" xs12>
              <div
                class="v-input v-text-field v-text-field--solo v-text-field--enclosed theme--light">
                <div class="v-input__control">
                  <div class="v-text-field__details">
                    <div class="v-messages theme--light error--text ">
                      <div
                        v-for="(message, index) in nonFieldErrors"
                        :key="index"
                        class="v-messages__wrapper">
                        {{ message }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </v-flex>

            <v-flex xs12>
              <v-text-field
                ref="email"
                v-model="form.email"
                browser-autocomplete="off"
                prepend-inner-icon="account_circle"
                placeholder="Correo electrónico"
                type="email"
                flat
                solo
                :rules="[rules.email, rules.required.email]"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                :error-messages="getEmailErrors()"/>
            </v-flex>

            <v-flex xs12>
              <v-text-field
                ref="password"
                v-model="form.password"
                browser-autocomplete="off"
                prepend-inner-icon="lock"
                placeholder="Contraseña"
                type="password"
                flat
                solo
                required
                :rules="[rules.passwordLength, rules.required.password]"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                :error-messages="getPasswordErrors()"/>
            </v-flex>

            <v-flex xs12>
              <v-text-field
                ref="passwordConfirm"
                v-model="form.passwordConfirm"
                browser-autocomplete="off"
                prepend-inner-icon="lock"
                placeholder="Confirma tu contraseña"
                type="password"
                flat
                solo
                required
                :rules="[rules.required.passwordConfirm]"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"/>
            </v-flex>

            <v-flex xs12 py-0>
              <v-checkbox
                v-model="form.suscribedToNewsletter"
                required
                class="mt-2">
                <div slot="label">
                  Me gustaría recibir comunicaciones promocionales.
                </div>
              </v-checkbox>
            </v-flex>

            <v-flex xs12 py-0>
              <v-checkbox
                v-model="form.termsAndConditions"
                required
                class="mt-2"
                :rules="[rules.required.termsAndConditions]"
                :error-messages="getTermsAndConditionsErrors()">
                <div slot="label">
                  Acepto términos y condiciones de la politíca de privacidad y
                  tratamiento de datos personales.
                </div>
              </v-checkbox>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-card-actions class="pa-0">
        <v-container grid-list-lg>
          <v-layout row wrap justify-center>
            <v-flex xs6 class="py-0">
              <v-btn
                block
                depressed
                color="accent"
                class="d-btn d-btn--bold d-btn--no-transform"
                @click="handleSignup">
                Registrarme
              </v-btn>
            </v-flex>

            <v-flex xs6 class="py-0">
              <v-btn
                block
                flat
                class="d-btn d-btn--bold d-btn--no-transform accent--text"
                @click="handleExistingAccount">
                {{ secondaryActionText }}
              </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import { REMOVE_SIGNUP_MESSAGES } from '@/store/_processes'
import { ROOT } from '@/router'
import { LOGIN } from '@/router/auth'
import { AuthMixin } from '../_mixins'
import { EMAIL } from '../_utils'

export default {
  name: 'd-signup-form',
  mixins: [AuthMixin],
  props: {
    secondaryActionText: {
      type: String,
      default: 'Ya tengo una cuenta.'
    },
    redirectAfterSignup: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
      form: {
        email: '',
        password: '',
        passwordConfirm: '',
        suscribedToNewsletter: false,
        termsAndConditions: false
      },
      rules: {
        email: v => EMAIL.test(v) || 'Email inválido',
        passwordLength: v =>
          (v && v.length >= 8) ||
          'La contraseña debe tener al menos 8 caracteres',
        required: {
          email: v => !!v || 'Ingresa tu correo electrónico.',
          password: v => !!v || 'Ingresa tu contraseña.',
          passwordConfirm: v => !!v || 'Confirma tu contraseña.',
          termsAndConditions: v =>
            !!v || '¡Debes estar de acuerdo para continuar!'
        }
      }
    }
  },
  computed: {
    ...mapState('auth', {
      signingup: 'signingup',
      signupSuccess: 'signupSuccess',
      signupFailure: 'signupFailure',
      signupMessages: 'signupMessages'
    }),
    nonFieldErrors () {
      const { signupMessages } = this
      let nonFieldErrors = null

      if (signupMessages && signupMessages.nonFieldErrors) {
        nonFieldErrors = [...signupMessages.nonFieldErrors]
      }
      return nonFieldErrors
    }
  },
  watch: {
    signupSuccess (val, oldVal) {
      if (val) {
        const { form } = this.$refs
        form.reset()

        const { closeAction } = this

        if (closeAction) {
          closeAction()
        }

        if (this.redirectAfterSignup) {
          let next = this.$route.query.next

          if (next) {
            this.$router.push(next)
          } else {
            this.$router.push({ name: ROOT })
          }
        }
      }
    }
  },
  methods: {
    ...mapActions('auth', {
      signup: 'signup'
    }),
    ...mapMutations('auth', {
      clearMessages: REMOVE_SIGNUP_MESSAGES
    }),
    getEmailErrors () {
      const { signupMessages } = this
      let emailErrors = []

      if (signupMessages && signupMessages.email) {
        emailErrors = [...signupMessages.email]
      }
      return emailErrors
    },
    passwordMatchError () {
      const { password, passwordConfirm } = this.form

      const emptyPasswords = password === '' || passwordConfirm === ''
      if (emptyPasswords) return ''

      const passwordsMatch = password === passwordConfirm
      if (passwordsMatch) return ''

      return ['Las contraseñas no coindice.']
    },
    getPasswordErrors () {
      const { signupMessages } = this
      let passwordErrors = []

      if (signupMessages && signupMessages.password) {
        passwordErrors = [...signupMessages.password]
      }
      return [...passwordErrors, ...this.passwordMatchError()]
    },
    getTermsAndConditionsErrors () {
      const { signupMessages } = this
      let termsAndConditionsErrors = []
      if (signupMessages && signupMessages.termsAndConditions) {
        termsAndConditionsErrors = [...signupMessages.termsAndConditionsErrors]
      }
      return termsAndConditionsErrors
    },
    handleSignup () {
      this.clearMessages()

      const { form } = this.$refs
      form.validate()

      if (this.isValidForm) {
        this.signup({ ...this.form })
      }
    },
    handleExistingAccount () {
      const { form } = this.$refs
      form.reset()

      if (!this.secondaryAction) {
        const { $router } = this
        $router.push({ name: LOGIN })
      } else {
        this.secondaryAction()
      }
    },
    handleCloseAction () {
      const { form } = this.$refs
      form.reset()

      if (this.closeAction) {
        this.closeAction()
      }
    }
  }
}
</script>
