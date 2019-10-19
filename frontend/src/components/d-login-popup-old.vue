<template>
  <v-dialog
    v-model="innerValue"
    width="500"
    persistent
    color="q-orange--background"
    content-class="d-login-popup">
    <v-card class="py-3 px-4">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
        <v-avatar
          class="subheading white--text"
          size="24"
          style="cursor: pointer;"
          @click="close">
          <d-icon name="b-close" style="color: red;"/>
        </v-avatar>
      </v-card-title>
      <v-divider></v-divider>

      <v-window
        v-model="step">
        <v-window-item
          :value="1">
          <v-form
            ref="loginForm"
            lazy-validation>
            <v-container
              grid-list-md>
              <v-layout
                row
                wrap>
                <v-flex
                  xs12
                  class="mb-3">
                  Inicia sesión con
                </v-flex>

                <v-flex
                  xs6>
                  <v-btn
                    block
                    dark
                    depressed
                    color="#415A99"
                    class="ma-0 font-weight-600 border-radius">
                    Facebook
                  </v-btn>
                </v-flex>

                <v-flex
                  xs6>
                  <v-btn
                    dark
                    block
                    depressed
                    color="#E63A3A"
                    class="ma-0 font-weight-600 border-radius">
                    Gmail
                  </v-btn>
                </v-flex>

                <v-flex
                  xs12
                  class="my-3">
                  O ingresa tus credenciales
                </v-flex>

                <v-flex
                  xs12>
                  E-mail:
                </v-flex>
                <v-flex
                  xs12
                  py-0>
                  <v-text-field
                    v-model="loginForm.email"
                    class="border-radius"
                    flat
                    outline
                    required
                    type="email"
                    validate-on-blur
                    :rules="[
                      rules.email,
                      rules.emailRequired,
                    ]"/>
                </v-flex>
                <v-flex
                  xs12>
                  Contraseña:
                </v-flex>
                <v-flex
                  xs12
                  py-0>
                  <v-text-field
                    v-model="loginForm.password"
                    class="border-radius"
                    flat
                    outline
                    required
                    type="password"
                    validate-on-blur
                    :rules="[
                      rules.passwordRequired
                    ]"/>
                </v-flex>
                <v-flex text-xs-right>
                  <router-link
                    :to="links.passwordRecovery"
                    class="black--text"
                    style="text-decoration:none;">
                    Olvidé mi Contraseña*
                  </router-link>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-window-item>

        <v-window-item
          :value="2">
          <v-form
            lazy-validation>
            <v-container
              grid-list-md>
              <v-layout
                row
                wrap>
                <v-flex
                  xs12
                  class="mb-3">
                  Crea tu cuenta con
                </v-flex>

                <v-flex
                  xs6>
                  <v-btn
                    class="ma-0 font-weight-600 border-radius"
                    color="#415A99"
                    block
                    dark
                    depressed>
                    Facebook
                  </v-btn>
                </v-flex>
                <v-flex
                  xs6>
                  <v-btn
                    class="ma-0 font-weight-600 border-radius"
                    color="#E63A3A"
                    dark
                    block
                    depressed>
                    Gmail
                  </v-btn>
                </v-flex>

                <v-flex
                  xs12
                  class="my-3">
                  O completa el fomulario
                </v-flex>

                <v-flex
                  xs6
                  py-0>
                  <v-flex>
                    Nombre
                  </v-flex>
                  <v-text-field
                    class="border-radius"
                    :rules="[
                      rules.required
                    ]"
                    outline
                    flat
                    required
                    type="text"/>
                </v-flex>
                <v-flex
                  xs6
                  py-0>
                  <v-flex>
                    Apellido
                  </v-flex>
                  <v-text-field
                    class="border-radius"
                    :rules="[
                      rules.required
                    ]"
                    outline
                    flat
                    required
                    type="text"/>
                </v-flex>
                <v-flex
                  xs6
                  py-0>
                  <v-flex>
                    E-mail:
                  </v-flex>
                  <v-text-field
                    class="border-radius"
                    :rules="[
                      rules.required,
                      rules.email
                    ]"
                    outline
                    flat
                    required
                    type="email"/>
                </v-flex>
                <v-flex
                  xs6
                  py-0>
                  <v-flex>
                    DNI
                  </v-flex>
                  <v-text-field
                    class="border-radius"
                    mask="########"
                    :rules="[
                      rules.dni
                    ]"
                    outline
                    flat
                    hide-details
                    type="text"/>
                </v-flex>
                <v-flex
                  xs6
                  py-0>
                  <v-flex>
                  Contraseña:
                  </v-flex>
                  <v-text-field
                    class="border-radius"
                    type="password"
                    :rules="[
                      rules.required,
                      rules.min
                    ]"
                    outline
                    flat
                    required/>
                </v-flex>
                <v-flex
                  xs6
                  py-0>
                  <v-flex>
                    Confirmar contraseña
                  </v-flex>
                  <v-text-field
                    class="border-radius"
                    type="password"
                    :rules="[
                      rules.required,
                      rules.min
                    ]"
                    outline
                    flat
                    required/>
                </v-flex>
                <v-flex
                  xs12
                  py-0>
                  <v-checkbox
                    class="mt-2 d-login-popup-checkbok"
                    v-model="newletter"
                    :rules="[
                      v => !!v || '¡Debes estar de acuerdo para continuar!'
                    ]"
                    label="Me gustaría recibir comunicaciones promocionales."
                    required/>
                </v-flex>
                <v-flex
                  xs12
                  py-0>
                  <v-checkbox
                    class="mt-2 d-login-popup-checkbok"
                    v-model="termsAndConfitions"
                    :rules="[
                      v => !!v || '¡Debes estar de acuerdo para continuar!'
                    ]"
                    label="Acepto términos y condiciones de la politíca de privacidad y tratamiento de datos personales."
                    required/>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>
      <v-card-actions class="pt-3">
        <v-btn
          v-if="step == 2"
          class="font-weight-600"
          flat
          @click="step--">
          <d-icon class="mr-2" medium right dark name="b-left"/>
          Iniciar sesión
        </v-btn>
        <v-btn
          v-else
          class="ml-2 font-weight-600 q-orange--background border-radius"
          dark
          depressed
          v-on:keyup.enter="handleLogin"
          @click="handleLogin">
          Iniciar Sesion
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          class="font-weight-600"
          v-if="step == 1"
          flat
          @click="step++">
          Crear Cuenta
          <d-icon class="ml-2" medium right dark name="b-right"/>
        </v-btn>
        <v-btn
          v-else
          class="mr-2 font-weight-600 q-orange--background border-radius"
          dark
          depressed
          @click="handleSignup">
          Crear Cuenta
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style lang="less">
.v-btn.v-btn--disabled.v-btn--flat.theme--light {
  color: transparent !important;
  i {
    color: transparent !important;
  }
}
</style>

