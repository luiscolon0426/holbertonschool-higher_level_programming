#!/usr/bin/node
// Print first argument if it can be converted to an integer

const number = process.argv[2];
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
