from peli import Peli

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
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        jatketaanko_pelia = Peli(vastaus).pelaa()

if __name__ == "__main__":
    main()
