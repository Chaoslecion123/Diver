<template>
  <div class="d-address-map">
    <v-divider />
    <div class="pa-3">
      <div>
        Busca tu dirección
      </div>
      <div
        :class="[
          'v-input ',
          'v-text-field ',
          'v-text-field--single-line ',
          'v-text-field--solo ',
          'v-text-field--solo-flat ',
          'v-text-field--enclosed ',
          'theme--light ',
          'd-input ',
          'd-input--rounded ',
          'd-input--bordered',
          'd-address-map-input'
        ]">
        <div class="v-input__control">
          <div class="v-input__slot ma-0">
            <div class="v-text-field__slot">
              <gmap-autocomplete
                type="text"
                :value="searchedAddress"
                :select-first-on-enter="true"
                :componentRestrictions="{ country: 'pe' }"
                autocomplete="off"
                @place_changed="handlePlaceChange"/>
            </div>
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
        fullscreenControlOptions: {
          position: 9
        },
        streetViewControl: false,
        zoomControlOptions: {
          position: 3
        }
      }">
      <gmap-marker
        :position="marker.position"
        :draggable="true"
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

  .d-address-map-input {
    display: block;
    flex: initial;
  }
}
</style>

<script>
import vincenty from '@/_utils/vicenty'
import { gmapApi } from 'vue2-google-maps'

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
    },
    address: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      searchedAddress: '',
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
      },
      currentPosition: {
        lat: null,
        lng: null
      },
      innerChange: false
    }
  },
  watch: {
    currentPosition (val, oldVal) {
      this.map.center.lat = val.lat
      this.map.center.lng = val.lng

      this.marker.position.lat = val.lat
      this.marker.position.lng = val.lng

      this.updateAddress(this.map.center)
    }
  },
  methods: {
    getCurrentPosition () {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          position => {
            position = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            }
            this.currentPosition = { ...position }
          },
          error => {
            console.log(error)
          },
          {
            enableHighAccuracy: true,
            timeout: 100000
          }
        )
      }
    },
    getFormatedAddress (position, address) {
      let postalCode = address.address_components.find(
        component => component.types.indexOf('postal_code') > -1
      )
      postalCode = postalCode ? postalCode.short_name : ''

      let country = address.address_components.find(
        component => component.types.indexOf('country') > -1
      )
      country = country ? country.short_name : ''

      let countryArea = address.address_components.find(
        component => component.types.indexOf('administrative_area_level_1') > -1
      )
      countryArea = countryArea ? countryArea.long_name : ''
      countryArea =
        countryArea === 'Municipalidad Metropolitana de Lima'
          ? 'Lima'
          : countryArea

      let city = address.address_components.find(
        component => component.types.indexOf('administrative_area_level_2') > -1
      )
      city = city ? city.long_name : ''
      city = city === 'Provincia de Lima' ? 'Lima' : city
      city = city.replace('Provincia de', '').trim()

      let cityArea = address.address_components.find(
        component => component.types.indexOf('administrative_area_level_2') > -1
      )
      cityArea = cityArea ? cityArea.long_name : ''
      cityArea = cityArea === 'Provincia de Lima' ? 'Lima' : cityArea
      cityArea = cityArea.replace('Provincia de', '').trim()

      let streetAddress2 = address.address_components.find(
        component => component.types.indexOf('sublocality_level_1') > -1
      )
      streetAddress2 = streetAddress2 ? streetAddress2.long_name : ''

      let route = address.address_components.find(
        component => component.types.indexOf('route') > -1
      )
      route = route ? route.long_name : ''

      let streetNumber = address.address_components.find(
        component => component.types.indexOf('street_number') > -1
      )
      streetNumber = streetNumber ? streetNumber.long_name : ''

      return {
        streetAddress1: `${route} ${streetNumber}`,
        streetAddress2,
        cityArea,
        city,
        countryArea,
        country,
        postalCode,
        position
      }
    },
    getNearestAddress (position, addresses) {
      let distances = addresses.map(address => {
        return vincenty(position, {
          lat: address.geometry.location.lat(),
          lng: address.geometry.location.lng()
        })
      })
      let minimaIndex = distances.indexOf(Math.min(...distances))
      return addresses[minimaIndex]
    },
    updateAddress (position) {
      let { Geocoder } = gmapApi().maps
      let geocoder = new Geocoder()

      geocoder.geocode({ location: position }, (results, status) => {
        if (status === 'OK') {
          let nearestAddress = this.getNearestAddress(position, results)
          let address = this.getFormatedAddress(position, nearestAddress)
          this.$emit('change', address)
        }
      })

      // this.$geocoder.setDefaultMode('lat-lng')
      // this.$geocoder.send(position, response => {
      //   if (response && response.status === 'OK') {
      //     let nearestAddress = this.getNearestAddress(position, response)
      //     let address = this.getFormatedAddress(position, nearestAddress)
      //     this.$emit('change', address)
      //   }
      // })
    },
    getPosition (address) {
      address = {
        streetAddress1: address.streetAddress1,
        city: address.city,
        postal_code: address.postalCode,
        country: address.country
      }

      this.$geocoder.setDefaultMode('address')
      this.$geocoder.send(address, response => {
        if (response && response.status === 'OK') {
        }
      })
    },
    handleDragend (event) {
      if (event && event.latLng) {
        this.map.center.lat = event.latLng.lat()
        this.map.center.lng = event.latLng.lng()

        this.updateAddress(this.map.center)
      }
    },
    handlePlaceChange (place) {
      if (place && place.geometry && place.geometry.location) {
        this.map.center.lat = place.geometry.location.lat()
        this.map.center.lng = place.geometry.location.lng()

        this.marker.position.lat = place.geometry.location.lat()
        this.marker.position.lng = place.geometry.location.lng()

        this.updateAddress(this.map.center)
      }
    }
  },
  created () {
    if (this.address) {
      if (this.address.position) {
        this.map.center.lat = this.address.position.lat
        this.map.center.lng = this.address.position.lng

        this.marker.position.lat = this.address.position.lat
        this.marker.position.lng = this.address.position.lng
      } else {
        this.getPosition(this.address)
      }
    } else {
      this.getCurrentPosition()
    }
  }
}
</script>
