#!/usr/bin/node
// Script that printsall characters of Star Warsconst fs = require('request');
const fs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

fs(url, function (a, response, body) {
  const characterURLs = JSON.parse(body).characters;
  characterURLs.forEach((url) => {
    fs(url, function (a, response, body) {
      const character = JSON.parse(body).name;
      console.log(character);
    });
  });
});
