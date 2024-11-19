import time
import random
open_inventory = False

class player:
    strength = 50
    xp = 0
    level = 0
    health = 10
    inventory = []

class items:
    Svärd = 4
    Apa = 4
    Ingefärsshot = 4
    Rustning = 4
    Bandage = 4

item_list = ["ett svärd", "en apa", "ett ingefärsshot", "en rustning", "ett bandage","en fälla"]
trap_list = ["damage trap", "stealing trap"]

#Boss fight för slutet

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

#LevelSystem

if player.xp >= 500:
    player.level = 10
    print("Du är nu level 10 Snyggt jobbat!")
elif player.xp >= 380:
    player.level = 9
    print("Du är nu level 9 snyggt jobbat!")
elif player.xp >= 300:
    player.level = 8
    print("Du är nu level 8 snyggt jobbat!")
elif player.xp >= 230:
    player.level = 7
    print("Du är nu level 7 snyggt jobbat!")
elif player.xp >= 170:
    player.level = 6
    print("Du är nu level 6 snyggt jobbat!")
elif player.xp >= 120:
    player.level = 5
    print("Du är nu level 5 snyggt jobbat!")
elif player.xp >= 80:
    player.level = 4
    print("Du är nu level 4 snyggt jobbat!")
elif player.xp >= 50:
    player.level = 3
    print("Du är nu level 3 snyggt jobbat!")
elif player.xp >= 30:
    player.level = 2
    print("Du är nu level 2 snyggt jobbat!")    

# Inledning/tutorial 

print("Du är fast i en djungel. Du ser en öppning framför dig!")
val = input("Vill du gå igenom öppningen? --> ").lower()
if val == "ja":
    print("Du sprang in i ett monster. försök döda det!")
    time.sleep(3)
    print("Du dödade monstret och gick därför upp en level.")
    print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
    player.level = player.level+1
if val == "nej":
    print("Det börjar brinna bakom dig du måste springa igenom öppningen.")
    time.sleep(3)
    print("Du sprang in i ett monster. försök döda det!")
    time.sleep(3)
    print("Du dödade monstret och gick därför upp en level.")
    time.sleep(2)
    print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
    player.level = player.level+1

öppningar = ["Du ser ytterligare tre öppningar framför dig vilket håll vill du gå åt, höger, vänster eller rakt fram? Du kan också skriva i för att öppna förrådet--> ","Du ser en grotta till vänster, ett tempel till höger och ett dimmigt vattenfall rakt fram. Vilket håll vill du gå åt, höger, vänster eller rakt fram? Du kan också skriva i för att öppna förrådet --> " ]
faith_list = ["kista","panter","panter","panter","panter","panter","aligator","aligator","aligator","aligator","aligator","stammfolk","stammfolk","stammfolk","stammfolk","stammfolk","stone golem","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","fälla","fälla","fälla","fälla","fälla","fälla","fälla","fälla","shop"]

#Gameloop

