# List to track the player's path
TRACK = []

# Function to choose the direction based on the current room
def choose_direction(current):
    choosen_direction = input("left or right or forward or back or you can choose to exit the game with q (r/l/f/b/q): ").lower()

    if current == 0:
        if choosen_direction == "l":
            room1()
        elif choosen_direction == "r":
            room2()
        elif choosen_direction == "f":
            print("Ow! You run into a wall... Choose again")
            cell()
        elif choosen_direction == "b":
            print("Ow! You run into a wall... Choose again")
            cell()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            cell()

    elif current == 1:
        if choosen_direction == "l":
            room3()
        elif choosen_direction == "f":
            room4()
        elif choosen_direction == "r":
            room5()
        elif choosen_direction == "b":
            cell()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            room1()

    elif current == 4:
        if choosen_direction == "l":
            room6()
        elif choosen_direction == "f":
            room7()
        elif choosen_direction == "r":
            room8()
        elif choosen_direction == "b":
            room1()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            room4()

    elif current == 5:
        if choosen_direction == "f":
            room9()
        elif choosen_direction == "b":
            room1()
        elif choosen_direction == "l":
            print("You run into a cubicle, theres no where to go from here. Choose again.")
            room5()
        elif choosen_direction == "r":
            print("Ow! You run into a sink. Choose again.")
            room5()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            room5()

    elif current == 6:
        if choosen_direction == "l":
            room10()
        elif choosen_direction == "f":
            room11()
        elif choosen_direction == "r":
            room12()
        elif choosen_direction == "b":
            room4()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            room6()

    elif current == 7:
        if choosen_direction == "f":
            room4()
        elif choosen_direction == "b":
            room4()
        elif choosen_direction == "l":
            print("Ow! You run into a wall. Choose again.")
            room7()
        elif choosen_direction == "r":
            print("Ow! You run into a wall. Choose again.")
            room7()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            room7()

    elif current == 9:
        if choosen_direction == "l":
            room14()
        elif choosen_direction == "r":
            room15()
        elif choosen_direction == "b":
            room5()
        elif choosen_direction == "f":
            print("Ow! You run into the fence. Choose again.")
            room9()
        elif choosen_direction == "q":
            return
        else:
            print("Please choose a direction")
            room9()

# Initial room where the player starts
def cell():
    print('\n')
    print("-" * 100)
    print("Hello, welcome to Pentonville Prison.\n You are an inmate serving a life sentence for a crime you did you not commit. \n About 2 hours ago a guard dropped his keys as he passed your cell but it wasn't a good time to leave. \n The coast is finally clear... this is your chance... you unlock the door...\n You are stood in the hallway and you can go either left or right. \n Which do you choose?")
    TRACK.append(0)
    choose_direction(0)

# Room 1 logic
def room1():
    print('\n')
    print("-" * 100)
    TRACK.append(1)
    print("At the end of the hallway you find a guard dog sleeping.\n You can either go left, right or forward.\n Which do you chose?")
    choose_direction(1)

# Room 2 logic
def room2():
    print('\n')
    print("-" * 100)
    TRACK.append(2)
    print("You run into a guard, game over.")
    print("Game Over!")

# Room 3 logic
def room3():
    print('\n')
    print("-" * 100)
    TRACK.append(3)
    print("You have woken up the dog, game over.")
    print("Game Over!")

# Room 4 logic
def room4():
    print('\n')
    print("-" * 100)
    TRACK.append(4)
    print("You find yourself in the canteen.\n Luckily no one is here right now.\n There are three possible doors to take, which one do you chose? ")
    choose_direction(4)

# Room 5 logic
def room5():
    print('\n')
    print("-" * 100)
    TRACK.append(5)
    print("You have entered the toilets where you find your friend.\n He tells you theres a rumour of a gap in the fence but doesn't know where.\n It seems theres nowhere else to go apart from forwards out the window.\n They offers to give you a lift, what do you decide to do? ")
    choose_direction(5)

# Room 6 logic
def room6():
    TRACK.append(6)
    print("You have found yourself in the guards room... by some miracle theres no guards in here right now and theres a set of keys for the staff exit on the table.\n However theres three possible doors to take and you don't have time to try them all.\n Which one do you chose?")
    choose_direction(6)

# Room 7 logic
def room7():
    TRACK.append(7)
    print("You are in a storage cupboard with nowhere else to go, you must turn back.")
    choose_direction(7)

# Room 8 logic
def room8():
    print('\n')
    print("-" * 100)
    TRACK.append(8)
    print("You enter the kitchen but the chef is on duty cooking tonight's dinner.\n In a panic he rings the alarm, game over.")
    print("Game Over")

# Room 9 logic
def room9():
    print('\n')
    print("-" * 100)
    TRACK.append(9)
    print("You are now in the courtyard.\n You remember your friend telling you about a gap in the fence but was it right or left?")
    choose_direction(9)

# Room 10 logic
def room10():
    print('\n')
    print("-" * 100)
    TRACK.append(10)
    print("You're in the staff toilets where you run into a guard, game over.")
    print("Game Over")

# Room 11 logic
def room11():
    print('\n')
    print("-" * 100)
    TRACK.append(11)
    print("You successfully exit through the staff exit without being caught.")
    print("Congratulations!")

# Room 12 logic
def room12():
    print('\n')
    print("-" * 100)
    TRACK.append(12)
    print("The door leads out to the courtyard where you get spotted by a guard, game over.")
    print("Game Over")

# Room 14 logic
def room14():
    print('\n')
    print("-" * 100)
    TRACK.append(14)
    print("You found the hole in the fence and succesfully escaped Pentonville.\n Congratulations.")
    print("Congratz!")

# Room 15 logic
def room15():
    print('\n')
    print("-" * 100)
    TRACK.append(15)
    print("You get spotted by a guard on the watch tower, game over.")
    print("Game Over")

# Main function to start the game
def prison_break():
    cell()
    print(f"This is the route you have taken {TRACK}")

# Start the game
prison_break()