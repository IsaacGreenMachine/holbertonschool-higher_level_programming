#!/usr/bin/node
exports.converter = function (base) {
  return function (secondBase) {
    return parseInt(secondBase).toString(base);
  };
};
