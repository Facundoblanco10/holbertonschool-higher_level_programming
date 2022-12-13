#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

counter = 0
request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    for (const episode of data.results) {
      for (const character of episode.characters) {
        let route = character.split("/");
        charId = route.slice(-2)[0];
        if (charId == 18) {
            counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
