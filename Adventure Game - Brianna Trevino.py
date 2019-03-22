world_map = {
    'Bean_Room': {
        'NAME': "Bean Room",
        'DESCRIPTION': "This is the ",
        'PATHS': {
            'NORTH': "BEAN_LOT",
            'WEST': "BEAN_POOL"
        }
    },
    'BEAN_LOT': {
        'NAME': "The Bean Lot",
        'DESCRIPTION': "There are a couple beans parked here",
        'PATHS': {
            'SOUTH': 'Bean_Room',
            'WEST': 'BEAN_POOL'

        }
    },

    'BEAN_POOL': {
        'NAME': "The Bean Pool",
        'DESCRIPTION': "There are a couple beans swimming here",
        'PATHS': {
            'SOUTH': 'BEAN_BAR',
            'EAST': 'BEAN_LOT'
        }
    },
    'BEAN_BAR': {
        'NAME': "The Bean Bar",
        'DESCRIPTION': "There are a couple beans drinking legal drinks here",
        'PATHS': {
            'NORTH': 'BEAN_POOL',
            'SOUTH': 'BEAN_COMPUTER_LAB'
        }
    },
    'BEAN_COMPUTER_LAB': {
        'NAME': "The Bean Computer Lab",
        'DESCRIPTION': "There are a couple beans looking up information here",
        'PATHS': {
            'NORTH': 'BEAN_BAR',
            'EAST': 'KITCHEN'
        }
    },
    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "Where the beans make food",
        'PATHS': {
            'WEST': 'BEAN_COMPUTER_LAB',
            'EAST': 'STORAGE_ROOM'

        }
    },
    'STORAGE_ROOM': {
        'NAME': "The Bean Storage Room",
        'DESCRIPTION': "The storage units are located here",
        'PATHS': {
            'WEST': 'KITCHEN',
            'EAST': 'GARAGE_ROOM'
        }
    },
    'GARAGE_ROOM': {
        'NAME': "The Bean Storage Room",
        'DESCRIPTION': "The storage units are located here",
        'PATHS': {
            'WEST': 'STORAGE_ROOM',
            'NORTH': 'KITCHEN'
       }
    },
    'DINING_ROOM': {
        'NAME': "The Dining Room",
        'DESCRIPTION': "The dining room is where the beans eat.",
        'PATHS': {
            'WEST': 'CLASS_ROOM',
            'NORTH': ''
        }
    },
    'HALLWAY_ROOM': {
        'NAME': "The Main Hallway",
        'DESCRIPTION': "Main Hallway of the House .",
        'PATHS': {
            'WEST': 'CLASS_ROOM',
            'NORTH': ''
        }
    },
    'HALLWAY2_ROOM': {
        'NAME': "The Main Hallway",
        'DESCRIPTION': "Main Hallway of the House .",
        'PATHS': {
            'WEST': 'CLASS_ROOM',
            'NORTH': ''
        }
    },
    'Dragon_ROOM': {
        'NAME': "The Dragon's dungeon",
        'DESCRIPTION': "a dragon lives here.",
        'PATHS': {
            'WEST': '',
            'NORTH': ''
        }
    },
    'CAFE_ROOM': {
        'NAME': "The Dragon's cafe",
        'DESCRIPTION': "a dragon drinks coffee here.",
        'PATHS': {
            'WEST': '',
            'NORTH': ''
        }
    },
    'FROG_ROOM': {
        'NAME': "The Frogs room",
        'DESCRIPTION': "The frogs live here after being captured by the dragon.",
        'PATHS': {
            'WEST': '',
            'NORTH': ''
        }
    },
    'LAB_ROOM': {
        'NAME': "The Lab",
        'DESCRIPTION': "A scientist lives here and experiments on little beans then turns them "
                       "into dragons to capture frogs",
        'PATHS': {
            'WEST': '',
            'NORTH': ''
        }
    },
    'HALLWAY3_ROOM': {
        'NAME':"The secondary hallway",
        'DESCRIPTION': "Hallway connecting the kitchen and garage",
        'PATHS': {
            'WEST': '',
        }
    },
}


playing = True
current_node = world_map['Bean_Room']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
