#!/usr/bin/node
// Update Script by adding a new funcion that increments the int

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  myObject.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
