#!/usr/bin/node
// task 4

const axios = require('axios');
const url = process.argv[2];
const p18 = 'https://swapi-api.hbtn.io/api/people/18/';
let res = 0;

axios.get(url).then(function (response) {
  const films = response.data.results;
  for (let n = 0; n < films.length; n++) {
    if (films[n].characters.includes(p18)) {
      res = res + 1;
    }
  }
  console.log(res);
}).catch(function (error) {
  console.log(error);
});
