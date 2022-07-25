var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
    resolve: {
        extensions: ['.js', '.vue']
    },
    module: {
        rules: [
            {
                test: /\.vue?$/,
                exclude: /(node_modules)/,
                use: 'vue-loader'
            },
            {
                test: /\.js?$/,
                exclude: /(node_modules)/,
                use: 'babel-loader'
            }
        ]
    },
    plugins: [new HtmlWebpackPlugin({
        template: './src/index.html'
    })],
    devServer: {
        historyApiFallback: true,
        headers: {
            "X-Powered-By": 'Beyond',
            "Cache-Control": "max-age=300, must-revalidate",
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
