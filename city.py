class City:

    def __init__(self, name, x, y, get_plane_ticket = False):
        self.name = name
        self.x = x
        self.y = y
        self.get_plane_ticket = get_plane_ticket
        self.connections = []

    def add_connections(self, connections):
        self.connections = connections

