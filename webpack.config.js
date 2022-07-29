var HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader')

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
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({ template: './src/index.html' })],
    devServer: {
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
        }
    },
    externals: {
        config: JSON.stringify({
            djangoApi: 'http://localhost:8000'
        })
    }
}