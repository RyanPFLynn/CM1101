import game
from map import *
from player import *


mission = {
    "mission_1": "",
    "mission_2": "",
    "mission_3": "",
    "mission_4": ""
}

def mission1():
    for i in garage["items"]:
        if "battery" == i["id"]:
            garage["items"].remove(items["battery"])
            garage["description"] = """ The lights are now on, you can now see where you are going around
the house. I wonder if there was anything in the freezer."""
            freezer["items"].append(items["pick"])
            freezer["description"] = """Walking through the broken door, hanging of its hinges.
You enter into the freezer, I can see soemthing on the floor, I wonder if it could open the safe. """
            mission["mission_1"] = "complete"

def mission2():
    for i in lounge["items"]:
        if "pick" == i["id"]:
            lounge["items"].remove(items["pick"])
            lounge["description"] = """ Upon picking this safe in the lounge, i seem to have come accross a 
a message.It reads that if i look closer in the backyard, i could find a key. There is nothing more i
could find in this room"""
            backyard["items"].append(items["key"])
            mission["mission_2"] = "complete"

def mission3():
    for i in entrance_hall["items"]:
        if "key" == i["id"]:
            
            #entrance_hall["exits"] = {"south":"Exit"}

            entrance_hall["items"].remove(items["key"])
            entrance_hall["description"] = """ This seems to have unlocked the door, this could be my escaape.
"""
            mission["mission_3"] = "complete"

def miss_com():
    if (mission["mission_1"] == "complete") and (mission["mission_2"] == "complete") and (mission["mission_3"] == "complete"):
        game.won = True



