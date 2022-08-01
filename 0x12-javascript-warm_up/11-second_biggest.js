#!/usr/bin/node

if (process.argv.length > 3) {
  const arg = process.argv.map(Number);
  arg.slice(2);
  arg.sort((a, b) => b - a);
  console.log(arg[3]);
} else {
  console.log(0);
}
