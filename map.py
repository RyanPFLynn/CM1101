from items import *

entrance_hall = {
    "name": "Entrance Hall",

    "description":
    """You are in the entrance hall to the manner. You see a room filled with 
cob webs and dust. The stench of damp srouds the place, and the leaking walls 
bring a feel of being followed. To the north is a rusted kitchen, to the west 
is the lounge. Looks like I need a key to escape this place.""",

    "exits": {"north": "Kitchen", "west":"Lounge"}, 

    "items": [item_battery]
}

kitchen = {
    "name": "kitchen",

    "description":
    """You walk through the rusted door. The smell of rotting food
and rats engulfs the room. Sitting on one of the work tops is a
torch. To the north is the backgarden, to the east of me i can
feel a chill of the freezer. To the west looks to be the dining
room. If i go south i will end up at the entrance hall.""",

    "exits":{"north":"Backyard", "east":"Freezer", "west":"Dining", "south": "Hall"}, 

    "items": [item_torch]
}

freezer = {
    "name": "the kitchen freezer",

    "description":
    """Walking through the broken door, hanging of its hinges.
    You enter into the freezer, there seems to be something on the floor,
but I need some power to see it.  """,

    "exits":{"west":"Kitchen"},

    "items": []
}

garage = {
    "name": "the garage",

    "description":
    """You are in the garage. An empty bleak room, there must be something around here.
There seems to be a battery box in here. I wonder if i find a battery and get some light for 
this dark house.""",

    "exits":{"north":"Backyard"},

    "items": []
}

lounge = {
    "name": "the lounge",

    "description":
    """You are standing next to a chair in the lounge. You look down and notice the 
dust filled floor. As you walk in, you notice your blurred reflection in the 
broken smeared mirror. There is a safe, looks like i'll need a pick to 
open this.""",

    "exits":{"north":"Dining"},

    "items": []
}

dining_room = {
    "name": "the dining room",

    "description":
    """Walking into the dining room you notice the floors creaking. A table is 
pushed to one side, and a empty glass of wine is all that remains of 
civilisation.""",
   
    "exits":{"north":"Backyard","east":"Kitchen"},

    "items": [item_glass]
}

backyard = {
    "name": "the backyard",

    "description":
    """I seem to be outside, I can see the night sky with a full 
moon beaming down on me.To the south, behind me is the kitchen, 
to the east of me is the garage. Tbe floor is convered in 
rubbish, I wonder if there is anything useful here?""",

    "exits": {"south":"Kitchen", "east":"Garage"},

    "items": []
}

#exit = {
    #"name": "the exit",

    #"description":
    #""" I have escaped the house and i am free!!! """,

    #"exits":{},

    #"items":[]
#}

rooms = {
    "Kitchen": kitchen, 
    "Hall": entrance_hall, 
    "Freezer": freezer, 
    "Garage": garage, 
    "Lounge": lounge, 
    "Dining": dining_room, 
    "Backyard": backyard
    #"Exit": exit
}


