<template>
  <d-popup
    v-model="recovery"
    width="500">
    <slot>
      <v-btn
        class=" ma-0 pa-0 font-weight-600"
        flat
        :ripple="false"
        @click="login=!login">
        <!--v-icon medium left dark>keyboard_arrow_left</v-icon-->
        <d-icon medium left dark name="b-left"/>
        <span style="font-size:1.25rem;">CREAR CUENTA</span>
      </v-btn>
    </slot>
    <v-container fluid pa-0 grid-list-md slot="content">
      <v-form lazy-validation>
        <v-layout row wrap>
          <v-flex xs6 py-0>
            <v-flex>
              Nombre
            </v-flex>
            <v-text-field
              class="border-radius"
              :rules="[rules.required]"
              outline
              flat
              required
              type="text"></v-text-field>
          </v-flex>
          <v-flex xs6 py-0>
            <v-flex>
              Apellido
            </v-flex>
            <v-text-field
              class="border-radius"
              :rules="[rules.required]"
              outline
              flat
              required
              type="text"></v-text-field>
          </v-flex>
          <v-flex xs6 py-0>
            <v-flex>
              E-mail:
            </v-flex>
            <v-text-field
              class="border-radius"
              :rules="[rules.required, rules.email]"
              outline
              flat
              required
              type="email"></v-text-field>
          </v-flex>
          <v-flex xs6 py-0>
            <v-flex>
              DNI
            </v-flex>
            <v-text-field
              class="border-radius"
              mask="########"
              :rules="[rules.dni]"
              outline
              flat
              hide-details
              type="text"></v-text-field>
          </v-flex>
          <v-flex xs6 py-0>
            <v-flex>
            Contraseña:
            </v-flex>
            <v-text-field
              class="border-radius"
              :rules="[rules.required, rules.min]"
              outline
              flat
              required
              error></v-text-field>
          </v-flex>
          <v-flex xs6 py-0>
            <v-flex>
            Confirmar contraseña
            </v-flex>
            <v-text-field
              class="border-radius"
              :rules="[rules.required, rules.min]"
              outline
              flat
              required
              error></v-text-field>
          </v-flex>
          <v-checkbox
            class="mt-2"
            v-model="checkbox1"
            :rules="[v => !!v || '¡Debes estar de acuerdo para continuar!']"
            label="Me gustaría recibir comunicaciones promocionales."
            required></v-checkbox>
          <v-checkbox
            class="mt-2"
            v-model="checkbox2"
            :rules="[v => !!v || '¡Debes estar de acuerdo para continuar!']"
            label="Acepto términos y condiciones de la politíca de privacidad y tratamiento de datos personales."
            required></v-checkbox>

          <v-container pa-0 my-2 grid-list-md>
            <v-layout row wrap mx-1>
              <v-flex xs6>
                <v-btn
                  class="ma-0 font-weight-600 border-radius"
                  color="#415A99"
                  block
                  dark
                  depressed>
                  Facebook
                </v-btn>
                </v-flex>
              <v-flex xs6>
                <v-btn
                  class="ma-0 font-weight-600 border-radius"
                  color="#E63A3A"
                  dark
                  block
                  depressed>
                  Gmail
                </v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-layout>
      </v-form>
      <v-divider class="mt-3"></v-divider>
    </v-container>
    <div slot="button">Crear cuenta</div>
  </d-popup>
</template>

<style lang="less">
</style>

<script>
export default {
  name: 'd-new-account-popup',
  data () {
    return {
      login: false,
      recovery: false,
      checkbox1: false,
      checkbox2: false,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Email inválido'
        },
        min: v => (v && v.length >= 8) || 'La contraseña debe tener al menos 8 caracteres',
        dni: v => (v && v.length === 8) || 'El DNI debe tener 8 dígitos.'
      }
    }
  }
}
</script>
