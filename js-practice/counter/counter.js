var count = 0;

const colors = ["#ffffff", "#FFFFCC", "#FFFF99", "#FFFF66", "#FFFF33", "#FFFF00", "#CCCC00", "#999900", "#666600", "#333300"]

function plusButton(){
    count += 1;
    document.getElementById("valuePara").innerHTML = ("Count: " + count);
    document.getElementById("backColor").style.backgroundColor = colors[count-1]
}


function lessOne(){
    count -= 1;
    document.getElementById("valuePara").innerHTML = "Count: " + count;
    document.getElementById("backColor").style.backgroundColor = colors[count-1]
}