from city import City
from connection import Connection
from game import Game
from path import Path


if __name__ == "__main__":
    
    game = Game()
    
    # create cities:
    game.all_cities.append(City("Fairbanks", "a", "1"))
    game.all_cities.append(City("Inuvik", "a", "1"))
    
    game.all_cities.append(City("Nuuk", "c", "1"))
    
    game.all_cities.append(City("Reykjavik", "d", "1"))
    
    game.all_cities.append(City("Barentsburg", "e", "1"))
    game.all_cities.append(City("Trondheim", "e", "1"))
    game.all_cities.append(City("Oslo", "e", "1"))
    game.all_cities.append(City("Stockholm", "e", "1"))
    
    game.all_cities.append(City("Helsinki", "f", "1"))
    game.all_cities.append(City("Murmansk", "f", "1"))
    game.all_cities.append(City("StPetersburg", "f", "1"))
    game.all_cities.append(City("Archangelsk", "f", "1"))
    
    game.all_cities.append(City("Norilsk", "h", "1"))
    
    game.all_cities.append(City("Jakutsk", "j", "1"))
    
    game.all_cities.append(City("Juneau", "a", "2"))
    game.all_cities.append(City("Vancouver", "a", "2"))
    game.all_cities.append(City("Portland", "a", "2"))
    game.all_cities.append(City("SaltLakeCity", "a", "2"))
    game.all_cities.append(City("SanFrancisco", "a", "2"))
    
    game.all_cities.append(City("Churchill", "b", "2"))
    game.all_cities.append(City("Edmonton", "b", "2"))
    game.all_cities.append(City("Winnipeg", "b", "2"))
    game.all_cities.append(City("Toronto", "b", "2"))
    game.all_cities.append(City("Chicago", "b", "2", True))
    game.all_cities.append(City("StLouis", "b", "2"))
    game.all_cities.append(City("Washington", "b", "2"))
    
    game.all_cities.append(City("Montreal", "c", "2"))
    game.all_cities.append(City("StJohns", "c", "2"))
    game.all_cities.append(City("NewYork", "c", "2"))

    game.all_cities.append(City("Dublin", "d", "2"))

    game.all_cities.append(City("London", "e", "2"))
    game.all_cities.append(City("Kopenhagen", "e", "2"))
    game.all_cities.append(City("Amsterdam", "e", "2"))
    game.all_cities.append(City("Berlin", "e", "2", True))
    game.all_cities.append(City("Brussel", "e", "2"))
    game.all_cities.append(City("Warschau", "e", "2"))
    game.all_cities.append(City("Prag", "e", "2"))
    game.all_cities.append(City("Paris", "e", "2"))
    game.all_cities.append(City("Bern", "e", "2"))
    game.all_cities.append(City("Wien", "e", "2"))
    game.all_cities.append(City("Belgrad", "e", "2"))
    game.all_cities.append(City("Rom", "e", "2"))
    game.all_cities.append(City("Madrid", "e", "2"))
    game.all_cities.append(City("Budapest", "e", "2"))

    game.all_cities.append(City("Riga", "f", "2"))
    game.all_cities.append(City("Moskau", "f", "2"))
    game.all_cities.append(City("Kiew", "f", "2"))
    game.all_cities.append(City("Wolgograd", "f", "2"))
    game.all_cities.append(City("Bukarest", "f", "2"))
    game.all_cities.append(City("Sofia", "f", "2"))
    game.all_cities.append(City("Tiflis", "f", "2"))
    game.all_cities.append(City("Baku", "f", "2"))

    game.all_cities.append(City("Almaty", "g", "2"))
    game.all_cities.append(City("Jekaterinburg", "g", "2"))

    game.all_cities.append(City("Nowosibirsk", "h", "2", True))
    game.all_cities.append(City("Irkutsk", "h", "2"))
    game.all_cities.append(City("UlanBator", "h", "2"))
    game.all_cities.append(City("Urummqi", "h", "2"))

    game.all_cities.append(City("Wladiwostok", "j", "2"))
    
    game.all_cities.append(City("Magadan", "k", "2"))
    game.all_cities.append(City("Sapporo", "k", "2"))
    game.all_cities.append(City("PetropawlowskKamtschatskij", "k", "2"))

    game.all_cities.append(City("LosAngeles", "a", "3"))

    game.all_cities.append(City("ElPaso", "b", "3"))
    game.all_cities.append(City("NewOrleans", "b", "3"))
    game.all_cities.append(City("Houston", "b", "3"))
    game.all_cities.append(City("Jacksonville", "b", "3"))
    game.all_cities.append(City("Miami", "b", "3"))
    game.all_cities.append(City("Havanna", "b", "3"))
    game.all_cities.append(City("Kingston", "b", "3"))
    game.all_cities.append(City("Managua", "b", "3"))
    game.all_cities.append(City("Guatemala", "b", "3"))
    game.all_cities.append(City("MexikoCity", "b", "3"))

    game.all_cities.append(City("SantoDomingo", "c", "3"))

    game.all_cities.append(City("Azoren", "d", "3"))
    game.all_cities.append(City("Lissabon", "d", "3"))
    game.all_cities.append(City("Casablanca", "d", "3"))
    game.all_cities.append(City("LasPalmas", "d", "3"))

    game.all_cities.append(City("Algier", "e", "3"))
    game.all_cities.append(City("Tunis", "e", "3"))
    game.all_cities.append(City("Tripolis", "e", "3"))

    game.all_cities.append(City("Athen", "f", "3"))
    game.all_cities.append(City("Ankara", "f", "3"))
    game.all_cities.append(City("Nikosia", "f", "3"))
    game.all_cities.append(City("Damaskus", "f", "3"))
    game.all_cities.append(City("Bagdad", "f", "3"))
    game.all_cities.append(City("Jerusalem", "f", "3"))
    game.all_cities.append(City("Kairo", "f", "3"))
    game.all_cities.append(City("Djidda", "f", "3"))
    game.all_cities.append(City("Kuwait", "f", "3"))

    game.all_cities.append(City("Teheran", "g", "3"))
    game.all_cities.append(City("Samarkand", "g", "3"))
    game.all_cities.append(City("Kabul", "g", "3"))
    game.all_cities.append(City("Delhi", "g", "3"))
    game.all_cities.append(City("Karachi", "g", "3"))
    game.all_cities.append(City("Dubai", "g", "3"))
    game.all_cities.append(City("Bombay", "g", "3"))

    game.all_cities.append(City("Varanasi", "h", "3"))
    game.all_cities.append(City("Kalkutta", "h", "3"))
    game.all_cities.append(City("Hanoi", "h", "3"))
    game.all_cities.append(City("Chongqing", "h", "3"))
    game.all_cities.append(City("Lhasa", "h", "3"))

    game.all_cities.append(City("Peking", "j", "3"))
    game.all_cities.append(City("Xian", "j", "3"))
    game.all_cities.append(City("Wuhan", "j", "3"))
    game.all_cities.append(City("Shanghai", "j", "3"))
    game.all_cities.append(City("Hongkong", "j", "3", True))
    game.all_cities.append(City("Taipeh", "j", "3"))
    game.all_cities.append(City("Seoul", "j", "3"))
    game.all_cities.append(City("Hiroshima", "j", "3"))
    
    game.all_cities.append(City("Tokio", "k", "3"))

    game.all_cities.append(City("GalapagosInseln", "b", "4"))
    game.all_cities.append(City("Panama", "b", "4"))
    game.all_cities.append(City("Bogota", "b", "4"))
    game.all_cities.append(City("Quito", "b", "4", True))
    game.all_cities.append(City("Lima", "b", "4"))

    game.all_cities.append(City("Caracas", "c", "4"))
    game.all_cities.append(City("Paramaribo", "c", "4"))
    game.all_cities.append(City("Manaus", "c", "4"))

    game.all_cities.append(City("Recife", "d", "4"))
    game.all_cities.append(City("Dakar", "d", "4"))
    game.all_cities.append(City("Monrovia", "d", "4"))

    game.all_cities.append(City("Bamako", "e", "4"))
    game.all_cities.append(City("Niamey", "e", "4"))
    game.all_cities.append(City("NDjamena", "e", "4", True))
    game.all_cities.append(City("Abidjan", "e", "4"))
    game.all_cities.append(City("Lagos", "e", "4"))
    game.all_cities.append(City("Douala", "e", "4"))
    game.all_cities.append(City("Kinshasa", "e", "4"))

    game.all_cities.append(City("Khartum", "f", "4"))
    game.all_cities.append(City("AddisAbeda", "f", "4"))
    game.all_cities.append(City("Aden", "f", "4"))
    game.all_cities.append(City("Mogadischu", "f", "4"))
    game.all_cities.append(City("Nairobi", "f", "4"))
    game.all_cities.append(City("DaresSalaam", "f", "4"))

    game.all_cities.append(City("Madras", "h", "4"))
    game.all_cities.append(City("Colombo", "h", "4"))
    game.all_cities.append(City("Rangun", "h", "4"))
    game.all_cities.append(City("Bangkok", "h", "4"))
    game.all_cities.append(City("HoChiMinhStadt", "h", "4"))
    game.all_cities.append(City("Singapur", "h", "4"))
    game.all_cities.append(City("Jakarta", "h", "4"))

    game.all_cities.append(City("Manilla", "j", "4"))

    game.all_cities.append(City("Guam", "k", "4"))

    game.all_cities.append(City("Osterinsel", "a", "5"))

    game.all_cities.append(City("Santiago", "b", "5"))

    game.all_cities.append(City("LaPaz", "c", "5"))
    game.all_cities.append(City("Brasilia", "c", "5"))
    game.all_cities.append(City("Asuncion", "c", "5"))
    game.all_cities.append(City("BuenosAires", "c", "5"))
    game.all_cities.append(City("SaoPaulo", "c", "5"))
    game.all_cities.append(City("RioDeJaneiro", "c", "5"))

    game.all_cities.append(City("Luanda", "e", "5"))

    game.all_cities.append(City("Windhuk", "f", "5"))
    game.all_cities.append(City("Lusaka", "f", "5"))
    game.all_cities.append(City("Harare", "f", "5"))
    game.all_cities.append(City("Johannesburg", "f", "5"))
    game.all_cities.append(City("Maputo", "f", "5"))
    game.all_cities.append(City("Antananarivo", "f", "5"))

    game.all_cities.append(City("Denpasar", "j", "5"))
    game.all_cities.append(City("Darwin", "j", "5"))
    game.all_cities.append(City("Perth", "j", "5"))
    game.all_cities.append(City("AliceSprings", "j", "5"))

    game.all_cities.append(City("PortMoresby", "k", "5"))
    game.all_cities.append(City("Brisbane", "k", "5"))
    game.all_cities.append(City("Sydney", "k", "5", True))

    game.all_cities.append(City("SanCarlosDeBariloche", "b", "6"))
    game.all_cities.append(City("PuntaArenas", "b", "6"))

    game.all_cities.append(City("Kapstadt", "f", "6"))

    game.all_cities.append(City("Adelaide", "j", "6"))
    game.all_cities.append(City("Melbourne", "j", "6"))

    game.all_cities.append(City("Canberra", "k", "6"))
    game.all_cities.append(City("Wellington", "k", "6"))

    # create connections

    #start connections in A, B, C
    game.add_connection(["fairbanks", "inuvik"])
    game.add_connection(["inuvik", "churchill"])
    game.add_connection(["fairbanks", "juneau"])
    game.add_connection(["juneau", "edmonton"])
    game.add_connection(["juneau", "vancouver"])
    game.add_connection(["juneau", "petropawlowskkamtschatskij"], True)
    game.add_connection(["vancouver", "edmonton"])
    game.add_connection(["vancouver", "portland"])
    game.add_connection(["portland", "sanfrancisco"])
    game.add_connection(["portland", "saltlakecity"])
    game.add_connection(["sanfrancisco", "saltlakecity"])
    game.add_connection(["sanfrancisco", "losangeles"])
    game.add_connection(["losangeles", "saltlakecity"])
    game.add_connection(["losangeles", "osterinsel"], True)
    game.add_connection(["losangeles", "mexikocity"])
    game.add_connection(["mexikocity", "elpaso"])
    game.add_connection(["mexikocity", "houston"])
    game.add_connection(["mexikocity", "havanna"])
    game.add_connection(["mexikocity", "guatemala"])
    game.add_connection(["elpaso", "houston"])
    game.add_connection(["elpaso", "saltlakecity"])
    game.add_connection(["elpaso", "winnipeg"])
    game.add_connection(["saltlakecity", "winnipeg"])
    game.add_connection(["edmonton", "winnipeg"])
    game.add_connection(["churchill", "winnipeg"])
    game.add_connection(["winnipeg", "chicago"])
    game.add_connection(["winnipeg", "montreal"])
    game.add_connection(["churchill", "montreal"])
    game.add_connection(["chicago", "stlouis"])
    game.add_connection(["chicago", "toronto"])
    game.add_connection(["stlouis", "newyork"])
    game.add_connection(["stlouis", "washington"])
    game.add_connection(["stlouis", "neworleans"])
    game.add_connection(["neworleans", "houston"])
    game.add_connection(["neworleans", "jacksonville"])
    game.add_connection(["jacksonville", "miami"])
    game.add_connection(["miami", "neworleans"])
    game.add_connection(["jacksonville", "washington"])
    game.add_connection(["washington", "newyork"])
    game.add_connection(["montreal", "newyork"])
    game.add_connection(["montreal", "toronto"])
    game.add_connection(["mexikocity", "galapagosinseln"])
    game.add_connection(["miami", "havanna"])
    game.add_connection(["havanna", "kingston"])
    game.add_connection(["guatemala", "kingston"])
    game.add_connection(["guatemala", "managua"])
    game.add_connection(["managua", "kingston"])
    game.add_connection(["kingston", "santodomingo"])
    game.add_connection(["panama", "managua"])
    game.add_connection(["panama", "santodomingo"])
    game.add_connection(["panama", "galapagosinseln"])
    game.add_connection(["panama", "caracas"])
    game.add_connection(["panama", "bogota"])
    game.add_connection(["caracas", "bogota"])
    game.add_connection(["quito", "bogota"])
    game.add_connection(["quito", "lima"])
    game.add_connection(["quito", "manaus"])
    game.add_connection(["lima", "manaus"])
    game.add_connection(["manaus", "paramaribo"])
    game.add_connection(["bogota", "paramaribo"])
    game.add_connection(["caracas", "paramaribo"])
    game.add_connection(["manaus", "lapaz"])
    game.add_connection(["lima", "lapaz"])
    game.add_connection(["lapaz", "asuncion"])
    game.add_connection(["lapaz", "riodejaneiro"])
    game.add_connection(["lapaz", "santiago"])
    game.add_connection(["asuncion", "buenosaires"])
    game.add_connection(["asuncion", "brasilia"])
    game.add_connection(["manaus", "brasilia"])
    game.add_connection(["santiago", "sancarlosdebariloche"])
    game.add_connection(["santiago", "buenosaires"])
    game.add_connection(["lapaz", "osterinsel"], True)
    game.add_connection(["santiago", "osterinsel"], True)
    game.add_connection(["galapagosinseln", "osterinsel"])
    game.add_connection(["galapagosinseln", "lima"])
    game.add_connection(["osterinsel", "wellington"], True)
    game.add_connection(["sancarlosdebariloche", "buenosaires"])
    game.add_connection(["puntaarenas", "sancarlosdebariloche"])
    game.add_connection(["puntaarenas", "buenosaires"])
    game.add_connection(["brasilia", "riodejaneiro"])
    game.add_connection(["brasilia", "recife"])
    game.add_connection(["manaus", "recife"])
    game.add_connection(["brasilia", "saopaulo"])
    game.add_connection(["riodejaneiro", "saopaulo"])
    game.add_connection(["newyork", "stjohns"])
    game.add_connection(["montreal", "stjohns"])
    game.add_connection(["montreal", "nuuk"])
    game.add_connection(["stjohns", "nuuk"])
    game.add_connection(["nuuk", "reykjavik"])
    # end connections in A, B, C

    print("Done setup")

    # results = game.get_city_by_name("LosAngeles").get_adjacent_cities()
    #
    # result = game.get_city_by_name("LosAngeles").get_possible_destinations(3)
    #
    # la = game.get_city_by_name("LosAngeles")
    # sf = game.get_city_by_name("SanFrancisco")
    # slc = game.get_city_by_name("Saltlakecity")
    # mc = game.get_city_by_name("MexikoCity")
    # ep = game.get_city_by_name("ElPaso")
    # p1 = Path([la, sf, la])  # not valid
    # p2 = Path([la, sf, slc, la])  # valid
    # p3 = Path([sf, la, mc, ep, slc])  # valid
    # p4 = Path([sf, la, mc, la, slc])  # not valid
    # print(p1.is_valid())
    # print(p2.is_valid())
    # print(p3.is_valid())
    # print(p4.is_valid())


    print("Test concluded")

