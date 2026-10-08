
/*
//function declaration
function greetInMandarin(isFeelingMean, nameToPrint){ // input
    let greeting = isFeelingMean ? "Gundan " : "Nihao ";
    print(greeting + nameToPrint);
}

greetInMandarin(false, "Bryan");
greetInMandarin(true, "Tiger");
*/
/*
function formatName(isEvil){
    let niceGreeting = "I'm so glad you're here ";
    let evilGreeting = "get the fuck outta here ";

    let greeting = isEvil ? evilGreeting : niceGreeting;
    let nameToGreet = "gustav";

    let formatted = greeting + nameToGreet;

    return formatted;
}

let hiGustav = formatName();
print(hiGustav + " :D")
*/
/*
function squareNumber(number) { //function declaration
        return number * number; //return is the output
}
// BEFORE function is CALLED, code is HYPOTHETICAL.
let num = squareNumber(5000);
print(num);
*/
/*
function getIsBaked(bakeDuration){
    let isBaked = bakeDuration > 10;
    return isBaked ? "Oh my godd" : "It's underbaked";
}

let isBreadBaked = getIsBaked(5);
print(isBreadBaked);
*/

/*
function getSliceAngle(numAttendee){
    if (numAttendee === 0) return 0; 

    let wholeCake = Math.PI * 2;
    let cakeDivision = wholeCake / numAttendee;
    return cakeDivision;
}

let slice = getSliceAngle(0);
print(slice);
*/
const squre = (num) => {
    return num * num;
}