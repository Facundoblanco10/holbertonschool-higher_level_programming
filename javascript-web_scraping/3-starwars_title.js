#!/usr/bin/node

const request = require('request');

const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
