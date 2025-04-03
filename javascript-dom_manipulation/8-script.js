document.addEventListener('DOMContentLoaded', function(){
const helloId = document.getElementById('hello')

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')

.then(function(responseObject){

    console.log(responseObject.status);
    return responseObject.json();
    })

.then(function(parsedData){
    
    console.log(parsedData);
    helloId.textContent = parsedData.hello;
    });
});