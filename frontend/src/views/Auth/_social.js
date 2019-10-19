export class Facebook {
  constructor (clientId, redirectUri) {
    this.clientId = clientId
    this.redirectUri = redirectUri
    this.provider = 'facebook'
    this.apiVerison = '2.9'
    this.baseUrl = 'https://www.facebook.com'
  }

  getUrlParams () {
    return `client_id=${this.clientId}&redirect_uri=${this.redirectUri}&return_scopes=true&scope=email`
  }

  getUrl () {
    const urlParams = this.getUrlParams()
    return `${this.baseUrl}/v${this.apiVerison}/dialog/oauth?${urlParams}`
  }
}

export class Google {
  constructor (clientId, redirectUri) {
    this.clientId = clientId
    this.redirectUri = redirectUri
    this.provider = 'facebook'
    this.apiVerison = '2.9'
    this.baseUrl = 'https://www.google.com'
  }

  getUrlParams () {
    return `client_id=${this.clientId}&redirect_uri=${this.redirectUri}&return_scopes=true&scope=email`
  }

  getUrl () {
    const urlParams = this.urlParams
    return `${this.baseUrl}/v${this.apiVerison}/dialog/oauth?${urlParams}`
  }
}
