#!/usr/bin/env python3

# Exercise 36. Designing and Debugging

# Rules for if-statements
# -----------------------
# every if-statement must have an else
# if the else ist not run, is must contain a die function
# never nest if-statements more than two levels deep
# if-statements are to be treated as paragraphs, put blank lines before and after
# boolean tests should be simple

# rules for loops
# ---------------
# use a while loop only to loop forever
# use a for-loop for all other kinds of looping

# TODO

from time import sleep
from random import randint

# amount of keys 
keys = 0
# green potion found yet?
green_potion = False


def wait(seconds=3, wait_char="."):
    """
    wait for an ammount of seconds
    """
    
    for _ in range(1, seconds):
        print(wait_char)
        sleep(1)


# ---------------------------
def room_entrance():
    """
    this function describes the entrance of the dungeon
    """
    
    global keys

    print()
    print("You are standing in the entrance room.")
    print("The rooms light is coming from torches attached to the walls.")

    display_keys()
    display_potions()

    print("Directions:")
    print("  (w)est  \t: a dark room")
    print("  (n)orth \t: you can hear voices behind the big door")
    print("  (e)ast  \t: a big door is blocking your view to this room")
    print("  (s)outh \t: exit dungeon")

    choice = input("> ").strip()

    if choice == 's':
        print("You exit the dungeon and see the door closing.")
        print("There is no second chance for you.")
        exit(0)
    
    elif choice == 'w':
        print("You move to the west room.")
        room_key_1()
    
    elif choice == 'n':
        print("You move north. Entering the big rooms")
        room_boss()
    
    elif choice == 'e':
        
        if(keys > 0):
            print("You open the door with on of your keys and step forward.")
            room_chest_1()
        
        else:
            print("Without any keys, you cannot open the door.")
            room_entrance()
    
    else:
        print("Command not found. Please use one of [n,e,s,w]")
        room_entrance()


def display_keys():
    if keys > 0:
        print(f"You have found the key.")
    
    else:
        print("No keys")


def display_potions():
    global green_potion
    
    if green_potion:
        print("You have a green potion which makes you stronger")
    
    else:
        print("No potions found yet.")


# ---------------------------
def room_key_1():
    """
    this function describes the the rooms where you find the first key
    """
    global keys

    print()
    print("After moving west, you are now standing in a dark room.")
    print("A bit of light is coming from behind.")
    
    if keys < 1:
        print("You can barely see a monster.")
        print("What do you do?")
        print("  (a)ttack\t: attack the monster")
        print("  (f)lee\t: try to flee")
    else:
        print("You alread defeated the monster here.")
        print("There is nothing left for you to do.")
        print("  (r)eturn\t: go back to the entrance")
        

    choice = input("> ").strip()
    
    if choice == 'a':
        print("You attack the monster.")
        wait(1)
        print("You barely hit, and try it again.")
        wait(1)
        print("Finally you were able to hit the monster which vanishes it front of your eyes.")
        print("You hear a quiet sound from a key dropping onto the floor.")
        keys += 1
        wait(1)
        print("After picking up the key, you return to the entrance.")
        input("Press enter to continue...")
        room_entrance()
    
    elif choice == 'f':
        print("You try to flee.")
        wait(randint(2,4))
        print("You are able to escape the monsters claws. You managed to flee. ")
        print("Back in the entrance room, you have the feeling, that you need to go back.")
        input("Press enter to continue...")
        room_entrance()
    
    elif choice == 'r':
        room_entrance()

    else:
        print("Command not found. Please use one of [a,f]")
        room_key_1()


# ---------------------------
def room_chest_1():
    """
    this function describes the the room with the first chest
    """
    global keys
    global green_potion

    print()
    print("After opening the door, you stand in bright room ")
    print("where you can see a chest in the middle on the floor.")
    print()
    print("What do you do?")
    print("  (o)pen\t: open the chest")
    print("  (w)est\t: go back to the entrance")

    choice = input("> ").strip()
    
    if choice == 'o':
        print("You try to open the chest.")
        wait(1)
        if not green_potion:
            print("You find a green potion.")
            print("It looks like that increases your strength.")
        else:
            print("Oh no, the chest is empty.")
            print("You already collected the green potion from this chest.")
        green_potion = True
        room_entrance()

    elif choice == 'w':
        print("You go back to the entrance.")
        room_entrance()
        
    else:
        print("Command not found. Please use one of [o,w]")
        room_chest_1()


# --------------------------
def room_boss():
    """
    this function describes the the room with the first chest
    """
    global green_potion

    potion_consumed = False

    # after three tries you are able to hit the boss
    tries = 1

    print()
    print("You are in the room with the boss. He seems to be very angry.")
    print("The door behind you is closed. There is no way out, except in defeating the boss.")

    print("What do you do?")
    print("  (a)attack\t: attack the boss")
    
    if not potion_consumed and green_potion:
        print("  (d)rink\t: drink the green potion")
    
    elif not potion_consumed and not green_potion:
        print("  (d)rink\t: drin the red potion right next to the door")
        
    else:
        print("  There is no potion to consume.")

    choice = input("> ").strip()

    if choice == 'a':
        print("With a fast and unexpected move by the boss,")
        print("you run fast and get behind the boss.")
        
        if potion_consumed and green_potion:
            print("With the power of the green potion you manage")
            print("to hit the boss so hard, that he falls onto the ground.")
            end()
        
        elif tries >= 3:
            print("After hitting the boss three times, he collapses.")
            end()

        else:
            print("You hit the boss. But he just laughs at you.")
            tries += 1

            if randint(1,10) == 9:
                print("The boss looks at you and hits you with his fist.")
                print("You fall to the ground and your life is leaving your body.")
                print("You are dead.")
                exit(0)

            else:
                print("The boss looks at you and tries to hit you with his fist.")
                print("You can barely escape and reposition yourself back at the door.")
                room_boss()

    elif choice == 'd':
        
        if green_potion:
            print("You drink the green potion. You feel very strong now.")
        
        else:
            print("You drink the red potion. You feel weaker now.")
            print("You need more hits on the boss now.")
            tries -= 2
        
        potion_consumed = True
        room_boss()
        
    else:
        print("Command not found. Please use one of [o,w]")
        room_boss


# ---------------------------
def end():
    print("You grab the jewel from the podest and head back up the stairs.")
    wait(2)
    print("You take a deep breath of air when you reach back out of the dungeon.")
    exit(0)

# ---------------------------
def start():
    print("You, the brave hero stand in front of the dungeon.")
    print("Gathering all your courage you go down the dark steps.")
    wait(1)
    
    print("After reaching the last step you look around to find out where you are.")
    room_entrance()


# ---------------------------
if __name__ == "__main__":
    start()