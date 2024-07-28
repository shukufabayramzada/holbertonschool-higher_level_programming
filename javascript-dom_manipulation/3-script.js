let toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
  let headerElement = document.querySelector('header');
  if (headerElement.classList.contains('red')) {
    headerElement.classList.toggle('green');
  } else if (headerElement.classList.contains('green')) {
    headerElement.classList.toggle('red');
  }
});
