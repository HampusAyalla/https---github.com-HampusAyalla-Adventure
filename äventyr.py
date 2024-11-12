import time
import random

class player:
    strength = 50
    xp = 500
    level = 0
    health = 104
    inventory = []

class items:
    Svärd = 
    Apa =
    Ingefärashot = 
    Rustning = 
    Bandage = 


def boss_fight():
    target_clicks = 45
    time_limit = 15 
    clicks = 0
    
    start_time = time.time()
    
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Stenjätten tog dig i sin hand, förde dig mot sin mun och bet av ditt huvud!")
            break
        
        input()
        clicks += 1
        print("Klick:",clicks,"/",target_clicks)
        
        if clicks >= target_clicks:
            print("Snyggt! Du dödade stenjätten!")
            return

if player.xp >= 500:
    level = 10
    print("Du är nu level 10 Snyggt jobbat!")
elif player.xp >= 380:
    level = 9
    print("Du är nu level 9 snyggt jobbat!")
elif player.xp >= 300:
    level = 8
    print("Du är nu level 8 snyggt jobbat!")
elif player.xp >= 230:
    level = 7
    print("Du är nu level 7 snyggt jobbat!")
elif player.xp >= 170:
    level = 6
    print("Du är nu level 6 snyggt jobbat!")
elif player.xp >= 120:
    level = 5
    print("Du är nu level 5 snyggt jobbat!")
elif player.xp >= 80:
    level = 4
    print("Du är nu level 4 snyggt jobbat!")
elif player.xp >= 50:
    level = 3
    print("Du är nu level 3 snyggt jobbat!")
elif player.xp >= 30:
    level = 2
    print("Du är nu level 2 snyggt jobbat!")    

time.sleep(5)
print("Du är fast i en djungel. Du ser en öppning framför dig!")
val = input("Vill du gå igenom öppningen? --> ").lower()
if val == "ja":
    print("Du sprang in i ett monster. försök döda det!")
    time.sleep(3)
    print("Du dödade monstret och gick därför upp en level.")
    print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
    level = level+1
if val == "nej":
    print("Det börjar brinna bakom dig du måste springa igenom öppningen.")
    time.sleep(3)
    print("Du sprang in i ett monster. försök döda det!")
    time.sleep(3)
    print("Du dödade monstret och gick därför upp en level.")
    time.sleep(2)
    print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
    level = level+1

öppningar = ["Du ser ytterligare tre öppningar framför dig vilket håll vill du gå åt, höger, vänster eller rakt fram? Du kan också skriva i för att öppna förrådet--> ","Du ser en grotta till vänster, ett tempel till höger och ett dimmigt vattenfall rakt fram. Vilket håll vill du gå åt, höger, vänster eller rakt fram? Du kan också skriva i för att öppna förrådet --> " ]
faith_list = ["panter","panter","panter","panter","panter","aligator","aligator","aligator","aligator","aligator","stammfolk","stammfolk","stammfolk","stammfolk","stammfolk","stone golem","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","fälla","fälla","fälla","fälla","fälla","fälla","fälla","fälla","shop"]

while True:
    if health <= 0:
        print("Vad händer, det blir ljust, du förblöder! Du dog!")
        break
    elif level >= 10:
        print("Du börjar se ljuset, Du ser en sista utväg. Du springer in mellan två stenmurar, du känner en hård smäll på kinden. Du kollar upp och ser en stor stenjätte.")
        time.sleep(4)
        print("Du måste döda jätten!")
        time.sleep(2)
        print("Slå honom genom att trycka på enterknappen.")
        time.sleep(3)
        print("Fighten börjar om 5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1!")
        boss_fight()
        break
    
    time.sleep(3)
    direction = input(öppningar[random.randint(0,1)]).lower()
    left = faith_list[random.randint(0,4)]
    straight = faith_list[random.randint(0,4)]
    right = faith_list[random.randint(0,4)]
    if direction == "vänster":
        faith = left
    elif direction == "rakt fram":
        faith = straight
    elif direction == "höger":
        faith = right
    elif direction == "i":
        open_inventory = True
    else:
        direction = input("Du måste svara vänster, höger, rakt fram eller i. --> ").lower

    while open_inventory == True:
        print("1.")

    if faith == "panter":
        print("Du stötte på en vild panther! Döda den!")
        enemy_strength = random.randint(30,70)
        time.sleep(2)
        if player.strength > enemy_strength:
            print("Du dödade pantern, du fick 3 guld mynt och",enemy_strength,"xp")
            xp = xp+enemy_strength
        elif player.strength < enemy_strength:
            print("Du blev överväldigad av pantern och tappade 2 Hp")
            health = health-2
            print("Nu har du bara",health,"Hp kvar!")
        elif player.strength == enemy_strength:
            print("Du tog ut en köttbit ur fickan och lurade bort pantern!")
    elif faith == "aligator":
        print("Du stötte på en aligator! Döda den!")
        enemy_strength = random.randint(0,60)
        time.sleep(2)
        if player.strength > enemy_strength:
            time.sleep(2)
            print("Du tog kol på den där aligatorn, du fick 1 guld mynt och", enemy_strength, "xp")
        elif player.strength < enemy_strength:
            print("Aligatorn tog ett stort bett av dig! Du tappade 2 Hp")
            health = health-2
            print("Nu har du bara",health,"Hp kvar!") 
        elif player.strength == enemy_strength:
            print("Du hopppade på alligatorns huvud och kom förbi oskad.")
    elif faith == "stammfolk":
        print("Några stammfolk ringar in dig i ett hörn! Visa dem vad du kan!")
        enemy_strength = random.randint(35,80)
        time.sleep(2)
        if player.strength > enemy_strength:
            print("Du visade de där stammfolket vad du går för, snyggt!","du fick 5 guld mynt och", enemy_strength, "xp" )
        elif player.strength < enemy_strength:
            print("De visade att vart skåpet ska stå! Känn på den du! du tappade 2 Hp")
            health = health-2
            print("Nu har du bara",health,"Hp kvar!")
        elif player.strength == enemy_strength:
            print("Visar sig att de var chill like that, ni skakade hand på det och du går vidare!")
    elif faith == "fälla":
        print("Vänta vad är det som låter?")
        time.sleep(4)
        print("Du gick rakt in i en fälla!")
        health = health-1
        time.sleep(2)
        print("Du tappade 1 hp!")
        print("Nu har du bara",health,"Hp kvar!")
        