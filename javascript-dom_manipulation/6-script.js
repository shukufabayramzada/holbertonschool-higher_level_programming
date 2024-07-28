fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    let charElement = document.getElementById('character');
    charElement.textContent = data.name;
  })
  .catch((error) => {
    console.error('Error getting character name:', error);
  });
