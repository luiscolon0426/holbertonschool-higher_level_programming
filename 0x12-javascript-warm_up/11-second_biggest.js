#!/usr/bin/node

let big = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  big = args[args.length - 2];
}
console.log(big);
