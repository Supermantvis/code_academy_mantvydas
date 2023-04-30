import unittest
from testavimas_testu_kurimo_praktikos_uzduotys import PaskolosKalkuliatorius


class TestPaskolosKalkuliatorius(unittest.TestCase):
    def setUp(self):
        self.obj = PaskolosKalkuliatorius(10000, 5, 5)
        self.padidinti_palukanas = PaskolosKalkuliatorius(10000, 10, 5)
        self.padidinti_laikotarpi = PaskolosKalkuliatorius(10000, 10, 10)

    def test_menesine_imoka(self):
        self.assertEqual(self.obj.menesine_imoka(), 175)
        self.assertAlmostEqual(self.padidinti_palukanas.menesine_imoka(), 183.3333, 3)
        self.assertAlmostEqual(self.padidinti_laikotarpi.menesine_imoka(), 91.6666, 3)


if __name__ == "__main__":
    unittest.main()