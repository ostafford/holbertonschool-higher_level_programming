const listMovies = document.getElementById('list_movies')

fetch('https://swapi-api.hbtn.io/api/films/?format=json')

.then(function(responseObject){

    console.log(responseObject.status);
    return responseObject.json();
})

.then(function(parsedData){

    console.log(parsedData);

    const movies = parsedData.results;
    console.log(movies);

    movies.forEach(function(movie){
        const addMovie = document.createElement('li');
        console.log(addMovie);
        addMovie.textContent = movie.title;
        listMovies.append(addMovie);
    });



    // addMovie.textContent =  parsedData.results[0].title;
    // listMovies.append(addMovie)
})