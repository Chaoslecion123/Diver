<template>
  <div class="d-address-map">
    <v-divider />
    <div class="pa-2"></div>
    <div
      class="v-input v-text-field v-text-field--single-line v-text-field--solo v-text-field--solo-flat v-text-field--enclosed theme--light d-input d-input--rounded d-input--bordered">
      <div class="v-input__control">
        <div class="v-input__slot">
          <div class="v-text-field__slot">
            <gmap-autocomplete
              :value="address"
              placeholder="Busca tu dirección"
              :select-first-on-enter="true"/>
          </div>
        </div>
      </div>
    </div>
    <v-divider />
    <gmap-map
      :zoom="16"
      :center="map.center"
      :options="{
        mapTypeControl: false,
        fullscreenControl: false,
        streetViewControl: false,
        zoomControlOptions: {
          position: 3
        }
      }">
      <gmap-marker
        :position="marker.position"
        :draggable="true"
        :animation="1"
        @dragend="handleDragend"/>
    </gmap-map>
  </div>
</template>

<style lang="less">
.d-address-map {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;

  .vue-map-container {
    flex: 1 1 auto;
  }
}
</style>

<script>
/* global google */
import assert from 'assert'
import { loaded } from 'vue-google-maps/manager'

export default {
  name: 'd-address-map',
  props: {
    position: {
      type: Object,
      default () {
        return {
          lat: -12,
          lng: -77
        }
      }
    }
  },
  data () {
    return {
      address: '',
      map: {
        center: {
          lat: -12,
          lng: -77
        }
      },
      marker: {
        position: {
          lat: -12,
          lng: -77
        }
      }
    }
  },
  watch: {},
  methods: {
    handlePlaceChange (place) {
      if (place && place.geometry && place.geometry.location) {
        this.map.center.lat = place.geometry.location.lat()
        this.map.center.lng = place.geometry.location.lng()

        this.marker.position.lat = place.geometry.location.lat()
        this.marker.position.lng = place.geometry.location.lng()
      }
    },
    handlePositionChange (event) {
      // this.map.center.lat = event.lat()
      // this.map.center.lng = event.lng()
      this.marker.position.lat = event.lat()
      this.marker.position.lng = event.lng()
    },
    handleDragend (event) {
      console.log(event)
      console.log('pichula!')
      // this.map.center = { ...this.marker.position }
    }
  },
  mounted () {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        position => {
          position = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          }
          this.map.center = { ...position }
          this.marker.position = { ...position }
        },
        {
          enableHighAccuracy: true,
          timeout: 5000
        }
      )
    } else {
      alert('Geolocation is not supported by this browser.')
    }

    loaded.then(() => {
      assert(
        typeof google.maps.places.Geocoder === 'function',
        "google.maps.places.Geocoder is undefined. Did you add 'places' to libraries when loading Google Maps?"
      )
      console.log('Pichulaa!!!')
    })
  }
}
</script>
