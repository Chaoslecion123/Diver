<template>
  <d-popup
    v-model="editPassword"
    width="500"
    color="q-orange--background">
    <slot>
      Cambiar contraseña
    </slot>
    <v-container fluid pa-0 grid-list-md slot="content">
      <v-layout row wrap>
        <v-flex xs12>
          Contraseña actual:
        </v-flex>
        <v-flex xs12 py-0>
          <v-text-field
            class="border-radius"
            :rules="[rules.required, rules.emailMatch]"
            outline
            flat
            required></v-text-field>
        </v-flex>
        <v-flex xs12>
          Nueva contraseña:
        </v-flex>
        <v-flex xs12 py-0>
          <v-text-field
            class="border-radius"
            :rules="[rules.required, rules.min]"
            outline
            :append-icon="show ? 'visibility_off' : 'visibility'"
            solo
            flat
            required
            :type="show ? 'text' : 'password'"
            name="input-10-2"
            hint="Elija una contraseña segura"
            @click:append="show = !show"></v-text-field>
        </v-flex>
        <v-flex xs12>
          Confirmar contrañseña:
        </v-flex>
        <v-flex xs12 py-0>
          <v-text-field
            class="border-radius"
            :rules="[rules.required, rules.min]"
            outline
            :append-icon="show ? 'visibility_off' : 'visibility'"
            solo
            flat
            required
            :type="show ? 'text' : 'password'"
            name="input-10-2"
            @click:append="show = !show"></v-text-field>
        </v-flex>
      </v-layout>
    </v-container>
    <div slot="button">Guardar contraseña</div>
  </d-popup>
</template>

<style lang="less">

</style>

<script>
export default {
  name: 'd-edit-email-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      editPassword: this.value,
      show: false,
      password: 'Contraseña',
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        emailMatch: () => ('El e-mail y la constraseña son incorrectos.'),
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Email inválido'
        },
        min: v => (v && v.length >= 8) || 'La contraseña debe tener al menos 8 caracteres'
      }
    }
  },
  watch: {
    value () {
      this.editPassword = this.value
    },
    editPassword () {
      this.$emit('input', this.editPassword)
    }
  }
}
</script>
