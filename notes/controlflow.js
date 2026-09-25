/*
const minHeight = 3; 
let myHeight = prompt("how tall are you?")
let isTallEnough = myHeight >= minHeight;

if (isTallEnough){ 
    let message = "LFG you are: " + myHeight + " tall"
    print(message); 

} else {
    print("Drink some fucking milk");
}

print("Amusement parks are so fun!");
*/
/*
let numInstruments = prompt("How many instruments do you play?");
numInstruments = Number(numInstruments);

if(numInstruments > 1){
    print("Wow you are a multi-instrumentalist!");

} else if(numInstruments === 1){
    print("Good for you!")

} else if (){

} else {
    print("Do you even have a stable job?");


} else {
    print("it's all good music is so hard");
}

print("See ya later alligator!");
*/
/*
let randomNumber = Math.random(); // 0~1
randomNumber = randomNumber * 20; // 0~20
randomNumber = Math.floor(randomNumber);
randomNumber = randomNumber - 10; // -10 ~ 10
print(randomNumber);

if (randomNumber > 0){
    print("omg im melting!");

} else if (randomNumber < 0){
    print("It's so cold!")

} else {
    print("Whew!")
}
*/
/*
for(let i = 1; i <= 10; i++){
    print(i);
}
*/
/*
for(let i = 10; i > 0; i--){
    print(i);
}
print("KABOOM");
print("muahahaha");
*/
/*
let games = [
    "pokemon",
    "ghost of tsushima",
    "street fighter",
    "Balatro",
    "Rocket league",
    "GTA5",
    "Zelda",
    "League",
    "Beam.NG"
];

for(let index = 0; index < games.length; index++){
    print(games[index]);
}
*/
const numGreencardsAvailable = 20;
let numImmigrants = 120;

for(let p = 0; p < numImmigrants; p++){
    if (p < numGreencardsAvailable){
        print("Welcome!");

    } else {
        print("Please try again next year :)");
    }

}