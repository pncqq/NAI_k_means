# 🔍 NAI_k_means

Implementacja klasycznego algorytmu **k-means** do grupowania danych z pliku `iris.data`. Projekt realizowany w ramach kursu NAI (Narzędzia AI).

Celem jest przeprowadzenie klasteryzacji danych bez wykorzystania etykiet (nadzoru), a następnie obserwacja zbieżności centroidów oraz jakości grup.

## 📂 Zawartość repozytorium

- `main.py` – główny plik uruchamiający program
- `functions.py` – pomocnicze funkcje do obsługi algorytmu k-means
- `data/iris.data` – zbior danych (zignorowany atrybut decyzyjny)
- `.idea/` – pliki konfiguracyjne IDE (PyCharm)

## ⚙️ Technologie

- Python 3.x
- NumPy
- Pandas (opcjonalnie)

## 🚀 Funkcjonalności

- Wczytanie danych z pliku `iris.data`
- Możliwość wyboru liczby klastrów `k`
- Iteracyjne aktualizowanie centroidów i przypisanie punktów do grup
- Po każdej iteracji:
  - wypisywana jest suma odległości wszystkich przykładów od ich centroidów
- Na końcu:
  - wyświetlane są składy końcowe grup
  - (opcjonalnie) obliczane są miary czystości (np. procent klas w klastrach)

### ✨ Przykładowy output:
```
Iteracja 1: 126.38
Iteracja 2: 86.34
Iteracja 3: 49.91
...
```

## ▶️ Jak uruchomić

1. Sklonuj repozytorium:
```bash
git clone https://github.com/pncqq/NAI_k_means.git
cd NAI_k_means
```

2. Uruchom program:
```bash
python main.py
```

> 🔎 Program zapyta o liczbę klastrów `k` oraz automatycznie przeanalizuje dane.

## 👨‍💻 Autor
**Filip Michalski**  
Projekt wykonany w ramach kursu NAI (Narzędzia AI) jako implementacja uczenia nienadzorowanego z wykorzystaniem metody k-średnich.
