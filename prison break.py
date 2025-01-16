## prison break
def prison_break():
    ## game begins, introduction is shown
    print("Hello, welcome to Pentonville Prison.\n You are an inmate serving a life sentence for a crime you did you not commit. \n About 2 hours ago a guard dropped his keys as he passed your cell but it wasn't a good time to leave. \n The coast is finally clear... this is your chance... you unlock the door...\n You are stood in the hallway and you can go either left or right. \n Which do you choose?")
    ## asking user to chose to go left or right
    hallway_choice = input("Do you want to go left or right? (l/r/f/b): ").lower()
    ## condition for user chosing left in the hallway
    if hallway_choice == "l":
        print("You go left.\n At the end of the hallway you find a guard dog sleeping.\n You can either go left, right or forward.\n Which do you chose?")
        ## asking user to go left, right or forwards
        sleeping_dog_choice = input("Do you want to go left, right or forward? (l/r/f/b): ").lower()
        ## condition for user chosing left at the sleeping dog
        if sleeping_dog_choice == "l":
            print("You go left.\n You have woken up the dog, game over.")
        ## condtition for user chosing right at the sleeping dog
        elif sleeping_dog_choice == "r":
            print("You go right.\n You have entered the toilets where you find your friend, it seems theres nowhere else to go apart from forwards out the window.\n They offers to give you a lift, what do you decide to do? ")
            ## asking the user to choose a direction from the toilets
            toilet_choice = input("Do you want to go left, right, forward or back? (l/r/f/b): ").lower()
            ## condition for moving forwards
            if toilet_choice == "f":
                print("You go forward.\n You are now in the courtyard, you see a gap in the fence ahead")
                ## asking the user to choose a direction in the courtyard
                court_yard_choice = input("Do you chose to go left or right?").lower()
                ## condition for chosing left at the courtyard
                if court_yard_choice == "l":
                    print("You go left.\n You found the hole in the fence and succesfully escaped Pentonville.\n Congratulations.")
                ## conditino for chosing right at the courtyard  
                elif court_yard_choice == "r":
                    print("You go right.\n You get spotted by a guard on the watch tower, game over.")
                ## condition for any other input at the courtyard
                else: print("You cannot move in this direction")
            ## condition for any other input at the sleeping dog
            else: print("You cannot move in this direction")
        ## condition for chosing forward at the sleeping dog          
        elif sleeping_dog_choice == "f":
            print("You go forward.\n You find yourself in the canteen.\n Luckily no one is here right now.\n There are three possible doors to take, which one do you chose? ")
            ## asking the user to choose a direction at the canteen
            canteen_choice = input("Do you want to go left, right or forward? (l/r/f/b): ").lower()
            ## condition for chosing left in the canteen
            if canteen_choice == "l":
                print("You go left. You have found yourself in the guards room... luckily theres no guards in here right now...\n You find the set of keys for the staff exit.\n Which door do you take out of the guards room?")
                ## asking user to choose a direction from the guards room
                guards_room_choice = input("Which door do you want to take?")
                ## condidition for chosing left or right in the guards room
                if guards_room_choice == "l" or "r":
                    print("You run into a guard, game over")
                ## condition for chosing forwards in the gaurds room    
                elif guards_room_choice == "f":
                    print("You successfully exit through the staff exit without being caught.\n Congratulations.")
                ## condition for any other input in the guards room    
                else: print("You cannot move in this direction")
            ## condition for chosing right at the canteen        
            elif canteen_choice == "r":
                print("You go right.\n You enter the kitchen but the chef is on duty and rings the alarm, game over.")
            ## condition for chosing forwards in the canteen
            elif canteen_choice == "f":
                print("You go forward.\n You are in a storage cupboard with nowhere else to go, you must turn back.")
            ## condition for any another input  
            else: print("You cannot move in this direction")
    ## condition for user chosing right in the hallway   
    elif hallway_choice == "r":
        print("You run into a guard, game over.") 
    ## conditino for any other input    
    else: print("You cannot move in this direction. Please choose left or right")   
        

prison_break()