<template>
  <div
    v-if="variantPickerData">
    <v-card
      flat
      v-for="(attribute, i) in variantPickerData.variantAttributes"
      :key="i">
      <v-card-title
        class="pa-0">
        {{ attribute.name }}
      </v-card-title>
      <v-card-text
        class="px-0">
        <v-btn-toggle
          mandatory
          class="elevation-1">
          <v-btn
            v-for="(value, j) in attribute.values"
            :key="j"
            flat
            @click="selectAttribute(attribute.pk, value.pk)">
            {{ value.name }}
          </v-btn>
        </v-btn-toggle>
      </v-card-text>
    </v-card>
  </div>
</template>

<style lang="less">
</style>

<script>
const compareObjects = (obj1, obj2) => {
  // Loop through properties in object 1
  for (let p in obj1) {
    // Check property exists on both objects
    if (obj1.hasOwnProperty(p) !== obj2.hasOwnProperty(p)) return false

    switch (typeof (obj1[p])) {
      // Deep compare objects
      case 'object':
        if (!compareObjects(obj1[p], obj2[p])) return false
        break
      // Compare function code
      case 'function':
        if (typeof (obj2[p]) === 'undefined' || (p !== 'compare' && obj1[p].toString() !== obj2[p].toString())) return false
        break
      // Compare values
      default:
        if (obj1[p] !== obj2[p]) return false
    }
  }

  // Check object 2 for any extra properties
  // for (let p2 in obj2) {
  //   if (typeof (obj1[p2]) === 'undefined') return false
  // }
  return true
}

export default {
  name: 'd-product-attributes',
  props: {
    variantPickerData: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      panel: 0,
      selectedAttributes: {}
    }
  },
  computed: {
    selectedVariant () {
      const { selectedAttributes } = this
      const { variants } = this.variantPickerData

      return variants.find(variant => compareObjects(variant.attributes, selectedAttributes)) || {}
    }
  },
  watch: {
    selectedVariant (val, oldVal) {
      this.$emit('change', val)
    }
  },
  methods: {
    selectAttribute (attrId, valueId) {
      let selectedAttributes = { ...this.selectedAttributes }
      selectedAttributes[attrId.toString()] = valueId.toString()
      this.selectedAttributes = selectedAttributes
    },
    changeView (view) {
      this.$emit('changeview', view)
    }
  }
}
</script>
