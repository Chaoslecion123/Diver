const vincenty = (p1, p2) => {
  if (p1.lat === p2.lat && p1.lng === p2.lng) {
    return 0.0
  }
  const MAX_ITERATIONS = 200
  const CONVERGENCE_THRESHOLD = 1e-12

  const a = 6378137.0 // metres in WGS-84
  const f = 1.0 / 298.257223563 // in WGS-84
  const b = 6356752.314245 // meters in WGS-84 / (1 - f)a

  let U1 = Math.atan((1 - f) * Math.tan(p1.lat))
  let U2 = Math.atan((1 - f) * Math.tan(p2.lat))
  let sinU1 = Math.sin(U1)
  let cosU1 = Math.cos(U1)
  let sinU2 = Math.sin(U2)
  let cosU2 = Math.cos(U2)

  let L = p1.lng - p2.lng

  let lambda = L
  let lambdaP = 0
  let iterations = 0

  let sinLambda
  let cosLambda
  let sinSigma
  let cosSigma
  let sigma
  let sinAlpha
  let cosSqAlpha
  let cos2SigmaM
  let C

  while (Math.abs(lambda - lambdaP) > CONVERGENCE_THRESHOLD) {
    if (iterations > MAX_ITERATIONS) {
      break
    }

    iterations += 1
    lambdaP = lambda

    sinLambda = Math.sin(lambda)
    cosLambda = Math.cos(lambda)

    sinSigma = Math.sqrt(
      (cosU2 * sinLambda) ** 2 +
        (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda) ** 2
    )

    if (sinSigma === 0) {
      return 0.0
    }

    cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLambda
    sigma = Math.atan2(sinSigma, cosSigma)
    sinAlpha = (cosU1 * cosU2 * sinLambda) / sinSigma
    cosSqAlpha = 1 - sinAlpha ** 2

    cos2SigmaM = cosSigma - (2 * sinU1 * sinU2) / cosSqAlpha
    if (cos2SigmaM === Infinity) {
      cos2SigmaM = 0
    }

    C = (f / 16) * cosSqAlpha * (4 + f * (4 - 3 * cosSqAlpha))

    lambda =
      L +
      (1 - C) *
        f *
        sinAlpha *
        (sigma +
          C *
            sinSigma *
            (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM ** 2)))
  }

  let uSq = (cosSqAlpha * (a ** 2 - b ** 2)) / b ** 2
  let A = 1 + (uSq / 16384) * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
  let B = (uSq / 1024) * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))
  let deltaSigma =
    B *
    sinSigma *
    (cos2SigmaM +
      (B / 4) *
        (cosSigma * (-1 + 2 * cos2SigmaM ** 2) -
          (B / 6) *
            cos2SigmaM *
            (-3 + 4 * sinSigma ** 2) *
            (-3 + 4 * cos2SigmaM ** 2)))
  let s = b * A * (sigma - deltaSigma)
  s /= 1000

  return parseFloat(s.toFixed(6))
}

export default vincenty
