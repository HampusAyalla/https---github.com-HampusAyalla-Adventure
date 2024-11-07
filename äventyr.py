Level = 0
Health = 10
Strenght = 50

import random
print("Du är fast i en djungel. Du ser tre öppningar framför dig en till vänster en till höger och en rakt fram.")
direction = input("Vilket håll vill du gå åt? --> ").lower()

faith_list = ["panther","panther","panther","panther","panther","aligator","aligator","aligator","aligator","aligator","tribe member","tribe member","tribe member","tribe member","tribe member","stone golem","chest","chest","chest","chest","chest","chest","chest","chest","chest","chest","chest","chest","trap","trap","trap","trap","trap","trap","trap","trap","shop"]
left = faith_list[random.randint(0,36)]
straight = faith_list[random.randint(0,36)]
right = faith_list[random.randint(0,36)]
if direction == "vänster":
    faith = left
elif direction == "rakt fram":
    faith = straight
elif direction == "höger":
    faith = right
else:
    direction = input("Du måste svara vänster, höger eller rakt fram. --> ").lower
