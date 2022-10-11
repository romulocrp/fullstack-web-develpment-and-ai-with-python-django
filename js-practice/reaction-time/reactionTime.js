var formsList = ["circle", "triangule", "square"];
var colorList = ["red", "yellow", "green"];
var appendSeconds = document.getElementById("seconds");
var appendMiliseconds = document.getElementById("miliseconds");
var seconds = 00;
var miliseconds = 00;
var interval ;
var form ;

function randomForm() {
    return formsList[Math.floor(Math.random()*formsList.length)];
}

function randomNumber(min, max) {
    return (Math.floor(Math.random() * (max - min + 1) ) + min);
}

function start() {
    clearInterval(interval);
    interval = setInterval(startTimer, 10);
    form = randomForm()
    if (form == "triangule") {
        document.getElementById(form).style.borderBottomColor = colorList[Math.floor(Math.random()*colorList.length)];
        document.getElementById(form).style.marginLeft = randomNumber(0, 650)+"px";
        document.getElementById(form).style.marginTop = randomNumber(0, 300)+"px";
    } else {
        document.getElementById(form).style.backgroundColor = colorList[Math.floor(Math.random()*colorList.length)];
        document.getElementById(form).style.marginLeft = randomNumber(0, 650)+"px";
        document.getElementById(form).style.marginTop = randomNumber(0, 300)+"px";
    }
}

function stop() {
    clearInterval(interval);
    if (form == "triangule") {
        document.getElementById(form).style.borderBottomColor = "transparent";
        document.getElementById(form).style.marginLeft = 0+"px";
        document.getElementById(form).style.marginTop = 0+"px";
    } else {
        document.getElementById(form).style.backgroundColor = "transparent";
        document.getElementById(form).style.marginLeft = 0+"px";
        document.getElementById(form).style.marginTop = 0+"px";
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