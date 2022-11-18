import unittest
from algoritmit.dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.nodes = {}
        self.neighbours = {}
        self.visited = []
        self.dijkstra_map = []
        self.cordinates = [0,0,9,9]

        self.map1 = [
            "ooopoooppo",
            "oooppooopo",
            "ppopoppopo",
            "opopoooopo",
            "oooppooooo",
            "oooooooopp",
            "ooooppoopo",
            "oopoopoooo",
            "ooopooopoo",
            "ooppoooppo"]

        self.map2 = [
            "opooppooop",
            "opoppooopp",
            "ooopoopopp",
            "ooopppoopo",
            "ppoppooooo",
            "pooooooopp",
            "poooppoopo",
            "poppppoooo",
            "oopoooopoo",
            "oopopooppo"]

        self.level_1 = Dijkstra(1)
        self.level_2 = Dijkstra(2)


    def test_start_True(self):
        self.assertTrue(self.level_1)

    def test_make_neighbour(self):
        result = self.level_1.make_neighbour(0, 0)
        self.assertEqual(result, True)

    def test_make_neighbour_2(self):
        result = self.level_1.make_neighbour(0, 2)
        self.assertEqual(result, False)

    def test_make_nodes(self):
        result = self.level_1.make_nodes([0,0,9,9])
        self.assertEqual(result, None)