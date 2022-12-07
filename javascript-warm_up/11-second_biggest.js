#!/usr/bin/node

let args = require('process').argv;

if (args[2] && args[3]){
  for (i in args) {
    args[i] = parseInt(args[i]);
  }
  console.log(args.sort().reverse()[3])
}
else {
  console.log(0)
}