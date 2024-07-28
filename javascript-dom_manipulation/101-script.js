document.addEventListener('DOMContentLoaded', function () {
  const translateButton = document.getElementById('btn_translate');
  const languageCodeSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  translateButton.addEventListener('click', function () {
    const languageCode = languageCodeSelect.value;

    if (languageCode) {
      const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          if (data && data.hello) {
            helloDiv.textContent = data.hello;
          } else {
            helloDiv.textContent = 'Translation not found';
          }
        })
        .catch((error) => {
          console.error('Error fetching translation:', error);
          helloDiv.textContent = 'Error fetching translation';
        });
    } else {
      helloDiv.textContent = 'Please select a language code';
    }
  });
});
