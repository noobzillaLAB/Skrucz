import pandas as pd
from datetime import datetime

class MenedżerWydatków:
    def __init__(self, nazwa_pliku="dane/wydatki.csv"):
        self.nazwa_pliku = nazwa_pliku
        self.kolumny = ["Data", "Kategoria", "Kwota"]
        self.wczytaj_dane()

    def wczytaj_dane(self):
        """Ładuje dane z pliku CSV, jeśli plik istnieje, w przeciwnym razie tworzy pusty DataFrame."""
        try:
            self.df = pd.read_csv(self.nazwa_pliku)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=self.kolumny)

    def dodaj_wydatek(self, kategoria, kwota):
        """Dodaje nowy wydatek do bazy."""
        dzisiaj = datetime.now().strftime("%Y-%m-%d")
        nowy_wydatek = pd.DataFrame([[dzisiaj, kategoria, kwota]], columns=self.kolumny)
        self.df = pd.concat([self.df, nowy_wydatek], ignore_index=True)
        self.zapisz_dane()

    def zapisz_dane(self):
        """Zapisuje dane z powrotem do pliku CSV."""
        self.df.to_csv(self.nazwa_pliku, index=False)

    def pobierz_wydatki(self):
        """Zwraca wszystkie wydatki."""
        return self.df
    
    def wyczyść_wydatki(self):
        """Usuwa wszystkie wydatki."""
        self.df = pd.DataFrame(columns=self.kolumny)
        self.zapisz_dane()

    def cofnij_ostatni_wydatek(self):
        """Usuwa ostatni dodany wydatek."""
        if not self.df.empty:
            self.df = self.df[:-1]
            self.zapisz_dane()
        else:
            print("Brak danych do usunięcia.")

