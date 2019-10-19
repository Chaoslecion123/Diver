<template>
  <v-dialog
    v-model="shareUs"
    :width="width">
    <v-card>
      <v-container pa-3>
        <v-card-title class="py-2">
          <v-layout row wrap justify-space-between>
            <v-flex class="font-weight-600" style="font-size:1.25rem;" align-self-center>
              Compártelo en tus redes sociales
            </v-flex>
            <v-btn
              class="ma-0"
              @click="shareUs = false"
              flat
              icon
              :ripple="false"
              color="#EE2E22">
              <!--v-icon>close</v-icon-->
              <d-icon name="b-close"/>
            </v-btn>
        </v-layout>
        </v-card-title>
        <v-divider class="mx-3" style="border-color:#000;"></v-divider>
        <v-card-text>
          <v-layout row wrap >
            <v-flex xs10 offset-xs1 my-2
              v-for="(item,i) in socialButtons"
              :key="i"
              style="font-size:1.25rem;"
              align-self-center>
              <v-btn
                class="font-weight-600 border-radius"
                @click="shareUs = false"
                block
                depressed
                dark
                :to="item.to"
                :ripple="false"
                :color="item.color">
                {{item.name}}
              </v-btn>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'd-share-popup',
  props: {
    value: {
      type: Boolean,
      default: false
    },
    width: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      shareUs: this.value,
      socialButtons: {
        1: {
          name: 'Facebook',
          color: '#3b5998',
          to: ''
        },
        2: {
          name: 'Twitter',
          color: ' #00aced',
          to: ''
        },
        3: {
          name: 'Instagram',
          color: '#e95950',
          to: ''
        }
      }
    }
  },
  watch: {
    value () {
      this.shareUs = this.value
    },
    shareUs () {
      this.$emit('input', this.shareUs)
    }
  }
}
</script>
