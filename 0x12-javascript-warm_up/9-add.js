#!/usr/bin/node

function add (e, f) {
  return e + f;
}

const e = parseInt(process.argv[2]);
const f = parseInt(process.argv[3]);

console.log(add(e, f));
