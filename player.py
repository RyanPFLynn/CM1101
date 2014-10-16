from items import *
from map import rooms
import game

inventory = [item_money]

# Start game at the reception
current_room = rooms["Hall"]

fear = 0

def inv_weight_limit(item_id):
    weight = 0
    print("Checking inventory weight.")
    for i in inventory:
        weight = float(weight) + float(i["weight"])
    weight = float(weight) + float(items[item_id]["weight"])
    if float(weight) <= 5:
        return True
    else:
        return False

def fear_level():
    if fear > 25:
        game.won = False