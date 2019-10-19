<template>
  <v-card flat :class="['d-card', 'd-address-card']" v-on="this.$listeners">
    <v-card-text>
      <div>
        <strong>{{ address.firstName }} {{ address.lastName }}</strong>
      </div>
      <div v-if="address.companyName || address.phone">
        <template v-if="address.companyName">{{ address.companyName }},</template>
        {{ address.phone }}
      </div>
      <div>{{ address.streetAddress1 }}</div>
      <div>{{ address.streetAddress2 }}</div>
      <div v-if="address.cityArea || address.city">
        <template v-if="address.cityArea">{{ address.cityArea }},</template>
        {{ address.city }}
      </div>
      <div v-if="address.countryArea || address.countryName || address.country">
        <template v-if="address.countryArea">{{ address.countryArea }},</template>
        {{ address.countryName || address.country }}
      </div>
      <div v-if="address.postalCode">{{ address.postalCode }}</div>
    </v-card-text>
    <v-card-text
      v-if="allowEdit || allowDelete"
      :class="['pt-0', 'text-xs-right']">
      <v-btn
        v-if="allowDelete"
        icon
        color="error"
        :class="['ma-0']"
        @click.stop="handleDelete">
        <d-icon name="b-trash" />
      </v-btn>

      <v-btn
        v-if="allowEdit"
        icon
        outline
        color="accent"
        :class="['my-0', 'mr-0', 'ml-3']"
        @click.stop="handleEdit">
        <d-icon name="b-edit" />
      </v-btn>
    </v-card-text>
    <d-address-popup v-model="addressPopupIsOpen" :address="address" />
  </v-card>
</template>

<style lang="less">
.d-card {
  &.d-address-card {
    display: flex;
    flex-direction: column;

    .v-card__text:first-of-type {
      flex: 1 1 auto;
    }
  }
}
</style>

<script>
import AddressPopup from './popup'
import { mapActions } from 'vuex'

export default {
  name: 'd-address-card',
  components: {
    'd-address-popup': AddressPopup
  },
  props: {
    address: {
      type: Object,
      default: null
    },
    allowEdit: {
      type: Boolean,
      default: false
    },
    allowDelete: {
      type: Boolean,
      default: false
    },
    outline: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      addressPopupIsOpen: false
    }
  },
  methods: {
    ...mapActions('address', {
      deleteAddress: 'delete'
    }),
    handleEdit () {
      this.addressPopupIsOpen = true
    },
    handleDelete () {
      this.deleteAddress({ id: this.address.id })
    }
  }
}
</script>
