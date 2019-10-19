/**
 * @param {Object} obj JSON-compilant object to copy
 */
export const copyObj = obj => {
  return JSON.parse(JSON.stringify(obj))
}
