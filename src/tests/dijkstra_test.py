import unittest
from algoritmit.dijkstra import Dijkstra
from tests.test_assets.d_assets import Assets


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.level_1 = Dijkstra(1)
        self.level_2 = Dijkstra(2)

    def test_start_True(self):
        self.assertTrue(self.level_1)

    def test_make_neighbour(self):
        result = self.level_1.tee_naapuri(0, 0)
        self.assertEqual(result, True)

    def test_make_neighbour_2(self):
        result = self.level_1.tee_naapuri(0, 2)
        self.assertEqual(result, True)

    def test_make_nodes(self):
        result = self.level_1.tee_ruudut([0, 0, 9, 9])
        self.assertEqual(result, Assets().nodes_tests(1))

    def test_algorithim(self):
        result = Dijkstra(1).algoritmi(
            Assets().node_algorithim(), Assets().neighbours_algorithim(), [0, 0, 9, 9])
        self.assertEqual(result, Assets().algorithim_result())
