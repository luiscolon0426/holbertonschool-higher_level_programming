#!/usr/bin/node
// script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  if (newdict[dict[key]] === undefined) {
    newdict[dict[key]] = [];
  }
  newdict[dict[key]].push(key);
}
console.log(newdict);
