var time = new Date().getHours();

if (time > 7 & time <= 12) {
    document.getElementById("greeting").innerHTML = "Good Morning!";
    document.body.style.backgroundColor = "lightyellow";
    document.getElementById("image").src = "images/day.jpg";
} else if (time > 12 & time <= 19){
    document.getElementById("greeting").innerHTML = "Good Afternoon!";
    document.body.style.backgroundColor = "orange";
    document.getElementById("image").src = "images/afternoon.jpg";
} else {
    document.getElementById("greeting").innerHTML = "Good Night!";
    document.body.style.backgroundColor = "lightblue";
    document.getElementById("image").src = "images/night.jpeg";
}