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
        <div class="d-form d-form__auth">
          <v-card>
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
            <template v-if="verifyUser && verifyUser.exists">
              <v-card-text class="text-xs-center">
                <div>
                  Hemos encontrado una cuenta con tu correo electrónico.
                </div>
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
                  @click="goToLogIn">
                  Quiero iniciar sesión
                </v-btn>
              </v-card-text>
            </template>
            <template v-else>
              <v-card-text class="text-xs-center">
                <div>
                  Parece que no tienes una cuenta en Quimder.
                </div>
                <div>
                  Registrate y disfruta de grandes beneficios para tu piel.
                </div>
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
                  @click="goToSignUp">
                  Quiero registrarme
                </v-btn>
              </v-card-text>
            </template>
            <v-card-text class="text-xs-center d-form__auth--separator pt-0">
              O
            </v-card-text>
            <v-card-text class="text-xs-center pt-0">
              Puedes comprar sin registrarte.
            </v-card-text>
            <v-card-text class="text-xs-center pt-0">
              <v-btn
                large
                outline
                color="accent"
                :class="[
                  'ma-0',
                  'd-btn',
                  'd-btn--no-transform',
                  'd-btn--bold',
                  'd-btn--rounded'
                ]"
                @click="close">
                Quiero comprar como invitado
              </v-btn>
            </v-card-text>
          </v-card>
        </div>
      </v-window-item>

      <v-window-item :value="2">
        <d-login-form
          secondaryActionText="Continuar como invitado"
          :secondaryAction="close"
          :closeAction="close"
          :redirectAfterLogin="false"/>
      </v-window-item>

      <v-window-item :value="3">
        <d-signup-form
          secondaryActionText="Continuar como invitado"
          :secondaryAction="close"
          :closeAction="close"
          :redirectAfterSignup="false"/>
      </v-window-item>
    </v-window>
  </v-dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex'
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
    },
    email: {
      type: String,
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
    ...mapState('user', {
      verifyUser: 'verify'
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
    value (val, oldVal) {
      if (val) {
        this.step = 1
        this.verifyUserExistence({
          data: {
            email: this.email
          }
        })
      }
    }
  },
  methods: {
    ...mapActions('user', {
      verifyUserExistence: 'verify'
    }),
    goToLogIn () {
      this.step = 2
    },
    goToSignUp () {
      this.step = 3
    },
    handleCloseAction () {},
    close () {
      this.innerValue = false
    }
  }
}
</script>
