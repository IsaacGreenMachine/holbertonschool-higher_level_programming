#!/usr/bin/node
let bigBoy = 0;
let medBoy = 0;
for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > bigBoy) {
    medBoy = bigBoy;
    bigBoy = parseInt(process.argv[i]);
  }
}
console.log(medBoy);
