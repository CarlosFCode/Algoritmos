def quicksort(lista):
    if len(lista) <= 1:
        return lista

    list_metade = len(lista) // 2
    pivô = lista[list_metade]

    menores = [x for x in lista if x < pivô]
    maiores = [x for x in lista if x > pivô]
    ig_piv = [x for x in lista if x == pivô]

    return quicksort(menores) + ig_piv + quicksort(maiores)

lista = [9, 4, 5, 8, 2, 1, 0, 3]
list_metade = int(len(lista) / 2 - 1)
print(quicksort(lista))