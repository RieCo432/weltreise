from copy import deepcopy, copy
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

        current_path = Path([self])

        valid_paths = [[current_path]]

        for i in range(number_of_moves):
            valid_paths.append([])
            for old_path in valid_paths[i]:
                for next_city in old_path.cities_in_order[-1].get_adjacent_cities():
                    old_path_cities = []
                    for city in old_path.cities_in_order:
                        old_path_cities.append(city)
                    old_path_cities.append(next_city)
                    new_path = Path(old_path_cities)
                    if new_path.is_valid():
                        valid_paths[i+1].append(new_path)



        possible_destinations = []

        for path in valid_paths[-1]:
            if path.cities_in_order[-1].name not in possible_destinations:
                possible_destinations.append(path.cities_in_order[-1].name)

        return possible_destinations


