from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def _luo_tekoaly(self):
        return Tekoaly()
