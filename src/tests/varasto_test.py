import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_neg = Varasto(-2, -1)
        self.vastaus = str(self.varasto)
        self.varasto_pos = Varasto(10, 11)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_ei_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.varasto_neg.tilavuus, 0)

    def test_alku_saldo_ei_negatiivinen(self):
        self.assertAlmostEqual(self.varasto_neg.saldo, 0)

    def test_vastaus(self):
        self.assertAlmostEqual(self.vastaus, "saldo = 0, vielä tilaa 10")

    def test_saldo_sama_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto_pos.saldo, 10)

    def test_lisaa_varastoon_neg_maara(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual("", "")

    def test_lisaa_varastoon_tilaa_riittaa(self):
        self.varasto.lisaa_varastoon(2)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_lisaa_varastoon_enemman_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_neg_maara(self):
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual("-2", "-2")

    def test_ota_varastosta_enemman_kuin_saldo(self):
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.saldo, 0)
