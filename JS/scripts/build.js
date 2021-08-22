"use strict";
process.env.BABEL_ENV = "production";
process.env.NODE_ENV = "production";
process.env.CI = false;

process.on("unhandledRejection", (err) => {
  throw err;
});

const chalk = require("chalk");
const path = require("path");
const fs = require("fs");
const wp = require("webpack");

const wpConfigFactory = require("../webpack.config");

const [nodePath, selfPath, dirName] = process.argv;

const buildPath = (dirname) => {
  return path.resolve(fs.realpathSync(process.cwd()), './src/', dirname);
}
(async () => {
  try {
    if (!dirName) {
      throw Error("yan build --dirName: dirName 존재하지 않습니다.");
    }
    wp(wpConfigFactory(buildPath(dirName))).run();
  } catch (error) {
    console.error(chalk.red(error));
  }
})();
