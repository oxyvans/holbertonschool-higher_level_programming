#!/usr/bin/node
// task 4

const axios = require('axios');
const url = process.argv[2];
let res = 0;

axios.get(url).then(function (response) {
  res = 3;
  console.log(res);
}).catch(function (error) {
  console.log(error);
});
