from kartat.kartta1 import Kartat

class IDA_Star:
    def __init__(self, nyky_kartta):
        self.kartta = Kartat().maps(nyky_kartta)
        self.alku = "0,0"
        self.loppu = "2,2"
        self.koordinaatit = None
        self.ruudut = {}
        self.naapurit = {}
        self.tarkastettu = []
        self.matka = 0
        self.ida_star_map = []
        self.katsottu = []

    def tee_ruudut(self, alku_ja_loppu):
        self.koordinaatit = alku_ja_loppu
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[0])):
                if self.kartta[y][x] != "p":
                    self.ruudut[f"{x},{y}"] = []
                    self.tee_naapuri(x, y)

        return self.ruudut, self.naapurit

    def tee_naapuri(self, x, y):
        self.naapurit[f"{x},{y}"] = []
        # Handle different directions
        # left
        if x > 0:
            if self.kartta[y][x-1] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x-1},{y}")
        # up
        if y > 0:
            if self.kartta[y-1][x] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x},{y-1}")
        # right
        if x < len(self.kartta[0])-1:
            if self.kartta[y][x+1] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x+1},{y}")
        # down
        if y < len(self.kartta)-1:
            if self.kartta[y+1][x] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x},{y+1}")
        return True    
    
    def ida_funktio(self, ruutuja, naapureita, koordinaatti):
        self.ruudut = ruutuja
        self.naapurit = naapureita
        self.alku = f"{koordinaatti[1]},{koordinaatti[0]}"
        self.loppu = f"{koordinaatti[3]},{koordinaatti[2]}"
        start = self.alku
        fin = self.loppu
        raja = self.heurestinen_arvo(start, fin)
        print(raja)
        while True:
            ruudun_tila = self.etsi(start, 0, raja, fin)
            if ruudun_tila == True:
                print(len(self.tarkastettu))
                break
            if ruudun_tila >= 999:
                return False
            raja = ruudun_tila
        return self.kartan_palautus(start, fin)


    def etsi(self, node, maara, raja, fin):
        f=maara+self.heurestinen_arvo(node,fin)
        if f > raja:
            return f
        if node == self.loppu:
            return True
        min_arvo = 999
        for naapuri in self.naapurit[node]:
            self.katsottu.append(naapuri)
            if naapuri == self.alku:
                continue
            if naapuri not in self.tarkastettu:
                self.tarkastettu.append(naapuri)
                etsi_naapuri = self.etsi(naapuri, maara+1, raja, fin)
                if etsi_naapuri == True:
                    self.matka += 1
                    return True
                if etsi_naapuri < min_arvo:
                    min_arvo = etsi_naapuri
                self.tarkastettu.pop()

        return min_arvo



    def heurestinen_arvo(self, ruutu, loppu):
        arvot_alku = ruutu.split(",")
        arvot_loppu = loppu.split(",")

        ruutu_x = abs(int(arvot_alku[0]) - int(arvot_loppu[0]))
        ruutu_y = abs(int(arvot_alku[1]) - int(arvot_loppu[1]))
        return ruutu_x+ruutu_y

    def kartan_palautus(self, start, fin):
        row = ""
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[0])):
                if self.kartta[y][x] == "p":
                    row += "p"
                elif start == f"{x},{y}":
                    row += "o"
                elif fin == f"{x},{y}":
                    row += "o"
                elif f"{x},{y}" in self.tarkastettu:
                    row += "r"
                elif f"{x},{y}" in self.katsottu:
                    row += "d"
                else:
                    row += "o"
            self.ida_star_map.append(row)
            row = ""
        return self.ida_star_map
