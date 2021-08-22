const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const paths = (buildDir) => {
  console.log(path.resolve(buildDir, "index.js"));
  return {
		entry: path.resolve(buildDir, "index.js"),
		output: {
			filename: "main.js",
			path: path.resolve(buildDir, "dist"),
		},
		htmlPluginOption: {
			inject: true,
			template: path.resolve(buildDir, "index.html"),
		},
	};
};

module.exports = (buildDir) => {
  const { entry, output, htmlPluginOption } = paths(buildDir);
  console.log(buildDir)
  return {
		entry,
		output,
		plugins: [new HtmlWebpackPlugin(htmlPluginOption)],
		module: {
			rules: [
				{
					test: [/\.js$/],
					include: [buildDir],
					exclude: /node_modules/,
					loader: require.resolve("babel-loader"),
				},
			],
		},
    devtool: 'source-map',
	};
};
