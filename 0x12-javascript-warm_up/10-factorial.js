#!/usr/bin/node
// Script that computs and prints a factorial

const func = process.argv[2];

function factorial (func) {
  if (isNaN(func) || func === 1) {
    return (1);
  } else {
    return (func * factorial(func - 1));
  }
}
console.log(factorial(parseInt(func)));
