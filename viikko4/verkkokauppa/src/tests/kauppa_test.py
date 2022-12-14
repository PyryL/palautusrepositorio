import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 45
        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()

    def varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        elif tuote_id == 2:
            return 8
        elif tuote_id == 3:
            return 0

    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        elif tuote_id == 2:
            return Tuote(2, "juusto", 7)
        elif tuote_id == 3:
            return Tuote(3, "kahvi", 3)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paaytyttya_pankin_metodilla_tilisiirto_oikeat_parametrit(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 45, "12345", "33333-44455", 5)

    def test_kahden_saman_ostoksen_paaytyttya_pankin_metodilla_tilisiirto_oikeat_parametrit(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 45, "12345", "33333-44455", 10)

    def test_kahden_eri_ostoksen_paaytyttya_pankin_metodilla_tilisiirto_oikeat_parametrit(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 45, "12345", "33333-44455", 12)

    def test_kahden_loppuvan_ostoksen_paaytyttya_pankin_metodilla_tilisiirto_oikeat_parametrit(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 45, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_edelliset_ostokset(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 7)

    def test_uusi_viitenumero_pyydetaan_jokaiselle_maksutapahtumalle(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("matti", "98765")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_korista_poisto_palauttaa_varastoon(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.varasto_mock.palauta_varastoon.assert_called_once()
