#!/usr/bin/node

const time = parseInt(process.argv[2]);

if (isNaN(time)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < time; i++) {
    console.log('X'.repeat(time));
  }
}
