let loading = document.getElementById("loading");
console.log(loading);
let restaurants = document.getElementById("restaurants");
console.log(restaurants);
let user = document.getElementById("user");
let keyword = document.getElementsByClassName("likes")[0];



fetch(`/restaurants/${user.innerText}/${keyword.innerText}`)
.then(res => res.json())
.then((res) => {
    console.log(res);
    for (var i = 0; i < res.results.length; i++) {
        var col = document.createElement("div");
        col.classList.add("col");
        restaurants.appendChild(col);
        //Create Images
        var img = document.createElement("img");
        img.classList.add("restaurant_thumbnail");
        img.classList.add("image-fluid");
        img.src = res.results[i].photo;
        col.appendChild(img);
        var name = document.createElement("h1");
        name.innerText = res.results[i].result.name;
        col.appendChild(name);
        loading.remove();
        
    }
})
.catch((error) => {
    console.error(error);
    
})