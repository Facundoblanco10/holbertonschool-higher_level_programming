#!/usr/bin/node

const args = require('process').argv;
let i = 0;
if (args[2] && args[3]) {
  for (i in args) {
    args[i] = parseInt(args[i]);
  }
  console.log(args.sort(function (a, b) { return b - a; })[3]);
} else {
  console.log(0);
}
