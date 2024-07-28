fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    let movieElement = document.getElementById('list_movies');

    data.results.forEach((movie) => {
      let liElement = document.createElement('li');
      liElement.textContent = movie.title;
      movieElement.appendChild(liElement);
    });
  })
  .catch((error) => {
    console.error('Error getting movies:', error);
  });
