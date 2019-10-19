<template>
  <d-popup
    v-model="addToFavorite"
    :onOk="onOk"
    v-if="product.image"
    width="600">
    <div>Agregar a favoritos</div>
    <v-container fluid pa-0 grid-list-lg slot="content">
      <v-layout row wrap>
        <v-flex xs12 px-5 mx-5 my-2>
          <v-card flat color="grey lighten-3 border-radius">
            <v-layout row wrap>
              <v-img
                max-height="120"
                max-width="180"
                class="ma-2 fill-height"
                contain
                :src="product.image.image.card">
              </v-img>
              <v-card-title text-xs-center>
                <v-layout column fill-height>
                  <v-flex my-2>
                   {{ product.name }}
                  </v-flex>
                </v-layout>
              </v-card-title>
            </v-layout>
          </v-card>
        </v-flex>
        <v-divider style="border-widht: .5px;" class="ma-2"/>
        <v-flex xs12>
        COLECCIÓN:
        </v-flex>
        <v-flex xs12>
          <v-select
            label="Seleccionar"
            outline
            solo
            flat
            append-icon="expand_more"
            hide-details></v-select>
        </v-flex>
      </v-layout>
    </v-container>
    <div slot="button">Agregar a grupo</div>
  </d-popup>
</template>

<script>
// import { mapGetters } from 'vuex'

export default {
  name: 'd-add-favorite-popup',
  props: {
    product: {
      type: Object,
      default () {
        return {}
      }
    },
    value: {
      type: Boolean,
      default: false
    },
    onOk: {
      default: () => {}
    }
  },
  data () {
    return {
      image: '',
      addToFavorite: this.value,
      rules: {
        required: value => !!value || 'Este campo es requerido.',
        ruc: v => (v && v.length >= 11) || 'EL RUC debe tener al 11 caracteres'
      }
    }
  },
  computed: {
    // ...mapGetters('auth', {
    //  isAuthenticated: 'isAuthenticated'
    // })
  },
  watch: {
    value () {
      this.addToFavorite = this.value
    },
    addToFavorite () {
      this.$emit('input', this.addToFavorite)
    }
  },
  methods: {
    // onOk () {
    //  this.$router.push({ name: this.$route.name})
    //  if (this.isAuthenticated) {
    //    this.addToFavorite = false
    //  } else {
    //    this.$router.push({ name: this.$route.name, query: { login: true } })
    //  }
    // }
  }
}
</script>
