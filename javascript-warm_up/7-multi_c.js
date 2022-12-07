#!/usr/bin/node

const myVar = 'C is fun';
let i = 0;
while (i < parseInt(require('process').argv[2])) {
  console.log(myVar);
  i++;
}
