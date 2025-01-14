#Te23A  Jacob Norsell, Hampus Melin Österlindh, Hannes Park Brandberg. 
import time
import random
open_inventory = False
rustning_in_use = False
sword_in_use = False
adrenalin = False
boost = 0
monkey_strength = 1.5
monkey_on_the_back = False
monkey_dead = False 

class player:
    strength = 50
    xp = 0
    level = 0
    health = 10
    mynt = 15
    inventory = []

class item:
    svärd = 15
    apa = 1.5
    adrenalinshot = 20
    rustning = 1
    bandage = 2

def damage(skada,original):
    new = original-skada
    return new

def strengthchange(change,original):
    new = original+change
    return new

def xp_gain(change,original):
    new = change+original
    return new

def coins_gain(change,original):
    new = change+original
    return new

def coins_check(cost,money,item):
    if money >= cost:
        if len(player.inventory) < 5:
            money = money-cost
            player.inventory.append(item)
            print("Du har nu köpt", item,"och det har lagts till i ditt förråd")
            return [money, "yes"]
        else:
            item_gone = switchitems(item)
            money = money-cost
            return [money, item_gone]
    else:
        print("Du har inte råd med detta föremål. Du har bara ", money," Guld mynt")
        return [money, "no"]

def switchitems(item):
            print("Du har dessa saker i ditt förråd:")
            print(player.inventory)
            försvinna = input("Skriv platsen i ditt förråd som föremålet du vill byta ut finns på. Ett tal mellan 1 och 5 --> ")
            while True:
                if försvinna in ["1","2","3","4","5"]:
                    försvinna = int(försvinna)-1
                    item_gone = player.inventory[försvinna]
                    meddelande = "Är du säker att du vill byta ut " + item_gone + " med " + item + "? --> "
                    försäkring = input(meddelande).lower()
                    while True:
                        if försäkring == "ja":
                            print("Du lämnade kvar ",item_gone, " och du tog istället upp ",item)
                            player.inventory.remove(item_gone)
                            player.inventory.append(item)
                            print("Nu har du dessa saker i ditt förråd:")
                            print(player.inventory)
                            return item_gone
                        elif försäkring == "nej":
                            print("Du lämnade kvar ", item, " och går vidare!")
                            return "no"
                        else:
                            försäkring = input("Du måste svara ja eller nej! --> ").lower()
                else:
                    försvinna = input("Du måste svara med ett tal mellan 1 och 5 --> ")



item_list = ["en fälla", "ett adrenalinshot(20str i 3 rundor)","en apa(1.5str/runda)", "en rustning(0 dmg 1 gång)", "ett bandage(+2hp)","ett svärd(+15str)","Double chunk choclate cookie(placeholder)"]
trap_list = ["stealing trap","damage trap"]

#Level system
level_gränser = [30, 60, 100, 150, 210, 280, 360, 450, 600]
def vilken_level(xp):
    for i in range(0,len(level_gränser)):
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
            if monkey_dead == True:

            else:
                print("Stenjätten faller till sin död och du ser en utväg.")
                time.sleep(2)
                print("En röst kommer mot dig, som om den vore från djungelns själ.")
                time.sleep(2)
                print("Du har övervunnit djungeln, ")
                return
        
# Inledning/tutorial 
print("Du är fast i en djungel. Du ser en öppning framför dig!")
val = input("Vill du gå igenom öppningen? --> ").lower()
while True:  
    if val == "ja":
        print("Du sprang in i ett monster. försök döda det!")
        time.sleep(1.5)
        print("Du dödade monstret och gick därför upp en level.")
        time.sleep(1.5)
        print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
        player.level = player.level+1
        break
    if val == "nej":
        print("Det börjar brinna bakom dig du måste springa igenom öppningen.")
        time.sleep(1.5)
        print("Du sprang in i ett monster. försök döda det!")
        time.sleep(2)
        print("Du dödade monstret och gick därför upp en level.")
        time.sleep(1.5)
        print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
        player.level = player.level+1
        break
    else:
        val = input("Du måste svara ja eller nej! --> ").lower()

öppningar = ["Du ser ytterligare tre öppningar framför dig vilket håll vill du gå åt, höger(h), vänster(v) eller rakt fram(r)? Du kan också skriva (i) för att öppna förrådet--> ","Du ser en grotta till vänster(v), ett tempel till höger(h) och ett dimmigt vattenfall rakt fram(r). Vilket håll vill du gå åt, höger(h), vänster(v) eller rakt fram(r)? Du kan också skriva (i) för att öppna förrådet --> " ]
faith_list = ["panter","panter","panter","panter","panter","alligator","alligator","alligator","alligator","alligator","stammfolk","stammfolk","stammfolk","stammfolk","stammfolk","kista","kista","kista","kista","kista","kista","fälla","fälla","fälla","fälla","fälla","butik", "butik"]

