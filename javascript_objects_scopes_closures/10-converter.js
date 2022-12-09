#!/usr/bin/node

exports.converter = function (base) {
  return (
    function (num) {
      const result = parseInt(num, 10).toString(base);
      return result;
    }
  );
};