<script>
import { mapState, mapActions } from 'vuex'

import { PASSWORD_RECOVERY } from '@/router/password'

const EMAIL_PATTERN = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

export default {
  name: 'd-login-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      links: {
        passwordRecovery: {
          name: PASSWORD_RECOVERY
        }
      },
      step: 1,
      newletter: false,
      termsAndConfitions: false,
      recovery: false,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        emailRequired: value => !!value || 'Ingresa tu dirección de correo electrónico.',
        passwordRequired: value => !!value || 'Ingresa tu contraseña',
        emailMatch: () => ('El e-mail y la constraseña son incorrectos.'),
        email: value => {
          return EMAIL_PATTERN.test(value) || 'Email inválido'
        },
        min: v => (v && v.length >= 8) || 'La contraseña debe tener al menos 8 caracteres',
        dni: v => (v && v.length === 8) || 'El DNI debe tener 8 dígitos.'
      },
      loginForm: {
        email: '',
        password: ''
      },
      snackbar: {
        isOpen: false,
        timeout: 2000,
        text: 'Hello, I\'m a snackbar'
      }
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
    },
    currentTitle () {
      switch (this.step) {
        case 1: return 'INICIAR SESIÓN'
        default: return 'CREAR CUENTA'
      }
    },
    currentButton () {
      switch (this.step) {
        case 1: return 'Iniciar sesión'
        default: return 'Crear cuenta'
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
        this.snackbar.isOpen = true

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
    ...mapActions('auth', {
      performLogin: 'login'
    }),

    close () {
      let route = {
        name: this.$route.name,
        params: { ...this.$route.params },
        query: { ...this.$route.query }
      }

      delete route.query['login']
      this.innerValue = false
      this.$router.replace(route)
    },

    handleLogin () {
      // this.$router.push({ name: this.$route.name})
      if (this.$refs.loginForm.validate()) {
        this.performLogin({
          email: this.loginForm.email,
          password: this.loginForm.password,
          persistence: true
        })
      }
    },

    handleSignup () {
      console.log('handleSignup')
    }
  }
}
</script>
