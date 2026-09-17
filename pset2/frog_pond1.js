let numFrogs = prompt("How many frogs are about to jump in?");
const maxFrogCapacity = 15;
let isPondOverCapacity = numFrogs <= maxFrogCapacity;
let messageToPrint = isPondOverCapacity ? "Come on in!" : "It's too crowded!";
print(messageToPrint);