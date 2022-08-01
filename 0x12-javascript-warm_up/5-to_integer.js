#!/usr/bin/node

const arg = process.argv;
const n = parseInt(arg[2]);

if (isNaN(n))
	console.log('Not a number');
else
	console.log('My number:', n);
