import unittest
from karttaruutu import KarttaRuutu
from kayttoliittyma import UserInterface


class TestKarttaRuutu(unittest.TestCase):
    def setUp(self):
        pass

    def test_cordinates_for_canvas(self):
        result = KarttaRuutu.set_cordinates_for_canvas()
        self.assertEqual(result, True)
