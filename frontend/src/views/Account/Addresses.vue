<template>
  <v-container fluid fill-height class="pa-0 ma-0">
    <transition mode="out-in" name="fade">
      <d-loader v-if="listingAddresses" key="loading" />
      <d-empty
        v-else-if="!listingAddresses && userHasNoAddresses"
        key="userHasNoAddresses">
        <h2 class="mb-4">
          Aún no has registrado ninguna dirección
        </h2>
        <v-btn
          large
          color="accent"
          :class="[
            'd-btn',
            'd-btn--no-transform',
            'd-btn--bold',
            'd-btn--rounded'
          ]"
          @click="openPopup">
          <d-icon :scale="1.25" class="mr-2" name="b-add-circle" />
          Añadir una dirección
        </v-btn>
      </d-empty>

      <v-layout v-else key="order-list" row wrap class="ma-0">
        <v-flex xs12 class="pa-0">
          <v-layout row wrap>
            <v-flex xs12>
              <h2 style="font-weight: normal;">
                <d-icon name="b-enviroment-o" />
                Mis direcciones
              </h2>
              <v-divider />
            </v-flex>
            <v-flex
              v-for="address in addresses.items"
              :key="address.id"
              xs12
              sm6
              md4
              lg3
              xl3>
              <d-address-card
                :class="[
                  'd-card',
                  'd-card--outline',
                  'd-card--rounded',
                  'd-card--fill-height',
                  'transparent'
                ]"
                allowEdit
                allowDelete
                :address="address"/>
            </v-flex>
            <v-flex xs12>
              <v-btn
                outline
                color="accent"
                :block="$vuetify.breakpoint.xs"
                :class="[
                  'ma-0',
                  'd-btn',
                  'd-btn--rounded',
                  'd-btn--bold',
                  'd-btn--no-transform'
                ]"
                @click="openPopup">
                <d-icon class="mr-2" name="b-plus-circle-o" />
                Nueva dirección
              </v-btn>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </transition>
    <d-address-popup v-model="addressPopupIsOpen" />
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import Loader from './d-utils/loader'
import Empty from './d-utils/empty'

export default {
  name: 'AccountAddresses',
  components: {
    'd-loader': Loader,
    'd-empty': Empty,
    'd-address-card': () => import('@/components/d-address/card.vue'),
    'd-address-popup': () => import('@/components/d-address/popup.vue')
  },
  data () {
    return {
      addressPopupIsOpen: false
    }
  },
  computed: {
    ...mapState('address', {
      addresses: 'objects',
      listingAddresses: 'listing',
      addressCreateSuccess: 'createSuccess',
      addressUpdateSuccess: 'updateSuccess',
      addressDeleteSuccess: 'deleteSuccess'
    }),
    userHasNoAddresses () {
      const { addresses } = this

      if (addresses && addresses.meta) {
        return addresses.meta.count === 0
      }

      return true
    }
  },
  watch: {
    addressCreateSuccess (val, oldVal) {
      this.getAddresses()
    },
    addressUpdateSuccess (val, oldVal) {
      this.getAddresses()
    },
    addressDeleteSuccess (val, oldVal) {
      this.getAddresses()
    }
  },
  methods: {
    ...mapActions('address', {
      getAddresses: 'list'
    }),

    openPopup () {
      console.log('Addrress')
      this.addressPopupIsOpen = true
    }
  },
  created () {
    this.getAddresses()
  }
}
</script>
