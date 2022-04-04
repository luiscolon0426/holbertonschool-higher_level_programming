#!/usr/bin/node
// Script that prints the first argument passed to it

const i = process.argv[2];

if (i === undefined) {
  console.log('No argument');
} else {
  console.log(i);
}
