class Room(object):
    def __init__(self, name, description, north=None, east=None, south=None, west=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description


Room_1 = Room("BEAN_ROOM", "You are in the bean room ", None, None, 'Room_2', None)
Room_2 = Room("BEAN_LOT", "You are in the bean room ", None, None, None, None)



playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

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
