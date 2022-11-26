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
            "opooppooop",
            "opoppooopp",
            "ooopoopopp",
            "ooopppoopo",
            "ppoppooooo",
            "pooooooopp",
            "poooppoopo",
            "poppppoooo",
            "oopoooopoo",
            "oopopooppo"]
        self.map3 = [
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

    def maps(self, map_number):
        if map_number == 1:
            return self.map1
        if map_number == 2:
            return self.map2
        if map_number == 3:
            return self.map3
