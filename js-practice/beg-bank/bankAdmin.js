var accountName = "rcrp";
var accountPass = "rcrp123";
var balance = 1000;
var accountNameIn = document.getElementById("accountNameIn").value;
var accountPassIn = document.getElementById("accountPassIn").value;
var amountIn = document.getElementById("amountWithdrawn").value;

function withdrawFunction() {
    if ((accountName == accountNameIn) && (accountPass == accountPassIn)) {
        if (amountIn > balance) {
            alert("Not enough funds!");
        } else {
            balance -= amountIn;
            document.getElementById("withdrawMessage").innerHTML = `You have succesfully withdrawn ${amountIn}. Your balance is now ${balance}. Have a nice day ${accountName}!`;
        };
    } else {
        alert("Access Denied! Name and Password Wrong.");
    };
};