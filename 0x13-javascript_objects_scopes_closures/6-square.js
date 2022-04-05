#!/usr/bin/node
// Create an instance method that printst the rectangle using the char c

const NewSquare = require('./5-square.js');

module.exports = class Square extends NewSquare {
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