while True:
    if player.health <= 0:
        print("Vad händer, det blir ljust, du förblöder! Du dog!")
        break
    elif player.level >= 10:
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
    
    #Öde och inventory
    time.sleep(3)
    direction = input(öppningar[random.randint(0,len(öppningar)-1)]).lower()
    left = faith_list[random.randint(0,1)]
    straight = faith_list[random.randint(0,1)]
    right = faith_list[random.randint(-5,len(faith_list)-1)]
    while True:
        if direction == "vänster":
            faith = left
            break
        elif direction == "rakt fram":
            faith = straight
            break
        elif direction == "höger":
            faith = right
            break
        elif direction == "i":
            open_inventory = True
        else:
            direction = input("Du måste svara vänster, höger, rakt fram eller i. --> ").lower()

        while open_inventory == True:
            if len(player.inventory)> 0:
                print("I ditt förråd har du:")
                print(player.inventory)
                direction = input("Skriv vilket håll du vill gå åt när du har kollat klart")
                open_inventory = False
            elif len(player.inventory) == 0:
                print("Ditt förråd är tomt")
                direction = input("Skriv vilket håll du vill gå åt när du har kollat klart --> ")
                open_inventory = False
        
    #Fiender, Kistor, fällor och inventory
    if faith == "panter":
        print("Du stötte på en vild panther! Döda den!")
        enemy_strength = random.randint(30,70)
        time.sleep(2)
        if player.strength > enemy_strength:
            print("Du dödade pantern, du fick 3 guld mynt och",enemy_strength,"xp")
            player.xp = player.xp+enemy_strength
        elif player.strength < enemy_strength:
            print("Du blev överväldigad av pantern och tappade 2 Hp")
            player.health = player.health-2
            print("Nu har du bara",player.health,"Hp kvar!")
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
            player.health = player.health-2
            print("Nu har du bara",player.health,"Hp kvar!") 
        elif player.strength == enemy_strength:
            print("Du hopppade på alligatorns huvud och kom förbi oskadd.")
    elif faith == "stammfolk":
        print("Några stammfolk ringar in dig i ett hörn! Visa dem vad du kan!")
        enemy_strength = random.randint(35,80)
        time.sleep(2)
        if player.strength > enemy_strength:
            print("Du visade de där stammfolket vad du går för, snyggt!","du fick 5 guld mynt och", enemy_strength, "xp" )
        elif player.strength < enemy_strength:
            print("De visade vart skåpet ska stå istället! Känn på den du! du tappade 2 Hp")
            player.health = player.health-2
            print("Nu har du bara",player.health,"Hp kvar!")
        elif player.strength == enemy_strength:
            print("Visar sig att de var chill like that, ni skakade hand på det och du går vidare!")
    elif faith == "fälla":
        print("Vänta vad är det som låter?")
        time.sleep(4)
        print("Du gick rakt in i en fälla!")
        player.health = player.health-1
        time.sleep(2)
        print("Du tappade 1 hp!")
        print("Nu har du bara",player.health,"Hp kvar!")
    elif faith == "kista":
        innehåll = item_list[random.randint(0,len(item_list)-1)]
        print(innehåll)
        öppna = input("Du hittade en kista vill du öpnna den eller gå vidare? Svara ja om du vill öppna den och nej om du inte vill gå vidare. --> ").lower()
        if öppna == "ja":
            print("Du hittade", innehåll, "i kistan!")
            if innehåll == "en fälla":
                trap = trap_list[0,len(trap_list)-1]
                if trap == "damage trap" or len(player.inventory) == 0:
                    print("Kistan sprängdes och du tappade ett Hp")
                    player.health = player.health-1
                    print("Du har nu bara",player.health, "Hp kvar!")
                elif trap == "stealing trap":
                    print("En talande orm sa åt dig att ge honom ett föremål annars äter han upp dig!")
                    snott_föremål = player.inventory[random.randint(0,len(player.inventory)-1)]
                    print("Ormen slinker iväg efter du gav bort", snott_föremål,"till honom")
            elif len(player.inventory) < 5:
                print("Föremålet har lagts in i ditt förråd")
                player.inventory.append(innehåll)
            elif len(player.inventory) == 5:
                print("Ditt förråd är fullt!")
                byta = input("Vill du byta ut föremållet med någonting annat i ditt förråd? --> ").lower()
                if byta == "ja":
                    försvinna = input("Skriv platsen i ditt förråd som föremålet du vill byta ut finns på. Ett tal mellan 1-5 --> ")
                    if försvinna == "1" or försvinna == "2" or försvinna == "3" or försvinna == "4" or försvinna == "5":
                        försvinna = int(försvinna)-1
                        meddelande = "Är du säker att du vill byta ut" + innehåll + "mot" + player.inventory[försvinna] + "? --> "
                        försäkring = input(meddelande).lower()






       
    
        

