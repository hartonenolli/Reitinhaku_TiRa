class Kartat:
    def __init__(self):
        self.map1 = [
            "ooopoooppo",
            "oooppooopo",
            "ppopoppopo",
            "opopoooopo",
            "oooppooooo",
            "oooooooopp",
            "ooooppoopo",
            "oopoopoooo",
            "ooopooopoo",
            "ooppoooppo"]
        self.map2 = [
            "opoooooopoooooo",
            "opoppppopppppop",
            "ooopoooopoooooo",
            "opoooppppoppppp",
            "opopopooooooooo",
            "opopoooppoopppo",
            "ooopppppooopooo",
            "ppopopopppppopp",
            "opooopooooooopo",
            "opopoooopoopopo",
            "oppppppoppppppo",
            "oopooopoooooooo",
            "pooopooooppppoo",
            "poppppopopoopop",
            "oopoooopoppoooo"]
        self.map3 = [
            "opoooooopooooooooooo",
            "oooooopoppppopppppop",
            "opopooooooooopoooooo",
            "opoooppppooooooppppp",
            "opopopoooooooooooooo",
            "opoooopopoooppoopppo",
            "opopppoooooopooopooo",
            "ppopppppopppppoppppp",
            "opooopooooooopoooooo",
            "ooopoppppppoopoopopo",
            "oppppopoooppoppppppo",
            "oopooopooooooooooooo",
            "pooopoooopppppoooooo",
            "pooooooppppopppoooop",
            "oooooopopooooooopooo",
            "oppppoooooppoppppppo",
            "oopooopoooooopoooooo",
            "pooopoooopopppoooooo",
            "poooppppppoooopoopoo",
            "oopooooooooopooooppo"]

    def maps(self, map_number):
        if map_number == 1:
            return self.map1
        if map_number == 2:
            return self.map2
        if map_number == 3:
            return self.map3
