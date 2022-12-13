#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const results = {};
let userId = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (!userId || userId !== data[i].userId) {
        userId = data[i].userId;
        results[userId] = 0;
      }
      if (data[i].completed) {
        results[userId] += 1;
      }
    }
    for (const [key, value] of Object.entries(results)) {
      if (value === 0) delete results[key];
    }
    console.log(results);
  }
});
