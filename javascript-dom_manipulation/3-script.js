const toggle = document.querySelector('#toggle_header');
toggle.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.className = header.className === 'green' ? 'red' : 'green';
})
