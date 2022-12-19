from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Peli:
    def __init__(self, syote):
        pelit = {
            "a": KPSPelaajaVsPelaaja,
            "b": KPSTekoaly,
            "c": KPSParempiTekoaly
        }
        if syote[-1] in pelit:
            self._peli = pelit[syote[-1]]()
        else:
            self._peli = None

    def pelaa(self):
        if self._peli is not None:
            self._peli.pelaa()
            return True
        return False
