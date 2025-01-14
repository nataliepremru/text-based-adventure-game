
# def turn_r():
#     print("You have chosen to turn r")

# def turn_l():
#     print("You have chosen to turn l")

# def walk_straight():
#     print("You have chosen to walk straigh")

TRACK = []

def cell():
    print("Start")
    choose_direction(0)

def room1():
    print("Guard dog is sleeping")
    # print("Game Over!")
    choose_direction(1)

def room2():
    print("Prison Guard")
    print("Game Over!")
    exit()

def room3():
    print("Guard Dog")
    print("Game Over!")
    exit()

def room4():
    print("Canteen")

def room5():
    print("Toilet with company")

def room6():
    print("")

def room7():
    print("")

def room8():
    print("Game Over")

def room9():
    print("Window")

def room10():
    print("Window")

def room11():
    print("Window")

def room12():
    print("Window")

def room13():
    print("Window")

def room14():
    print("Window")

def room15():
    print("Window")

def choose_direction(current):
    choosen_direction = input("left or right (r/l): ").lower()
    if current == 0:
        # choosing = True
        # while choosing:
            if choosen_direction == "l":
                room1()
                TRACK.append(1)
                # choosing = False
            elif choosen_direction == "r":
                room2()
                # choosing = False
            else:
                print("Please choose a direction")
                # continue
    elif current == 1:
            if choosen_direction == "l":
                room3()
                TRACK.append(3)
            elif choosen_direction == "forward":
                room4()
                TRACK.append(4)
            elif choosen_direction == "r":
                room5()
                TRACK.append(5)
            else:
                print("Please choose a direction")
    elif current == 4:
        if choosen_direction == "l":
            room6()
            TRACK.append(6)
        elif choosen_direction == "forward":
            room7()
            TRACK.append(7)
        elif choosen_direction == "r":
            room8()
            TRACK.append(8)
        else:
            print("Please choose a direction")
    elif current == 5:
        print("Only forward")
        room9()

def prison_break():
    cell()
    TRACK.append(0)


prison_break()