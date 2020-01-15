import math

from connection import Connection

class Game:

    def __init__(self):

        self.all_cities = []
        self.all_connections = []
        self.flight_tickets_available = 20
        self.special_card_call_remaining = 5
        self.special_card_invitation_remaining = 5
        self.special_card_trade_remaining = 5
        self.players = []
        self.grey_cities = []

    def get_city_by_name(self, name):

        for city in self.all_cities:
            if city.name.lower() == name.lower():
                return city

        return None

    def get_cities_by_coordinate(self, x=None, y=None):

        result = []
        for city in self.all_cities:
            if (city.x == x.lower() or x is None) and (city.y == y.lower() or y is None):
                result.append(city)

        return result


    def add_connection(self, cities, isFlight=False):

        # print(cities)
        city1 = self.get_city_by_name(cities[0])
        city2 = self.get_city_by_name(cities[1])

        if city1.name >= city2.name:
            connshort = city2.name + city1.name
        else:
            connshort = city1.name + city2.name

        connecion_already_exists = False

        for exist_conn in self.all_connections:
            conn_city1, conn_city2 = exist_conn.cities
            if conn_city1.name >= conn_city2.name:
                exist_connshort = conn_city2.name + conn_city1.name
            else:
                exist_connshort = conn_city1.name + conn_city2.name

            if exist_connshort == connshort:
                print("double connection, ignoring")
                connecion_already_exists = True

        if not connecion_already_exists:
            new_connection = Connection([city1, city2], isFlight)

            city1.connections.append(new_connection)
            city2.connections.append(new_connection)
            self.all_connections.append(new_connection)

    # debug: list number of connections for each city to check if all added
    def check_conn_number(self):
        for x in "ABCDEFGHJK":
            for y in range(1, 7):
                cs = self.get_cities_by_coordinate(x, str(y))
                for c in cs:
                    print(c.name, len(c.connections))
                    input()


    @staticmethod
    # used as heuristic for a-star
    def estimate_city_dist(c1, c2):
        letter_list = "abcdefghjk"
        c1x = abs(5-letter_list.index(c1.x))
        c1y = int(c1.y)
        c2x = abs(5-letter_list.index(c2.x))
        c2y = int(c2.y)

        coord_dist = math.sqrt((c1x-c2x)**2 + (c1y-c2y)**2)

        return 1 + round(coord_dist * math.sqrt(2))

