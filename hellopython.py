DRIVING_AGE = 10
age = input("how old are u")
age = int(age)
is_old_enough = age > DRIVING_AGE

if (is_old_enough):
    print("don't forget to drink")
else: 
    print("go back home")


body_count = 10

print("how many did u 'kil' today")
for b in range(body_count):
    print("I 'killed' " + str(b) + " people!")
    print(f"I killed {b} people!") #template literal

for i in range(4, 10):
    print(i)

i = 0
while(i < 100):
    print(i)
    i += 1

places_to_hide = ["inside the closet",
                  "behind the fridge",
                  "under the bed",
                  "gender-neutral bathroom",
                  "in the attic"]

location = "under the bed"
for p in places_to_hide:
    print("----------")
    print(p)
    if (p == location):
        print("i found you!!!")
        continue

    print("lets keep looking")
    print("I wonder where he/she could be")
    print("eehehehehehehh")

    function addNumbers(a, b){
        let sum = a + b;
        return sum;
    }

    def add_numbers(a, b): #def instead of function
        return a + b

my_number = add_numbers(8, 2)
print(my_number)
def rescue_mission():
    # rodents
    rodents = ["rat",
            "mouse",
                "bedbugs",
                "raccoons",
                "squirrels",
                "termite",
                "thomas"]

    is_bob_rescued = None

    for r in rodents:
        print(f"ewww theres a {r}!!")

        if (r == "thomas"):
            print("you're not a rodent thomas!")
            print("you're rescued")
            is_bob_rescued = True
            break
is_rescue_successful = rescue_mission()
print(is_rescue_successful)

if (is_rescue_successful):
    print("eat a bullet bob")
else:
    print("I guess I have one less chore to do")

worst_dating_spot = {}

worst_dating_spot["matt"] = "160 Lobby"
worst_dating_spot["rain"] = "VR chat lobby"
worst_dating_spot["max"] = "twin towers"
worst_dating_spot["amir"] = "garage"

print(worst_dating_spot.get("min", "key not found")) #insntead of giving errro, will receive value "none" uninit. value. Defensive programming.

worst_halloween_costume = {} # homewokr
    while(i < 4):
    name = input("whats ur name? ")
    costume = input("whats ur worst costume? ")
    
    worst_halloween_costume[name] = costume
    i+= 1

    favorite_games = {
        "bryan" : "minesweeper",
        "luke" : "Cyberpunk 2077",
        "naoki" : "FF 7",
        "amir" : "NBA 2k",
        "gustav" : "ghost of tsushima"
    }

    just_keys = favorite_games.keys()
    print(just_keys)

    just_values = favorite_games.values()
    print(just_values)

    both_items = favorite_games.items()

import json

data_json = open("groceries.json") # NOT dict
data_dict = json.load(data_json) # dict. MUST DO BOTH
print(data_json)


little_secret = [
    {
        "name" : "takuma",
        "secret" : "peed his pants on the commuter rail",
        "dark_level" : 4
    },
    {
        "name" : "matt",
        "secret" : "stole a straw"
        "dark_level" : 1
    }
    {
        "name" : "max", 
        "secret" : "cannibal",
        "dark_level" : 8
    }
]

for secret in little_secret:
    secret_holders_name = secret.get('name')
    print(secret_holders_name)

    secret_content = secret.get("secret")
    print(secret_content)

    import json

    data_json = open("groceries.json") #NOT dict # homework
    data_dict = json.load(data_json)
        print(data_dict)


grocery_list = data_dict

category_sel = "fruits"

    for item in grocery_list:
    item_name = item.get("name")
    item_category = item.get("category")
    item_expire = item.get("expire")
        print(item_name)

    isFruit = item_category == "fruits"
    if(isFruit):
        print(item_name)

close_to_expire = item_expire <= 5
if(close_to_expire):
    print(f"the item {item_name} is going to expire in {item_expire}")