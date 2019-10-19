/* eslint-disable no-new */
/* JS Libraries ***************************************************************/
import Vue from 'vue'
import Vuetify from 'vuetify'
import VueCarousel from 'vue-carousel'
import VueCountdown from '@chenfengyuan/vue-countdown'
import FlagIcon from 'vue-flag-icon'
import VueYouTubeEmbed from 'vue-youtube-embed'

/* Style Libraries ************************************************************/
import 'vuetify/dist/vuetify.min.css'

/* Custom Components **********************************************************/
import router from './router'
import store from './store'

/* Plugins ********************************************************************/
import './plugins/icons'
import './plugins/diver'
import './plugins/filters'
import './plugins/gmaps'

import App from './App.vue'
import '@/registerServiceWorker'

/* Vue Components ************************************************************/
Vue.component('app', App)

const accentColorElement = document.querySelector(
  '[name=storefront-accent-color]'
)
if (accentColorElement) {
  const accentColor = accentColorElement.content
  Vue.use(Vuetify, {
    theme: {
      accent: accentColor
    },
    options: {
      customProperties: true
    }
  })
} else {
  Vue.use(Vuetify)
}

Vue.use(VueCarousel)
Vue.component(VueCountdown.name, VueCountdown)
Vue.use(FlagIcon)
Vue.use(VueYouTubeEmbed)

let app = null

store.dispatch('auth/initialize').then(() => {
  store.dispatch('cart/initialize')

  if (!app) {
    /* eslint-disable no-new */
    app = new Vue({
      router: router,
      store: store,
      render: h => h(App)
    }).$mount('#app')
  }
})
