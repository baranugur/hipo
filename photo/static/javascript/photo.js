var searchButton = document.querySelector("#searchButton")
var searchInput = document.querySelector("input");
var results = document.querySelector("#results")

searchButton.addEventListener("click", function() {
    searchTag = searchInput.value
    // alert(searchTag)
})

function showImage(src) {
    var img = document.createElement("img");
    img.src = src;

    results.appendChild(img);
}