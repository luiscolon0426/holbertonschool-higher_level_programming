#!/usr/bin/node
 // Script that concatenates 2 files

const conc = require('conc');
const a = conc.readFileSync(process.argv[2], 'utf8');
const b = conc.readFileSync(process.argv[3], 'utf8');
conc.writeFileSync(process.argv[4], a + b);