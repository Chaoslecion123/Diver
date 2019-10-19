/* global process */

import Vue from 'vue'
// import Geocoder from '@pderas/vue2-geocoder'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: process.env.VUE_APP_GOOGLE_MAPS_API_KEY,
    // This is required if you use the Autocomplete plugin
    libraries: 'places'
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)

    // If you want to set the version, you can do so:
    // v: '3.26',
  },

  // If you intend to programmatically custom event listener code
  // (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  // instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  // you might need to turn this on.
  // autobindAllEvents: false,

  // If you want to manually install components, e.g.
  // import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  // Vue.component('GmapMarker', GmapMarker)
  // then disable the following:
  installComponents: true
})

// Vue.use(Geocoder, {
//   defaultCountryCode: null, // 'PE', // e.g. 'CA'
//   defaultLanguage: null, // 'es', // e.g. 'en'
//   defaultMode: 'lat-lng', // or 'lat-lng'
//   googleMapsApiKey: process.env.VUE_APP_GOOGLE_GEOCODING_API_KEY
// })
