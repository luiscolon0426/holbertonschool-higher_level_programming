#!/usr/bin/node
// script that imports a dict of occurences
const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  if (newdict[dict[key]] === undefined) {
    newdict[dict[key]] = [];
  }
  newdict[dict[key]].push(key);
}
console.log(newdict);
