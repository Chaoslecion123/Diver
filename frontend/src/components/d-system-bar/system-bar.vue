<template>
  <v-system-bar
    app
    fixed
    class="d-system-bar">
    <v-container
      fluid
      fill-height>
      <v-layout
        row
        fill-height>
        <d-language-selector/>
        <v-spacer/>
        <!--
        Show on diver
        <v-btn
          flat
          class="d-btn d-btn--squared">
          <d-icon name="b-store"/>
          Abre tu tienda
        </v-btn>
        <v-divider
          vertical/>
        -->
        <v-btn
          flat
          class="d-btn d-btn--squared d-btn--no-min-width">
          <d-icon name="b-question-circle-o"/>
          <span v-if="$vuetify.breakpoint.mdAndUp">
            FAQ
          </span>
        </v-btn>
        <v-divider
          vertical/>
        <d-country-selector/>
      </v-layout>
    </v-container>
  </v-system-bar>
</template>

<style lang="less">
@import "./system-bar.less";
</style>

<script>
import CountrySelector from './country-selector'
import LanguageSelector from './language-selector'

export default {
  name: 'd-system-bar',
  components: {
    'd-country-selector': CountrySelector,
    'd-language-selector': LanguageSelector
  }
}
</script>
