var shapesList = ["circle", "triangule", "square"];
var colorList = ["red", "yellow", "green"];
var appendSeconds = document.getElementById("seconds");
var appendMiliseconds = document.getElementById("miliseconds");
var seconds = 00;
var miliseconds = 00;
var interval ;
var shape ;

function randomShape() {
    return shapesList[Math.floor(Math.random()*shapesList.length)];
}

function randomNumber(min, max) {
    return (Math.floor(Math.random() * (max - min + 1) ) + min);
}

function start() {
    clearInterval(interval);
    interval = setInterval(startTimer, 10);
    shape = randomShape()
    if (shape == "triangule") {
        document.getElementById(shape).style.borderBottomColor = colorList[Math.floor(Math.random()*colorList.length)];
        document.getElementById(shape).style.marginLeft = randomNumber(0, 650)+"px";
        document.getElementById(shape).style.marginTop = randomNumber(0, 300)+"px";
    } else {
        document.getElementById(shape).style.backgroundColor = colorList[Math.floor(Math.random()*colorList.length)];
        document.getElementById(shape).style.marginLeft = randomNumber(0, 650)+"px";
        document.getElementById(shape).style.marginTop = randomNumber(0, 300)+"px";
    }
}

function stop() {
    clearInterval(interval);
    if (shape == "triangule") {
        document.getElementById(shape).style.borderBottomColor = "transparent";
        document.getElementById(shape).style.marginLeft = 0+"px";
        document.getElementById(shape).style.marginTop = 0+"px";
    } else {
        document.getElementById(shape).style.backgroundColor = "transparent";
        document.getElementById(shape).style.marginLeft = 0+"px";
        document.getElementById(shape).style.marginTop = 0+"px";
    }
}

function reset(){
    clearInterval(interval);
    miliseconds = 00;
    seconds = 00;
    appendMiliseconds.innerHTML = "0" + miliseconds;
    appendSeconds.innerHTML = "0" + seconds;
}

function startTimer() {
    
    miliseconds++;

    if (miliseconds <= 9) {
        appendMiliseconds.innerHTML = "0" + miliseconds;
    }

    if (miliseconds > 9) {
        appendMiliseconds.innerHTML = miliseconds;
    }

    if (miliseconds > 99) {
        seconds++
        appendSeconds.innerHTML = "0" + seconds;
        miliseconds = 0;
        appendMiliseconds.innerHTML = "0" + miliseconds;
    }

    if (seconds > 9) {
        appendSeconds.innerHTML = seconds;
    }
}