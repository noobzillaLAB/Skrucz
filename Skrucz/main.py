from wydatki.wydatek import MenedżerWydatków
from wydatki.raport import MenedżerRaportów
from wydatki.pomocnicze import czy_prawidłowa_kwota

def main():
    menedżer_wydatków = MenedżerWydatków()
    menedżer_raportów = MenedżerRaportów(menedżer_wydatków)

    while True:
        print("\n::: SKRUCZ MENU ::: ")
        print("")
        print("1. Dodaj wydatek")
        print("2. Zobacz raport wydatków")
        print("3. Wyczyść wszystkie wydatki")
        print("4. Cofnij ostatni wydatek")
        print("5. Zakończ")
        print("")
        print("\nWykonano przez Pawel Kolodziejczyk - WI - 26421 ")
        print("")
        
        wybór = input("Wybierz opcję (1/2/3/4/5): ")

        if wybór == "1":
            kategoria = input("Podaj kategorię wydatku (np. jedzenie, paliwo, rachunki, edukacja): ").strip()
            kwota = input("Podaj kwotę wydatku: ").strip()

            if czy_prawidłowa_kwota(kwota):
                menedżer_wydatków.dodaj_wydatek(kategoria, float(kwota))
                print(f"Dodano wydatek: {kategoria} - {kwota} zł")
            else:
                print("Niepoprawna kwota! Spróbuj ponownie.")
        
        elif wybór == "2":
            menedżer_raportów.generuj_raport()
        
        elif wybór == "3":
            potwierdź = input("Czy na pewno chcesz usunąć wszystkie wydatki? (t/n): ")
            if potwierdź.lower() == "t":
                menedżer_wydatków.wyczyść_wydatki()
                print("Wszystkie dane zostały usunięte.")
                
        elif wybór == "4":
            menedżer_wydatków.cofnij_ostatni_wydatek()
            print("Ostatni wydatek został usunięty.")


        elif wybór == "5":
            print("Do widzenia!")
            break
        
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            


if __name__ == "__main__":
    main()

