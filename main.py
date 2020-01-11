from city import City
from connection import Connection
from game import Game

if __name__ == "__main__":
    
    game = Game()
    
    # create cities:
    game.all_cities.append(City("Fairbanks", "a", "1"))
    game.all_cities.append(City("Inuvit", "a", "1"))
    
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
    game.all_cities.append(City("SanFransisco", "a", "2"))
    
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

    game.all_cities.append(City("Los Angeles", "a", "3"))

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

    game.all_cities.append(City("Osterinseln", "a", "5"))

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

