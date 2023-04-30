import unittest
from testavimas_testu_kurimo_praktikos_uzduotys import PaskolosKalkuliatorius


class TestPaskolosKalkuliatorius(unittest.TestCase):
    def setUp(self):
        self.pradine_verte = PaskolosKalkuliatorius(10000, 0.05, 5)
        self.padidinti_palukanas = PaskolosKalkuliatorius(10000, 0.15, 5)
        self.padidinti_laikotarpi = PaskolosKalkuliatorius(10000, 0.05, 10)

    def test_menesine_imoka(self):
        self.assertAlmostEqual(self.pradine_verte.periodine_imoka(), 188.7123, 3)
        self.assertAlmostEqual(self.padidinti_palukanas.periodine_imoka(), 237.8993, 3)
        self.assertAlmostEqual(self.padidinti_laikotarpi.periodine_imoka(), 106.0655, 3)

    def test_menesine_imoka(self):
        self.assertAlmostEqual(self.pradine_verte.paskolos_palukanu_suma(), 1322.7401, 3)
        self.assertAlmostEqual(self.padidinti_palukanas.paskolos_palukanu_suma(), 4273.9580, 3)
        self.assertAlmostEqual(self.padidinti_laikotarpi.paskolos_palukanu_suma(), 2727.8618, 3)


if __name__ == "__main__":
    unittest.main()