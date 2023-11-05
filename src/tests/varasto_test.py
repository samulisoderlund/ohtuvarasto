import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_tilavuus_alle_0(self):
        self.varasto = Varasto(-1)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_alku_saldo_alle_0(self):
        self.varasto = Varasto(10, -1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_konstruktori_alku_saldo_yli_tilavuuden(self):
        self.varasto = Varasto(10, 20)
        self.assertEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_maara_alle_0(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, saldo_ennen)

    def test_lisays_maara_ylittaa_jaljella_olevan_tilavuuden(self):
        tilavuus = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(tilavuus + 10)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_maara_alle_0(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, saldo_ennen)

    def test_ottaminen_maara_ylittaa_saldon(self):
        saldo_ennen = self.varasto.saldo
        paljonko_saatiin = self.varasto.ota_varastosta(saldo_ennen + 10)
        self.assertEqual(paljonko_saatiin, saldo_ennen)
        self.assertEqual(self.varasto.saldo, 0)

    def test__str__ilmoittaa_saldon_ja_tilavuuden(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
