#!/usr/bin/node
// Create an instance method that printst the rectangle using the char c

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.height));
    }
  }
};
