#!/usr/bin/node
// Update rect1, if w or h is eq 0, create an empty obj

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
