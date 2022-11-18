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
                    self.nodes[f"{x},{y}"] = 0
                    self.neighbours[f"{x},{y}"] = []
                elif self.map[y][x] != "p":
                    self.nodes[f"{x},{y}"] = 999
                    self.neighbours[f"{x},{y}"] = []
                self.make_neighbour(x,y)
        self.algorithim()

    def make_neighbour(self, x, y):
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

    def algorithim(self):
        heap = []
        heapq.heappush(heap, (self.nodes.get(f"{self.cordinates[0]},{self.cordinates[1]}"), f"{self.cordinates[0]},{self.cordinates[1]}"))
        target = f"{self.cordinates[2]},{self.cordinates[3]}"
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
