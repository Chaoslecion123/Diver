/**
 * @param {Object|String} data string or keys of object are named in form of snake
 * @param {number} depth to which level of keys should it process
 * @return {Object|String} string or keys of object are named in form of camel case
 */
export const snakeToCamel = function (data, depth) {
  if (_isObject(data)) {
    if (typeof depth === 'undefined') {
      depth = 1
    }
    return _processKeys(data, _camelize, depth)
  } else {
    return _camelize(data)
  }
}

/**
 * @param {Object|String} data string or keys of object are named in form of camel case
 * @param {number} depth to which level of keys should it process
 * @return {Object|String} string or keys of object are named in form of snake
 */
export const camelToSnake = (data, depth) => {
  if (_isObject(data)) {
    if (typeof depth === 'undefined') {
      depth = 1
    }
    return _processKeys(data, _snakelize, depth)
  } else {
    return _snakelize(data)
  }
}

// snakelize a string formed in underscore
const _snakelize = key => {
  let separator = '_'
  let split = /(?=[A-Z])/

  return key
    .split(split)
    .join(separator)
    .toLowerCase()
}

// camelize a string formed in underscore
const _camelize = key => {
  if (_isNumber(key)) {
    return key
  }
  key = key.replace(/[-_\s]+(.)?/g, function (match, ch) {
    return ch ? ch.toUpperCase() : ''
  })
  // Ensure 1st char is always lowercase
  return key.substr(0, 1).toLowerCase() + key.substr(1)
}

// camelize/snakelize keys of an object
// @param {number} depth to which level of keys should it process
const _processKeys = (obj, processer, depth) => {
  if (depth === 0 || !_isObject(obj)) {
    return obj
  }

  let result = {}
  let keys = Object.keys(obj)

  for (let i = 0; i < keys.length; i++) {
    result[processer(keys[i])] = _processKeys(
      obj[keys[i]],
      processer,
      depth - 1
    )
  }

  return result
}

const _isObject = obj => {
  return obj === Object(obj)
}

const _isNumber = n => {
  return !isNaN(parseFloat(n)) && !isNaN(n - 0)
}
