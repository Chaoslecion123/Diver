const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')

const BASE_PORT = 8080
const BASE_HOST = '0.0.0.0'
const BASE_URL = `http://${BASE_HOST}:${BASE_PORT}`

module.exports = {
  publicPath: process.env.NODE_ENV !== 'production'
    ? `${BASE_URL}/`
    : '/',
  outputDir: './dist/',
  assetsDir: 'static/store',
  productionSourceMap: true,
  css: {
    extract: true,
    loaderOptions: {
      less: {
        javascriptEnabled: true
      }
    }
  },
  pwa: {
    name: 'Quimder',
    themeColor: '#F58220',
    msTileColor: '#F58220',
    appleMobileWebAppStatusBarStyle: 'black',
    workboxPluginMode: 'GenerateSW'
  },
  configureWebpack: {
    resolve: {
      extensions: [
        '.less'
      ],
      modules: [
        path.resolve(__dirname, 'src')
      ]
    }
  },
  chainWebpack: config => {
    config
      .optimization
      .splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(
        BundleTracker, [{
          filename: 'webpack-stats.json'
        }]
      )

    config
      .resolve
      .alias
      .set('__STATIC__', 'static')

    config
      .devServer
      .public(BASE_URL)
      .host(BASE_HOST)
      .port(BASE_PORT)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({
        'Access-Control-Allow-Origin': ['*']
      })
  }
}
