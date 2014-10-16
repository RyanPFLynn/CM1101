#!/usr/bin/python3

from items import *
from gameparser import *
from map import rooms
from missions import *
from player import *
import player


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string)."""
    
    item_list = []
    for word in items:
        item_list.append(word["name"])
    return ", ".join(item_list)


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. """

    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")
        print("")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". """

    inv = []
    for i in items:
        inv.append(i["name"])
    invent = ", ".join(inv)
    print("You have " + str(invent) + ".")
    print("")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). """

    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    print("")
    print_room_items(room)

def print_fear(fear):
    print("Your fear level is " + str(fear))
    print()

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. """

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:"""

    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print"""
    

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for i in room_items:
        print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    for i in inv_items:
        print("DROP " + i["id"].upper() + " to drop " + i["name"] + ".")
    for i in inv_items:
        print("EXAMINE " + i["id"].upper() + " to find out about " + i["name"] + ".")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input()."""
    return chosen_exit in exits

def is_item_in_room(item_id,room):
    for i in room["items"]:
        if item_id == i["id"]:
            return True
    return False

def is_item_in_inventory(item_id,inventory):
    for i in inventory:
        if item_id == i["id"]:
            return True
    return False

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    if direction in player.current_room["exits"]:
        player.current_room = move(player.current_room["exits"],direction)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    if is_item_in_room(item_id,player.current_room):
        if inv_weight_limit(item_id):
            inventory.append(items[item_id])
            player.current_room["items"].remove(items[item_id])
        else:
            print("You cannot pick up this item, you are carrying too much")
            input("Hit enter.")
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    if is_item_in_inventory(item_id,player.inventory):
        player.current_room["items"].append(items[item_id])
        inventory.remove(items[item_id])
    pass

def execute_examine(item_id):
    if is_item_in_inventory(item_id,player.inventory):
        print(item_id.upper())
        print(items[item_id]["description"])
        input("Hit enter:")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if command[0] == "go":
        if len(command) > 1:

            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "exit":
        quit()

    elif command[0] == "demo":
        game.won = True

    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned."""

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("Player: ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:"""
    
    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        if game.won == "":
            # Display game status (room description, inventory etc.)
            print_room(player.current_room)
            print_inventory_items(inventory)
            print_fear(player.fear)

            # Show the menu with possible actions and ask the player
            command = menu(player.current_room["exits"], player.current_room["items"], inventory)

            # Execute the player's command
            execute_command(command)

            # Checking objectives in mission.py
            mission1()
            mission2()
            mission3()
            miss_com()
            player.fear = player.fear + 1
            player.fear_level()
        elif game.won == True:
            print("")
            print("You have escaped and won the game!!!")
            print("")
            print("Thank you for playing the game")
            input("Hit enter.")
            quit()
        elif game.won == False:
            print("Your fear level got too high!!")
            print("")
            print("You faint!")
            print("")
            print("You have lost!")
            input("Hit enter.")
            quit()
           
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
won = ""
if __name__ == "__main__":
    main()