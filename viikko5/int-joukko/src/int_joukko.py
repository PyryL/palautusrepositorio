KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._tarkista_muoto(kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = self._tarkista_muoto(kasvatuskoko, OLETUSKASVATUS)
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _tarkista_muoto(self, luku, oletus):
        if luku is None:
            return oletus
        elif not isinstance(luku, int) or luku < 0:
            raise Exception("")
        return luku

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        self.ljono += [0] * self.kasvatuskoko

    def poista(self, n):
        try:
            kohta = self.ljono.index(n)
        except ValueError:
            return False

        self.ljono.pop(kohta)
        self.ljono.append(0)
        self.alkioiden_lkm -= 1

    def kopioi_taulukko(self, a, b):
        b[:len(a)] = a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for item in a_taulu + b_taulu:
            yhdiste.lisaa(item)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_item in a_taulu:
            for b_item in b_taulu:
                if a_item == b_item:
                    leikkaus.lisaa(a_item)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for item in a_taulu:
            erotus.lisaa(item)

        for item in b_taulu:
            erotus.poista(item)

        return erotus

    def __str__(self):
        return "{" + ', '.join([str(n) for n in self.to_int_list()]) + "}"
