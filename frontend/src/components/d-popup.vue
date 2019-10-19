<template>
  <v-dialog
    v-model="popupValue"
    :persistent="persistent"
    :width="width">
    <v-card>
      <v-container pa-3>
        <v-card-title class="py-2">
          <v-layout row wrap justify-space-between>
            <v-flex class="font-weight-600" style="font-size:1.25rem;" align-self-center>
              <slot/>
            </v-flex>
            <v-btn
              class="ma-0"
              @click="popupValue = false"
              flat
              icon
              :ripple="false"
              color="#EE2E22">
              <d-icon scale="1.25" name="b-close"/>
            </v-btn>
        </v-layout>
        </v-card-title>
        <v-divider class="mx-3" style="border-color:#000;"></v-divider>
        <v-card-text>
          <slot name="content"/>
        </v-card-text>
        <v-card-actions class="px-3">
          <v-layout row wrap>
            <v-spacer></v-spacer>
            <v-flex xs5>
              <v-btn
                class="border-radius mt-3 font-weight-600"
                :color="color"
                block
                dark
                @click="handleOk">
                <slot name="button"/>
              </v-btn>
            </v-flex>
          </v-layout>
        </v-card-actions>
        <v-card-actions class="px-3">
          <slot name="others"/>
        </v-card-actions>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'd-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    },
    width: {
      type: String,
      default: ''
    },
    persistent: {
      type: Boolean,
      default: false
    },
    color: {
      type: String,
      default: '#F58220'
    },
    onOk: {
      default: () => { }
    }
  },
  data () {
    return {
      popupValue: this.value
    }
  },
  watch: {
    value () {
      this.popupValue = this.value
    },
    popupValue () {
      this.$emit('input', this.popupValue)
    }
  },
  methods: {
    handleOk () {
      if (this.onOk) {
        this.onOk()
      }
    }
  }
}
</script>
