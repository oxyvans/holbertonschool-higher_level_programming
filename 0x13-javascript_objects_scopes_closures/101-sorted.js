#!/usr/bin/node

const dict = require('./101-data.js').dict;
const res = {};
Object.entries(dict).forEach(key => {
  if (res[key[1]]) {
    res[key[1]].push(key[0]);
  } else {
    res[key[1]] = [key[0]];
  }
});

console.log(res);
