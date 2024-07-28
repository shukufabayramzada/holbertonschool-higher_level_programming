let updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', function () {
  let headerElement = document.querySelector('header');
  headerElement.innerText = 'New Header!!!';
});
