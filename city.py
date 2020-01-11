from copy import deepcopy
from path import Path


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

        new_paths = [Path([self])]
        for i in range(number_of_moves):
            paths = deepcopy(new_paths)
            new_paths = []
            for path in paths:
                last_city = path.cities_in_order[-1]
                possible_next_cities = last_city.get_adjacent_cities()
                for c in possible_next_cities:
                    new_path_cities = deepcopy(path.cities_in_order)
                    new_path_cities.append(c)
                    new_paths.append(Path(new_path_cities))

        valid_paths = []

        for path in new_paths:
            if path.is_valid:
                valid_paths.append(path)

        possible_destinations = []

        for path in valid_paths:
            if path.cities_in_order[-1] not in possible_destinations:
                possible_destinations.append(path.cities_in_order[-1])

        return possible_destinations


