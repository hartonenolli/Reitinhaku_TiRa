from kartat.kartta1 import Kartat
import heapq

class Dijkstra:
    def __init__(self, map_number):
        self.nodes = {}
        self.neighbours = {}
        self.visited = []
        self.dijkstra_map = []
        self.cordinates = [0,0,9,9]
        self.map = Kartat().maps(map_number)
    
    def get_nodes(self):
        return self.nodes
    
    def make_nodes(self, start_and_finish):
        self.cordinates = start_and_finish
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if str(x) == self.cordinates[0] and str(y) == self.cordinates[1]:
                    #print(y, x)
                    self.nodes[f"{x},{y}"] = 0
                    self.neighbours[f"{x},{y}"] = []
                #else:
                elif self.map[y][x] != "p":
                    self.nodes[f"{x},{y}"] = 999
                    self.neighbours[f"{x},{y}"] = []
                self.make_neighbour(x,y)
        #print(self.nodes)
        #self.make_neighbour()
        #self.algorithim()
        #print(self.neighbours)
        self.algorithim()

    def make_neighbour(self, x, y):
        #for y in range(len(self.map)):
        #    for x in range(len(self.map[0])):
        if self.map[y][x] == "o":
            #Handle different directions
            #left
            if x > 0:
                if self.map[y][x-1] != "p":
                    self.neighbours[f"{x},{y}"].append(f"{x-1},{y}")
            #up
            if y > 0:
                if self.map[y-1][x] != "p":
                    self.neighbours[f"{x},{y}"].append(f"{x},{y-1}")
            #right
            if x < len(self.map[0])-1:
                if self.map[y][x+1] != "p":
                    self.neighbours[f"{x},{y}"].append(f"{x+1},{y}")
            #down
            if y < len(self.map)-1:
                if self.map[y+1][x] != "p":
                    self.neighbours[f"{x},{y}"].append(f"{x},{y+1}")
        #print(self.neighbours)

    def printtaa(self, number):
        print(self.map)
        self.make_nodes()

    def algorithim(self):
        #print(self.neighbours)
        heap = []
        heapq.heappush(heap, (f"{self.cordinates[0]},{self.cordinates[1]}", self.nodes.get(f"{self.cordinates[0]},{self.cordinates[1]}")))
        #print(heap)
        target = f"{self.cordinates[2]},{self.cordinates[3]}"
        while heap != []:
            #print(heap)
            #print(min(heap))
            knot = min(heap)
            heap.remove(min(heap))
            #print(knot[0])
            #print(self.neighbours.get(knot[0]))
            if knot[0] in self.visited:
                #print("visited")
                continue
            self.visited.append(knot[0])
            for next in self.neighbours.get(knot[0]):
                #print("täällä")
                #print(self.neighbours.get(knot[0]))
                now = self.nodes[next]
                new = self.nodes[knot[0]]+1
                #print(new, now)
                if new < now:
                    self.nodes[next] = new
                    heapq.heappush(heap, (next, new))
                    #heap.push((new,next))
                    #print("mentiin")
        #print(new)
        #print(target)
        print(self.nodes[target])
