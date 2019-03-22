class Room(object):
    def __init__(self, name, north, south, east, description, west):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.characters = []


BEAN_ROOM = Room('The Bean Pool', None, None, None, 'BEAN_BAR', "There are a couple beans swimming here")
BEAN_BAR = Room('The Bean Bar', None, None, 'BEAN_Room', None, "There are a couple beans drinking legal drinks here")
