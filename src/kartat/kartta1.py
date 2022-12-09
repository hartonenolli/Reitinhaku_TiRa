
"""Karttaruutu ja algoritmit hakevat kartat täältä
    kartta palautetaan yhden funktion avulla
"""

class Kartat:

    def __init__(self):
        """Alustetaan kolme käytössä olevaa karttaa ja
            testissä oleva kartta
        """
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
        self.map_test = ["oo", "oo"]

    def maps(self, map_number):
        """Funktio kartan palauttamista varten.
            Kutsutaan kartan numerolla ja palautetaan vastaava kartta
        """
        if map_number == 1:
            return self.map1
        if map_number == 2:
            return self.map2
        if map_number == 3:
            return self.map3
        return self.map_test
