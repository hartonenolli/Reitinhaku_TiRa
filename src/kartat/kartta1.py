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
    
    def maps(self, map_number):
        if map_number == 1:
            return self.map1
