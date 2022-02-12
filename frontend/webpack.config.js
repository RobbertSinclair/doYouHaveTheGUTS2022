const path = require("path");

module.exports = {
    entry: "./src/index.js",
    module:{
        rules: [
            {
                test: /\.svg$/,
                use: "svg-inline-loader"
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"]
            },
            {
                test: /\.(js)$/,
                use: "babel-loader"
            },
            {
                test: /\.(jpe?g|png|gif|svg|key)$/i,
                loader: 'file-loader',
                options: {
                    name: '/public/icons/[name].[ext]'
                }
            }
        ],
    },
    output: {
        path: path.resolve(__dirname, "../backend/static/js"),
        filename: "bundle.js"
    },
    mode: "production"
}