document.addEventListener('DOMContentLoaded', function () {
  const hello = document.querySelector('#hello')
  hello.textContent = '...Loading';

  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      hello.textContent = data.hello;
    })
    .catch((error) => {
      console.error('There was a problem with the fetch operation:', error);
    });

})
