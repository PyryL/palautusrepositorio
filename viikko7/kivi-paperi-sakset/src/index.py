from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def pelaa_peli(syote):
    print(
        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
    )
    pelit = {
        "a": KPSPelaajaVsPelaaja,
        "b": KPSTekoaly,
        "c": KPSParempiTekoaly
    }
    if syote[-1] in pelit:
        peli = pelit[syote[-1]]()
        peli.pelaa()
        return True
    return False

def main():
    jatketaanko_pelia = True
    while jatketaanko_pelia:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        jatketaanko_pelia = pelaa_peli(vastaus)

if __name__ == "__main__":
    main()
