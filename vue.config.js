// todo https://github.com/symfony/webpack-encore/issues/1064
// https: true,


const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  // https://antoniandre.github.io/wave-ui/getting-started#standard-installation
  // transpileDependencies: ['wave-ui'], // ! \\

  // // You don't need this part if you haven't done step 2.
  // // ----------------------------------------------------
  // css: {
  //   loaderOptions: {
  //     // `additionalData` was called `prependData` prior sass-loader 9.
  //     sass: { additionalData: '@import "@/scss/variables.scss";' }
  //   }
  // },

  transpileDependencies: true,
  //  devServer: {
  //    proxy: 'http://localhost:8000/'
  //  },
  chainWebpack: config => {
    config.module
      .rule('img')
      .test(/\.(png|svg|jpg|jpeg|gif|json)$/i)
      .type('asset/resource')
      .end()

  }
})


// ////////////////////////////////////////////////////
// var HtmlWebpackPlugin = require('html-webpack-plugin');
// const { VueLoaderPlugin } = require('vue-loader')
// const path = require('path');
// const fs = require('fs');
// const webpack = require('webpack');


// //const dotenv = require('dotenv').config({ path: __dirname + '/.env' });
// // const dotenv = require('dotenv').config({ path: __dirname + '/.env' });

// module.exports = {
//   mode: 'development',
//   resolve: {
//     extensions: ['.js', '.vue', '.css']
//   },

//   module: {
//     rules: [
//       {
//         test: /\.vue$/,
//         exclude: /node_modules/,
//         loader: 'vue-loader'
//       },
//       {
//         test: /\.js?$/,
//         exclude: /node_modules/,
//         loader: 'babel-loader'
//       },
//       {
//         test: /\.css$/,
//         use: [
//           { loader: "style-loader" },
//           { loader: "css-loader" },
//         ],
//       },
//       {
//         test: /\.(png|svg|jpg|jpeg|gif)$/i,
//         type: 'asset/resource',
//       },
//       // {
//       //     test: /\.(ico)$/i,
//       //     type: 'asset/resource',
//       // },
//       {
//         test: /\.(json)$/i,
//         type: 'asset/resource',
//       },
//     ]
//   },
//   plugins: [
//     new VueLoaderPlugin(),
//     // new HtmlWebpackPlugin({
//     //     template: 'src/template/index.html',
//     //     title: 'Beyond',
//     //     BASE_URL: "localhost, not working"
//     // }),
//     // new webpack.ProvidePlugin({
//     //     // Make a global `process` variable that points to the `process` package,
//     //     // because the `util` package expects there to be a global variable named `process`.
//     //     // Thanks to https://stackoverflow.com/a/65018686/14239942
//     //     process: 'process/browser'
//     // })
//     // new webpack.DefinePlugin({
//     //     'process.env': JSON.stringify(dotenv.parsed),
//     // }),
//     //        new webpack.DefinePlugin({
//     //      'process.env.NODE_ENV': JSON.stringify(dotenv.NODE_ENV),
//     //      'process.env.MY_ENV': JSON.stringify(dotenv.MY_ENV),
//     //    })
//   ],
//   devServer: {
//     static: {
//       directory: path.join(__dirname, 'src', 'assets'),
//     },
//     historyApiFallback: true,
//     headers: {
//       "X-Powered-By": 'Beyond',
//       "Cache-Control": "no-cache, no-store, must-revalidate",
//       "Pragma": "no-cache",
//       "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
//     },
//     proxy: {
//       '/api*': {
//         target: 'http://localhost:8000/',
//       },

//     },

//   },
//   externals: {
//     config: JSON.stringify({
//       djangoApi: 'http://localhost:8000'
//     })
//   }
// }
