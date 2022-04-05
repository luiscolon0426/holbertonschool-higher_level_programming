#!/usr/bin/node
// Function that returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (const item of list) {
    if (item === searchElement) {
      ++total;
    }
  }
  return total;
};
