<template>
  <v-form
    ref="form"
    v-model="isValidForm"
    class="d-form d-form__auth">
    <v-card
      :flat="flat"
      :class="{
        'transparent': transparent
      }">
      <v-progress-linear
        v-if="restoring"
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
          'justify-center'
        ]">
        <span>Restablece tu contraseña</span>
      </v-card-title>
      <v-divider/>

      <!--
        EMAIL REGISTRATION
      -->
      <v-card-text
        class="pb-0">
        <v-container
          class="pa-0">
          <v-layout
            row
            wrap>
            <v-flex
              v-if="nonFieldErrors"
              xs12>
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

            <v-flex
              xs12>
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
                :rules="[
                  rules.passwordLength,
                  rules.required.password,
                ]"
                :class="[
                  'd-input',
                  'd-input--rounded',
                  'd-input--bordered',
                ]"
                :error-messages="getPasswordErrors()"/>
            </v-flex>

            <v-flex
              xs12>
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
                :rules="[
                  rules.required.passwordConfirm
                ]"
                :class="[
                  'd-input',
                  'd-input--rounded',
                  'd-input--bordered',
                ]"/>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-card-actions
        class="pa-0">
        <v-container
          grid-list-lg>
          <v-layout
            row
            wrap
            justify-center>
            <v-flex
              xs12
              class="py-0">
              <v-btn
                block
                dark
                color="accent"
                class="d-btn d-btn--bold d-btn--no-transform"
                @click="handlePasswordReset">
                Restablecer mi contraseña
              </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-actions>

      <v-divider/>
      <v-card-actions
        class="text-xs-center">
        <v-btn
          block
          flat
          :ripple="false"
          class="d-btn d-btn--no-transform"
          @click="handleReturnToLogin">
          Volver al inicio de sesión
        </v-btn>
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

export default {
  name: 'd-password-reset-form',
  mixins: [
    AuthMixin
  ],
  data () {
    return {
      form: {
        password: '',
        passwordConfirm: ''
      },
      rules: {
        passwordLength: v => (v && v.length >= 8) || 'La contraseña debe tener al menos 8 caracteres',
        required: {
          password: v => !!v || 'Ingresa tu contraseña.',
          passwordConfirm: v => !!v || 'Confirma tu contraseña.'
        }
      }
    }
  },
  computed: {
    ...mapState('auth', {
      restoring: 'restoring',
      resetSuccess: 'resetSuccess',
      resetFailure: 'resetFailure',
      resetMessages: 'resetMessages'
    }),
    nonFieldErrors () {
      const { resetMessages } = this
      let nonFieldErrors = null

      if (resetMessages && resetMessages.nonFieldErrors) {
        nonFieldErrors = [...resetMessages.nonFieldErrors]
      }
      return nonFieldErrors
    }
  },
  watch: {
    resetSuccess (val, oldVal) {
      if (val) {
        const { form } = this.$refs
        form.reset()

        const { closeAction } = this
        if (closeAction) {
          closeAction()
        }

        let next = this.$route.query.next

        if (next) {
          this.$router.push(next)
        } else {
          this.$router.push({ name: ROOT })
        }
      }
    }
  },
  methods: {
    ...mapActions('auth', {
      passwordReset: 'passwordReset'
    }),
    ...mapMutations('auth', {
      clearMessages: REMOVE_SIGNUP_MESSAGES
    }),
    passwordMatchError () {
      const { password, passwordConfirm } = this.form

      const emptyPasswords = password === '' || passwordConfirm === ''
      if (emptyPasswords) return ''

      const passwordsMatch = password === passwordConfirm
      if (passwordsMatch) return ''

      return ['Las contraseñas no coindice.']
    },
    getPasswordErrors () {
      const { resetMessages } = this
      let passwordErrors = []

      if (resetMessages && resetMessages.password) {
        passwordErrors = [...resetMessages.password]
      }
      return [...passwordErrors, ...this.passwordMatchError()]
    },
    handlePasswordReset () {
      this.clearMessages()

      const { form } = this.$refs
      form.validate()
      console.log(this.form)
      if (this.isValidForm) {
        this.passwordReset({
          newPassword1: this.form.password,
          newPassword2: this.form.passwordConfirm,
          token: this.$route.params.token,
          uid: this.$route.params.uid
        })
      }
    },
    handleReturnToLogin () {
      const { $router } = this
      $router.push({ name: LOGIN })
    }
  }
}
</script>
