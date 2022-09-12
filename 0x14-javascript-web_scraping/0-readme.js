#!/usr/bin/node
// task 0
const fs = require("fs");

fs.readFile(process.argv[2], "utf8", (error, info) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(info);
});
