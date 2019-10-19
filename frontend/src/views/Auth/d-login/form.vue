<template>
  <v-form
    ref="form"
    v-model="isValidForm"
    lazy-validation
    class="d-form d-form__auth"
    onSubmit="return false;"
    @submit="handleLogIn">
    <v-card
      :flat="flat"
      :class="{
        transparent: transparent
      }">
      <v-progress-linear
        v-if="authenticating"
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
        <span>Ingresa a Quimder</span>
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
        SOCIAL LOGIN
      -->
      <template v-if="isSocialLoginEnabled">
        <v-card-title class="justify-center pb-0">
          <span>Inicia sesión con tus redes sociales</span>
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
        EMAIL LOGIN
      -->
      <v-card-title class="justify-center pb-0">
        <span>Inicia sesión con tu correo electrónico</span>
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
                :rules="[rules.required.password]"
                :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                :error-messages="getPasswordErrors()"/>
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
                @click="handleLogIn">
                Iniciar sesión
              </v-btn>
            </v-flex>

            <v-flex xs6 class="py-0">
              <v-btn
                block
                flat
                class="d-btn d-btn--bold d-btn--no-transform accent--text"
                @click="handleNoHaveAccount">
                {{ secondaryActionText }}
              </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-actions>

      <v-divider />
      <v-card-actions class="text-xs-center">
        <v-btn
          block
          flat
          :ripple="false"
          class="d-btn d-btn--no-transform"
          @click="handleForgotPassword">
          Olvidé mi contraseña.
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import { ROOT } from '@/router'
import { REMOVE_LOGIN_MESSAGES } from '@/store/_processes'
import { SIGNUP, PASSWORD_RECOVERY } from '@/router/auth'
import { AuthMixin } from '../_mixins'
import { EMAIL } from '../_utils'

export default {
  name: 'd-login-form',
  mixins: [AuthMixin],
  props: {
    secondaryActionText: {
      type: String,
      default: 'No tengo una cuenta.'
    },
    redirectAfterLogin: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
      form: {
        email: '',
        password: '',
        persistence: true
      },
      rules: {
        email: v => EMAIL.test(v) || 'Email inválido',
        required: {
          email: v => !!v || 'Ingresa tu correo electrónico.',
          password: v => !!v || 'Ingresa tu contraseña.'
        }
      }
    }
  },
  computed: {
    ...mapState('auth', {
      authenticating: 'authenticating',
      loginSuccess: 'loginSuccess',
      loginFailure: 'loginFailure',
      loginMessages: 'loginMessages'
    }),
    nonFieldErrors () {
      const { loginMessages } = this
      let nonFieldErrors = null

      if (loginMessages && loginMessages.nonFieldErrors) {
        nonFieldErrors = [...loginMessages.nonFieldErrors]
      }
      return nonFieldErrors
    }
  },
  watch: {
    loginSuccess (val, oldVal) {
      if (val) {
        const { form } = this.$refs
        form.reset()

        const { closeAction } = this
        if (closeAction) {
          closeAction()
        }

        if (this.redirectAfterLogin) {
          let next = this.$route.query.next
          if (next) {
            if (next.includes('dashboard')) {
              let { protocol, host } = window.location
              window.location.href = `${protocol}//${host}${next}`
            }
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
      login: 'login'
    }),
    ...mapMutations('auth', {
      clearMessages: REMOVE_LOGIN_MESSAGES
    }),
    getEmailErrors () {
      const { loginMessages } = this
      let emailErrors = []

      if (loginMessages && loginMessages.email) {
        emailErrors = [...loginMessages.email]
      }
      return emailErrors
    },
    getPasswordErrors () {
      const { loginMessages } = this
      let passwordErrors = []

      if (loginMessages && loginMessages.password) {
        passwordErrors = [...loginMessages.password]
      }
      return passwordErrors
    },
    handleLogIn () {
      this.clearMessages()

      const { form } = this.$refs
      form.validate()

      if (this.isValidForm) {
        this.login({ ...this.form })
      }
    },
    handleNoHaveAccount () {
      const { form } = this.$refs
      form.reset()

      if (!this.secondaryAction) {
        const { $router } = this
        $router.push({ name: SIGNUP })
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
    },
    handleForgotPassword () {
      const { $router } = this

      if (this.closeAction) {
        this.closeAction()
      }

      $router.push({ name: PASSWORD_RECOVERY })
    }
  }
}
</script>
