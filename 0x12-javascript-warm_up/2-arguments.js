#!/usr/bin/node
// Script that prints a message depending of the arguments passed

if (process.argv.length === 2) {
  console.log('No argument');
}
if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
