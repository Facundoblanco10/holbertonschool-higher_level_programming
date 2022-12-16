#!/usr/bin/node

const header = document.getElementsByTagName('header');
const toggleHeader = document.getElementById('toggle_header').onclick = function () {
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  };

