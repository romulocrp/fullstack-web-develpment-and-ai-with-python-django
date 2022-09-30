var cars = ["Fiat", "Chevrolet", "Volkswagen", "Ford", "Pegeout", "Citroen"];
var text = "";

for (i = 0; i < cars.length; i++) {
    text += `${cars[i]} <br>`;
}

document.getElementById("carList").innerHTML = text;