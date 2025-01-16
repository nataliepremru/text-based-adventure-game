prison_map = {
# ------------------------------------------------------------JAIL CELL----------------------------------------------------------------------------------------------------------------------------------------------
    "cell": {
        "description": "You are standing in the middle of your cell, to the East is the bucket you call your toilet, a plain Wall to the west, your bed to the North and the cell door to the South. ",
        "directions": {"n": "bed", "e": "toilet", "s": "hallway", "w": "cell wall"}
    },
    "toilet": {
        "description": "You walk up to you 'Toilet' and are surprised to find it empty with how stinky the cell is, the Sherrif must be a lot drunker than you thought he was.",
        "directions": {"n": "bed", "e": None, "s": "hallway", "w": "cell wall"}
    },
    "bed": {
        "description": "A raggedy old bed, if it wasn't for the bozze and head injury, it would be impossible to sleep in but luckily you had both.",
        "directions": {"n": None, "e": "toilet", "s": "hallway", "w": "cell wall"}
    },
    "cell wall": {
        "description": "A solid wall with metal bars for a window, now way out through here.",
        "directions": {"n": "bed", "e": "toilet", "s": "hallway", "w": None}
    },
# ------------------------------------------------------------ HALLWAY ----------------------------------------------------------------------------------------------------------------------------------------------
    "hallway": {
        "description": "You walk up to your cell door and reach for the keys on the Sheriff's belt, the smell is awful but you push through and get yourself out of the cell!!! \n"
                        "You now stand in the hallway, to you East is a sleeping guard, ",
        "directions": {"n": None, "e": "sleeping guard", "s": "canteen", "w": "Toilets"}
    },
}
# Start the game in the cell
current_room = "cell"
print("You wake up a jail cell with the worst hangover in your life, you swear that this time you really will never drink again. \n"
      "The last thing you remember is getting in a fight with the Sherrifs brother, Cleetus, he was cheating at Poker again but this time you'd had enough!!! \n"
      "Now you were in a real fine mess, the Sherrif was going to send you off to a rigged court and sent off to a real prison, not one like this shoebox town jail you are in. \n"
      "Unless some miracle happened, you are in some real deep cow patties partner!!! \n"
      "Just as your head is clearing up, you get hit with the smell of booze and beans. Looking around you, you see the Sherrif passed out drunk right outside your cell \n"
      "                                                           THIS IS YOUR CHANCE!!!")
print('-' * 250)
print("Press 'n' to move North, 'e' to move East, 's' to move South, 'w' to move West and 'q' will end the game." )
print('-' * 250)
while True:
    # Print the current room's description
    print(prison_map[current_room]["description"])
    print('-' * 30)
    print("Where would you like to go?")
    print(f"Options: {', '.join(prison_map[current_room]['directions'].keys())}")
    print('-' * 30)
    choice = input().lower()
    if choice == "q":
        print('-' * 30)
        print("Thanks for playing! Goodbye.")
        print('-' * 30)
        break
    if choice in prison_map[current_room]["directions"]:
        next_room = prison_map[current_room]["directions"][choice]
        if next_room is None:
            print('-' * 33)
            print("You can't move in that direction!")
            print('-' * 33)
        else:
            current_room = next_room
    else:
        print('-' * 33)
        print("Invalid choice. Please try again.")
        print('-' * 33)
    print('-' * 250)