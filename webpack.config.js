const path = require('path');

module.exports = {
    mode: 'development', // Or 'production' for optimized builds
    entry: './src/js/main.js', // Your main JavaScript file (e.g., 'src/js/main.js')
    output: {
        filename: 'js/bundle.js',
        path: path.resolve(__dirname, 'static'), // Output directory for built files
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            // Add other rules for your project (e.g., for images, fonts)
        ],
    },
};
