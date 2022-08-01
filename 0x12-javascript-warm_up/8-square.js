#!/usr/bin/node

const time = parseInt(process.argv[2]);

if (isNaN(time)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < time; i++) {
    console.log('X'.repeat(time));
  }
}
