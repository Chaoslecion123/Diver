/**
 * Session object tohandle CSFR Token.
 * With this object we can work submitting forms via post request in conpilance
 * with CSFR Django mechanism.
 */
import axios from 'axios'

/*
 * TODO:
 * The cookie name need to be loaded from an envfile
 */
const CSRF_COOKIE_NAME = 'csrftoken'
const CSRF_HEADER_NAME = 'X-CSRFToken'

const session = axios.create({
  xsrfCookieName: CSRF_COOKIE_NAME,
  xsrfHeaderName: CSRF_HEADER_NAME
  // headers: {
  //   'Content-Type': 'application/json;charset=UTF-8'
  // }
  // headers: {
  //   "Access-Control-Allow-Origin": "*",
  //   "Access-Control-Allow-Methods": "*",
  //   "Access-Control-Max-Age": "1000",
  //   "Access-Control-Allow-Headers": "X-Requested-With, Content-Type"
  // }
})

export default session
