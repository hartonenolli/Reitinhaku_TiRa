from kartat.kartta1 import Kartat
import heapq


class Dijkstra:
    """Alustetaan algoritmin toimintaan tarvittavat asiat.
        nodet: sisältää kaikki ruudut ja etäisyydet
        naapurit: sisältää kaikkien ruutujen viereiset ruudut
        käydyt: merkataan ruutu käydyksi, kun se on käsitelty
        dijkstra_kartta: 
        koordinaatit: aloitus ja lopetuskoordinaatit
        kartta: mitä karttaa käytetään
    """

    def __init__(self, map_number, nodes={}, neighbours={}, cordinates=[0, 0, 9, 9]):
        self.nodes = nodes
        self.neighbours = neighbours
        self.visited = []
        self.dijkstra_map = []
        self.cordinates = cordinates
        self.map = Kartat().maps(map_number)

    """Tehdään nodet käymällä kartta läpi.
        Ensin alustetaan alku ja loppu koordinaatteihin.
        Karttaa käydään läpi kahdella silmukalla
        Asetetaan jokaiselle valkoiselle ruudulle etäisyys lähtöruudusta = 999
        Lähtöruudulle annetaan etäisyydeksi = 0
        Kutsutaan naapurien teko funktiota jokaisella valkoisella ruudulla
        Kun kaikki ruudut on käyty läpi kutsutaan algoritmifunktiota.
    """

    def make_nodes(self, start_and_finish):
        self.cordinates = start_and_finish
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if str(x) == self.cordinates[1] and str(y) == self.cordinates[0]:
                    self.nodes[f"{x},{y}"] = 0
                    #self.neighbours[f"{x},{y}"] = []
                    self.make_neighbour(x, y)
                elif self.map[y][x] != "p":
                    self.nodes[f"{x},{y}"] = 999
                    #self.neighbours[f"{x},{y}"] = []
                    self.make_neighbour(x, y)
        # self.algorithim()
        # print(self.nodes)
        # print(self.neighbours)
        return self.nodes, self.neighbours

    """Käydään kartan ruudulta läpi naapurit
        Tarkastetaan ylös, alas, vasen ja oikea
        jos naapuri on valkoinen ruutu, niin lisätään se naapureihin.
    """

    def make_neighbour(self, x, y):
        self.neighbours[f"{x},{y}"] = []
        # Handle different directions
        # left
        if x > 0:
            if self.map[y][x-1] != "p":
                self.neighbours[f"{x},{y}"].append(f"{x-1},{y}")
        # up
        if y > 0:
            if self.map[y-1][x] != "p":
                self.neighbours[f"{x},{y}"].append(f"{x},{y-1}")
        # right
        if x < len(self.map[0])-1:
            if self.map[y][x+1] != "p":
                self.neighbours[f"{x},{y}"].append(f"{x+1},{y}")
        # down
        if y < len(self.map)-1:
            if self.map[y+1][x] != "p":
                self.neighbours[f"{x},{y}"].append(f"{x},{y+1}")
        return True

    """Algoritmin funktio
        Asetetaan kekoon alkuruutu etäisyys = 0 ja koordinaatit
        maali = loppuruudun koordinaatit
        Käydään kekoa läpi, niin kauan että ollaan käyty kaikki ruudut ja niiden naapurit
        Lisätään aina käsiteltävä ruutu käytyihin
        Jos käsiteltävä ruutu on käydyissä, niin ohitetaan se
        Tarkastellaan pienintä arvoa mitä on maaliruutuun.
    """

    def algorithim(self, nodes, neighbours, cordinates):
        self.nodes = nodes
        self.neighbours = neighbours
        self.cordinates = cordinates
        self.visited = []
        heap = []
        path = []
        heapq.heappush(heap, (0, f"{self.cordinates[1]},{self.cordinates[0]}"))
        target = f"{self.cordinates[3]},{self.cordinates[2]}"
        while heap != []:
            knot = min(heap)
            heap.remove(min(heap))
            if knot[1] in self.visited:
                continue
            self.visited.append(knot[1])
            for next in self.neighbours.get(knot[1]):
                now = self.nodes[next]
                new = self.nodes[knot[1]]+1
                if new < now:
                    self.nodes[next] = new
                    heapq.heappush(heap, (new, next))

        print(self.nodes[target])
        to_start = ""
        to_start += target
        prev_node = self.nodes[target]
        while len(path) < int(self.nodes[target]) - 1:
            for previous in self.neighbours[to_start]:
                if self.nodes[previous] < prev_node:
                    path.append(previous)
                    to_start = previous
                    prev_node = self.nodes[previous]
                    continue

        row = ""
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == "p":
                    row += "p"
                elif self.cordinates[1] == str(x) and self.cordinates[0] == str(y):
                    row += "o"
                elif self.cordinates[3] == str(x) and self.cordinates[2] == str(y):
                    row += "o"
                elif f"{x},{y}" in path:
                    row += "r"
                else:
                    row += "d"
            self.dijkstra_map.append(row)
            row = ""
        return self.dijkstra_map
