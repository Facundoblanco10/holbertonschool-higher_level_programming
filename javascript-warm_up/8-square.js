#!/usr/bin/node

const args = require('process');
const size = parseInt(args.argv[2]);
if (!size) {
  console.log('Missing size');
  process.exit(1);
}
let i = 0;
while (i < size) {
  console.log('X'.repeat(size));
  i++;
}
