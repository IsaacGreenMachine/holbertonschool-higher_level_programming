#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  let n = 0;
  const moviesList = JSON.parse(body).results;
  for (let i = 0; i < moviesList.length; i++) {
    for (let j = 0; j < moviesList[i].characters.length; j++) {
      if (moviesList[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        n++;
      }
    }
  }
  console.log(n);
});
