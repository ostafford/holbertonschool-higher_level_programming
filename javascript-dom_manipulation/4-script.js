const addItem = document.getElementById("add_item");
const myList = document.querySelector("ul");

addItem.addEventListener("click", function(){
    const liElement = document.createElement("li");
    
    liElement.textContent = "Item";
    myList.append(liElement);
})