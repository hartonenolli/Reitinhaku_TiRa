import unittest
from algoritmit.ida_star import IDA_Star
from tests.test_assets.d_assets import Assets

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.kartta_1 = IDA_Star(1)
        self.kartta_testeille = IDA_Star(4)

    def test_start_True(self):
        self.assertTrue(self.kartta_1)

    def test_tee_naapuri(self):
        tulos = self.kartta_1.tee_naapuri(0, 0)
        self.assertEqual(tulos, True)

    def test_tee_naapuri_2(self):
        tulos = self.kartta_1.tee_naapuri(0, 2)
        self.assertEqual(tulos, True)

    def test_tee_naapurit(self):
        tulos = self.kartta_testeille.tee_ruudut([0, 0, 1, 1])
        self.assertEqual(tulos, ({'0,0': [], '1,0': [], '0,1': [], '1,1': []},
        {'0,0': ['1,0', '0,1'], '1,0': ['0,0', '1,1'],
        '0,1': ['0,0', '1,1'], '1,1': ['0,1', '1,0']}))
    
    def test_algoritmi(self):
        tulos = IDA_Star(4).ida_funktio({'0,0': [], '1,0': [], '0,1': [], '1,1': []},
        {'0,0': ['1,0', '0,1'], '1,0': ['0,0', '1,1'],
        '0,1': ['0,0', '1,1'], '1,1': ['0,1', '1,0']}, [0, 0, 1, 1])
        self.assertEqual(tulos, ['or', 'oo'])