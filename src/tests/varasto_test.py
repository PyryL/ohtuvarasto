import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_tilavuus_nollataan(self):
        # negatiivisella tilavuudella tilavuuden pitaisi asettua nollaan
        varasto2 = Varasto(-1)
        self.assertAlmostEqual(varasto2.tilavuus, 0)
    
    def test_alkusaldo_parametri_toimii(self):
        # jos varastolle annetaan alkusaldo, sen pitaisi tallentua saldoon
        varasto2 = Varasto(10, 3)
        self.assertAlmostEqual(varasto2.saldo, 3)
    
    def test_negatiivinen_alkusaldo_nollataan(self):
        # jos alkusaldo on negatiivinen, saldon pitaisi olla nolla
        varasto2 = Varasto(10, -3)
        self.assertAlmostEqual(varasto2.saldo, 0)
    
    def test_alkusaldo_korkeintaan_tilavuus(self):
        # jos alkusaldo on tilavuutta suurempi, saldon pitaisi olla tilavuus
        varasto2 = Varasto(10, 11)
        self.assertAlmostEqual(varasto2.saldo, 10)
    
    def test_negatiivinen_lisays_ei_vaikuta(self):
        # lisataan ensin jokin validi maara, ja sitten negatiivinen
        # jalkimmaisen operaation ei pitaisi vaikuttaa mihinkaan
        self.varasto.lisaa_varastoon(3)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 3)
    
    def test_ylisuuri_lisays_ei_ylita_tilavuutta(self):
        # saldon pitaisi kasvaa vain tilavuuden maksimimaaraan asti
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_negatiivinen_ottaminen_ottaa_nollan(self):
        # otettaessa negatiivinen maara varastosta, pitaisi funktion palauttaa nolla
        self.varasto.lisaa_varastoon(5)
        otettu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otettu_maara, 0)
    
    def test_negatiivinen_ottaminen_ei_vaikuta(self):
        # negatiivisen maaran ottamisen ei pitaisi muuttaa saldoa
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 5)
    
    def test_ottaminen_ei_anna_tilavuutta_enempaa(self):
        # kun varastosta otetaan enemman kuin siella on, saadaan vain siella olevat
        self.varasto.lisaa_varastoon(5)
        otettu_maara = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(otettu_maara, 5)
    
    def test_merkkijono_konstruktori_toimii(self):
        self.varasto.lisaa_varastoon(3)
        merkkijono = str(self.varasto)
        self.assertAlmostEqual(merkkijono, "saldo = 3, vielä tilaa 7")
