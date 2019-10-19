<template>
  <!-- v-menu offset-y :value="openMenu" input-activator>
    <template v-slot:activator="{ on }">
      <v-text-field
        browser-autocomplete="off"
        type="text"
        flat
        solo
        :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
        hint="Ingresa una referencia: Edificio, Urbanización, ..."
        persistent-hint
        @input="handleSearch"/>
    </template>
    <v-list>
      <v-list-tile v-for="item in items" :key="item.id">
        <v-list-tile-title>{{ item }}</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu -->
  <v-combobox
    v-model="model"
    :class="['d-input', 'd-input--rounded', 'd-input--bordered']"
    :items="items"
    :loading="listingCityArea"
    :search-input.sync="search"
    color="white"
    flat
    solo
    hide-no-data
    item-text="label"
    item-value="name"
    placeholder="Distrito"
    return-object>
  </v-combobox>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'pichula',
  data () {
    return {
      openMenu: false,
      descriptionLimit: 60,
      entries: [],
      model: null,
      search: null
    }
  },
  computed: {
    ...mapState('city-area', {
      cityAreas: 'objects',
      listingCityArea: 'listing'
    }),
    fields () {
      if (!this.model) return []

      return Object.keys(this.model).map(key => {
        return {
          key,
          value: this.model[key] || 'n/a'
        }
      })
    },
    items () {
      if (
        this.cityAreas &&
        this.cityAreas.meta &&
        this.cityAreas.meta.count > 0
      ) {
        return [...this.cityAreas.items].map(item => ({
          ...item,
          label: `${item.city.countryArea.name} / ${item.city.name} / ${
            item.name
          }`
        }))
      }

      return []
    }
  },
  watch: {
    items (val) {
      console.log(val)
      this.openMenu = val && val.length > 0
    },
    search (val) {
      if (val && val.length > 0 && !this.isLoading) {
        this.getCityAreas({
          query: {
            q: val
          }
        })
      }
    }
  },
  methods: {
    ...mapActions('city-area', {
      getCityAreas: 'list'
    }),
    handleSearch (value) {
      if (value && value.length > 0 && !this.isLoading) {
        this.getCityAreas({
          query: {
            q: value
          }
        })
      }
    }
  }
}
</script>
