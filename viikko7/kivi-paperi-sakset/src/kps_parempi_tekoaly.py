from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def _luo_tekoaly(self):
        return TekoalyParannettu(10)
