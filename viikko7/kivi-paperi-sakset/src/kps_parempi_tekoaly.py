from tekoaly_parannettu import TekoalyParannettu
from peli import Peli

class KPSParempiTekoaly(Peli):
    def _luo_tekoaly(self):
        return TekoalyParannettu(10)
