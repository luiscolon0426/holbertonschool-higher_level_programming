#!/usr/bin/node
// Script that display the status code

const request = require('request');
const url = process.argv[2];
request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
