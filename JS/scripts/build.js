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

const [nodePath, selfPath, dirPath] = process.argv;

const buildPath = (relativePath) =>
  path.resolve(fs.realpathSync(process.cwd()), relativePath);

(async () => {
  try {
    if (!dirPath) {
      throw Error("yan build --dirPath: dirPath가 존재하지 않습니다.");
    }
    wp(wpConfigFactory(buildPath(dirPath))).run();
  } catch (error) {
    console.log(chalk.red(error));
  }
})();
