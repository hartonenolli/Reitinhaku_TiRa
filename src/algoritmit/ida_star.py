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
    
    def ida_funktio(self, ruutuja, naapureita):
        self.ruudut = ruutuja
        self.naapurit = naapureita
        self.alku = "0,0"
        self.loppu = "2,2"
        start = "0,0"
        fin = "2,2"
        raja = self.heurestinen_arvo(start, fin)
        print(raja)
        while True:
            ruudun_tila = self.etsi(start, 0, raja, fin)
            if ruudun_tila == True:
                print("loppu")
                break
            if ruudun_tila >= 999:
                return False
            raja = ruudun_tila
            print(raja)

    def etsi(self, node, maara, raja, fin):
        print("haku")
        f=maara+self.heurestinen_arvo(node,fin)
        if f > raja:
            print(f"f>raja, {f}>{raja}")
            return f
        if node == self.loppu:
            print("node oli loppu")
            return True
        min_arvo = 999
        print(self.naapurit[node])
        for naapuri in self.naapurit[node]:
            print(naapuri)
            if naapuri == self.alku:
                continue
            if naapuri not in self.tarkastettu:
                self.tarkastettu.append(naapuri)
                etsi_naapuri = self.etsi(naapuri, maara+1, raja, fin)
                if etsi_naapuri == True:
                    self.matka += 1
                    return True
                if etsi_naapuri < min_arvo:
                    print("etsi naaapuri pienempi", etsi_naapuri)
                    min_arvo = etsi_naapuri
                print(self.tarkastettu)
                self.tarkastettu.pop()
                print(self.tarkastettu)
            else:
                print("naapuri oli tarkastetuissa")
        return min_arvo



    def heurestinen_arvo(self, ruutu, loppu):
        arvot_alku = ruutu.split(",")
        arvot_loppu = loppu.split(",")

        ruutu_x = abs(int(arvot_alku[0]) - int(arvot_loppu[0]))
        ruutu_y = abs(int(arvot_alku[1]) - int(arvot_loppu[1]))
        print("heurestiikka", ruutu_x+ruutu_y)
        return ruutu_x+ruutu_y

if __name__=="__main__":
    test = IDA_Star()
    test.heurestinen_arvo("0,0", "9,9")
    test.heurestinen_arvo("4,5","5,5")
    test.heurestinen_arvo("9,9", "8,8")
