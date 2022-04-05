#!/usr/bin/node
// Write a function that prints the numberof argumetns already printed

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
