#Te23A  Jacob Norsell, Hampus Melin Österlindh, Hannes Park Brandberg. 
import time
import random
open_inventory = False
armor_in_use = False
sword_in_use = False
adrenalin = False
boost = 0
monkey_strength = 0
monkey_on_the_back = False
monkey_dead = False
stay = True 
stay2 = True
removed_item = "no"

class player:
    strength = 50
    xp = 0
    level = 0
    health = 10
    coins = 0
    inventory = []

class item:
    sword = 15
    monkey = 1.5
    adrenalinshot = 20
    armor = 1
    bandage = 2

def damage(damage,original):
    new = original-damage
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
            removed_item = switchitems(item)
            money = money-cost
            return [money, removed_item]
    else:
        print("Du har inte råd med detta föremål. Du har bara ", money," Guld mynt")
        return [money, "no"]

def switchitems(item):
            print("Du har dessa saker i ditt förråd:")
            print(player.inventory)
            remove = input("Skriv platsen i ditt förråd som föremålet du vill byta ut finns på. Ett tal mellan 1 och 5 --> ").strip()
            while True:
                if remove in ["1","2","3","4","5"]:
                    remove = int(remove)-1
                    removed_item = player.inventory[remove]
                    message = "Är du säker att du vill byta ut " + removed_item + " med " + item + "? --> "
                    insurance = input(message).lower().strip()
                    while True:
                        if insurance == "ja":
                            print("Du lämnade kvar ",removed_item, " och du tog istället upp ",item)
                            player.inventory.remove(removed_item)
                            player.inventory.append(item)
                            print("Nu har du dessa saker i ditt förråd:")
                            print(player.inventory)
                            return removed_item
                        elif insurance == "nej":
                            print("Du lämnade kvar ", item, " och går vidare!")
                            return "no"
                        else:
                            insurance = input("Du måste svara ja eller nej! --> ").lower().strip()
                else:
                    remove = input("Du måste svara med ett tal mellan 1 och 5 --> ").strip()



item_list = ["en fälla", "ett adrenalinshot(20str i 3 rundor)","en apa(1.5str/runda)", "en rustning(0 dmg 1 gång)", "ett bandage(+2hp)","ett svärd(+15str)"]
trap_list = ["stealing trap","damage trap"]

#Level system
needed_xp = [30, 60, 100, 150, 210, 280, 360, 450, 600]
def vilken_level(xp):
    for i in range(0,len(needed_xp)):
        if xp >= needed_xp[i]:
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
                print("Stenjätten faller till sin död och du ser en utväg.")
                time.sleep(2)
                print("Men något känns fel, du hör din kära apas läte och du ser hans ande.")
                time.sleep(2)
                print("Han tackar dig för er vänskap och ger dig två alternativ.")
                time.sleep(2)
                print("Antingen stannar du i djungeln för att hedra han och ta över rollen som beskyddare av djungeln.")
                time.sleep(2)
                print("Eller så accepterar du djungelns öde och lämnar den och alla minnen bakom dig.")
                choice2 = input("Stannar du i djungel(s) eller lämnar du allt bakom dig(b)?").lower().strip()
                if choice2 == "b":
                    time.sleep(2)
                    print("Du tar ett djupt andetag, säger förlåt till din apa med tårar som rinner ner för ditt ansikte och du tar ditt första steg ut från djungeln.")
                elif choice2 == "s":
                    time.sleep(2)
                    print("Du ser dig omkring, apans själ kollar dig stolt i ögonen och du tar över rollen som djungeln beskyddare!")
            elif monkey_on_the_back == True:
                print("Stenjätten faller till sin död och du ser en utväg.")
                time.sleep(2)
                print("En röst kommer mot dig, som om den vore från djungelns själ.")
                time.sleep(2)
                print("Du har övervunnit djungeln, det är dags att göra ett val! Viskar rösten")
                time.sleep(2)
                print("Antingen tar du det blå pillret och stannar i djungel som beskyddare över djungeln, med din kära apa vid din sida!")
                time.sleep(2)
                print("Eller så tar du det röda pillret och går här ifrån som om inget har hänt och lämnar din apa som djungelns beskyddare!")
                time.sleep(2)
                choice3 = input("Väljer du det blå pillret(b) eller det röda pilret(r)?").lower().strip()
                if choice3 == "b":
                    time.sleep(2)
                    print("Du ser dig omkring, tar in djungelns andar, apan hoppar upp på din axel och du tar över rollen som djungeln beskyddare!")
                elif choice3 == "r":
                    time.sleep(2)
                    print("Du tar ett djupt andetag, tackar din apa för all fina minnen och er vänskap, visar hur stolt du är över honom och tar ditt första steg närmare ditt hem.")
            elif choice1 == "nej":
                print("Stenjätten faller till sin död och du ser din utgväg, men just då ser du hur elden har spridit sig som en magisk cirkel runt hela jungeln och du måste gå tillbaka")
                time.sleep(1)
                print("Du inser att du är fast och aldrig kommer ta dig ut!")
            else:
                print("Stenjätten faller till sin död och du ser din utväg")
                time.sleep(1)
                print("Du tar dig en titt runt jungeln och tänker på allt du åstadkommit")
                time.sleep(1)
                print("Men du tar dig lånsamt till utgången och inser att du är fri!")

                return
        
