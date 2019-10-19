import Vue from 'vue'

const PREFIXED_CURRENCIES = ['PEN']
const CURRENCIES = {
  PEN: 'S/'
}

const _isNumber = n => {
  return !isNaN(+n) && isFinite(n)
}

Vue.filter('price', value => {
  if (_isNumber(value)) {
    let val = (value / 1.0).toFixed(2) // .replace('.', ',')
    return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
  }

  return ''
})

Vue.filter('moneyFormat', value => {
  let amount = parseFloat(value.amount)
  let currency = value.currency
  let prefixCurrency = PREFIXED_CURRENCIES.indexOf(currency) >= 0

  if (_isNumber(amount)) {
    let val = (amount / 1.0).toFixed(2)
    amount = val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
  }

  if (prefixCurrency) {
    return `${CURRENCIES[currency]} ${amount}`
  }

  return `${amount} ${CURRENCIES[currency]}`
})
