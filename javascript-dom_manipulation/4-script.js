#!/usr/bin/node

const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addItemButton.addEventListener('click', function () {
  const newListItem = document.createElement('li');
  newListItem.innerHTML = 'Item';
  myList.appendChild(newListItem);
});
