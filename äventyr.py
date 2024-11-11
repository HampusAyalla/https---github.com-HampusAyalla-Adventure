xp = 0
level = 0
health = 10
strenght = 50
inventory = []

import time
import random
print("Du är fast i en djungel. Du ser en öppning framför dig!")
val = input("Vill du gå igenom öppningen? --> ").lower()
if val == "ja":
    print("Du sprang in i ett monster. försök döda det!")
    time.sleep(2)
    print("Du dödade monstret och gick därför upp en level.")
    level = level+1
if val == "nej":
    print("Det börjar brinna bakom dig du måste springa igenom öppningen.")
    time.sleep(2)
    print("Du sprang in i ett monster. försök döda det!")
    time.sleep(2)
    print("Du dödade monstret och gick därför upp en level.")
    level = level+1

faith_list = ["panter","panter","panter","panter","panter","aligator","aligator","aligator","aligator","aligator","stammfolk","stammfolk","stammfolk","stammfolk","stammfolk","stone golem","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","fälla","fälla","fälla","fälla","fälla","fälla","fälla","fälla","shop"]
while True:
    direction = input("Vilket håll vill du gå åt? --> ").lower()
    left = faith_list[random.randint(0,4)]
    straight = faith_list[random.randint(0,4)]
    right = faith_list[random.randint(0,4)]
    if direction == "vänster":
        faith = left
    elif direction == "rakt fram":
        faith = straight
    elif direction == "höger":
        faith = right
    else:
        direction = input("Du måste svara vänster, höger eller rakt fram. --> ").lower

    if faith == "panter":
        print("Du stötte på en vild panther! Döda den!")
        enemy_strenght = random.randint(30,70)
        time.sleep(2)
        if strenght > enemy_strenght:
            print("Du dödade pantern, du fick 3 coins och",enemy_strenght,"xp")
            xp = xp+enemy_strenght
        if strenght < enemy_strenght:
            print("Du blev överveldigad av pantern och tappade 2 hp")
            health = health-2
    elif faith == "aligator":
        print("Du stötte på en aligator! Döda den!")
        enemy_strenght = random.randint(0,60)
        time.sleep(2)
        if strenght > enemy_strenght:
            time.sleep(2)
            print("Du tog kol på den där aligatorn, du fick 3 coins och", enemy_strenght, "xp")
        if strenght < enemy_strenght:
            print("Aligatorn tog ett stort bett av dig!")
            health = health-2
    elif faith == "stammfolk":
        print("Några stammfolk ringar in dig i ett hörn! Visa dem vad du kan!")
        enemy_strenght = random.randint(35,80)
        time.sleep(2)
        if strenght > enemy_strenght:
            print("Du visade de där stammfolket vad du går för, snyggt!")
        if strenght < enemy_strenght:
            print("De visade att vart skåpet ska stå! Känn på den du!")
            health = health-2
    elif faith == "fälla":
        print("Vänta vad är det som låter? du gick rakt in i en fälla!")
        health == health-1
        time.sleep(2)
        print("Du tappade 1 hp!")
