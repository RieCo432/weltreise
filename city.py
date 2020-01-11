from copy import deepcopy

class City:

    def __init__(self, name, x, y, get_plane_ticket = False):
        self.name = name
        self.x = x
        self.y = y
        self.get_plane_ticket = get_plane_ticket
        self.connections = []

    def add_connections(self, connections):
        self.connections = connections

    def get_adjacent_cities(self):
        adjacent_cities = []
        for connection in self.connections:
            city1, city2 = connection.cities
            if city1.name == self.name:
                adjacent_cities.append(city2)
            else:
                adjacent_cities.append(city1)

        return adjacent_cities

    def get_possible_destinations(self, number_of_moves):
        possible_destinations = [self]
        all_visited = [self]
        for i in range(number_of_moves):
            intermediates = deepcopy(possible_destinations)
            possible_destinations = []
            for city in intermediates:
                for c in city.get_adjacent_cities():
                    if c not in all_visited:
                        possible_destinations.append(c)
                        all_visited.append(c)

        return possible_destinations


