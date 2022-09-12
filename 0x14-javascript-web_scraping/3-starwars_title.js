#!/usr/bin/node
// task 3

const axios = require('axios');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios.get(url).then(function (response) {
  console.log(response.data.title);
}).catch(function (error) {
  console.log('code: ' + error.response.status);
});
