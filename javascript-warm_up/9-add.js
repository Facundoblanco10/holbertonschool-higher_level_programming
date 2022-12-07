#!/usr/bin/node

const args = require('process').argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
console.log(add(a, b));
function add (a, b) {
  return a + b;
}
