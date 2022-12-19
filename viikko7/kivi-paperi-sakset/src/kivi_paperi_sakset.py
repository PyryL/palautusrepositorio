from tuomari import Tuomari

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = self._luo_tekoaly()
        
        ekan_siirto, tokan_siirto = self._pelaa_kierros(tekoaly)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto, tokan_siirto = self._pelaa_kierros(tekoaly)
            if tekoaly is not None and callable(tekoaly.aseta_siirto):
                tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _pelaa_kierros(self, tekoaly):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        if tekoaly is None:
            tokan_siirto = input("Toisen pelaajan siirto: ")
        else:
            tokan_siirto = tekoaly.anna_siirto()
            print(f"Tietokone valitsi: {tokan_siirto}")
        return (ekan_siirto, tokan_siirto)

    def _luo_tekoaly(self):
        return None

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
