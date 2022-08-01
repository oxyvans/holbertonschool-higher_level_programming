#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
	console.log('No argument');
} else {
	console.log('My number: ', n);
}
