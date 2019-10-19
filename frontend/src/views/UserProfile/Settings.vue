<template>
  <v-flex xs12 md10 pl-3 style="font-size:14px;" class="remove-padding">
    <v-card class="mb-3" flat color="grey lighten-4">
      <v-layout row wrap align-center>
        <v-flex xs8 style="font-size:1.25rem;" class="font-weight-600">
          Datos personales
        </v-flex>

        <v-spacer />

        <v-flex xs5 sm3>
          <v-btn
            style="height:32px;"
            class="my-0 border-radius"
            :class="isEditingUser ? 'd-none' : 'd-block'"
            color="grey darken-4"
            depressed
            block
            dark
            @click="isEditingUser = !isEditingUser">
            Editar datos
          </v-btn>

          <v-btn
            style="height:32px;"
            class="my-0 border-radius"
            :class="!isEditingUser ? 'd-none' : 'd-block'"
            color="grey darken-4"
            depressed
            block
            dark
            @click="saveUserInfo">
            Guardar datos
          </v-btn>
        </v-flex>
      </v-layout>
    </v-card>

    <v-layout>
      <v-card class="py-3" flat color="grey lighten-4">
        <v-layout row wrap justify-space-between>
          <v-flex xs12 sm6 px-3 class="d-divider--right">
            <v-container pa-0 fluid grid-list-lg>
              <v-form ref="userInfoForm">
                <v-layout row wrap>
                  <v-flex xs12 md6 py-0>
                    {{ updateUserError }}
                    <v-flex px-0 mb-2>
                      Nombres
                    </v-flex>
                    <v-text-field
                      v-model="userFirstName"
                      class="border-radius"
                      :disabled="!isEditingUser"
                      :rules="[rules.required]"
                      solo
                      flat
                      required
                      type="text"/>
                  </v-flex>

                  <v-flex xs12 md6 py-0>
                    <v-flex px-0 mb-2>
                      Apellidos
                    </v-flex>
                    <v-text-field
                      v-model="userLastName"
                      class="border-radius"
                      :disabled="!isEditingUser"
                      :rules="[rules.required]"
                      solo
                      flat
                      required
                      type="text"/>
                  </v-flex>

                  <v-flex xs12 sm8 md6 py-0>
                    <v-flex px-0 mb-2>
                      Fecha de Nacimiento
                    </v-flex>
                    <v-dialog
                      ref="dialog"
                      v-model="datePopup"
                      :return-value.sync="date"
                      persistent
                      lazy
                      width="360px">
                      <v-text-field
                        class="border-radius"
                        slot="activator"
                        :disabled="!isEditingUser"
                        v-model="date"
                        solo
                        flat
                        readonly/>

                      <v-date-picker
                        v-model="date"
                        color="#F58220"
                        scrollable
                        width="360px"
                        :disabled="!isEditingUser">
                        <v-spacer />
                        <v-btn flat color="q-orange" @click="datePopup = false">Cancel</v-btn>
                        <v-btn
                          flat
                          color="q-orange"
                          @click="$refs.dialog.save(date)">OK</v-btn>
                      </v-date-picker>
                    </v-dialog>
                  </v-flex>
                </v-layout>
              </v-form>
            </v-container>
          </v-flex>

          <v-flex class="set-margin-top-3" xs12 sm6 px-3>
            <v-container pa-0 fluid grid-list-lg>
              <v-form lazy-validation ref="changeUserEmail">
                <v-layout row wrap>
                  <v-flex xs12 py-0>
                    <v-flex px-0 mb-2>
                      Correo:
                    </v-flex>
                    <v-text-field
                      v-model="userEmail"
                      class="border-radius"
                      solo
                      flat
                      disabled
                      type="email"/>
                  </v-flex>
                </v-layout>
              </v-form>

              <v-layout row wrap>
                <v-flex mb-2 xs12 offset-xs0 sm12 offset-sm0 md6 offset-md0>
                  <v-btn
                    style="height:32px;"
                    class="my-0 border-radius"
                    color="grey darken-4"
                    depressed
                    block
                    dark
                    @click="changeEmailPopupIsOpen = !changeEmailPopupIsOpen">
                    Cambiar correo
                  </v-btn>

                  <d-popup
                    v-model="changeEmailPopupIsOpen"
                    width="500"
                    color="q-orange--background"
                    :onOk="changeEmail">
                    <slot>
                      CAMBIAR CORREO
                    </slot>
                    <v-container fluid pa-0 grid-list-md slot="content">
                      <v-form lazy-validation ref="changeEmailForm">
                        <v-layout row wrap>
                          <v-flex xs12 py-0>
                            <v-flex px-0 py-1>
                              Nuevo correo:
                            </v-flex>
                            <v-flex px-0 py-1>
                              <v-text-field
                                v-model="newUserEmail"
                                class="border-radius"
                                :rules="[rules.required, rules.email]"
                                outline
                                flat
                                required
                                type="email"/>
                            </v-flex>
                          </v-flex>

                          <v-flex xs12 py-0>
                            <v-flex px-0 py-1>
                              Contraseña:
                            </v-flex>
                            <v-flex px-0 py-1>
                              <v-text-field
                                class="border-radius"
                                :rules="[rules.required, rules.min]"
                                outline
                                flat
                                type="password"
                                required/>
                            </v-flex>
                          </v-flex>
                        </v-layout>
                      </v-form>
                    </v-container>
                    <div slot="button">Guardar cambios</div>
                  </d-popup>
                </v-flex>

                <v-flex mb-3 xs12 offset-xs0 sm12 offset-sm0 md6 offset-md0>
                  <v-btn
                    style="height:32px;"
                    class="my-0 border-radius"
                    color="grey darken-4"
                    depressed
                    block
                    dark
                    @click="
                      changePasswordPopupIsOpen = !changePasswordPopupIsOpen
                    ">
                    Cambiar contraseña
                  </v-btn>

                  <d-popup
                    v-model="changePasswordPopupIsOpen"
                    width="500"
                    color="q-orange--background"
                    :onOk="changePassword">
                    <slot>
                      CAMBIAR CONTRASEÑA
                    </slot>
                    <v-container fluid pa-0 grid-list-md slot="content">
                      <v-form lazy-validation ref="changePasswordForm">
                        <v-layout row wrap>
                          <v-flex xs12 py-0>
                            <v-flex px-0 py-1>
                              Contraseña actual:
                            </v-flex>
                            <v-flex px-0 py-1>
                              <v-text-field
                                class="border-radius"
                                :rules="[rules.required]"
                                outline
                                flat
                                type="password"
                                required/>
                            </v-flex>
                          </v-flex>

                          <v-flex xs12 py-0>
                            <v-flex px-0 py-1>
                              Nueva contraseña:
                            </v-flex>
                            <v-flex px-0 py-1>
                              <v-text-field
                                class="border-radius"
                                :rules="[rules.required, rules.min]"
                                :append-icon="
                                  show ? 'visibility_off' : 'visibility'
                                "
                                :type="show ? 'text' : 'password'"
                                hint="Elija una contraseña segura"
                                name="input-10-2"
                                outline
                                flat
                                required
                                @click:append="show = !show"/>
                            </v-flex>
                          </v-flex>

                          <v-flex xs12 py-0>
                            <v-flex px-0 py-1>
                              Confirmar contraseña:
                            </v-flex>
                            <v-flex px-0 py-1>
                              <v-text-field
                                class="border-radius"
                                :rules="[rules.required, rules.min]"
                                :append-icon="
                                  show ? 'visibility_off' : 'visibility'
                                "
                                :type="show ? 'text' : 'password'"
                                hint="Elija una contraseña segura"
                                name="input-10-2"
                                outline
                                flat
                                required
                                @click:append="show = !show"/>
                            </v-flex>
                          </v-flex>
                        </v-layout>
                      </v-form>
                    </v-container>
                    <div slot="button">Guardar contraseña</div>
                  </d-popup>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
    </v-layout>
  </v-flex>
