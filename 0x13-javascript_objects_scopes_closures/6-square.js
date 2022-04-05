#!/usr/bin/node
// Create an instance method that printst the rectangle using the char c

const NewSquare = require('./5-square.js');

module.exports = class Square extends NewSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