# Inledning/tutorial 
print("Du är fast i en djungel. Du ser en öppning framför dig!")
choice1 = input("Vill du gå igenom öppningen? --> ").lower().strip()
while True:  
    if choice1 == "ja":
        print("Du sprang in i ett monster. försök döda det!")
        time.sleep(1.5)
        print("Du dödade monstret och gick därför upp en level.")
        time.sleep(1.5)
        print("Du hamnade i djungel och monstret blockarar utgången, Du måste fortsätta in i djungeln")
        player.level = player.level+1
        break
    if choice1 == "nej":
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
        choice1 = input("Du måste svara ja eller nej! --> ").lower().strip()

opening_list = ["Du ser ytterligare tre öppningar framför dig vilket håll vill du gå åt, höger(h), vänster(v) eller rakt fram(r)? Du kan också skriva (i) för att öppna förrådet--> ","Du ser en grotta till vänster(v), ett tempel till höger(h) och ett dimmigt vattenfall rakt fram(r). Vilket håll vill du gå åt, höger(h), vänster(v) eller rakt fram(r)? Du kan också skriva (i) för att öppna förrådet --> " ]
faith_list = ["panter","panter","panter","panter","panter","panter","panter","alligator","alligator","alligator","alligator","stammfolk","stammfolk","stammfolk","stammfolk","stammfolk","kista","kista","kista","kista","kista","kista","kista","kista","fälla","fälla","fälla","fälla","butik"]

