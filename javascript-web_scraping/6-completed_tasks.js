#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const results = {};
let counter = 0;
let userId = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (!userId || userId !== data[i].userId) {
        userId = data[i].userId;
        counter = 0;
      }
      if (data[i].completed) {
        results[userId] = ++counter;
      }
    }
    console.log(results);
  }
});
