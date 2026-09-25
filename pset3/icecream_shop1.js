const priceOfIceCream = 3
let paymentRecieved = prompt("That'll be 3 dollars pls");
let isPaymentEnough = paymentRecieved >= priceOfIceCream;
if (isPaymentEnough){
    print("Thanks! Enjoy the ice cream!")
} else if (isPaymentEnough = paymentRecieved > priceOfIceCream) {
    print("Thanks! Your change is" + (paymentRecieved - priceOfIceCream))
} else {
    print("Not enough cash!")
}
