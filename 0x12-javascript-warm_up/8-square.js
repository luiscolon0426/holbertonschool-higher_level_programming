#!/usr/bin/node
// Print a square

const x = process.argv[2];

if (parseInt(x)) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
