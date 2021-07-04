def game_2():
    # Setup
    yes_no = ["yes", "no"]
    directions = ["left", "right", "forward", "backward"]
    
    # Introduction
    name = input("What is your name, adventurer?\n")
    print("Greetings, " + name + ". Let us go on a quest!")
    print("You find yourself on the edge of a dark forest.")
    print("Can you find your way through?\n")
    
    # Start of game
    response = ""
    while response not in yes_no:
        response = input("Would you like to step into the forest?\nyes/no\n")
        if response == "yes":
            print("You head into the forest. You hear crows cawwing in the distance.\n")
        elif response == "no":
            print("You are not ready for this quest. Goodbye, " + name + ".")
            quit()
        else: 
            print("That is not the right answer, friend\n")
    
    # Next part of game
    response = ""
    while response not in directions:
        print("To your left, you see a bear.")
        print("To your right, there is more forest.")
        print("There is a rock wall directly in front of you.")
        print("Behind you is the forest exit.\n")
        response = input("What direction do you move?\nleft/right/forward/backward\n")
        if response == "left":
            print("The bear eats you. Farewell, " + name + ".")
            quit()
        elif response == "right":
            print("You head deeper into the forest.\n")
        elif response == "forward":
            print("You cannot scale the wall.\n")
            response = "" 
        elif response == "backward":
            print("You leave the forest. Goodbye, " + name + ".")
            quit()
        else:
            print("That is not the right answer, friend\n")

            # Next part of game
    response = ""
    while response not in yes_no:

        response = input("You move deeper into the forest, and you come across a chest, do you open it?\nyes/no\n")
        if response == "yes":
            print("You open the chest at the bottom lies a map. The map shows directions to several miles of the dark forest and says that for your next 3 choices of direction you need to go right.\n")
        elif response == "no":
            print("You continue on your journey ignoring the chest's contents. " + name + ".")
            quit()
        else: 
            print("That is not the right answer, friend\n")

            # Next part of game
    response = ""
    while response not in directions:
        print("To your right, there is more forest.")
        print("To your left, there is more forest.")
        print("There is more forest directly in front of you.")
        print("Behind you is the forest exit.\n")
        response = input("What direction do you move?\nleft/right/forward/backward\n")
        if response == "left":
            print("You head deeper into the forest.\n")
        elif response == "right":
            print("You head deeper into the forest.\n")
        elif response == "forward":
            print("You head deeper into the forest.\n")
        elif response == "backward":
            print("You leave the forest. Goodbye, " + name + ".")
            quit()
        else:
            print("That is not the right answer, friend\n")

                # Next part of game
    response = ""
    while response not in directions:
        print("To your right, there is more forest.")
        print("To your left, there is more forest.")
        print("There is more forest directly in front of you.")
        print("Behind you is the forest exit.\n")
        response = input("What direction do you move?\nleft/right/forward/backward\n")
        if response == "left":
            print("As you move deeper in the forest, you feel the ground shift beneath you. You have fallen in a spiked pitfall trap and have died.")
            quit()
        elif response == "right":
            print("You head deeper into the forest.\n")
        elif response == "forward":
            print("You head deeper into the forest.\n")
        elif response == "backward":
            print("You leave the forest. Goodbye, " + name + ".")
            quit()
        else:
            print("That is not the right answer, friend\n")

                        # Next part of game
    response = ""
    while response not in directions:
        print("To your right, there is more forest.")
        print("To your left, there is more forest.")
        print("There is more forest directly in front of you.")
        print("Behind you is the forest exit.\n")
        response = input("What direction do you move?\nleft/right/forward/backward\n")
        if response == "left":
            print("As you move deeper in the forest, you feel the ground shift beneath you. You have fallen in a spiked pitfall trap and have died.")
            quit()
        elif response == "right":
            print("You head deeper into the forest till you come into a clearing in the forest where you see a cave.\n")
        elif response == "forward":
            print("As you move deeper in the forest, you feel the ground shift beneath you. You have fallen in a spiked pitfall trap and have died.")
            quit()
        elif response == "backward":
            print("You leave the forest. Goodbye, " + name + ".")
            quit()
        else:
            print("That is not the right answer, friend\n")

            # Next part of game

            response = ""
    while response not in yes_no:
        response = input("Will you enter the cave?\nyes/no\n")
        if response == "yes":
            print("You head into the cave, its dark but as you see a nearby torch and use it to move deeper into the cave.\n")
        elif response == "no":
            print("You are not ready for this quest. Goodbye, " + name + ".")
            quit()
        else: 
            print("That is not the right answer, friend\n")

    # Next part of game
            response = ""
    while response not in directions:
        response = input("As you move deeper in the cave, you hear screams, and the echos of screams grows louder the deeper you move in the cave. You press forward steelng yourself for whats ahead until you come to a fork in the cave.\nleft/right/backward\n")
        if response == "left":
            print("You decide to go left and head deeper into the cave, as you head deeper you are stoped by a large wooden door. You try the door, but its locked so you head beack where you came.")
            response = "" 
        elif response == "right":
            print("You decide to go right, as you move forward the screams get louder until you enter a large oval room where you see an altar in the center and a cloaked figure standing by.\n")
        elif response == "backward":
            print("You leave the scary cave. Goodbye, " + name + ".")
            quit()
        else: 
            print("That is not the right answer, friend\n")    

    # Next part of game
            response = ""
    while response not in yes_no:
        response = input("As you approach the cloaked figure he turns to you, and you see a older man with a very pale complexsion, you also noticed that there is someone on the altar, you assume they are dead but you sill see them breathing. The old man speaks and asks why you have come here, he gives you the option to leave if not he states that he will kill you. Will you fight the Necromancer?\nyes/no\n")
        if response == "yes":
            print("You ready your sword to fight the necromancer. He laughs, and tells you how stupid you are to face a necromancer.\n")
        elif response == "no":
            print("Fearing for your life you flee the cave, and you never turn your back. Goodbye, " + name + ".")
            quit()
        else: 
            print("That is not the right answer, friend\n")

    # Next part of game
            response = ""
    while response not in directions:
        response = input(" The necromancer fires a burst of black energy towards you, What direction do you move?\nleft/right/forward/backward\n")
        if response == "left":
            print("You jerk yourself to the left barely dodging the negative energy, and you notice the rocks behind you get vaporized by the blast.")
            
        elif response == "right":
            print("You jerk yourself to the right barely dodging the negative energy, and you notice the rocks behind you get vaporized by the blast.\n")
        elif response == "forward":
            print("You head straight towards the black energy and are vaporized, all thats left are your bones.")
            quit()
        elif response == "backward":
            print("You decide fighting him wasnt a good idea and you run. Goodbye, " + name + ".")
            quit()
        else:
            print("That is not the right answer, friend\n")



            # Next part of game
            response = ""
    while response not in yes_no:
        response = input("As you consider the danger of continuing to face this Necromancer, you begin to ask yourself if this adventure was worth it, this is your last chance to flee. Do you?\nyes/no\n")
        if response == "no":
            print("You gather your reslove and close the distance between you and the Necromancer.\n")
        elif response == "yes":
            print("Deciding that the consequences are too severe you flee the cave, and you never turn your back. Goodbye, " + name + ".")
            quit()
        else: 
            print("That is not the right answer, friend\n")

            # Next part of game
            response = ""
    while response not in directions:
        print("You have closed the distance between him and you, and you notice in his right hand a book")
        print("You have closed the distance between him and you, and you notice in his left hand a staff")
        print("You have closed the distance between him and you, and directly in front of you is the necromancer.")
        print("Behind you is the exit\n")
        response = input("What direction will you attack?\nleft/right/forward/backward\n")
        if response == "left":
            print("You aim for the arm with the staff, and you succefully slice the staff in half as he tries to block your sword. The Necromancer angred by this states he will get his revenge and vanishes.")
        elif response == "right":
            print("You aim for the arm with the book, and you succefully slice the book in two as he tries to block your sword. The Necromancer angred by this states he will get his revenge and vanishes.\n")
        elif response == "forward":
            print("You aim staight towards his chest and you stab him in his heart, the necromancer staggers back and dies.")
        elif response == "backward":
            print("You decide to flee, running towards the exit but as you reach the exit you hear a sound behind you and are vaporized. Goodbye, " + name + ".")
            quit()
        else:
            print("That is not the right answer, friend\n")

    # Next part of game
            
    while response not in yes_no:
        response = input("Having defeated the Necromancer, you approach the figure on the table and see that it was a small child. You take the child in your arms and leave the cave and the forrest. As you take the child to your home and you wonder if you should continue on your adventure, or return to your daily life as a farmer. Will you continue your adventure?\nyes/no\n")
        if response == "yes":
            print("Having defeated a mighty foe, and saved a life you look forward to the many adventures you will have, and thus the ends the first part of " + name + "'s story. THE END!\n")
            quit()
        elif response == "no":
            print("Content with the adventure you had, you are fine with returning to your old life Goodbye, " + name + ". THE END!")
            quit()
        else: 
            print("That is not the right answer, friend\n")
