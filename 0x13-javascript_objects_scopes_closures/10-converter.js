#!/usr/bin/node

exports.converter = function (base) {
  function elconveridor (n) {
    return n.toString(base);
  }
  return elconveridor;
};
