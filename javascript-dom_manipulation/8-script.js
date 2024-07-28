document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      let helloElement = document.getElementById('hello');
      let dataHello = data.hello;
      helloElement.textContent = dataHello;
    })

    .catch((error) => {
      console.error('Error getting the hello:', error);
    });
});
