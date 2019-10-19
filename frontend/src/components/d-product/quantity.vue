<template>
  <v-layout
    row
    align-center
    class="d-product-quantity">
    <v-flex
      shrink>
      <strong>
        Cantidad
      </strong>
    </v-flex>
    <v-flex
      grow>
      <div
        class="d-product-quantity__selector">
        <v-btn
          depresed
          class="elevation-0"
          color="grey lighten-3"
          @click.stop="decrement">
          <d-icon
            name="b-minus"/>
        </v-btn>
        <v-text-field
          v-model="quantity"
          flat
          solo
          read-only
          hide-details
          min="1"
          step="1"
          type="number"
          class="ma-0 pa-0"/>
        <v-btn
          depresed
          class="elevation-0"
          color="grey lighten-3"
          @click.stop="increment">
          <d-icon
            name="b-plus"/>
        </v-btn>
      </div>
    </v-flex>
  </v-layout>
</template>

<style lang="less">
.d-product-quantity {
  position: relative;

  .d-product-quantity__selector {
    position: relative;
    max-width: 180px;
    margin: 0 0 0 auto;
    display: flex;
    overflow: hidden;
    border-radius: 4px;
    flex-direction: row;
    border: 1px solid #b9b9b9;
  }

  input {
    text-align: right;
  }

  input[type="number"]::-webkit-inner-spin-button,
  input[type="number"]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  input[type="number"] {
    -moz-appearance: textfield;
  }

  .v-text-field.v-text-field--solo {
    .v-input__control {
      min-width: initial;
      min-height: initial;
    }
  }

  .v-btn {
    width: 48px;
    margin: 0;
    padding: 0;
    min-width: initial;
    border-radius: 0;
  }
}
</style>

<script>
export default {
  name: 'd-product-quantity',
  data () {
    return {
      quantity: 1
    }
  },
  watch: {
    quantity (val, oldVal) {
      this.$emit('change', parseInt(val))
    }
  },
  methods: {
    increment () {
      this.quantity = parseInt(this.quantity, 10) + 1
    },
    decrement () {
      if (this.quantity > 1) {
        this.quantity = parseInt(this.quantity, 10) - 1
      }
    }
  }
}
</script>
