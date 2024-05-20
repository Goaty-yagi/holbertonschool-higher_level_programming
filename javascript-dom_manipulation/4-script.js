const add = document.querySelector('#add_item');
add.addEventListener('click', () => {
  const myList = document.querySelector('ul');
  const li = document.createElement('li');
  li.textContent = 'Item';
  myList.appendChild(li);
})
