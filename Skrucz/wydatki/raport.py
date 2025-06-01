import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

class MenedżerRaportów:
    def __init__(self, menedżer_wydatków):
        self.menedżer_wydatków = menedżer_wydatków

    def generuj_raport(self):
        """Generuje raport wydatków za dany miesiąc."""
        df = self.menedżer_wydatków.pobierz_wydatki()

        if df.empty:
            print("Brak danych do wyświetlenia.")
            return

        # Podsumowanie wydatków według kategorii
        podsumowanie_kategorii = df.groupby("Kategoria")["Kwota"].sum().reset_index()
        
        # Wyświetlanie tabeli
        print("\nRaport wydatków:\n")
        print(tabulate(podsumowanie_kategorii, headers="keys", tablefmt="fancy_grid", showindex=False))
        
        # Suma wszystkich wydatków
        suma = podsumowanie_kategorii["Kwota"].sum()
        print(f"\nSuma wszystkich wydatków: {suma:.2f} zł\n")
