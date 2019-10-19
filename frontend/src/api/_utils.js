import qs from 'qs'

export const paramsSerializer = (params = {}) => {
  return qs.stringify(params, { arrayFormat: 'repeat' })
}

// Object.keys(data).map((key) => {
//   return encodeURIComponent(key) + '=' + encodeURIComponent(data[key])
// }).join('&')

export const serializeJsonData = (jsonData = {}) =>
  Object.entries(jsonData)
    .map(x => `${encodeURIComponent(x[0])}=${encodeURIComponent(x[1])}`)
    .join('&')
