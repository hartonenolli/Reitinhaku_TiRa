
"""Dijkstran algoritmi kutsuu luokkaa kolmen eri funktion avulla."""

class Keko:
    """Keko dijkstran algoritmia varten"""
    def __init__(self):
        """Alustetaan keolle lista"""
        self.keko_rakenne = []

    def tarkista_keon_pituus(self, ruutu):
        """Funktio keon pituuden tarkastamiselle.
            Jos koen pituus on 1 palautetaan keko sellaisenaan.
            Jon keon pituus on 2 järjestetään pienempi ensimmäiseksi.
            Muuten palautetaan: True
        """
        if len(self.keko_rakenne) == 1:
            return False
        if len(self.keko_rakenne) == 2:
            if ruutu[0] > self.keko_rakenne[1][0]:
                self.keko_rakenne[0] = self.keko_rakenne[1]
                self.keko_rakenne[1] = ruutu
            return False
        return True

    def lisaa_kekoon(self, ruutu):
        """Keon lisäämisen funktio.
            Lisätään uusi ruutu keon loppuun.
            Tarkastetaan vanhemman ja ruudun arvot.
            Vaihdetaan niiden paikkaa jos vanhempi on isompi.
            Ylläpidetään näin kekorakennetta.
            Palautetaan keko listana.
        """
        if self.keko_rakenne == []:
            self.keko_rakenne.append(ruutu)
            return self.keko_rakenne
        kohta = len(self.keko_rakenne)
        self.keko_rakenne.append(ruutu)
        vanhempi = self.keko_rakenne[kohta//2]
        while vanhempi[0] > ruutu[0]:
            self.keko_rakenne[kohta] = vanhempi
            self.keko_rakenne[kohta//2] = ruutu
            kohta = kohta//2
            vanhempi = self.keko_rakenne[kohta//2]

        return self.keko_rakenne

    def poista_keosta(self):
        """Funktio pienimmän alkion poistamiselle.
            Pienin alkio on keon ensimmäisenä.
            Jos keon pituus on poistamisen jälkeen yli kaksi,
            niin laitetaan viimeinen alkio ensimmäiseksi.
            Tarkastetaan vasemman- ja oikean lapsen suhdetta.
            Näin ylläpidetään kekorakennetta.
            Palautetaan pienein alkio.
        """
        if len(self.keko_rakenne) == 1:
            return self.keko_rakenne.pop()
        poistettu = self.keko_rakenne[0]
        self.keko_rakenne[0] = self.keko_rakenne[len(self.keko_rakenne)-1]
        ruutu = self.keko_rakenne.pop(-1)
        if self.tarkista_keon_pituus(ruutu) is True:
            vanhemman_indeksi = 0
            vasemman_indeksi = 1
            vasen_lapsi = self.keko_rakenne[1]
            oikea_lapsi = self.keko_rakenne[2]
            while vanhemman_indeksi < len(self.keko_rakenne) - 1:
                if vasen_lapsi[0] <= oikea_lapsi[0]:
                    if ruutu[0] > vasen_lapsi[0]:
                        self.keko_rakenne[vanhemman_indeksi] = vasen_lapsi
                        self.keko_rakenne[vasemman_indeksi] = ruutu
                        vanhemman_indeksi = vasemman_indeksi
                        vasemman_indeksi += vasemman_indeksi + 1
                        if vasemman_indeksi >= len(self.keko_rakenne) - 1:
                            break
                        vasen_lapsi = self.keko_rakenne[vasemman_indeksi]
                        oikea_lapsi = self.keko_rakenne[vasemman_indeksi+1]
                    else:
                        break
                elif vasen_lapsi[0] >= oikea_lapsi[0]:
                    if ruutu[0] > oikea_lapsi[0]:
                        self.keko_rakenne[vanhemman_indeksi] = oikea_lapsi
                        self.keko_rakenne[vasemman_indeksi+1] = ruutu
                        vanhemman_indeksi = vasemman_indeksi + 1
                        vasemman_indeksi += vasemman_indeksi + 1
                        if vasemman_indeksi >= len(self.keko_rakenne) - 1:
                            break
                        vasen_lapsi = self.keko_rakenne[vasemman_indeksi]
                        oikea_lapsi = self.keko_rakenne[vasemman_indeksi+1]
                    else:
                        break
                else:
                    break

        return poistettu
