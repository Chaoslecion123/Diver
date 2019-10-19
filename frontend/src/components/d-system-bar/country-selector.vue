<template>
  <v-menu
    bottom
    offset-y
    origin="center center"
    transition="slide-y-transition"
    class="d-country-selector">
    <v-btn
      flat
      slot="activator"
      class="d-btn d-btn--no-transform d-btn--squared d-btn--no-min-width">
      <flag :squared="false" :iso="selectedCountry.code || defaultCountry.code"/>
      <span v-if="$vuetify.breakpoint.smAndDown">
        {{ selectedCountry.code.toUpperCase() }}
      </span>
      <span v-else>
        {{ selectedCountry.name || defaultCountry.name }}
      </span>
    </v-btn>

    <!-- v-list
      class="d-country-selector__list">
      <v-list-tile
        v-for="country in countryList"
        :key="`country-${language.code}`">
        <v-list-tile-title>
          <v-list-tile-title>
            <flag :squared="false" :iso="country.code"/>
            {{ country.name }}
          </v-list-tile-title>
        </v-list-tile-title>
      </v-list-tile>
    </v-list -->
  </v-menu>

</template>

<style lang="less">
@import './country-selector.less';
</style>

<script>
export default {
  name: 'd-country-selector',
  data () {
    return {
      defaultCountry: {
        code: 'pe',
        name: 'Perú'
      },
      selectedCountry: {
        code: null,
        name: null
      },
      countryList: null
    }
  },
  created () {
    this.selectedCountry = { ...this.defaultCountry }

    try {
      const selectedCountry = JSON.parse(
        document.querySelector('[name="meta-selected-conutry"]').content
      )
      const code = selectedCountry.code
      const name = selectedCountry.name
      if (code && name) {
        this.selectedCountry.code = code
        this.selectedCountry.name = name
      }
    } catch (error) {}

    try {
      this.countryList = JSON.parse(
        document.querySelector('[name="meta-countries"]').content
      )
    } catch (error) {}
  }
}
</script>
