
# def turn_r():
#     print("You have chosen to turn r")

# def turn_l():
#     print("You have chosen to turn l")

# def walk_straight():
#     print("You have chosen to walk straigh")

TRACK = []

def choose_direction(current):

    choosen_direction = input("left or right or forward or back or you can choose to exit the game with q (r/l/f/b/q): ").lower()

    if current == 0:
            if choosen_direction == "l":
                room1()
            elif choosen_direction == "r":
                room2()
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
        else:
            print("Please choose a direction")
            room4()

    elif current == 5:
        if choosen_direction == "f":
            room9()
        elif choosen_direction == "b":
            room1()
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
        else:
            print("Please choose a direction")
            room6()

    elif current == 7:
        if choosen_direction == "f":
            room4()
        elif choosen_direction == "b":
            room4()
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
        else:
            print("Please choose a direction")
            room9()


def cell():
    print("Start")
    TRACK.append(0)
    choose_direction(0)

def room1():
    TRACK.append(1)
    print("Guard dog is sleeping")
    choose_direction(1)

def room2():
    TRACK.append(2)
    print("Prison Guard")
    print("Game Over!")

def room3():
    TRACK.append(3)
    print("Guard Dog")
    print("Game Over!")

def room4():
    TRACK.append(4)
    print("Canteen")
    choose_direction(4)

def room5():
    TRACK.append(5)
    print("Toilet with company")
    choose_direction(5)

def room6():
    TRACK.append(6)
    print("Empty Guardroom with keys")
    choose_direction(6)

def room7():
    TRACK.append(7)
    print("Storage Room")
    choose_direction(7)

def room8():
    TRACK.append(8)
    print("Kitchen Alarm")
    print("Game Over")

def room9():
    TRACK.append(9)
    print("Window to courtyard")
    choose_direction(9)

def room10():
    TRACK.append(10)
    print("Guard")
    print("Game Over")

def room11():
    TRACK.append(11)
    print("Break")
    print("Congratz!")

def room12():
    TRACK.append(12)
    print("Guard")
    print("Game Over")

# def room13():
#     TRACK.append(13)
#     print("")

def room14():
    TRACK.append(14)
    print("Hole in fence")
    print("Congratz!")

def room15():
    TRACK.append(15)
    print("Spotted")
    print("Game Over")


def prison_break():
    cell()
    print(TRACK)


prison_break()