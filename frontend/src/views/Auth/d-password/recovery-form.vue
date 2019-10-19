<template>
  <v-form
    ref="form"
    v-model="isValidForm"
    lazy-validation
    class="d-form d-form__auth"
    onSubmit="return false;"
    @submit="handleSubmit">
    <v-card
      :flat="flat"
      :class="{
        transparent: transparent
      }">
      <v-progress-linear
        v-if="requesting"
        height="2"
        color="accent"
        :indeterminate="true"/>

      <!--
        TITLE
      -->
      <v-card-title :class="['title', 'font-weight-regular', 'justify-center']">
        <span>Recupera tu contraseña</span>
      </v-card-title>
      <v-divider />

      <template v-if="!promptSendEmail">
        <!--
          EMAIL LOGIN
        -->
        <v-card-title class="text-xs-center pb-0">
          <span>
            Ingresa tu correo eletrónico y te enviaremos instrucciones para
            restablecer tu contraseña.
          </span>
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
                  :rules="[rules.email, rules.required]"
                  :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
                  :error-messages="getEmailErrors()"/>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>

        <v-card-actions class="px-3 pb-3 pt-0">
          <v-btn
            block
            depressed
            color="accent"
            class="d-btn d-btn--bold d-btn--no-transform"
            :disabled="requesting"
            @click="handleSubmit">
            Recuperar mi contraseña
          </v-btn>
        </v-card-actions>

        <v-divider />
        <v-card-actions>
          <v-btn
            block
            flat
            :ripple="false"
            class="d-btn d-btn--no-transform"
            :to="{ name: links.login }">
            Volver al inicio de sesión
          </v-btn>
        </v-card-actions>
      </template>
      <template v-else>
        <v-card-text class="text-xs-center">
          Si tu correo se encuentra en nuestros sistemas, recibiras un enlace
          para modificar tu contraseña.
        </v-card-text>

        <v-card-actions class="pa-3">
          <v-btn
            block
            depressed
            color="accent"
            class="d-btn d-btn--bold d-btn--no-transform"
            :to="{ name: links.home }">
            <d-icon scale="1.5" name="b-shopping-cart" class="mr-2" />
            Volver a la tienda
          </v-btn>
        </v-card-actions>
      </template>
    </v-card>
  </v-form>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import { REMOVE_RECOVERY_MESSAGES } from '@/store/_processes'
import { LOGIN } from '@/router/auth'
import { ROOT } from '@/router'
import { AuthMixin } from '../_mixins'
import { EMAIL } from '../_utils'

export default {
  name: 'd-password-recovery-form',
  mixins: [AuthMixin],
  data () {
    return {
      links: {
        home: ROOT,
        login: LOGIN
      },
      form: {
        email: ''
      },
      rules: {
        email: v => EMAIL.test(v) || 'Email inválido',
        required: v => !!v || 'Ingresa tu correo electrónico.'
      },
      promptSendEmail: false
    }
  },
  computed: {
    ...mapState('auth', {
      requesting: 'requesting',
      recoverySuccess: 'recoverySuccess',
      recoveryFailure: 'recoveryFailure',
      recoveryMessages: 'recoveryMessages'
    }),
    nonFieldErrors () {
      const { recoveryMessages } = this
      let nonFieldErrors = null

      if (recoveryMessages && recoveryMessages.nonFieldErrors) {
        nonFieldErrors = [...recoveryMessages.nonFieldErrors]
      }
      return nonFieldErrors
    }
  },
  watch: {
    recoverySuccess (val, oldVal) {
      if (val) {
        this.promptSendEmail = true
      }
    }
  },
  methods: {
    ...mapActions('auth', {
      passwordRecoveryRequest: 'passwordRecoveryRequest'
    }),
    ...mapMutations('auth', {
      clearMessages: REMOVE_RECOVERY_MESSAGES
    }),
    getEmailErrors () {
      const { recoveryMessages } = this
      let emailErrors = []

      if (recoveryMessages && recoveryMessages.email) {
        emailErrors = [...recoveryMessages.email]
      }
      return emailErrors
    },
    getPasswordErrors () {
      const { recoveryMessages } = this
      let passwordErrors = []

      if (recoveryMessages && recoveryMessages.password) {
        passwordErrors = [...recoveryMessages.password]
      }
      return passwordErrors
    },
    handleCloseAction () {
      const { form } = this.$refs
      form.reset()

      if (this.closeAction) {
        this.closeAction()
      }
    },
    handleSubmit () {
      this.clearMessages()

      const { form } = this.$refs
      form.validate()

      if (this.isValidForm) {
        this.passwordRecoveryRequest({ ...this.form })
      }
    }
  }
}
</script>
