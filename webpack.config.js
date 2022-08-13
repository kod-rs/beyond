var HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader')
const path = require('path');
const fs = require('fs');
//const dotenv = require('dotenv').config({ path: __dirname + '/.env' });
const webpack = require('webpack');
// const dotenv = require('dotenv').config({ path: __dirname + '/.env' });

module.exports = {
    mode: 'development',
    resolve: {
        extensions: ['.js', '.vue', '.css']
    },

    module: {
        rules: [
            {
                test: /\.vue$/,
                exclude: /node_modules/,
                loader: 'vue-loader'
            },
            {
                test: /\.js?$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            },
            {
                test: /\.css$/,
                use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" },
                ],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.(json)$/i,
                type: 'asset/resource',
            },
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({
            template: 'src/template/index.html',
            title: 'Beyond',
            BASE_URL: "localhost, not working"
        }),
        new webpack.ProvidePlugin({
            // Make a global `process` variable that points to the `process` package,
            // because the `util` package expects there to be a global variable named `process`.
            // Thanks to https://stackoverflow.com/a/65018686/14239942
            process: 'process/browser'
        })
        // new webpack.DefinePlugin({
        //     'process.env': JSON.stringify(dotenv.parsed),
        // }),
        //        new webpack.DefinePlugin({
        //      'process.env.NODE_ENV': JSON.stringify(dotenv.NODE_ENV),
        //      'process.env.MY_ENV': JSON.stringify(dotenv.MY_ENV),
        //    })
    ],
    devServer: {
        static: {
            directory: path.join(__dirname, 'src', 'assets'),
        },
        historyApiFallback: true,
        headers: {
            "X-Powered-By": 'Beyond',
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
        },
        proxy: {
            '/api*': {
                target: 'http://localhost:8000/',
            },

        },

    },
    externals: {
        config: JSON.stringify({
            djangoApi: 'http://localhost:8000'
        })
    }
}