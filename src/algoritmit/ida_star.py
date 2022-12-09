from kartat.kartta1 import Kartat


class IdaStar:
    def __init__(self, nyky_kartta):
        self.kartta = Kartat().maps(nyky_kartta)
        self.alku = "0,0"
        self.loppu = "9,9"
        self.koordinaatit = None
        self.naapurit = {}
        self.tarkastettu = []
        self.katsottu = []

    def tee_ruudut(self, alku_ja_loppu):
        """Käydään läpi karttaa.
            Kaikille ruuduille, jotka eivät ole 'p' tehdään naapurit.
            Funktiolle annetaan lista, jossa on alku ja loppu koordinaatit.
            Esimerkki:
            ['0', '0', '9', '9']
            Kutsutaan tee_naapurit funktiota.
            Palautetaan sanakirja, jossa on ruutujen naapurit listassa.
            Esimerkki:
            {'0,0': ['1,0','0,1'], '1,0': ['0,0', '2,0', '1,2']}
        """
        self.koordinaatit = alku_ja_loppu
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[0])):
                if self.kartta[y][x] != "p":
                    self.tee_naapuri(x, y)

        return self.naapurit

    def tee_naapuri(self, x, y):
        """Käydään läpi yksittäisen ruudun naapurit.
            Tarkastetaan vasen, oikea, ylä ja ala ruudut.
            Tehdään kutsutulle ruudulle sanakirjaan avain.
            Lisätään naapurit listana.
            Annetut arvot esimerkkinä:
            0, 0
            Tehty sanakirja esimerkkinä:
            {'0,0': ['1,0','0,1']}
        """
        self.naapurit[f"{x},{y}"] = []

        if x > 0:
            if self.kartta[y][x-1] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x-1},{y}")

        if y > 0:
            if self.kartta[y-1][x] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x},{y-1}")

        if x < len(self.kartta[0])-1:
            if self.kartta[y][x+1] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x+1},{y}")

        if y < len(self.kartta)-1:
            if self.kartta[y+1][x] != "p":
                self.naapurit[f"{x},{y}"].append(f"{x},{y+1}")
        return True

    def ida_funktio(self, naapureita, koordinaatti):
        """Algoritmifunktio, joka aloittaa algoritmin.
            Alustetaan naapurit. Merkataan alku ja loppu.
            Kutsutaan heurestisen arvon funktiota, jolla saadaan laskettu etäisyys.
            Silmukan avulla kutsutaan rekursiivista funktiota ja aloitetaan reitin etsintä.
            Kun reitti on löytynyt poistutaan silmukasta ja palautetaan kartan_palautus
            funktion arvo.
        """
        self.naapurit = naapureita
        self.alku = f"{koordinaatti[1]},{koordinaatti[0]}"
        self.loppu = f"{koordinaatti[3]},{koordinaatti[2]}"
        start = self.alku
        fin = self.loppu
        raja = self.heurestinen_arvo(start, fin)
        while True:
            ruudun_tila = self.etsi(start, 0, raja, fin)
            if ruudun_tila is True:
                print(len(self.tarkastettu))
                break
            if ruudun_tila >= 999:
                return False
            raja = ruudun_tila
        print(f"Reitin pituus {len(self.tarkastettu)} ruutua")
        return self.kartan_palautus(start, fin)

    def etsi(self, node, maara, raja, fin):
        """Rekursiivinen etsintäfunktio algoritmille.
            Lasketaan ensin kysisen ruudun etäisyys.
            Jos etäisyys on edellistä huonompi palautetaan edellinen.
            Jos ollaan saavuttu maaliin, niin voidaan poistua silmuksta.

            Käydään ruudun naapureita läpi ja kutsutaan niitä samalla rekursiivisella funktiolla.
            Löytämällä maalin lopetetaan silmukka.
            min_arvon avulla pidetään reitin etäisyyttä yllä.
            Palautetaan reitin etäisyys.

            Funktiolle annetaan:
                Tutkittava ruutu, ruudun etäisyys alusta, loppuetäisyys, loppuruutu
        """
        f = maara+self.heurestinen_arvo(node, fin)
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
                if etsi_naapuri is True:
                    return True
                if etsi_naapuri < min_arvo:
                    min_arvo = etsi_naapuri
                self.tarkastettu.pop()

        return min_arvo

    def heurestinen_arvo(self, ruutu, loppu):
        """Funktio laskee tutukittavan ruudun ja lopun heurestisen etäisyyden."""
        arvot_alku = ruutu.split(",")
        arvot_loppu = loppu.split(",")

        ruutu_x = abs(int(arvot_alku[0]) - int(arvot_loppu[0]))
        ruutu_y = abs(int(arvot_alku[1]) - int(arvot_loppu[1]))
        return ruutu_x+ruutu_y

    def kartan_palautus(self, start, fin):
        """Funktio palauttaa muokatun kartan.
            Reitti merkataan r-kirjaimella.
            Kartalle merkataan kaikki ruudut, jossa algoritmi on käynyt d-kirjaimella.
        """
        row = ""
        ida_star_map = []
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
            ida_star_map.append(row)
            row = ""
        return ida_star_map
