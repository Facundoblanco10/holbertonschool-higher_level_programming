#!/usr/bin/node
const Squaree = require('./5-square');

module.exports = class Square extends Squaree {
  constructor(size) {
    super(size);
  }
  charPrint(c) {}
};
