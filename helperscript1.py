# script is used to make the process of entering all the connections easier

while True:
    city1 = input("City1")
    city2 = input("City2")
    plane = input("Plane") is not ""

    with open("done_script.txt", "a") as fout:
        if not plane:
            fout.write('game.add_connection(["%s", "%s"])\n' % (city1, city2))
        else:
            fout.write('game.add_connection(["%s", "%s"], True)\n' % (city1, city2))