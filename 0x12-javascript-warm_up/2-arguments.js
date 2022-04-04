#!/usr/bin/node

const i = process.argv.length;
if (i === 2) {
    console.log('No argument');
} else if (i === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}