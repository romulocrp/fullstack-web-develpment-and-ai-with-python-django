const colorList = ["Black", "Navy", "DarkBlue", "MediumBlue", "Blue", "DarkGreen", "Green", "Teal", "DarkCyan", 
"DeepSkyBlue", "DarkTurquoise", "MediumSpringGreen", "Lime", "SpringGreen", "Aqua", "Cyan", "MidnightBlue", 
"DodgerBlue", "LightSeaGreen", "ForestGreen", "SeaGreen", "DarkSlateGray", "DarkSlateGrey", "LimeGreen", 
"MediumSeaGreen", "Turquoise", "RoyalBlue", "SteelBlue", "DarkSlateBlue", "MediumTurquoise", "Indigo", 
"DarkOliveGreen", "CadetBlue", "CornflowerBlue", "RebeccaPurple", "MediumAquaMarine", "DimGray", "DimGrey", 
"SlateBlue", "OliveDrab", "SlateGray", "SlateGrey", "LightSlateGray", "LightSlateGrey", "MediumSlateBlue", 
"LawnGreen", "Chartreuse", "Aquamarine", "Maroon", "Purple", "Olive", "Gray", "Grey", "SkyBlue", 
"LightSkyBlue", "BlueViolet", "DarkRed", "DarkMagenta", "SaddleBrown", "DarkSeaGreen", "LightGreen", 
"MediumPurple", "DarkViolet", "PaleGreen", "DarkOrchid", "YellowGreen", "Sienna", "Brown", "DarkGray", 
"DarkGrey", "LightBlue","GreenYellow", "PaleTurquoise", "LightSteelBlue", "PowderBlue", "FireBrick", 
"DarkGoldenRod", "MediumOrchid", "RosyBrown", "DarkKhaki", "Silver", "MediumVioletRed", "IndianRed", 
"Peru", "Chocolate", "Tan", "LightGray", "LightGrey", "Thistle", "Orchid", "GoldenRod", "PaleVioletRed", 
"Crimson", "Gainsboro", "Plum", "BurlyWood", "LightCyan", "Lavender", "DarkSalmon", "Violet", "PaleGoldenRod", 
"LightCoral", "Khaki", "AliceBlue", "HoneyDew", "Azure", "SandyBrown", "Wheat", "Beige", "WhiteSmoke", "MintCream", 
"GhostWhite", "Salmon", "AntiqueWhite", "Linen", "LightGoldenRodYellow", "OldLace", "Red", "Fuchsia", "Magenta", 
"DeepPink", "OrangeRed", "Tomato", "HotPink", "Coral", "DarkOrange", "LightSalmon", "Orange", "LightPink", "Pink", 
"Gold", "PeachPuff", "NavajoWhite", "Moccasin", "Bisque", "MistyRose", "BlanchedAlmond", "PapayaWhip", 
"LavenderBlush", "SeaShell", "Cornsilk", "LemonChiffon", "FloralWhite", "Snow", "Yellow", "LightYellow", "Ivory", 
"White"];

function randomNumber(min, max) {
    return (Math.floor(Math.random() * (max - min + 1) ) + min);
}

function boxOneChange() {
    document.getElementById("boxOne").style.backgroundColor = colorList[Math.floor(Math.random()*colorList.length)];
    document.getElementById("boxOne").style.color = colorList[Math.floor(Math.random()*colorList.length)];
    document.getElementById("boxOne").style.marginLeft = randomNumber(0, 650)+"px";
    document.getElementById("boxOne").style.marginTop = randomNumber(0, 450)+"px";
    document.body.style.backgroundColor = colorList[Math.floor(Math.random()*colorList.length)];
}

function boxTwoChange() {
    document.getElementById("boxTwo").style.backgroundColor = colorList[Math.floor(Math.random()*colorList.length)];
    document.getElementById("boxTwo").style.color = colorList[Math.floor(Math.random()*colorList.length)];
    document.getElementById("boxTwo").style.marginLeft = randomNumber(0, 650)+"px";
    document.getElementById("boxTwo").style.marginTop = randomNumber(0, 450)+"px";
    document.body.style.backgroundColor = colorList[Math.floor(Math.random()*colorList.length)];
}

