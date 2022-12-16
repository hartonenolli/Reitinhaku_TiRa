import unittest
from algoritmit.ida_star import IdaStar
from tests.test_assets.d_assets import Assets


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.kartta_1 = IdaStar(1)
        self.kartta_testeille = IdaStar(4)

    def test_start_True(self):
        self.assertTrue(self.kartta_1)

    def test_tee_naapuri(self):
        tulos = self.kartta_1.tee_naapuri(0, 0)
        self.assertEqual(tulos, True)

    def test_tee_naapuri_2(self):
        tulos = self.kartta_1.tee_naapuri(0, 2)
        self.assertEqual(tulos, True)

    def test_tee_ruudut_ilman_naapureita(self):
        self.kartta_testeille.kartta = ["ppp", "pop", "ppp"]
        tulos = self.kartta_testeille.tee_ruudut([0, 0, 1, 1])
        self.assertEqual(tulos, {'1,1': []})

    def test_tee_ruudut(self):
        tulos = self.kartta_testeille.tee_ruudut([0, 0, 1, 1])
        self.assertEqual(tulos,
                         {'0,0': ['1,0', '0,1'], '1,0': ['0,0', '1,1'],
                          '0,1': ['0,0', '1,1'], '1,1': ['0,1', '1,0']})

    def test_algoritmi(self):
        self.kartta_testeille.katsottu = ["0,1"]
        tulos = self.kartta_testeille.ida_funktio(
            {'0,0': ['1,0', '0,1'], '1,0': ['0,0', '1,1'],
             '0,1': ['0,0', '1,1'], '1,1': ['0,1', '1,0']}, [0, 0, 1, 1])
        self.assertEqual(tulos, ['or', 'do'])

    def test_algoritmi_huonola_syötteella(self):
        self.kartta_testeille.kartta = ["ppp", "pop", "ppp"]
        tulos = self.kartta_testeille.ida_funktio({'1,1': []},[1,1,0,0])
        self.assertEqual(tulos, False)

    def test_algoritmi_oikealta_vasemmalle(self):
        self.kartta_testeille.kartta = ["opo", "opo", "ooo"]
        tulos = self.kartta_testeille.ida_funktio({'0,0': ['0,1'], '2,0': ['2,1'],
            '0,1': ['0,0', '0,2'], '2,1': ['2,0', '2,2'], '0,2': ['0,1', '1,2'],
            '1,2': ['0,2', '2,2'], '2,2': ['1,2', '2,1']}, [2,2,0,0])
        self.assertEqual(tulos, ["opo", "rpo", "rro"])

    def test_etsi_f_isompi_raja(self):
        tulos = self.kartta_testeille.etsi("0,0", 10, 0, "9,9")
        self.assertEqual(tulos, 28)