<template>
  <d-popup
    v-model="editEmail"
    width="500"
    color="q-orange--background">
    <slot>
      Cambiar correo
    </slot>
    <v-container fluid pa-0 grid-list-md slot="content">
      <v-layout row wrap>
        <v-flex xs12>
          Correo actual:
        </v-flex>
        <v-flex xs12 py-0>
          <v-text-field
            class="border-radius"
            :rules="[rules.required, rules.emailMatch]"
            outline
            flat
            required
            type="email"></v-text-field>
        </v-flex>
        <v-flex xs12>
          Nuevo correo:
        </v-flex>
        <v-flex xs12 py-0>
          <v-text-field
            class="border-radius"
            :rules="[rules.required, rules.email]"
            outline
            flat
            required
            type="email"></v-text-field>
        </v-flex>
        <v-flex xs12>
          Contraseña:
        </v-flex>
        <v-flex xs12 py-0>
          <v-text-field
            class="border-radius"
            :rules="[rules.required, rules.emailMatch]"
            outline
            flat
            required></v-text-field>
        </v-flex>
      </v-layout>
    </v-container>
    <div slot="button">Guardar correo</div>
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
      editEmail: this.value,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        emailMatch: () => ('El e-mail y la constraseña son incorrectos.'),
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Email inválido'
        }
      }
    }
  },
  watch: {
    value () {
      this.editEmail = this.value
    },
    editEmail () {
      this.$emit('input', this.editEmail)
    }
  }
}
</script>
