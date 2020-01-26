import babel from 'rollup-plugin-babel';
import { eslint } from 'rollup-plugin-eslint';
import { uglify } from 'rollup-plugin-uglify';

const pathName = process.env.NODE_ENV === 'production' ? 'schart.min' : 'schart';

export default {
    input: './src/index.js',
    output: {
        file: `./lib/${pathName}.js`,
        format: 'umd',
        name: 'Schart'
    },
    plugins: [
        eslint({
            throwOnError: true,
            throwOnWarning: true,
            include: ['src/**'],
            exclude: ['node_modules/**']
        }),
        babel({
            exclude: 'node_modules/**'
        }),
        (process.env.NODE_ENV === 'production' && uglify())
    ]
};