const listMovies = document.querySelector('#list_movies')
listMovies.textContent = '...Loading'

const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then((data) => {
    listMovies.textContent = ''
    for (const movie of data.results) {
      const list = document.createElement('li');
      list.textContent = movie.title;
      listMovies.appendChild(list);
    }
  })
  .catch((error) => {
    console.error('There was a problem with the fetch operation:', error);
  });
