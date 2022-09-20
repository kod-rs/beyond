// todo https://github.com/symfony/webpack-encore/issues/1064
// https: true,

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({

  chainWebpack: config => {
    config.module
      .rule('img')
      .test(/\.(png|svg|jpg|jpeg|gif|json)$/i)
      .type('asset/resource')
      .end()

  },

  // fixme include headers
  // devServer: {
  //   historyApiFallback: true,
  //   headers: {
  //     "X-Powered-By": 'Beyond',
  //     "Cache-Control": "no-cache, no-store, must-revalidate",
  //     "Pragma": "no-cache",
  //     "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
  //   },
  //   proxy: {
  //     '/api*': {
  //       target: 'http://localhost:8000/',
  //     },

  //   },

  // },

})


