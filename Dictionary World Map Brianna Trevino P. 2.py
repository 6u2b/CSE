world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here",
        'PATHS': {
            'SOUTH': 'R19A'

        }
    }
}

playing = True
current_node = world_map ['R19A']
while playing:
    print(current_node['DESCRIPTION']
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']
    playing = False

