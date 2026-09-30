const priceOfIceCream = 3
let paymentRecieved = prompt("That'll be 3 dollars pls");
let isPaymentEnough = paymentRecieved >= priceOfIceCream;
let overpaid = paymentRecieved > priceOfIceCream;
let change = paymentRecieved - priceOfIceCream;

if (isPaymentEnough){
    print("Thanks! Enjoy the ice cream!")
} else {
    print("Not enough cash!")
}

if (overpaid){
    print("your change is " + "$" + change)
}