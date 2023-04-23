import collections
import copy
import random

import functions


def k_means(k, data):
    old_data = copy.deepcopy(data)
    for i in data:
        i.pop()
    centroids = random.sample(data, k)
    clusters = [[] for _ in range(k)]
    old_distances_sum = 0
    iteration = 0

    while True:
        distances_sum = 0

        # Przypisujemy każdy punkt do najbliższego centroidu
        for point in data:
            # Obliczanie dystansów między punktami a centroidami
            distances = [functions.euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid_index = distances.index(min(distances))
            clusters[closest_centroid_index].append(point)
            # Suma odległości
            distances_sum += min(distances)

        # Obliczamy nowe pozycje centroidów
        for i in range(k):
            if clusters[i]:
                centroids[i] = [sum(coords) / len(clusters[i]) for coords in zip(*clusters[i])]

        # Sprawdzamy, czy pozycje centroidów się zmieniły
        if distances_sum == old_distances_sum:
            break
        old_distances_sum = distances_sum

        # Czyścimy grupy
        clusters = [[] for _ in range(k)]

        # Informacje
        iteration = iteration + 1
        print(f'Suma odleglości w iteracji {iteration}: {distances_sum}')

    # Wyswietalnie skladow grup
    itr = 0
    final_clusters = []
    for _ in range(k):
        final_clusters.append([])

    for i in clusters:
        for j in i:
            for m in old_data:
                if j == m[:-1]:
                    final_clusters[itr].append(m[-1])
        itr = itr + 1

    itr = 1
    for i in final_clusters:
        print(f"Grupa {itr}: {i}")
        itr = itr + 1

    # Procentowe zawartości
    print("\n")
    for i in final_clusters:
        for j in range(k):
            clarity = 100 * i.count(j) / len(i)
            print(f"Procent zawartości {j} w grupie: {clarity}")
        print("\n")

    return clusters, centroids


if __name__ == '__main__':
    # Zmienne
    k = 3
    data = functions.load_data("data/iris.data")

    # Odpalanie algorytmu
    k_means(k, data)

    #Oznaczenia
    print("0 - Iris setosa")
    print("1 - Iris versicolor")
    print("2 - Iris virginica")