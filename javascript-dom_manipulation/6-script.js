const characterElement = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')

.then(function(responseObject){

    console.log(responseObject.status);
    return responseObject.json();

})

.then(function(parsedData){

    console.log(parsedData);
    characterElement.textContent = parsedData.name;
})

.catch(function(error){
    
    console.log('Error', error);
});
