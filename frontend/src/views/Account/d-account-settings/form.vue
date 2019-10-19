<template>
  <div>
    <div class="pb-5">
      <h2 style="font-weight: normal;">
        <d-icon name="b-user" />
        Datos personales
      </h2>
      <v-divider class="pb-3" />
      <v-form ref="personalForm" v-model="personalFormIsValid" lazy-validation>
        <div class="mb-2">Nombres</div>
        <div>
          <v-text-field
            ref="firstName"
            v-model="personalForm.firstName"
            browser-autocomplete="off"
            type="text"
            flat
            solo
            required
            style="width: 100%; max-width: 360px;"
            :class="['d-input', 'd-input--rounded', 'd-input--bordered']"/>
        </div>
        <div class="mb-2">Apellidos</div>
        <div>
          <v-text-field
            ref="lastName"
            v-model="personalForm.lastName"
            browser-autocomplete="off"
            type="text"
            flat
            solo
            required
            style="width: 100%; max-width: 360px;"
            :class="['d-input', 'd-input--rounded', 'd-input--bordered']"/>
        </div>
        <div>
          <v-btn
            depressed
            :loading="savingPersonalData"
            color="accent"
            :class="[
              'ma-0',
              'd-btn',
              'd-btn--no-transform',
              'd-btn--bold',
              'd-btn--rounded'
            ]"
            @click="updateNames">
            <d-icon :scale="1.25" class="mr-2" name="b-save" />
            Guardar
          </v-btn>
        </div>
      </v-form>
    </div>

    <div class="pb-5">
      <h2 style="font-weight: normal;">
        <d-icon name="b-mail" />
        Contacto
      </h2>
      <v-divider class="pb-3" />
      <v-form ref="contactForm" v-model="contactFormIsValid" lazy-validation>
        <div class="mb-2">Correo electrónico</div>
        <div>
          <v-text-field
            ref="email"
            v-model="contactForm.email"
            browser-autocomplete="off"
            type="text"
            flat
            solo
            required
            style="width: 100%; max-width: 360px;"
            :class="['d-input', 'd-input--rounded', 'd-input--bordered']"/>
        </div>
        <div>
          <v-btn
            depressed
            :loading="savingContactData"
            color="accent"
            :class="[
              'ma-0',
              'd-btn',
              'd-btn--no-transform',
              'd-btn--bold',
              'd-btn--rounded'
            ]">
            <d-icon :scale="1.25" class="mr-2" name="b-save" />
            Guardar
          </v-btn>
        </div>
      </v-form>
    </div>

    <div>
      <h2 style="font-weight: normal;">
        <d-icon name="b-lock" />
        Contraseña
      </h2>
      <v-divider class="pb-3" />
      <v-form ref="passwordForm" v-model="personalFormIsValid" lazy-validation>
        <div class="mb-2">Contraseña</div>
        <div>
          <v-text-field
            ref="firstName"
            v-model="passwordForm.password"
            browser-autocomplete="off"
            type="text"
            flat
            solo
            required
            style="width: 100%; max-width: 360px;"
            :class="['d-input', 'd-input--rounded', 'd-input--bordered']"/>
        </div>
        <div class="mb-2">Confirmar contraseña</div>
        <div>
          <v-text-field
            ref="lastName"
            v-model="passwordForm.passwordConfirm"
            browser-autocomplete="off"
            type="text"
            flat
            solo
            required
            style="width: 100%; max-width: 360px;"
            :class="['d-input', 'd-input--rounded', 'd-input--bordered']"/>
        </div>
        <div>
          <v-btn
            depressed
            :loading="savingPasswordData"
            color="accent"
            :class="[
              'ma-0',
              'd-btn',
              'd-btn--no-transform',
              'd-btn--bold',
              'd-btn--rounded'
            ]">
            <d-icon :scale="1.25" class="mr-2" name="b-save" />
            Guardar
          </v-btn>
        </div>
      </v-form>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'DAccountSettings',
  data () {
    return {
      personalFormIsValid: false,
      personalForm: {
        firstName: '',
        lastName: ''
      },
      savingPersonalData: false,
      contactFormIsValid: false,
      contactForm: {
        email: ''
      },
      savingContactData: false,
      passwordFormIsValid: false,
      passwordForm: {
        password: '',
        passwordConfirm: ''
      },
      savingPasswordData: false
    }
  },
  computed: {
    ...mapState('auth', {
      user: 'currentUser',
      updating: 'updating'
    }),
    ...mapState('user', {
      updating: 'updating'
    })
  },
  watch: {
    user (val, oldVal) {
      this.loadFormData(val)
    },
    updating (val, oldVal) {
      if (!val) {
        this.savingPersonalData = false
        this.savingContactData = false
        this.savingPasswordData = false
      }
    }
  },
  methods: {
    ...mapActions('user', {
      updateUser: 'update'
    }),
    loadFormData (user) {
      if (user) {
        this.personalForm.firstName = user.firstName
        this.personalForm.lastName = user.lastName
        this.contactForm.email = user.email
      }
    },
    updateNames () {
      this.savingPersonalData = true
      this.updateUser({
        id: this.user.id,
        data: this.personalForm
      })
    },
    updateEmail () {
      this.savingContactData = true
      this.updateUser({
        id: this.user.id,
        data: this.contactForm
      })
    },
    updatePassword () {
      this.savingPasswordData = true
      this.updateUser({
        id: this.user.id,
        data: this.passwordForm
      })
    }
  },
  mounted () {
    this.loadFormData(this.user)
  }
}
</script>
