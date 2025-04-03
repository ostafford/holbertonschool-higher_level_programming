const headerElement = document.querySelector("header");
const uptHeader = document.getElementById("update_header");

uptHeader.addEventListener("click", function(){
    headerElement.textContent = "New Header!!!";
});