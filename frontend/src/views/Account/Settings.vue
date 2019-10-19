<template>
  <v-container
    :fluid="$vuetify.breakpoint.mdAndDown"
    grid-list-xl
    class="pa-0 ma-0">
    <v-layout row wrap class="ma-0">
      <v-flex xs12 class="pa-0">
        <d-settings-form />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import Form from './d-account-settings/form'

export default {
  name: 'AccountSettings',
  components: {
    'd-settings-form': Form
  },
  data () {
    return {
      gettingUserInfo: false
    }
  },
  computed: {
    ...mapState('auth', {
      orders: 'currentUser'
    })
  }
}
</script>
