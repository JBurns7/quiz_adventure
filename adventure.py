# An adventure game
from random import randint
health = 10
poison_count = -1
fire_potion = False
mist_potion = False
poison_true = False


def poison():
    global poison_count
    global poison_true

    if mist_potion == False:

        poison_count = poison_count - 1
        
        if poison_count == 2:
            print("You start to feel woozy")
        elif poison_count == 1:
            print("You get a sharp pain in your chest")
        elif poison_count == 0:
            print("The mist from earlier was poison and you drop down dead")
            print("Game Over")
            quit()

    

    

def room1():

    global health
    lock = randint(0,1)

    print("You enter the crypt and see two doorways and a trapdoor")
    print("L: Left Doorway")
    print("R: Right Doorway")
    print("D: The Trapdoor")
    print("Where do you go")

    door = input("Doorway: ")

    if door.lower() == "d":
        if lock == 0:
            print("The Trapdoor is locked pick a different door")
            door = input("Doorway: ")
        if lock == 1:
            print("The Trapdoor slowly opens revealing a ladder")
            print("You climb down")
            dungeon()
        
    if door.lower() == "r":
        print("You head to the wooden door to your right")
        room2()

    if door.lower() == "l":
        print("You head to the iron door to your left")
        armory()

def dungeon():
    global health

    zombie_hp = 2
    hit_chance = randint(1,3)

    print("At the bottom of the ladder you are greeted by an intense moaning")
    print("Do you draw your dagger or bow")
    print("D: Dagger")
    print("B: Bow")

    weapon = input("Weapon: ")

    if weapon.lower() == "d":
        print("You edge towards the source of the moaning")

        while health > 0 and zombie_hp > 0:

            foe_damage = randint(0,2)
            damage = randint(1,3)
            
            print("The zombie attacks...")
            if foe_damage == 0:
                print("You narrowly avoid the zombie's lunge on you")
            else:
                print("You got hit")
                health = health - foe_damage
                

            if damage == 1:
                print("You lightly scathe the zombie but don't kill")
                print("He takes another lunge at you")
                zombie_hp = zombie_hp - 1
            else:
                print("You kill the zombie and leave him dead on the floor")
                print("You go towards the doorway ahead")
                vault()


        if health == 0:
            print("You are dead")
            quit()

    if weapon.lower() == "b":
        print("You throw a torch towards the moaning and take your shot")
        

        if hit_chance == 1:
                    print("You pierced the zombie's skull")
                    vault()

        if hit_chance == 2 or hit_chance == 3:
            print("The zombie leaps at you")
            print("Your health drops by 5 but the zombie fades to dust")
            print("You progress onwards")
            health = health - 5
            vault()
                    

def vault():
    global health

    print("After your tough battle you walk into a vault like room")
    print("You see two different prizes but you can only take one")
    print("G. A golden chalice with a mysterious liquid")
    print("J. A jewelry box")

    choice = input("Choice: ")

    if choice.lower() == "g":
        print("You drink the liquid and drop dead, your adventure for nothing")
        health = health - health
        print("You have died")
        quit()

    if choice.lower() == "j":
        print("You take the jewelry box and run out the way you came")
        print("You win: value of treasure - $500")
        quit()


def room2():
    global health
    global poison_count
    global mist_potion
    global fire_potion
    global poison_true

    print("Strange symbols scatter the ground around you, each one leading to a different door")
    print("One Green, One red, One blue")
    print("Where do you stand")
    print("G: Green")
    print("R: Red")
    print("B: Blue")

    symbol = input("Symbol: ")

    if symbol.lower() == "g":
        print("A strange mist overcomes you but you feel normal")
        if mist_potion == True:
            print("You remember your potion showing this room and drink it")
            print("The mist disappears and you feel fine")
            graveyard()
        if mist_potion == False:
            poison_count = 3
            print("You go onwards")
            graveyard()

    if symbol.lower() == "r":
        print("Fire spurts up into you")
        print("You feel some pain but not too much")
        health = health - 3
        print("Health: " ,health)
        butchers()

    if symbol.lower() == "b":
        print("Ice slowly overcomes your body")
        if fire_potion == True:
            print("You remember the fire potion and decide to drink it as this ice will kill you")
            print("The ice melts and you go onwards")
            ice_vault()
        if fire_potion == False:
            print("You are frozen")
            print("Game over")
            quit()

def graveyard():
    global poison_count
    global poison_true

    poison()
    
    print("Nothing is in the graveyard but a two doors")
    print("Do you enter")
    print("A. The Chapel Door")
    print("B. The Butchers")

    door = input("Door: ")

    if door.lower() == "a":
        if poison_count == -1:
            print("There is a mysterious ward on the door and you can't get in")
            print("You go into the butcher's")
            butchers()
        else:
            print("You enter the chapel")
            chapel()

    if door.lower() == "b":
        print("You enter the butchers")
        butchers()

def chapel():

    poison()

    print("You walk through the rows of pews to the altar where a potion stands")
    print("A ghostly apparition appears and speaks to you")
    print("You have only have a small amount of time left")
    print("That green mist was poison, the only cure is this potion")
    print("Drink it and leave this place or progress and die")
    print("D. Drink")
    print("P. Progress")

    choice = input("Choice: ")

    if choice.lower() == "d":
        print("You are teleported out of the crypt but you feel healthy again")
        print("Good Ending...")
        quit()

    if choice.lower() == "p":
        print("You leave to go to the butchers")
        poison()


