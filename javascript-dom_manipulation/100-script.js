document.addEventListener('DOMContentLoaded', function () {
  const addItemButton = document.getElementById('add_item');
  const removeItemButton = document.getElementById('remove_item');
  const clearListButton = document.getElementById('clear_list');
  const myList = document.querySelector('.my_list');

  addItemButton.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  removeItemButton.addEventListener('click', function () {
    if (myList.lastChild) {
      myList.removeChild(myList.lastChild);
    }
  });

  clearListButton.addEventListener('click', function () {
    while (myList.firstChild) {
      myList.removeChild(myList.firstChild);
    }
  });
});
