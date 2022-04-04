#!/usr/bin/node

const i = process.argv.length;
if (i > 3) {
    console.log('Arguments found');
} else if (i === 3) {
    console.log('Argument found');
} else {
    console.log('No argument');
}