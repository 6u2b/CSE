class Room(object):
    def __init__(self, name, north, south, east, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.characters = []


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room.

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

def find_next_room(self, direction):
        """ This method searches the current room so see if a room exists in that direction.
    :param direction: The direction that oyu want to move to.
    :return: The Room object if it exists, or None if it does not exist.
    """

    return getattr(self.current_location, direction)

R19A = Room("Mr. Wiebe's Room", 'parking lot')
parking_lot = Room ("Parking lot", None, "R19A")

player = Player(R19A)

playing = True
current_node = world_map ['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            next_room = player.find_next_room(command)
            plaer.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")