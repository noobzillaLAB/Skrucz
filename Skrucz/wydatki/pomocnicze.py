def czy_prawidłowa_kwota(kwota):
    """Sprawdza, czy kwota jest liczbą i większa od zera."""
    try:
        kwota = float(kwota)
        return kwota > 0
    except ValueError:
        return False

