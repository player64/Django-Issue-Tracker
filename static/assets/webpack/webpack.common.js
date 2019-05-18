const Path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const webpack = require('webpack');
const WebpackAssetsManifest = require('webpack-assets-manifest');
const BundleTracker  = require('webpack-bundle-tracker');
const staticDir = '../../../static/webpack-bundle';

module.exports = {
    entry: {
        app: Path.resolve(__dirname, '../scripts/main.js')
    },
    output: {
        path: Path.join(__dirname, staticDir),
        filename: 'js/[name].js'
    },
    optimization: {
        runtimeChunk: 'single',
        splitChunks: {
            chunks: 'all', // async // all
            //name: false
            maxInitialRequests: Infinity,
            // https://hackernoon.com/the-100-correct-way-to-split-your-chunks-with-webpack-f8a9df5b7758
            cacheGroups: {
                vendor: {
                    test: /[\\/]node_modules[\\/]/,
                    name(module) {

                        const match = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/);
                        if (!!match) {
                            const packageName = match[1];
                            return `npm.${packageName.replace('@', '')}`;
                        };

                        // npm package names are URL-safe, but some servers don't like @ symbols
                        // return `npm.${packageName.replace('@', '')}`;
                    },
                },
            },
        }
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery'
        }),
        new CleanWebpackPlugin(['static'], {root: Path.resolve(__dirname, '../../webpack-bundle')}),
        new CopyWebpackPlugin([
            {from: Path.resolve(__dirname, '../images'), to: `${staticDir}/images`}
        ]),

        // new WebpackAssetsManifest()
        new BundleTracker({path: __dirname, filename: '../../webpack-stats-json'})
    ],
    resolve: {
        alias: {
            '~': Path.resolve(__dirname, '../../assets')
        }
    },
    module: {
        rules: [
            {
                test: /\.mjs$/,
                include: /node_modules/,
                type: 'javascript/auto'
            },
            {
                test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
                include: Path.join(__dirname, '../../static'),
                use: {
                    loader: 'file-loader',
                    options: {
                        name: '[path][name].[ext]'
                    }
                }
            }
        ]
    }
};


