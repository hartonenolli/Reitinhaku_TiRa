from kartat.kartta1 import Kartat
import heapq

class Dijkstra:
    def __init__(self, map_number):
        self.nodes = {}
        self.map = Kartat().maps(map_number)
    
    def get_nodes(self):
        return self.nodes
    
    def make_nodes(self, number1, number2):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if str(i) == number1 and str(j) == number2:
                    print(i, j)
                    self.nodes[f"{i},{j}"] = 0
                else:
                    self.nodes[f"{i},{j}"] = 999
        #print(self.nodes)
        self.algorithim()

    def printtaa(self, number):
        print(self.map)
        self.make_nodes()

    def algorithim(self):
        keko = []
        heapq.heappush(keko, ("0,0", self.nodes.get("0,0")))
        print(keko)
        #while keko != []:
        solmu = keko.pop()[0]
        print(solmu)
        #    if kasitelty[solmu]
        #        continue
        #    kasitelty[solmu] = true
        #    for kaari in verkko[solmu]
        #        nyky = etaisyys[kaari.loppu]
        #        uusi = etaisyys[solmu]+kaari.paino
        #        if uusi < nyky
        #            etaisyys[kaari.loppu] = uusi
        #            keko.push((uusi,kaari.loppu))
