<template>
  <v-card-text>
    <v-card-title :class="['px-0', 'pt-0']">
      ¿En dónde recogerás tu pedido?
    </v-card-title>

    <v-layout row wrap fill-height>
      <v-flex
        v-for="{ name, address } in shippingAddresses"
        :key="address.id"
        :value="address.id"
        xs12
        sm6
        md4
        lg4
        xl3>
        <v-card
          flat
          :class="[
            'd-card',
            'd-card--outline',
            'd-card--rounded',
            'address-selector__item',
            {
              active: shippingAddress === address.id
            }
          ]"
          @click="handleChange(address.id)">
          <v-card-text>
            <div :class="['address-selector__item-name']">
              <strong>{{ name }}</strong>
            </div>
            <div>{{ address.streetAddress1 }}</div>
            <div>{{ address.streetAddress2 }}</div>
            <div v-if="address.cityArea || address.city">
              <template v-if="address.cityArea">{{ address.cityArea }},</template>
              {{ address.city }}
            </div>
            <div
              v-if="
                address.countryArea || address.countryName || address.country
              ">
              <template v-if="address.countryArea">{{ address.countryArea }},</template>
              {{ address.countryName || address.country }}
            </div>
            <div v-if="address.postalCode">{{ address.postalCode }}</div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card-text>
</template>

<style lang="less"></style>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'd-shipping-type-selector',
  model: {
    prop: 'shippingAddress',
    event: 'change'
  },
  props: {
    shippingAddress: {
      type: Number,
      default: null
    }
  },
  data () {
    return {}
  },
  computed: {
    ...mapState('cart', {
      cartToken: 'token'
    }),

    ...mapState('physical-store', {
      physicalStores: 'objects'
    }),

    shippingAddresses () {
      if (this.physicalStores && this.physicalStores.items) {
        return [...this.physicalStores.items]
      }

      return []
    }
  },
  methods: {
    ...mapActions('cart', {
      cartUpdate: 'update'
    }),

    handleChange (value) {
      this.$emit('change', value)

      this.cartUpdate({
        id: this.cartToken,
        data: {
          shippingAddress: value,
          shippingMethod: null
        }
      })
    }
  }
}
</script>
