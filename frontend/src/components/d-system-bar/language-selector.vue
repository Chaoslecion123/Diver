<template>
  <v-menu
    bottom
    offset-y
    origin="center center"
    transition="slide-y-transition"
    class="d-language-selector">
    <v-btn
      flat
      slot="activator"
      class="d-btn d-btn--no-transform d-btn--squared d-btn--no-min-width">
      <d-icon name="b-earth"/>
      <span v-if="$vuetify.breakpoint.smAndDown">
        {{ selectedLanguage.code.toUpperCase() }}
      </span>
      <span v-else>
        {{ selectedLanguage.name || defaultLanguage.name }}
      </span>
    </v-btn>

    <!-- v-list
      class="d-language-selector__list">
      <v-list-tile
        v-for="language in languageList"
        :key="`language-${language.code}`">
        <v-list-tile-title>
          {{ language.name }}
        </v-list-tile-title>
      </v-list-tile>
    </v-list -->
  </v-menu>

</template>

<style lang="less">
@import "./language-selector.less";
</style>

<script>
export default {
  name: 'd-language-selector',
  data () {
    return {
      defaultLanguage: {
        code: 'ES',
        name: 'Español'
      },
      selectedLanguage: {
        code: null,
        name: null
      },
      languageList: null
    }
  },
  created () {
    this.selectedLanguage = { ...this.defaultLanguage }

    try {
      const selectedLanguage = JSON.parse(document.querySelector('[name="meta-selected-language"]').content)
      const code = selectedLanguage.code
      const name = selectedLanguage.name
      if (code && name) {
        this.selectedLanguage.code = code
        this.selectedLanguage.name = name
      }
    } catch (error) { }

    try {
      this.languageList = JSON.parse(document.querySelector('[name="meta-languages"]').content)
    } catch (error) { }
  }
}
</script>
