# Algorytm k-means

Implementuj algorytm k-means. Grupuj dane z pliku iris.data (podczas grupowania
ignorujemy atrybut decyzyjny).
Program powinien:
- Umożliwiać wybór k.
- Po każdej iteracji: wypisywać sumę odległości przykładów od ich centroidów. Ta
wartość powinna zmniejszać się z każdą iteracją. Uwaga: należy wipisywać sumę dla
wszystkich przykładów, a nie każdej grupy osobno. Przykład:<p>
Iteracja 1: 126.38<p>
Iteracja 2: 86.34<p>
Iteracja 3: 49.91<p>
...
- Na końcu: wyświetlać składy grup.
- Dodatkowo (opcjonalnie): wyświetlać miary czystości grup, np. procentowe zawartości
każdej z klas Iris, lub entropię.