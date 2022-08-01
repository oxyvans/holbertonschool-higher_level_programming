#!/usr/bin/node

exports.callMeMoby = function (x, Func) {
  for (let i = 0; i < x; i++) {
    Func();
  }
};
