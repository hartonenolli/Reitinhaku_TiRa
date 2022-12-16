import unittest
from kekokansio.keko import Keko

class TestKeko(unittest.TestCase):
    def setUp(self):
        self.testi_keko = Keko()

    def test_keko_on_olemassa(self):
        self.assertTrue(Keko())

    def test_lisaa_kekoon(self):
        self.testi_keko.keko_rakenne = [(10, '3,7'), (10, '5,5'), (10, '0,6'), (11, '0,7'), (11, '1,8')]
        tulos = self.testi_keko.lisaa_kekoon((7, '7,7'))
        self.assertEqual(tulos, [(7, '7,7'), (10, '3,7'), (10, '5,5'), (11, '0,7'), (11, '1,8'), (10, '0,6')])
