#!/usr/bin/node

function factorial (n) {
  if (n <= 1) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
