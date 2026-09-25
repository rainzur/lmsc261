const conesSoldPerHour = 14
const inventory = 169
for(let hour = 1; hour < 13; hour++){
print(conesSoldPerHour * hour + " sold at hour " + hour)
print(inventory - (conesSoldPerHour * hour) + " left")};