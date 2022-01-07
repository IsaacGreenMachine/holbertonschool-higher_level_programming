#!/usr/bin/node
function factorial (a) {
  if (a > 1) {
    return (parseInt(a) * factorial(parseInt(a) - 1));
  } else {
    return 1;
  }
}

console.log(factorial(process.argv[2]));
