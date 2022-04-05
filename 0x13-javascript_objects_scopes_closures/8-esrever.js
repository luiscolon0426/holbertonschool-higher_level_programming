#!/usr/bin/node
// return a reverse version of the list

exports.esrever = function (list) {
  const total = [];
  for (let i = list.length - 1; i >= 0; i--) {
    total.push(list[i]);
  }
  return total;
};