#Gameloop
while True:

    old_level = player.level
    new_level = vilken_level(player.xp)
    if new_level > old_level:
        print("Du gick upp i level", new_level,"!","Snyggt jobbat!")
        player.level = new_level 

    if adrenalin == True and boost == 0:
        print("Adrenalinet i ditt blod börjar minska och du gör nu din vanliga skada igen!")
        adrenalin = False
        player.strength = strengthchange(-item.adrenalinshot,player.strength)
    if monkey_on_the_back == True:
        player.strength = strengthchange(item.monkey,player.strength)
        monkey_strength = monkey_strength+1.5

    if player.health <= 0:
        print("Vad händer, det blir ljust, du förblöder! Du dog!")
        print("Game over!")
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
        old_level = player.level
        new_level = vilken_level(player.xp)
        if new_level > old_level:
            print("Du gick upp i level", new_level,"!","Snyggt jobbat!")
            player.level = new_level 
        
        #Öde och inventory
        time.sleep(3)
        direction = input(opening_list[random.randint(0,len(opening_list)-1)]).lower().strip()
        left = faith_list[random.randint(0,len(faith_list)-1)]
        straight = faith_list[random.randint(0,len(faith_list)-1)]
        right = faith_list[random.randint(0,len(faith_list)-1)]
        while True:
            if direction == "v" or direction == "vänster":
                faith = left
                break
            elif direction == "r" or direction == "rakt fram":
                faith = straight
                break
            elif direction == "h" or direction == "höger":
                faith = right
                break
            elif direction == "i":
                open_inventory = True
            else:
                direction = input("Du måste svara (v), (h), (r) eller (i). --> ").lower().strip()

            while open_inventory == True:
                while True:
                    if len(player.inventory) == 0:
                        print("Ditt förråd är tomt")
                        print("Du har", player.strength, "styrka och", player.health, "hp")
                        print("I din ficka har du", player.coins, "mynt")
                        print("Du har samlat på dig", player.xp, "xp och är i level", player.level)
                        break
                    elif len(player.inventory)> 0:
                        print("I ditt förråd har du:")
                        print(player.inventory)
                        print("Du har", player.strength, "styrka och", player.health, "hp")
                        print("I din ficka har du", player.coins, "mynt")
                        print("Du har samlat på dig", player.xp, "xp och är i level", player.level)
                        interact = input("Vill du använda någonting i ditt förråd? --> ").lower().strip()
                        while True:
                            if interact == "ja":
                                do = input("Skriv platsen som ditt föremål ligger i förrådet --> ").strip()
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
                                                player.strength = strengthchange(item.sword,player.strength)
                                                break
                                            elif use == "ett svärd(+15str)" and sword_in_use == True:
                                                print("Du håller redan i ett svärd!")
                                                break
                                            elif use == "en rustning(0 dmg 1 gång)" and armor_in_use == False:
                                                armor_in_use = True
                                                print("Du tog på dig rustningen!")
                                                print("Nästa gång du förlorar mot ett monster eller går in i en fälla kommer du inte ta skada!")
                                                break
                                            elif use == "en rustning(0 dmg 1 gång)" and armor_in_use == True:
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
                                                print("Apan hoppade upp på din rygg och kommer nu hjälpa dig slåss. Han lär sig av att se dig slås!")
                                                monkey_on_the_back = True
                                                player.strength = strengthchange(item.monkey,player.strength)
                                                monkey_strength = 1.5
                                                break
                                            elif use == "Zeuz åskvigg(25str och 3hp)":
                                                print("Du tar upp Zeus åskvigg och känner blixten stråla. Du har nu ökat din styrka med 25 och ditt Hp med 10!")
                                                player.strength = strengthchange(25,player.strength)
                                                player.health = damage(-3,player.health)
                                        else:
                                            print("Du har ingenting på den positionen")
                                            break
                                    else:
                                        do = input("Du måste skriva ett tal mellan 1 och 5 --> ").strip()
                                break
                            elif interact == "nej":
                                print("Okej då säger vi så! ")
                                break
                            else:
                                interact = input("Du måste svara ja eller nej! ").lower().strip()
                        break   
                direction = input("Skriv vilket håll du vill gå åt när du har kollat klart (v)(h)(r)(i) --> ").lower().strip()
                open_inventory = False
                break
                    
        #Fiender, Kistor och fällor.
        if faith == "panter":
            print("Du stötte på en vild panther! Döda den!")
            enemy_strength = random.randint(40,75)
            time.sleep(2)
            if player.strength > enemy_strength:
                print("Du dödade pantern, du fick 3 guld mynt och",enemy_strength,"xp")
                player.xp = xp_gain(enemy_strength,player.xp)
                player.coins = coins_gain(3,player.coins)
            elif player.strength < enemy_strength and armor_in_use == True:
                print("Panterna bet sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                armor_in_use = False
            elif player.strength < enemy_strength:
                print("Du blev överväldigad av pantern och tappade 1 Hp")
                player.health = damage(1,player.health)
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
                player.coins = coins_gain(1,player.coins)
            elif player.strength < enemy_strength and armor_in_use == True:
                print("Alligatorn bet sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                armor_in_use = False
            elif player.strength < enemy_strength:
                print("Alligatorn tog ett stort bett av dig! Du tappade 2 Hp")
                player.health = damage(2,player.health)
                print("Nu har du bara",player.health,"Hp kvar!") 
            elif player.strength == enemy_strength:
                print("Du hopppade på alligatorns huvud och kom förbi oskadd.")
        elif faith == "stammfolk":
            print("Några stammfolk ringar in dig i ett hörn! Visa dem vad du kan!")
            enemy_strength = random.randint(50,90)
            time.sleep(2)
            if player.strength > enemy_strength:
                print("Du visade de där stammfolket vad du går för, snyggt!","du fick 5 guld mynt och", enemy_strength, "xp" )
                player.xp = xp_gain(enemy_strength,player.xp)
                player.coins = coins_gain(5,player.coins)
            elif player.strength < enemy_strength and armor_in_use == True:
                print("Stamfolket tog sönder din rustning men du kom iväg säkert!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                armor_in_use = False
            elif player.strength < enemy_strength:
                print("De visade vart skåpet ska stå istället! Känn på den du! du tappade 1 Hp")
                player.health = damage(1,player.health)
                print("Nu har du bara",player.health,"Hp kvar!")
            elif player.strength == enemy_strength:
                print("Visar sig att de var chill like that, ni skakade hand på det och du går vidare!")
        elif faith == "fälla":
            print("Vänta vad är det som låter?")
            time.sleep(4)
            print("Du gick rakt in i en fälla!")
            time.sleep(2)
            if armor_in_use == True:
                print("Rustningen räddade dig men ligger nu i bitar på marken!")
                player.inventory.remove("en rustning(0 dmg 1 gång)")
                armor_in_use = False
            else:
                print("Du tappade 1 hp!")
                player.health = damage(1,player.health)
                print("Nu har du bara",player.health,"Hp kvar!")
        elif faith == "butik":
            print("Åh, en vandrare som hittat hit. Djungeln är inte vänlig mot främlingar... men min butik är det. Vad söker du? Ta en titt på mina priser!", "Säger en röst runt hörnet.")
            time.sleep(2)
            print("ett bandage","(b)(5 coins), ","ett adrenalinshot","(a)(5 coins), ","Zeus åskvigg","(z)(30 coins)")
            time.sleep(2)
            print("Är det något som blänker i ögonen dina?")
            time.sleep(2)
            bought_item = input("Vad vill du köpa? Du kan också gå vidare genom att skriv (g) --> ").lower().strip()
            stay = True
            while stay == True:
                while True:
                    if bought_item == "b":
                        buy_list = coins_check(5,player.coins,"ett bandage(+2hp)")
                        player.coins = buy_list[0]
                        removed_item = buy_list[1]
                    elif bought_item == "a":
                        buy_list = coins_check(5,player.coins,"ett adrenalinshot(20str i 3 rundor)")
                        player.coins = buy_list[0]
                        removed_item = buy_list[1]
                    elif bought_item == "z":
                        buy_list = coins_check(30,player.coins,"Zeuz åskvigg(25str och 3hp)")
                        player.coins = buy_list[0]
                        removed_item = buy_list[1]
                    elif bought_item == "g":
                        stay = False
                        removed_item = "no"
                        break
                    if bought_item == "b" or bought_item == "a" or bought_item == "z":
                        if removed_item == "ett svärd(+15str)":
                            sword_in_use = False
                            player.strength = strengthchange(-item.sword,player.strength)  
                            break
                        elif removed_item == "en rustning(0 dmg 1 gång)":
                            armor_in_use = False  
                            break
                        elif removed_item == "en apa(1.5str/runda)":  
                            monkey_on_the_back = False
                            monkey_dead = True
                            player.strength = strengthchange(-monkey_strength,player.strength)   
                            break
                        elif removed_item == "Zeuz åskvigg(25str och 3hp)":
                            player.strength = strengthchange(-25,player.strength)
                            player.health = damage(3)
                            print("Du tappar styrkan av Zeus därför har du tappat 25 styrka och 3 Hp")
                            print("Nu har du bara ",player.health," Hp och ", player.strength, " styrka.") 
                            break
                        else:
                            removed_item = "no"
                            break
                    elif bought_item != "g":
                        bought_item = input("Du måste svara med a, b, z eller g --> ").lower().strip()
                        removed_item = "no"
                if stay == True:
                    bought_item = input("Vad mer vill du köpa? Eller vill du kanske gå vidare(g)? --> ").lower().strip()
                removed_item = "no"
            
        #Kistor
        elif faith == "kista":
            content = item_list[random.randint(0,len(item_list)-1)]
            open = input("Du hittade en kista vill du öppna den eller gå vidare? Svara ja om du vill öppna den och nej om du vill gå vidare. --> ").lower().strip()
            
            while True:
                if open == "ja":
                    print("Du hittade", content, "i kistan!")
                    if content == "en fälla":
                        trap = trap_list[random.randint(0,len(trap_list)-1)]
                        if trap == "damage trap" and armor_in_use == True:
                            print("Kistan sprängdes och din rustning gick sönder men du kom iväg säkert!")
                            player.inventory.remove("en rustning(0 dmg 1 gång)")
                            armor_in_use = False
                        elif trap == "damage trap" or len(player.inventory) == 0:
                            print("Kistan sprängdes och du tappade ett Hp")
                            player.health = damage(1,player.health)
                            print("Du har nu bara",player.health, "Hp kvar!")
                        elif trap == "stealing trap":
                            print("En talande orm sa åt dig att ge honom ett föremål annars äter han upp dig!")
                            stolen_item = random.randint(0,len(player.inventory)-1)
                            print("Ormen slinker iväg efter med", player.inventory[stolen_item],"som du gav till honom med tårar i ögonen.")
                            if player.inventory[stolen_item] == "ett svärd(+15str)":
                                sword_in_use = False
                                player.strength = strengthchange(-item.sword,player.strength)
                            elif player.inventory[stolen_item] == "en apa(1.5str/runda)":
                                monkey_dead = True
                                monkey_on_the_back = False
                                player.strength = strengthchange(-monkey_strength,player.strength)
                            elif removed_item == "en rustning(0 dmg 1 gång)":
                                armor_in_use = False
                            elif removed_item == "Zeuz åskvigg(25str och 3hp)":
                                player.strength = strengthchange(-25,player.strength)
                                player.health = damage(3)
                                print("Du tappar styrkan av Zeus därför har du tappat 25 styrka och 3 Hp")
                                print("Nu har du bara ",player.health," Hp och ", player.strength, " styrka.")
                            player.inventory.pop(stolen_item)    
                    elif len(player.inventory) < 5:
                        print("Föremålet har lagts in i ditt förråd")
                        player.inventory.append(content)
                        if content == "en apa(1.5str/runda)":
                            item_list.remove("en apa(1.5str/runda)")
                    elif len(player.inventory) == 5:
                        print("Ditt förråd är fullt!")
                        print(player.inventory)
                        switch = input("Vill du byta ut föremålet med någonting annat i ditt förråd? --> ").lower().strip()
                        while True:
                            if switch == "ja":
                                removed_item = switchitems(content)
                                if removed_item == "ett svärd(+15str)":
                                    sword_in_use = False
                                    player.strength = strengthchange(-item.sword,player.strength)
                                    break
                                elif removed_item == "en rustning(0 dmg 1 gång)":
                                    armor_in_use = False
                                    break
                                elif removed_item == "en apa(1.5str/runda)":
                                    monkey_on_the_back = False
                                    monkey_dead = True
                                    player.strength = strengthchange(-monkey_strength,player.strength)
                                    break
                                elif removed_item == "Zeuz åskvigg(25str och 3hp)":
                                    player.strength = strengthchange(-25,player.strength)
                                    player.health = damage(3)
                                    print("Du tappar styrkan av Zeus därför har du tappat 25 styrka och 3 Hp")
                                    print("Nu har du bara ",player.health," Hp och ", player.strength, " styrka.")
                                    break
                                else:
                                    break  
                            elif switch == "nej":
                                print("Du lämnade kvar ", content, " och gick vidare")
                                break
                            else:
                                switch = input("Du får bara svara ja eller nej! --> ").lower().strip()
                    break
                elif open == "nej":
                    print("Du öppnade inte kistan och gick vidare!")
                    break
                else:
                    open = input("Du måste svara ja eller nej! --> ").lower().strip()
    if adrenalin == True:
        boost = boost-1