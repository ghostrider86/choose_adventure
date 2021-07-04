
def game_1():
    #Start of Adventure
    name = input("Every adventurer needs a name, what is your name adventurer?\n")
    print(name + " huh, thats a great name.\n")
    print("Now " + name + ", every adventurer needs weapons, how about three?\n")

    # Gear of Choice, 


    gear_1 = "sword"
    gear_2 = "bow"
    gear_3 = "wand"

    WayToGo = ["left", "right", "forward"]

    choice = input("In front of you you see three weapons a SWORD, a BOW, and a WAND\n Will you use them? YES/NO\n")
    if choice == "yes":
        print("You pick up your weapons and try to test them out")
    else:
        print("Why not?")
        if choice == "no":
            print("Without these you cant be an adventurer, anyway lets try them out")
            
            

    # Next
    print("Now that you have your weapon lets try it out!\n")
    choice = input("You see a dummy in front of you\n Will you use the SWORD, BOW, or WAND? \n")
    if choice == gear_1:
        print("You ready your weapon")
        if choice == "sword":
            print("Using your sword you hack the dummy to pieces")
    if choice == gear_2:
        print("You ready your weapon")
        if choice == "bow":
            print("Using your bow you notch an arrow in the dummie's head")
    if choice == gear_3:
        print("You ready your weapon")
        if choice == "wand":
            print("Using your wand you fire a magic missle and blast off the dummie's head")
        else: 
            print("you need to pick a weapon")
                    

    # Next
    print("You are now ready for your advenuture, you head towards a nearby dungeon to test your skills.\n")
    print("On your way to the dungeon you hear some rustling in some nearby bushes, and you are ambushed by some goblins\n")
    choice = input("Will you use the SWORD, BOW, or WAND? \n")
    if choice == gear_1:
        print("You ready your weapon")
        if choice == "sword":
            print("Using your sword you easily dipatch the goblins")
    if choice == gear_2:
        print("You ready your weapon")
        if choice == "bow":
            print("you try to use your bow but they are to close and easily take you out\n YOU ARE DEAD")
            quit()
    if choice == gear_3:
        print("You ready your weapon")
        if choice == "wand":
            print("Using your wand you fire a magic missle and blast the goblins")
        else: 
            print("you need to pick a weapon")


    # Next

    WayToGo = input("After defeating the goblins you enter the dungeon you are faced with three doors, will you go STRAIGHT, LEFT, or RIGHT.\n")
    if WayToGo == "left":
        print("You enter a room with slimes, you ready your weapon")
        if WayToGo == "left":
            choice = input("You prepare yourself to face the slimes, Will you use the SWORD, BOW, or WAND? \n")
        if choice == gear_1:
            print("You ready your weapon")
            if choice == "sword":
                print("you try to use your sword, but your attacks bounce off them like jelly and they eat you.\n YOU ARE DEAD")
                
        if choice == gear_2:
            print("You ready your weapon")
            if choice == "bow":
                print("you try to use your bow and aim an arrow at their core and defeat them, you move forward.\n")
        if choice == gear_3:
            print("You ready your weapon")
            if choice == "wand":
                print("Using your wand you fire a magic missle and blast the slimes, you move forward.\n ")
    elif WayToGo == "right":
        print("You enter a room with more goblins, you ready your weapon")
        if WayToGo == "right":
            choice = input("You prepare yourself to face the goblins, Will you use the SWORD, BOW, or WAND? \n")
            if choice == gear_1:
                print("You ready your weapon")
                if choice == "sword":
                    print("Using your sword you easily dipatch the goblins, you move forward\n")
            if choice == gear_2:
                print("You ready your weapon")
                if choice == "bow":
                    print("you use your bow and snipe the goblins at the end of the room, you move forward\n")
            if choice == gear_3:
                print("You ready your weapon")
                if choice == "wand":
                    print("Using your wand you fire a fireball in the room however the room is too small and you blast yourself as well.\n YOU ARE DEAD")
                    
    elif WayToGo == "straight":
        print("You enter the room, but it appears to be empty so you continue")
        if WayToGo == "straight":
            print("with nothing in the room you move forward.")
        else: 
            print("with nothing in the room you move forward.")
    else:
        print("unable to decide you go forward and find yourself in an empty room.")

    # Next

    print("Moving Forward you find yourself at the end of the dungeon, and you see a chest\n")
    choice = input("Will you open the chest? YES/NO")
    if choice == "yes":
        print("You open the chest to find a bag with gold pieces!")
        if choice == "yes":
            print("Congratulations, you have completed your first adventure, may many more continue\n THE END")
            
    else:
        print("Thinking the chest is a trap, you leave it alone")
        if choice == "no":
            print("Congratulations, you have completed your first adventure, may many more continue\n THE END")