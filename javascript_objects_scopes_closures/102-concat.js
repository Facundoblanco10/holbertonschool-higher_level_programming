#!/usr/bin/node

const fs = require('fs');

const file1 = './' + process.argv[2];
const file2 = './' + process.argv[3];
const file3 = './' + process.argv[4];

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.log(err);
  } else {
    fs.readFile(file2, 'utf8', (err, data2) => {
      if (err) {
        console.log(err);
      } else {
        const data = data1 + '\n' + data2;
        fs.writeFile(file3, data, (err) => {
          if (err) {
            console.log(err);
          }
        });
      }
    });
  }
});