def butchers():

    poison()

    print("A mad butcher, cleaver in hand patrols the shop")
    print("Do you...")
    print("S. Sneak past him")
    print("R. Run screaming to the next door")

    choice = input("Choice: ")

    if choice.lower() == "s":
        print("As you sneak along the floor you knock a rack of meat over")
        print("The butcher spots you and comes towards you")
        print("Do you run or not")
        print("Y. Yes")
        print("N. No")

        run = input("Run: ")
        if run.lower() == "y":
            print("When you stand to run the butcher grabs your skull and crushes it in his hands")
            print("Game over")
            quit()
        if run.lower() == "n":
            print("You cower in a corner ready to embrace death")
            print("The butcher is chained and cannot reach you")
            print("He seems to instantaniously forget about you so you can move on")
            arena()

    if choice.lower() == "r":
        print("You narrowly avoid his grasp and make it to the door")
        arena()

def arena():
    boss_hp = 10
    global health
    poison()

    print("You approach a towering gate and as you reach the center the gate opens")
    print("You walk through the now open gate into the center of the room")
    print("You hear lots of cheering and look around")
    print("It seems like you are in some kind of colosseum")
    print("A crowd member throws a sword to your hand and says")
    print("Get prepared here it comes")
    print("Another gate opens and a skeletal collosal emerges")
    print("You need to fight")
    print("Do you run at him or wait for him to come to you")
    print("W. Wait")
    print("R. Run at him")

    battle_choice = input("Battle Choice: ")

    if battle_choice.lower() == "w":
        print("You wait for the brute to reach you but he stays still")
        print("Everything goes silent")
        print("You pass out")
        print("You wake up in an open field outside")
        print("You have escaped the nightmare")
        print("Good Ending")
        quit()

    if battle_choice.lower() == "r":
        print("You run at the collosal")
        print("He stays still")
        print("Do you...")
        print("S. Slash his arm with your sword")
        print("H. Hit the leg")

        battle_choice = input("Battle Choice: ")

        if battle_choice.lower() == "s":
            print("You chop both his arms off in one swoop but he kicks you back")
            health = health - 4
            print("Health: " ,health)
            boss_hp = boss_hp - 5
            print("You feel immense pain but stand back up")
            print("Do you...")
            print("F. Flee back to the butchers")
            print("C. Charge towards the monster")

            battle_choice = input("Battle Choice: ")

            if battle_choice.lower() == "c":
                print("Yet again the skeleton hits you and you can't avoid")
                print("That is it for you")
                print("As light fades the skeleton approaches you and carries you to the butchers")
                print("The butcher cuts you open, but you still stay alive")
                print("Just as he is about to pull out your intestines you hear a bang")
                print("The whole roof caves in everybody dies")
                print("Game Over")
                quit()

            if battle_choice.lower() == "f":
                print("You slowly back into the butchers")
                print("Do you...")
                print("C. Chop the butcher's chain off")
                print("B. Back away more")

                battle_choice = input("Battle Choice: ")

                if battle_choice.lower() == "c":
                    print("When you chop the butcher's chain in half he progresses to grab you")
                    print("He slices you in half")
                    print("Game Over")
                    quit()

                if battle_choice.lower() == "b":
                    print("The butcher grabs the skeleton's skull and crushes it with it's bear hands")
                    print("The collosal is dead")
                    print("You now return to the arena and you see another gate is open")
                    print("You progress")
                    treasure_room()
            

        if battle_choice.lower() == "h":
            print("You chop the beast's legs of and he lies flat on the floor")
            print("He starts using his arms to move")
            boss_hp = boss_hp - 3

            print("Do you...")
            print("S. Stab him in the head")
            print("H. Hit where his legs used to be")

            battle_choice = input("Battle Choice: ")
            

            if battle_choice.lower() == "h":
                print("You end up hitting his heart and he falls dead you can progress to the treasure room")
                treasure_room()
                

        if battle_choice.lower() == "s":
            print("You strike his skull with the sword but his head is too strong")
            print("The sword bounces back up and hits you in the neck")
            health = health - 7
            if health == 0:
                print("You have died")
                print("Game Over")
                quit()
            else:
                print("You instantly strike through his chest in a pain induced rage")
                print("He dies and you can now progress")
                print("A hidden hole in the arena opens and an announcer speaks to you")
                print("He has did it, the first person to not only survive but defeat the skelton in the hidden way")
                print("Enjoy the greatest treasure the crypt has to give")
                secret_treasure()


def treasure_room():

    print("You have reached the fruit of your troubles")
    print("Treasure chests as far as you can see litter the floor")
    print("Good Ending")
    print("Treasure Value: $72,000")
    quit()

def secret_treasure():

    print("Due to you completeing the hidden task the golden monkey stands above you")
    print("It is the most renown treasure never to be found")
    print("Until now")
    print("Secret Ending")
    print("Treasure Value: $1,000,000,000")
    quit()

def armory():
    global mist_potion
    global fire_potion

    print("When you enter the room you see three potions")
    print("One with a picture of fire on a human")
    print("Another showing a room covered in green mist")
    print("The final has no label")
    print("Which do you take")
    print("A. Fire Potion")
    print("B. Mist Potion")
    print("C. Mystery Potion")

    potion = input("Potion: ")

    if potion.lower() == "a":
        fire_potion = True
        print("With your fire potion you return to the first room")
        room1()

    if potion.lower() == "b":
        mist_potion = True
        print("With your mist potion you return to the first room")
        room1()

    if potion.lower() == "c":
        print("You decide to drink the mystery potion")
        print("Nothing Happens")
        print("You go back to the first room")
        room1()

def ice_vault():

    print("You enter a vault of snow with treasure all around")
    print("You take the treasure and leave")
    print("Good Ending")
    print("Treasure Value: $10,000")
    quit()
          

    
        
                
                  
            

        

    
        
    
        
        

    
   


# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
