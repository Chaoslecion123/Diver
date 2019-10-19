<template>
  <d-popup
    v-model="newBill"
    width="600">
    <div>Datos de la factura</div>
    <v-container fluid pa-0 grid-list-lg slot="content">
      <v-form>
        <v-container pa-0 fluid grid-list-md>
          <v-layout row wrap>
            <v-flex xs12>
              <v-flex px-0>
                Razón social
              </v-flex>
              <v-text-field
                class="border-radius"
                :rules="[rules.required]"
                value="Softbutterfly SAC"
                solo
                flat
                required
                outline
                type="text"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-flex px-0>
                RUC
              </v-flex>
              <v-text-field
                class="border-radius"
                mask="###########"
                value="10987654321"
                :rules="[rules.required, rules.ruc]"
                solo
                flat
                required
                outline
                type="text"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-flex px-0>
                Dirección del domicilio fiscal
              </v-flex>
              <v-text-field
                class="border-radius"
                :rules="[rules.required]"
                value="Av Garcilaso de la Vega"
                solo
                flat
                required
                outline
                type="text"></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
      </v-form>
    </v-container>
    <div slot="button">Guardar datos</div>
  </d-popup>
</template>

<script>
export default {
  name: 'd-new-address-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      newBill: this.value,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        ruc: v => (v && v.length >= 11) || 'EL RUC debe tener al 11 caracteres'
      }
    }
  },
  watch: {
    value () {
      this.newBill = this.value
    },
    newBill () {
      this.$emit('input', this.newBill)
    }
  }
}
</script>
