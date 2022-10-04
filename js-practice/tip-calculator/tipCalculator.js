function tipCalculation() {
    var bill = document.getElementById("totalBill").value;
    var percSelect = document.getElementById("tipPercentage").value;
    var split = document.getElementById("peopleSplit").value;

    if (bill == ""){
        document.getElementById("tipAmountResult").innerHTML = "<b>Please insert<br>the bill amount.";
    } else if (bill <= 0)  {
        document.getElementById("tipAmountResult").innerHTML = "<b>Bill must be<br>higher than 0!</b>";
    } else if (split == "") {
        document.getElementById("tipAmountResult").innerHTML = "<b>Please insert the<br>number of people.";
    } else if (split == 0){
        var tip = (bill * percSelect);
        document.getElementById("tipAmountResult").innerHTML = `<b>Tip Amount:<br>${Math.round(tip)}</b>`;
    } else {
        var tip = ((bill * percSelect)/split);
        document.getElementById("tipAmountResult").innerHTML = `<b>Tip Amount:<br>${Math.round(tip)}<br>each</b>`;
    }
}

