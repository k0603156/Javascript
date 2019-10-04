module.exports = {
  env: {
    browser: true,
    commonjs: false,
    es6: true
  },
  extends: [
    'standard'
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly'
  },
  parserOptions: {
    ecmaVersion: 2018
  },
  rules: {
    "indent": ["error", 2],
    "space-before-function-paren": ["error", {
      "anonymous": "always",
      "named": "always",
      "asyncArrow": "always"
    }],
    "object-curly-spacing": ["error", "never"],
    "semi":["error","always"],
      "semi-style": ["error", "last"]
  }
}