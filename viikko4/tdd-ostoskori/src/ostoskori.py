from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._ostokset])

    def hinta(self):
        return sum([ostos.hinta() for ostos in self._ostokset])

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        ostos = Ostos(lisattava)
        self._ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for i, ostos in enumerate(self._ostokset):
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self._ostokset.pop(i)
                return

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
