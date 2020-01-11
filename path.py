from copy import deepcopy


class Path:

    def __init__(self, cities):
        self.cities_in_order = cities

    def append_city(self, city):
        return self.cities_in_order.append(city)

    def is_valid(self):
        if len(self.cities_in_order) >= 3:
            for i in range(len(self.cities_in_order) - 2):
                if self.cities_in_order[i] == self.cities_in_order[i+2]:
                    return False

        return True