#!/usr/bin/node
// Write a square that inherits from rectangle

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
