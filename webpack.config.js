var HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader')
const path = require('path');
const fs = require('fs');

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
                test: /\.(jpe?g|png|gif|svg)$/i,
                loader: 'file-loader',
                options: {
                    name: '/login/[name].[ext]'
                }
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({
            template: 'src/template/index.html',
            title: 'Beyond',
            BASE_URL: "f"
        })
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
            }
        },

    },
    externals: {
        config: JSON.stringify({
            djangoApi: 'http://localhost:8000'
        })
    }
}