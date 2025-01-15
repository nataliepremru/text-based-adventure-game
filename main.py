
# def turn_r():
#     print("You have chosen to turn r")

# def turn_l():
#     print("You have chosen to turn l")

# def walk_straight():
#     print("You have chosen to walk straigh")

TRACK = []

def choose_direction(current):
    choosen_direction = input("left or right or forward or back (r/l/f/b): ").lower()
    if current == 0:
            if choosen_direction == "l":
                room1()
            elif choosen_direction == "r":
                room2()
            else:
                print("Please choose a direction")
    elif current == 1:
            if choosen_direction == "l":
                room3()
            elif choosen_direction == "forward":
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
        elif choosen_direction == "forward":
            room7()
        elif choosen_direction == "r":
            room8()
        else:
            print("Please choose a direction")
    elif current == 5:
        print("Only forward")
        room9()

def cell():
    TRACK.append(0)
    print("Start")
    choose_direction(0)


def room1():
    TRACK.append(1)
    print("Guard dog is sleeping")
    # print("Game Over!")
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

def room5():
    TRACK.append(5)
    print("Toilet with company")

def room6():
    TRACK.append(6)
    print("")

def room7():
    TRACK.append(7)
    print("")

def room8():
    TRACK.append(8)
    print("Game Over")

def room9():
    TRACK.append(9)
    print("Window")

def room10():
    TRACK.append(10)
    print("")

def room11():
    TRACK.append(11)
    print("")

def room12():
    TRACK.append(12)
    print("")

def room13():
    TRACK.append(13)
    print("")

def room14():
    TRACK.append(14)
    print("")

def room15():
    TRACK.append(15)
    print("")


def prison_break():
    cell()
    print(TRACK)


prison_break()