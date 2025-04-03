const headerElement = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener("click", function(){

    if (headerElement.classList.contains('green')){
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    } else {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    }
});