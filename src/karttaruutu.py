
"""KarttaRuutu luokka alustaa käyttöliittymän.
    Kutsutaan käytettäviä karttoja Kartat luokasta.
    Algoritmeja kutsutaan omista luokistaan.
"""

from tkinter import ttk, constants, Canvas
from kartat.kartta1 import Kartat
from algoritmit.dijkstra import Dijkstra
from algoritmit.ida_star import IdaStar
import datetime


class KarttaRuutu:
    """Käyttäjälle avataan näkymä, josta voi valita käytettäväksi:
        kartan, alun- ja lopun koordinaatiyt ja millä algoritmilla
        reitti haetaan.
    """

    def __init__(self, root):
        self._juuri = root
        self._freimi = None
        self.kanvas = None
        self.x_y_lista = ["0", "0", "9", "9"]
        self.dijkstra = None
        self.ida_star = None
        self.kartta = 1
        self._alusta()

    def pack(self):
        self._freimi.pack(fill=constants.X)

    def destroy(self):
        self._freimi.destroy()

    def aseta_dijkstra(self, koordinaatit, number):
        """Funktio dijkstran algoritmin etsimisen alustamiseksi."""
        self.kartta = number
        self.dijkstra = 1
        self.ida_star = None
        self._tarkasta_koordinaatit(koordinaatit, self.kartta)

    def set_ida_star(self, koordinaatit, number):
        """Funktio ida-* algoritmin etsimisen alustamiseksi."""
        self.kartta = number
        self.ida_star = 1
        self.dijkstra = None
        self._tarkasta_koordinaatit(koordinaatit, self.kartta)

    def aseta_koordinaatit_kanvakselle(self):
        """Alustetaan kartta käymällä rivejä läpi,
            jos kartalla on 'o', niin tulee valkoinen,
            jos kartalla on 'p', niin tulee musta.
            Lisäksi, jos valkoisella on valittu alku koordinaatti,
            niin tulee sininen. Punainen tulee loppukoordinaatille.
        """
        nayta_kartta = Kartat().maps(self.kartta)
        if self.kanvas is not None:
            self.kanvas.after(0, self.kanvas.destroy())
        self.kanvas = Canvas(self._juuri, width=500, height=500)
        if nayta_kartta[int(self.x_y_lista[0])][int(self.x_y_lista[1])] == "p":
            print("Alku ei ole oikein!")
            self._alusta()
        elif nayta_kartta[int(self.x_y_lista[2])][int(self.x_y_lista[3])] == "p":
            print("Loppu ei ole oikein!")
            self._alusta()
        elif self.dijkstra == 1:
            print("Lyhyin reitti löydetty:")
            aika_alkaa = datetime.datetime.now()
            tee_kartta = Dijkstra(self.kartta).tee_ruudut(self.x_y_lista)
            nayta_kartta = Dijkstra(
                self.kartta).algoritmi(tee_kartta[0], tee_kartta[1], self.x_y_lista)
            aika_loppuu = datetime.datetime.now()
            lopullinen_aika = aika_loppuu-aika_alkaa
            sekuntit = str(lopullinen_aika).split(":")
            print(f"Reitti löytyi ajassa {sekuntit[-1]}s")
        elif self.ida_star == 1:
            print("Lyhin reitti löydetty:")
            aika_alkaa = datetime.datetime.now()
            tee_kartta = IdaStar(self.kartta).tee_ruudut(self.x_y_lista)
            nayta_kartta = IdaStar(self.kartta).ida_funktio(
                tee_kartta, self.x_y_lista)
            aika_loppuu = datetime.datetime.now()
            lopullinen_aika = aika_loppuu-aika_alkaa
            sekuntit = str(lopullinen_aika).split(":")
            print(f"Reitti löytyi ajassa {sekuntit[-1]}s")
        y_koordinaatti = 0
        x_koordinaatti = 0

        mista = 40
        mihin = 401

        if self.kartta == 2:
            mista = 30
            mihin = 461
        elif self.kartta == 3:
            mista = 23
            mihin = 461

        for i in range(mista, mihin, mista):
            for j in range(mista, mihin, mista):
                if nayta_kartta[y_koordinaatti][x_koordinaatti] == "o":
                    self.kanvas.create_rectangle(
                        j, i, j+mista, i+mista, fill="white")
                    if str(y_koordinaatti
                           ) == self.x_y_lista[0] and str(x_koordinaatti) == self.x_y_lista[1]:
                        self.kanvas.create_rectangle(
                            j, i, j+mista, i+mista, fill="blue")
                    if str(y_koordinaatti
                           ) == self.x_y_lista[2] and str(x_koordinaatti) == self.x_y_lista[3]:
                        self.kanvas.create_rectangle(
                            j, i, j+mista, i+mista, fill="red")
                elif nayta_kartta[y_koordinaatti][x_koordinaatti] == "d":
                    self.kanvas.create_rectangle(
                        j, i, j+mista, i+mista, fill="green")
                elif nayta_kartta[y_koordinaatti][x_koordinaatti] == "r":
                    self.kanvas.create_rectangle(
                        j, i, j+mista, i+mista, fill="yellow")
                elif nayta_kartta[y_koordinaatti][x_koordinaatti] == "p":
                    self.kanvas.create_rectangle(
                        j, i, j+mista, i+mista, fill="black")
                    if str(y_koordinaatti
                           ) == self.x_y_lista[0] and str(x_koordinaatti) == self.x_y_lista[1]:
                        self.kanvas.create_rectangle(
                            j, i, j+mista, i+mista, fill="grey")
                    if str(y_koordinaatti
                           ) == self.x_y_lista[2] and str(x_koordinaatti) == self.x_y_lista[3]:
                        self.kanvas.create_rectangle(
                            j, i, j+mista, i+mista, fill="grey")
                x_koordinaatti += 1
            y_koordinaatti += 1
            x_koordinaatti = 0
        self.dijkstra = None
        self.ida_star = None
        self.kanvas.pack(padx=0, pady=50)

    def _tarkasta_koordinaatit(self, koordinaatit, kartta_numero):
        """Tarkastetaan annetut koordinaattien syötteet.
            Jos syöte ei ole oikean muotoinen, niin asetetaan oletusarvot.
            Syötteet annetaan listana ja karttanumero kertoo
            kuinka iso syöte voi olla.
        """
        if kartta_numero == 1:
            if str(koordinaatit[1]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, alku x väärin. Asetettu 0")
                koordinaatit[1] = str(0)
            if str(koordinaatit[0]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, alku y väärin. Asetetu 0")
                koordinaatit[0] = str(0)
            if str(koordinaatit[3]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, loppu x väärin. Asetettu 9")
                koordinaatit[3] = str(9)
            if str(koordinaatit[2]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, loppu y väärin. Asetettu 9")
                koordinaatit[2] = str(9)
        elif kartta_numero == 2:
            if str(koordinaatit[1]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, alku x väärin. Asetettu 0")
                koordinaatit[1] = str(0)
            if str(koordinaatit[0]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, alku y väärin. Asetetu 0")
                koordinaatit[0] = str(0)
            if str(koordinaatit[3]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, loppu x väärin. Asetettu 14")
                koordinaatit[3] = str(14)
            if str(koordinaatit[2]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, loppu y väärin. Asetettu 14")
                koordinaatit[2] = str(14)
        else:
            if str(koordinaatit[1]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, alku x väärin. Asetettu 0")
                koordinaatit[1] = str(0)
            if str(koordinaatit[0]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, alku y väärin. Asetetu 0")
                koordinaatit[0] = str(0)
            if str(koordinaatit[3]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, loppu x väärin. Asetettu 19")
                koordinaatit[3] = str(19)
            if str(koordinaatit[2]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                          "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, loppu y väärin. Asetettu 19")
                koordinaatit[2] = str(19)
        print("Valitut koordinaatit:")
        print(f"Alku:  {koordinaatit[1]:2} {koordinaatit[0]}")
        print(f"Loppu: {koordinaatit[3]:2} {koordinaatit[2]}")
        self.x_y_lista = koordinaatit
        self.kartta = kartta_numero
        self.aseta_koordinaatit_kanvakselle()

    def _alusta(self):
        """Alustetaan näkymä.
            Tässä asetetaan kaikki elementit paikoilleen.
            Painamalla Kartta painikkeita saa kartat näkyviin.
            Painamalla Dijkstra painiketta ennen kartta painiketta
            aloitetaan reitinhaku algoritmilla.
            Painamalla ida-* painiketta aloitetaan reitinhaku algoritmilla.
        """
        self._freimi = ttk.Frame(master=self._juuri)
        label = ttk.Label(master=self._freimi, text="Reitin haku")
        label_alulle = ttk.Label(
            master=self._freimi, text="Aloituskoordinaatti")
        label_lopulle = ttk.Label(
            master=self._freimi, text="Lopetuskoordinaatti")

        x_1 = ttk.Entry(master=self._freimi)
        y_1 = ttk.Entry(master=self._freimi)
        x_2 = ttk.Entry(master=self._freimi)
        y_2 = ttk.Entry(master=self._freimi)

        label.grid(row=0, column=0)
        label_alulle.grid(row=3, column=0)
        x_1.grid(row=3, column=1)
        y_1.grid(row=3, column=2)
        label_lopulle.grid(row=4, column=0)
        x_2.grid(row=4, column=1)
        y_2.grid(row=4, column=2)

        painike_1 = ttk.Button(
            master=self._freimi,
            text="Kartta1",
            command=lambda: self._tarkasta_koordinaatit(
                [y_1.get(), x_1.get(), y_2.get(), x_2.get()], 1)
        )

        painike_1.grid(row=1, column=0)

        painike_2 = ttk.Button(master=self._freimi,
                                text="Kartta2",
                                command=lambda:
                                self._tarkasta_koordinaatit(
                                    [y_1.get(), x_1.get(), y_2.get(), x_2.get()],
                                    2))

        painike_2.grid(row=1, column=1)

        painike_3 = ttk.Button(master=self._freimi,
                              text="Kartta3",
                              command=lambda:
                              self._tarkasta_koordinaatit(
                                  [y_1.get(), x_1.get(), y_2.get(), x_2.get()],
                                  3))

        painike_3.grid(row=1, column=2)

        painike_dijkstra = ttk.Button(master=self._freimi,
                                     text="Dijkstra",
                                     command=lambda:
                                     self.aseta_dijkstra([y_1.get(), x_1.get(), y_2.get(), x_2.get()],
                                                       self.kartta))

        painike_dijkstra.grid(row=2, column=0)

        painike_ida = ttk.Button(master=self._freimi,
                                text="IDA-*",
                                command=lambda:
                                self.set_ida_star([y_1.get(), x_1.get(), y_2.get(), x_2.get()],
                                                  self.kartta))

        painike_ida.grid(row=2, column=1)
