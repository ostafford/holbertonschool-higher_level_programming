const headerElement = document.querySelector('header');
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', function(){
    headerElement.classList.add('red');
});