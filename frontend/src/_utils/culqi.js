export default class Culqi {
  constructor (publicKey) {
    if (process.browser) {
      this.appendCulqiScript().then(() => {
        window.Culqi.publicKey = publicKey
        window.Culqi.init()
      })
    }
  }

  appendCulqiScript () {
    return new Promise(resolve => {
      let c = 0
      if (!document.getElementById('culqui-lib')) {
        let culqiScript = document.createElement('script')
        culqiScript.setAttribute('src', 'https://checkout.culqi.com/v2')
        // culqiScript.setAttribute('src', 'https://checkout.culqi.com/plugins/v2')
        culqiScript.setAttribute('id', 'culqui-lib')
        document.body.appendChild(culqiScript)
      }

      let checkCulqi = setInterval(() => {
        c++
        if (c > 10) {
          clearInterval(checkCulqi)
        }
        if (window.Culqi) {
          clearInterval(checkCulqi)
          resolve()
        }
      }, 1000)
    })
  }

  createToken () {
    return new Promise(resolve => {
      window.__culqi_token = null
      window.Culqi.createToken()
      /* REVISA QUE ESTÁ DISPONIBLE EL TOKEN Y RESUELVE LA PROMESA */
      let c = 0
      let checkToken = setInterval(() => {
        c++
        if (c > 20) clearInterval(checkToken)
        if (window.__culqi_token) {
          clearInterval(checkToken)
          resolve(window.__culqi_token)
        } else {
        }
      }, 1000)
    })
  }

  settings (settings) {
    window.Culqi.settings(settings)
  }

  open () {
    window.Culqi.open()
  }

  get token () {
    return window.Culqi.token
  }
}
