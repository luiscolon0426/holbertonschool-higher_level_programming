#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const f = require('fs');
const webpage = process.argv[2];
const file = process.argv[3];

request(webpage, function (error, res, content) {
  if (error) {
    console.error('error:', error);
  }

  f.writeFile(file, content, 'utf-8', (errorB) => {
    if (errorB) {
      console.error('error:', errorB);
    }
  });
});
