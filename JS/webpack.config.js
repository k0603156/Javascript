const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const paths = (buildPath) => ({
  entry: path.resolve(buildPath, "index.js"),
  output: {
    filename: "main.js",
    path: path.resolve(buildPath, "dist"),
  },
  htmlPluginOption: {
    inject: true,
    template: path.resolve(buildPath, "index.html"),
  },
});

module.exports = (buildPath) => {
  const { entry, output, htmlPluginOption } = paths(buildPath);
  return {
    entry,
    output,
    plugins: [new HtmlWebpackPlugin(htmlPluginOption)],
  };
};
