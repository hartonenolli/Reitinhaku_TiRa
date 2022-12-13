
"""Algoritmi, jota kutsutaan karttaruudun kautta"""

from kartat.kartta1 import Kartat
from kekokansio.keko import Keko


class Dijkstra:
    """Luokka etsii lyhyimmän reitin Dijkstran algoritmin avulla.
        Luokka käyttää kekorakennetta kekokansio.keko tiedostoosa olevalla luokalla Keko.
        Kartta Haetaan kartat.kartta1 tiedostosta Kartta luokasta."""

    def __init__(self, kartta_num):
        """Alustetaan algoritmin toimintaan tarvittavat asiat.
            nodet: sisältää kaikki ruudut ja etäisyydet
            naapurit: sisältää kaikkien ruutujen viereiset ruudut
            käydyt: merkataan ruutu käydyksi, kun se on käsitelty
            dijkstra_kartta:
            koordinaatit: aloitus ja lopetuskoordinaatit
            kartta: mitä karttaa käytetään
        """
        self.ruudut = {}
        self.naapurit = {}
        self.vierailtu = []
        self.dijkstra_kartta = []
        self.koordinaatit = None
        self.kartta = Kartat().maps(kartta_num)

    def tee_ruudut(self, alku_loppu):
        """Tehdään nodet käymällä kartta läpi.
            Ensin alustetaan alku ja loppu koordinaatteihin.
            Karttaa käydään läpi kahdella silmukalla
            Asetetaan jokaiselle valkoiselle ruudulle etäisyys lähtöruudusta = 999
            Lähtöruudulle annetaan etäisyydeksi = 0
            Kutsutaan naapurien teko funktiota jokaisella valkoisella ruudulla
            Kun kaikki ruudut on käyty läpi kutsutaan algoritmifunktiota.
        """
        self.koordinaatit = alku_loppu
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[0])):
                if str(x) == self.koordinaatit[1] and str(y) == self.koordinaatit[0]:
                    self.ruudut[f"{x},{y}"] = 0
                    self.tee_naapuri(x, y)
                elif self.kartta[y][x] != "p":
                    self.ruudut[f"{x},{y}"] = 999
                    self.tee_naapuri(x, y)

        return self.ruudut, self.naapurit

    def tee_naapuri(self, x, y):
        """Käydään kartan ruudulta läpi naapurit
            Tarkastetaan ylös, alas, vasen ja oikea
            jos naapuri on valkoinen ruutu, niin lisätään se naapureihin.
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

    def algoritmi(self, ruudut, naapurit, koordinaatit):
        """Algoritmin funktio
            Asetetaan kekoon alkuruutu etäisyys = 0 ja koordinaatit
            maali = loppuruudun koordinaatit
            Käydään kekoa läpi, niin kauan että ollaan käyty kaikki ruudut ja niiden naapurit
            Lisätään aina käsiteltävä ruutu käytyihin
            Jos käsiteltävä ruutu on käydyissä, niin ohitetaan se
            Tarkastellaan pienintä arvoa mitä on maaliruutuun.
        """
        self.ruudut = ruudut
        self.naapurit = naapurit
        self.koordinaatit = koordinaatit
        keko = Keko()
        polku = []
        keko.lisaa_kekoon(
            (0, f"{self.koordinaatit[1]},{self.koordinaatit[0]}"))
        maali = f"{self.koordinaatit[3]},{self.koordinaatit[2]}"
        while keko.keko_rakenne != []:
            solmu = keko.poista_keosta()
            if solmu[1] in self.vierailtu:
                continue
            self.vierailtu.append(solmu[1])
            for seuraava in self.naapurit.get(solmu[1]):
                nyt = self.ruudut[seuraava]
                uusi = self.ruudut[solmu[1]]+1
                if uusi < nyt:
                    self.ruudut[seuraava] = uusi
                    keko.lisaa_kekoon((uusi, seuraava))

        print(f"Reitin pituus {self.ruudut[maali]} ruutua")
        alkuun = ""
        alkuun += maali
        aikaisempi_ruutu = self.ruudut[maali]
        while len(polku) < int(self.ruudut[maali]) - 1:
            for previous in self.naapurit[alkuun]:
                if self.ruudut[previous] < aikaisempi_ruutu:
                    polku.append(previous)
                    alkuun = previous
                    aikaisempi_ruutu = self.ruudut[previous]
                    continue

        return self.kartan_palautus(polku)

    def kartan_palautus(self, polku):
        """Kartan tekevä funktio.
            Asetetaan reitti kartalle merkkaamalla se r kirjaimella
        """
        rivi = ""
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[0])):
                if self.kartta[y][x] == "p":
                    rivi += "p"
                elif self.koordinaatit[1] == str(x) and self.koordinaatit[0] == str(y):
                    rivi += "o"
                elif self.koordinaatit[3] == str(x) and self.koordinaatit[2] == str(y):
                    rivi += "o"
                elif f"{x},{y}" in polku:
                    rivi += "r"
                else:
                    rivi += "d"
            self.dijkstra_kartta.append(rivi)
            rivi = ""
        return self.dijkstra_kartta