</template>

<style lang="less">
.settings-card {
  min-height: 120px;
  .close-btn {
    top: 0;
    right: 0;
  }
  .edit-btn {
    bottom: 0;
    right: 0;
    .fa-icon {
      height: 24px;
      width: 24px;
      &:hover {
        color: #f58220;
      }
    }
  }
}
</style>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'UserSettings',
  data () {
    return {
      isEditingUser: null,
      date: new Date().toISOString().substr(0, 10),
      datePopup: false,
      changeEmailPopupIsOpen: false,
      newUserEmail: '',
      changePasswordPopupIsOpen: false,
      show: false,
      password: 'Contraseña',
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Email inválido'
        },
        passwordConfirmation: v =>
          v === this.password || 'Las contraseñas deben coincidir',
        min: v =>
          (v && v.length >= 8) ||
          'La contraseña debe tener al menos 8 caracteres'
      }
    }
  },
  computed: {
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('user', {
      user: 'object'
    }),
    ...mapState('auth', {
      user: 'currentUser'
    }),
    ...mapState('user', {
      updateUserSuccess: 'updateSuccess',
      updateUserMessages: 'updateMessages',
      updateUserError: 'updateError'
    }),
    userId () {
      if (this.user) {
        return this.user.id
      }
      return null
    },
    userFirstName () {
      if (this.user) {
        return this.user.firstName
      }
      return null
    },
    userLastName () {
      if (this.user) {
        return this.user.lastName
      }
      return null
    },
    userEmail () {
      if (this.user) {
        return this.user.email
      }
      return null
    }
  },
  watch: {
    updateUserSuccess (val, oldVal) {
      if (val) {
        this.isEditingUser = !this.isEditingUser

        this.changeEmailPopupIsOpen = false
        this.$refs.changeEmailForm.reset()

        this.changePasswordPopupIsOpen = false
        this.$refs.changePasswordForm.reset()

        this.updateUser()
      }
    },
    updateUserError (val, oldVal) {
      if (val) {
        this.changeEmailPopupIsOpen = true
        this.changePasswordPopupIsOpen = true
      }
    }
  },
  methods: {
    ...mapActions('user', {
      updateUser: 'update'
    }),
    ...mapActions('user', {
      updateUser: 'read'
    }),
    saveUserInfo () {
      if (this.$refs.userInfoForm.validate() && this.isAuthenticated) {
        const userUpdate = {
          firstName: this.userFirstName,
          lastName: this.userLastName
        }

        this.updateUser({
          id: this.userId,
          data: userUpdate
        })
      }
    },
    changeEmail () {
      if (this.$refs.changeEmailForm.validate() && this.isAuthenticated) {
        const userEmail = {
          email: this.newUserEmail
        }

        this.updateUser({
          id: this.userId,
          data: userEmail
        })
      }
    },
    changePassword () {
      if (this.$refs.changePasswordForm.validate() && this.isAuthenticated) {
        const userPassword = {}

        this.updateUser({
          id: this.userId,
          data: userPassword
        })
      }
    }
  },
  created () {
    this.updateUser()
  }
}
</script>
