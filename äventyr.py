#Te23A, Hampus Melin Österlind, Hannes Park Brandberg och Jacob Norsell.

import time
import random
open_inventory = False
rustning_in_use = False
sword_in_use = False

class player:
    strength = 50
    xp = 0
    level = 0
    health = 10
    inventory = []

class item:
    svärd = player.strength+15
    apa = 4
    adrenalineshot = player.health+1
    rustning = 1
    bandage = player.health+2


item_list = ["en fälla","en apa", "en adrenalinshot", "en rustning", "ett bandage","ett svärd"]
trap_list = ["stealing trap","damage trap"]

#Level system
level_gränser = [30, 60, 100, 150, 210, 280, 360, 450, 600, 0]
def vilken_level(xp):
    for i in range(0,len(level_gränser)-1):
        if xp >= level_gränser[i]:
            player.level = i+2
    return player.level

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
faith_list = ["kista","panter","panter","panter","panter","panter","alligator","alligator","alligator","alligator","alligator","stammfolk","stammfolk","stammfolk","stammfolk","stammfolk","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","kista","fälla","fälla","fälla","fälla","fälla","fälla","fälla","fälla"]

#Gameloop

while True:
    if player.health <= 0:
        print("Vad händer, det blir ljust, du förblöder! Du dog!")
        break
    elif player.level == 10:
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
    else:
        gamla_level = player.level
        ny_level = vilken_level(player.xp)
        if ny_level > gamla_level:
            print("Du gick upp i level", ny_level,"! Snyggt jobbat!")
            player.level = ny_level 
        

        #Öde och inventory

        time.sleep(3)
        direction = input(öppningar[random.randint(0,len(öppningar)-1)]).lower()
        left = faith_list[random.randint(0,len(faith_list)-1)]
        straight = faith_list[random.randint(0,len(faith_list)-1)]
        right = faith_list[random.randint(0,len(faith_list)-1)]
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
                while True:
                    if len(player.inventory) == 0:
                        print("Ditt förråd är tomt")
                        break
                    elif len(player.inventory)> 0:
                        print("I ditt förråd har du:")
                        print(player.inventory)
                        interact = input("Vill du använda någonting i ditt förråd? --> ").lower()
                        while True:
                            if interact == "ja":
                                do = input("Skriv platsen som ditt föremål ligger i förrådet --> ")
                                while True:
                                    if do == "1" or do == "2" or do == "3" or do == "4" or do == "5":
                                        do = int(do)-1
                                        if do <= len(player.inventory)-1:
                                            use = player.inventory[do]
                                            if use == "ett bandage":
                                                player.health = item.bandage
                                                player.inventory.pop(do)
                                                print("Du använde ett bandage och fick därför 2Hp")
                                                print("Nu har du", player.health, " Hp")
                                                break
                                            elif use == "ett svärd" and sword_in_use == False:
                                                sword_in_use = True
                                                print("Du håller nu i ditt svärd och kommer därför göra mer skada mot alla monster!")
                                                player.strength = item.svärd
                                                break
                                            elif use == "ett svärd" and sword_in_use == True:
                                                print("Du håller redan i ett svärd!")
                                                break
                                            elif use == "en rustning" and rustning_in_use == False:
                                                rustning_in_use = True
                                                print("Du tog på dig rustningen!")
                                                print("Nästa gång du förlorar mot ett monster eller går in i en fälla kommer du inte ta skada!")
                                                break
                                            elif use == "en rustning" and rustning_in_use == True:
                                                print("Du har redan en rustning på dig")
                                                break
                                        else:
                                            print("Du har ingenting på den positionen")
                                            break
                                    else:
                                        do = input("Du måste skriva ett tal mellan 1 och 5 --> ")
                                break
                            elif interact == "nej":
                                print("okej då säger vi så! ")
                                break
                            else:
                                interact = input("Du måste svara ja eller nej! ").lower()
                            
                direction = input("Skriv vilket håll du vill gå åt när du har kollat klart --> ").lower()
                open_inventory = False
                break
                    
            
        #Fiender, Kistor och fällor.
        if faith == "panter":
            print("Du stötte på en vild panther! Döda den!")
            enemy_strength = random.randint(30,70)
            time.sleep(2)
            if player.strength > enemy_strength:
                print("Du dödade pantern, du fick 3 guld mynt och",enemy_strength,"xp")
                player.xp = player.xp+enemy_strength
            elif player.strength < enemy_strength and rustning_in_use == True:
                print("Panterna bet sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning")
            elif player.strength < enemy_strength:
                print("Du blev överväldigad av pantern och tappade 2 Hp")
                player.health = player.health-2
                print("Nu har du bara",player.health,"Hp kvar!")
            elif player.strength == enemy_strength:
                print("Du tog ut en köttbit ur fickan och lurade bort pantern!")
        elif faith == "alligator":
            print("Du stötte på en alligator! Döda den!")
            enemy_strength = random.randint(0,60)
            time.sleep(2)
            if player.strength > enemy_strength:
                time.sleep(2)
                print("Du tog kol på den där alligatorn, du fick 1 guld mynt och", enemy_strength, "xp")
                player.xp = player.xp+enemy_strength
            elif player.strength < enemy_strength and rustning_in_use == True:
                print("Alligatorn bet sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning")
            elif player.strength < enemy_strength:
                print("Alligatorn tog ett stort bett av dig! Du tappade 2 Hp")
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
                player.xp = player.xp+enemy_strength
            elif player.strength < enemy_strength and rustning_in_use == True:
                print("Stamfolket tog sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning")
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
            time.sleep(2)
            if rustning_in_use == True:
                print("Rustningen räddade dig men ligger nu i bitar på marken!")
                player.inventory.remove("en rustning")
            else:
                print("Du tappade 1 hp!")
                print("Nu har du bara",player.health,"Hp kvar!")
                player.health = player.health-1
        elif faith == "kista":
            innehåll = item_list[random.randint(0,len(item_list)-1)]
            öppna = input("Du hittade en kista vill du öpnna den eller gå vidare? Svara ja om du vill öppna den och nej om du inte vill gå vidare. --> ").lower()
            
            #Kistor
            
            while True:
                if öppna == "ja":
                    print("Du hittade", innehåll, "i kistan!")
                    if innehåll == "en fälla":
                        trap = trap_list[random.randint(0,len(trap_list)-1)]
                        if trap == "damage trap" or len(player.inventory) == 0 and rustning_in_use == True:
                            print("Kistan sprängdes och din rustning gick sönder men du kom iväg säkert!")
                            player.inventory.remove("en rustning")
                        elif trap == "damage trap" or len(player.inventory) == 0:
                            print("Kistan sprängdes och du tappade ett Hp")
                            player.health = player.health-1
                            print("Du har nu bara",player.health, "Hp kvar!")
                        elif trap == "stealing trap":
                            print("En talande orm sa åt dig att ge honom ett föremål annars äter han upp dig!")
                            snott_föremål = random.randint(0,len(player.inventory)-1)
                            print("Ormen slinker iväg efter du gav bort", player.inventory[snott_föremål],"till honom")
                            if player.inventory[snott_föremål] == "ett svärd":
                                sword_in_use = False
                                player.strength = player.strength-15
                            player.inventory.pop(snott_föremål)
                    elif len(player.inventory) < 5:
                        print("Föremålet har lagts in i ditt förråd")
                        player.inventory.append(innehåll)
                    elif len(player.inventory) == 5:
                        print("Ditt förråd är fullt!")
                        print(player.inventory)
                        byta = input("Vill du byta ut föremålet med någonting annat i ditt förråd? --> ").lower()
                        while True:
                            if byta == "ja":
                                försvinna = input("Skriv platsen i ditt förråd som föremålet du vill byta ut finns på. Ett tal mellan 1 och 5 --> ")
                                while True:
                                    if försvinna == "1" or försvinna == "2" or försvinna == "3" or försvinna == "4" or försvinna == "5":
                                        försvinna = int(försvinna)-1
                                        meddelande = "Är du säker att du vill byta ut " + innehåll + " mot " + player.inventory[försvinna] + "? --> "
                                        försäkring = input(meddelande).lower()
                                        while True:
                                            if försäkring == "ja":
                                                if player.inventory[försvinna] == "ett svärd":
                                                    sword_in_use = False
                                                    player.strength = player.strength-15
                                                print("Du lämnade kvar ",player.inventory[försvinna], " och du tog istället upp ",innehåll)
                                                player.inventory.pop(försvinna)
                                                player.inventory.append(innehåll)
                                                print("Nu har du dessa saker i ditt förråd:")
                                                print(player.inventory)
                                                break
                                            elif försäkring == "nej":
                                                print("Du lämnade kvar ", innehåll, " i kistan och går vidare!")
                                                break
                                            else:
                                                försäkring = input("Du måste svara ja eller nej! --> ").lower()
                                        break
                                    else:
                                        försvinna = input("Du måste svara med ett tal mellan 1 och 5 --> ")
                                break
                            elif byta == "nej":
                                print("Du lämnade kvar ", innehåll, " och gick vidare")
                                break
                            else:
                                byta = input("Du får bara svara ja eller nej! --> ").lower()
                    break
                elif öppna == "nej":
                    print("Du öppnade inte kistan och gick vidare!")
                    break
                else:
                    öppna = input("Du måste svara ja eller nej! --> ").lower()