#Gameloop
while True:

    if adrenalin == True and boost == 0:
        print("Adrenalinet i ditt blod börjar minska och du gör nu din vanliga skada igen!")
        adrenalin = False
        player.strength = strengthchange(-item.adrenalinshot,player.strength)
    if monkey_on_the_back == True:
        player.strength = strengthchange(item.apa,player.strength)
        monkey_strength = monkey_strength+1.5

    if player.health <= 0:
        print("Vad händer, det blir ljust, du förblöder! Du dog!")
        break
    elif player.level == 10:
        print("Du börjar se ljuset, Du ser en sista utväg. Du springer in mellan två stenmurar, du känner en hård smäll på kinden. Du kollar upp och ser en stor stenjätte.")
        time.sleep(3)
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
        
    #Level
    else:
        gamla_level = player.level
        ny_level = vilken_level(player.xp)
        if ny_level > gamla_level:
            print("Du gick upp i level", ny_level,"!","Snyggt jobbat!")
            player.level = ny_level 
        
        #Öde och inventory
        time.sleep(3)
        direction = input(öppningar[random.randint(0,len(öppningar)-1)]).lower()
        left = faith_list[random.randint(-9,-8)]
        straight = faith_list[random.randint(-2,-1)]
        right = faith_list[random.randint(0,len(faith_list)-1)]
        while True:
            if direction == "v":
                faith = left
                break
            elif direction == "r":
                faith = straight
                break
            elif direction == "h":
                faith = right
                break
            elif direction == "i":
                open_inventory = True
            else:
                direction = input("Du måste svara (v), (h), (r) eller (i). --> ").lower()

            while open_inventory == True:
                while True:
                    if len(player.inventory) == 0:
                        print("Ditt förråd är tomt")
                        print("Du har", player.strength, "styrka och", player.health, "hp")
                        print("I din ficka har du", player.mynt, "mynt")
                        print("Du har samlat på dig", player.xp, "xp och är i level", player.level)
                        break
                    elif len(player.inventory)> 0:
                        print("I ditt förråd har du:")
                        print(player.inventory)
                        print("Du har", player.strength, "styrka och", player.health, "hp")
                        print("I din ficka har du", player.mynt, "mynt")
                        print("Du har samlat på dig", player.xp, "xp och är i level", player.level)
                        interact = input("Vill du använda någonting i ditt förråd? --> ").lower()
                        while True:
                            if interact == "ja":
                                do = input("Skriv platsen som ditt föremål ligger i förrådet --> ")
                                while True:
                                    if do in ["1","2","3","4","5"]:
                                        do = int(do)-1
                                        if do <= len(player.inventory)-1:
                                            use = player.inventory[do]
                                            if use == "ett bandage(+2hp)":
                                                player.health = damage(-item.bandage,player.health)
                                                player.inventory.pop(do)
                                                print("Du använde ett bandage och fick därför 2Hp")
                                                print("Nu har du", player.health, " Hp")
                                                break
                                            elif use == "ett svärd(+15str)" and sword_in_use == False:
                                                sword_in_use = True
                                                print("Du håller nu i ditt svärd och kommer därför göra mer skada mot alla monster!")
                                                player.strength = strengthchange(item.svärd,player.strength)
                                                break
                                            elif use == "ett svärd(+15str)" and sword_in_use == True:
                                                print("Du håller redan i ett svärd!")
                                                break
                                            elif use == "en rustning(0 dmg 1 gång)" and rustning_in_use == False:
                                                rustning_in_use = True
                                                print("Du tog på dig rustningen!")
                                                print("Nästa gång du förlorar mot ett monster eller går in i en fälla kommer du inte ta skada!")
                                                break
                                            elif use == "en rustning(0 dmg 1 gång)" and rustning_in_use == True:
                                                print("Du har redan en rustning på dig")
                                                break
                                            elif use == "ett adrenalinshot(20str i 3 rundor)" and adrenalin == True:
                                                print("Du har redan adrenalin i blodet om du dricker en till shot kommer du överdosera! vänta ",boost," runder till innan du kan dricka en till!")
                                                break
                                            elif use == "ett adrenalinshot(20str i 3 rundor)":
                                                print("Du drack en adrenalinshot och känner styrkan pumpa i dina veins")
                                                print("Du kommer nu göra mer skada under de tre följande rundorna")
                                                boost = 3
                                                adrenalin = True
                                                player.strength = strengthchange(item.adrenalinshot,player.strength)
                                                player.inventory.remove("ett adrenalinshot(20str i 3 rundor)")
                                                break
                                            elif use == "en apa(1.5str/runda)":
                                                print("Apan hoppade upp på din rygg och kommer nu hjälpa dig slås. Han lär sig av att se dig slås!")
                                                monkey_on_the_back = True
                                                player.strength = strengthchange(item.apa,player.strength)
                                                monkey_strength = 1.5
                                                break
                                            elif use == "Zeuz åskvigg(25str och 10hp)":
                                                print("Du tar upp Zeus åskvigg och känner blixten stråla. Du har nu ökat din styrka med 25 och ditt Hp med 10!")
                                                player.strength = strengthchange(25,player.strength)
                                                player.health = damage(-10,player.health)
                                        else:
                                            print("Du har ingenting på den positionen")
                                            break
                                    else:
                                        do = input("Du måste skriva ett tal mellan 1 och 5 --> ")
                                break
                            elif interact == "nej":
                                print("Okej då säger vi så! ")
                                break
                            else:
                                interact = input("Du måste svara ja eller nej! ").lower()
                        break   
                direction = input("Skriv vilket håll du vill gå åt när du har kollat klart (v)(h)(r)(i) --> ").lower()
                open_inventory = False
                break
                    
        #Fiender, Kistor och fällor.
        if faith == "panter":
            print("Du stötte på en vild panther! Döda den!")
            enemy_strength = random.randint(30,65)
            time.sleep(2)
            if player.strength > enemy_strength:
                print("Du dödade pantern, du fick 3 guld mynt och",enemy_strength,"xp")
                player.xp = xp_gain(enemy_strength,player.xp)
                player.mynt = coins_gain(3,player.mynt)
            elif player.strength < enemy_strength and rustning_in_use == True:
                print("Panterna bet sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                rustning_in_use = False
            elif player.strength < enemy_strength:
                print("Du blev överväldigad av pantern och tappade 2 Hp")
                player.health = damage(2,player.health)
                print("Nu har du bara",player.health,"Hp kvar!")
            elif player.strength == enemy_strength:
                print("Du tog ut en köttbit ur fickan och lurade bort pantern!")
        elif faith == "alligator":
            print("Du stötte på en alligator! Döda den!")
            enemy_strength = random.randint(1,60)
            time.sleep(2)
            if player.strength > enemy_strength:
                time.sleep(2)
                print("Du tog kol på den där alligatorn, du fick 1 guld mynt och", enemy_strength, "xp")
                player.xp = xp_gain(enemy_strength,player.xp)
                player.mynt = coins_gain(1,player.mynt)
            elif player.strength < enemy_strength and rustning_in_use == True:
                print("Alligatorn bet sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                rustning_in_use = False
            elif player.strength < enemy_strength:
                print("Alligatorn tog ett stort bett av dig! Du tappade 2 Hp")
                player.health = damage(2,player.health)
                print("Nu har du bara",player.health,"Hp kvar!") 
            elif player.strength == enemy_strength:
                print("Du hopppade på alligatorns huvud och kom förbi oskadd.")
        elif faith == "stammfolk":
            print("Några stammfolk ringar in dig i ett hörn! Visa dem vad du kan!")
            enemy_strength = random.randint(35,80)
            time.sleep(2)
            if player.strength > enemy_strength:
                print("Du visade de där stammfolket vad du går för, snyggt!","du fick 5 guld mynt och", enemy_strength, "xp" )
                player.xp = xp_gain(enemy_strength,player.xp)
                player.mynt = coins_gain(5,player.mynt)
            elif player.strength < enemy_strength and rustning_in_use == True:
                print("Stamfolket tog sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                rustning_in_use = False
            elif player.strength < enemy_strength:
                print("De visade vart skåpet ska stå istället! Känn på den du! du tappade 2 Hp")
                player.health = damage(2,player.health)
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
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                rustning_in_use = False
            else:
                print("Du tappade 1 hp!")
                player.health = damage(1,player.health)
                print("Nu har du bara",player.health,"Hp kvar!")
        elif faith == "butik":
            print("Åh, en vandrare som hittat hit. Djungeln är inte vänlig mot främlingar... men min butik är det. Vad sökers du? Ta en titt på mina priser!", "Säger en röst runt hörnet.")
            time.sleep(2)
            print("ett bandage","(b)(5 coins), ","ett adrenalinshot","(a)(5 coins), ","Zeus åskvigg","(z)(20 coins)")
            time.sleep(2)
            print("Är det något som blänker i ögonen dina?")
            time.sleep(2)
            bought_item = input("Vad vill du köpa? Du kan också gå vidare genom att skriv g --> ").lower()
            while True:
                if bought_item == "b":
                    buy_list = coins_check(5,player.mynt,"ett bandage(+2hp)")
                    player.mynt = buy_list[0]
                    item_gone = buy_list[1]
                elif bought_item == "a":
                    buy_list = coins_check(5,player.mynt,"ett adrenalinshot(20str i 3 rundor)")
                    player.mynt = buy_list[0]
                    item_gone = buy_list[1]
                elif bought_item == "z":
                    buy_list = coins_check(30,player.mynt,"Zeuz åskvigg(25str och 10hp)")
                    player.mynt = buy_list[0]
                    item_gone = buy_list[1]
                    
                elif bought_item == "g":
                    break
                if item_gone == "ett svärd(15str)":
                    sword_in_use = False
                    player.strength = strengthchange(-item.svärd,player.strength)
                elif item_gone == "en rustning(0 dmg 1 gång)":
                    rustning_in_use = False
                elif item_gone == "en apa(1.5str/runda)":  
                    monkey_on_the_back = False
                    monkey_dead = True
                    player.strength = strengthchange(-monkey_strength,player.strength)
                bought_item = input("Vill du köpa nått annat eller vill du gå vidare(g)? --> ").lower()
            
        #Kistor
        elif faith == "kista":
            innehåll = item_list[random.randint(0,len(item_list)-2)]
            öppna = input("Du hittade en kista vill du öpnna den eller gå vidare? Svara ja om du vill öppna den och nej om du vill gå vidare. --> ").lower()
            
            while True:
                if öppna == "ja":
                    print("Du hittade", innehåll, "i kistan!")
                    if innehåll == "en fälla":
                        trap = trap_list[random.randint(0,len(trap_list)-1)]
                        if trap == "damage trap" and rustning_in_use == True:
                            print("Kistan sprängdes och din rustning gick sönder men du kom iväg säkert!")
                            player.inventory.remove("en rustning(0 dmg 1 gång)")
                            rustning_in_use = False
                        elif trap == "damage trap" or len(player.inventory) == 0:
                            print("Kistan sprängdes och du tappade ett Hp")
                            player.health = damage(1,player.health)
                            print("Du har nu bara",player.health, "Hp kvar!")
                        elif trap == "stealing trap":
                            print("En talande orm sa åt dig att ge honom ett föremål annars äter han upp dig!")
                            snott_föremål = random.randint(0,len(player.inventory)-1)
                            print("Ormen slinker iväg efter med", player.inventory[snott_föremål],"som du gav till honom med tårar i ögonen.")
                            if player.inventory[snott_föremål] == "ett svärd(+15str)":
                                sword_in_use = False
                                player.strength = strengthchange(-item.svärd,player.strength)
                            elif player.inventory[snott_föremål] == "en apa(1.5str/runda)":
                                monkey_dead = True
                                monkey_on_the_back = False
                                player.strength = strengthchange(-monkey_strength,player.strength)
                            elif item_gone == "en rustning(0 dmg 1 gång)":
                                rustning_in_use = False
                            player.inventory.pop(snott_föremål)    
                    elif len(player.inventory) < 5:
                        print("Föremålet har lagts in i ditt förråd")
                        player.inventory.append(innehåll)
                        if innehåll == "en apa(1.5str/runda)":
                            item_list.remove("en apa(1.5str/runda)")
                    elif len(player.inventory) == 5:
                        print("Ditt förråd är fullt!")
                        print(player.inventory)
                        byta = input("Vill du byta ut föremålet med någonting annat i ditt förråd? --> ").lower()
                        while True:
                            if byta == "ja":
                                item_gone = switchitems(innehåll)
                                if item_gone == "ett svärd(15str)":
                                    sword_in_use = False
                                    player.strength = strengthchange(-item.svärd,player.strength)
                                    break
                                elif item_gone == "en rustning(0 dmg 1 gång)":
                                    rustning_in_use = False
                                    break
                                elif item_gone == "en apa(1.5str/runda)":
                                    monkey_on_the_back = False
                                    monkey_dead = True
                                    player.strength = strengthchange(-monkey_strength,player.strength)
                                    break
                                else:
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
    if adrenalin == True:
        boost = boost-1