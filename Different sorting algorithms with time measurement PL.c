import time
import random


# generator list roznego typu
def losowa_lista_liczb(min_mozliwa_liczba, max_mozliwa_liczba, dlugosc_listy):
    lista = []
    for i in range(dlugosc_listy):
        lista.append(random.randint(min_mozliwa_liczba, max_mozliwa_liczba))
    return lista


def losowa_lista_liczb_rosnacych(min_mozliwa_liczba, max_mozliwa_liczba, dlugosc_listy):
    lista = []
    for i in range(dlugosc_listy):
        lista.append(random.randint(min_mozliwa_liczba, max_mozliwa_liczba))
    return sorted(lista)


def losowa_lista_liczb_malejacych(min_mozliwa_liczba, max_mozliwa_liczba, dlugosc_listy):
    lista = []
    for i in range(dlugosc_listy):
        lista.append(random.randint(min_mozliwa_liczba, max_mozliwa_liczba))
    lista = sorted(lista)
    lista.reverse()
    return lista


def losowa_lista_liczb_stalych(min_mozliwa_liczba, max_mozliwa_liczba, dlugosc_listy):
    lista = []
    liczba = random.randint(min_mozliwa_liczba, max_mozliwa_liczba)
    for i in range(dlugosc_listy):
        lista.append(liczba)
    return lista


def losowa_lista_a_ksztaltna(min_mozliwa_liczba, max_mozliwa_liczba, dlugosc_listy):
    lista1 = []
    for i in range(dlugosc_listy):
        lista1.append(random.randint(min_mozliwa_liczba, max_mozliwa_liczba))
    lista = []
    while lista1:
        lista.insert(0, max(lista1))
        lista1.remove(max(lista1))
        if lista1:
            lista.append(max(lista1))
            lista1.remove(max(lista1))
    return lista


# algorytmy sortowania
def insertion_sort(sequence):
    for i in range(len(sequence)):
        k = i
        for j in range(i - 1, -1, -1):
            if sequence[j] > sequence[k]:
                sequence[j], sequence[k] = sequence[k], sequence[j]
                k = j
    return sequence


def shellsort(sequence, sequence_length):
    gaps = [1]
    while 3 * gaps[-1] + 1 < sequence_length:
        gaps.append(3 * gaps[-1] + 1)
    gaps.reverse()
    for gap in gaps:
        for shift in range(0, gap):
            for i in range(shift, len(sequence), gap):
                k = i
                for j in range(i - gap, -1, -gap):
                    if sequence[j] > sequence[k]:
                        sequence[j], sequence[k] = sequence[k], sequence[j]
                        k = j
    return sequence


def selection_sort(sequence):
    for i in range(len(sequence)):
        min_index = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[min_index]:
                min_index = j
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
    return sequence


def heapify(lista, indeks_rodzica, dlugosc_do_sprawdzenia):
    indeks_najwiekszego_elementu = indeks_rodzica
    # czy lewy wiekszy
    if 2 * indeks_rodzica < dlugosc_do_sprawdzenia and lista[indeks_rodzica] < lista[2 * indeks_rodzica]:
        indeks_najwiekszego_elementu = 2 * indeks_rodzica
    # czy prawy wiekszy
    if 2 * indeks_rodzica + 1 < dlugosc_do_sprawdzenia and lista[indeks_najwiekszego_elementu] < lista[
2 * indeks_rodzica + 1]:
        indeks_najwiekszego_elementu = 2 * indeks_rodzica + 1
    # ewentualna zamiana
    if indeks_najwiekszego_elementu != indeks_rodzica:
        # zamiana
        lista[indeks_rodzica], lista[indeks_najwiekszego_elementu] = lista[indeks_najwiekszego_elementu], lista[
            indeks_rodzica]
        # sprawdzamy jedno wyzej
        heapify(lista, indeks_najwiekszego_elementu, dlugosc_do_sprawdzenia)


def heap_sort(lista):
    dlugosc_do_sprawdzenia = len(lista)
    # budowa kopca
    for element in range(dlugosc_do_sprawdzenia // 2, -1, -1):
        heapify(lista, element, dlugosc_do_sprawdzenia)
    # sortowanie
    for element in range(dlugosc_do_sprawdzenia - 1, 0, -1):
        lista[element], lista[0] = lista[0], lista[element]
        heapify(lista, 0, element)
    return lista


def quicksort_right(i, j, sequence):
    pivot = sequence[j]
    left = i
    right = j
    unsorted = True
    while unsorted:
        while sequence[i] < pivot:
            i += 1
        while sequence[j] > pivot:
            j -= 1
        if i < j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
        elif i > j:
            if left < j:
                quicksort_right(left, j, sequence)
            if i < right:
                quicksort_right(i, right, sequence)
            unsorted = False
        elif i == j:
            if left < i - 1:
                quicksort_right(left, i - 1, sequence)
            if i + 1 < right:
                quicksort_right(i + 1, right, sequence)
            unsorted = False
        i += 1
        j -= 1
    return sequence


def quicksort_random(i, j, sequence):
    pivot = sequence[random.randint(i, j)]
    left = i
    right = j
    keep_sorting = True
    while keep_sorting:
        while sequence[i] < pivot:
            i += 1
        while sequence[j] > pivot:
            j -= 1
        if i < j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
        elif i > j:
            if left < j:
                quicksort_random(left, j, sequence)
            if i < right:
                quicksort_random(i, right, sequence)
            keep_sorting = False
        elif i == j:
            if left < i - 1:
                quicksort_random(left, i - 1, sequence)
            if i + 1 < right:
                quicksort_random(i + 1, right, sequence)
            keep_sorting = False
        i += 1
        j -= 1
    return sequence


# menu programu
opcja = None
min_liczba = 1
max_liczba = 10000
dlugosc_listy = 1000
ciag = losowa_lista_liczb(min_liczba, max_liczba, dlugosc_listy)
typ_listy = '1'
rodzaje_ciagow = {
    '1': "losowy",
    '2': "rosnacy",
    '3': "malejacy",
    '4': "staly",
    '5': "A-ksztaltny"
}
while opcja != '0':
    print("--------------------------------------------------------------")
    print("Wybierz opcje:")
    print("1.Wybierz przedzial losowanych liczb(obecnie {}-{})".format(min_liczba, max_liczba))
    print("2.Wybierz dlugosc ciagu(obecnie {})".format(dlugosc_listy))
    print("3.Wybierz rodzaj ciagu(obecnie {})".format(rodzaje_ciagow[typ_listy]))
    print("4.Wybierz algorytm sortowania i sortuj")
    print("0.Wyjscie")
    print("Uwaga: Skorzystanie z opcji 1-3 generuje nowy ciag")
    print("--------------------------------------------------------------")
    opcja = input(">")
    if opcja == '1':
        print("Podaj przedzial wedlug wzoru: min-max (np. 1-1000): ")
        min_liczba, max_liczba = list(map(int, input(">").split('-')))
        print("Trwa generowanie ciagu...")
        if typ_listy == "1":
            ciag = losowa_lista_liczb(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "2":
            ciag = losowa_lista_liczb_rosnacych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "3":
            ciag = losowa_lista_liczb_malejacych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "4":
            ciag = losowa_lista_liczb_stalych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "5":
            ciag = losowa_lista_a_ksztaltna(min_liczba, max_liczba, dlugosc_listy)
        print("Ciag zostal wygenerowany")
    elif opcja == '2':
        dlugosc_listy = int(input("Podaj dlugosc listy (np.1000):\n>"))
        print("Trwa generowanie ciagu...")
        if typ_listy == "1":
            ciag = losowa_lista_liczb(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "2":
            ciag = losowa_lista_liczb_rosnacych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "3":
            ciag = losowa_lista_liczb_malejacych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "4":
            ciag = losowa_lista_liczb_stalych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "5":
            ciag = losowa_lista_a_ksztaltna(min_liczba, max_liczba, dlugosc_listy)
        print("Ciag zostal wygenerowany")
    elif opcja == '3':
        print("Wybierz rodzaj ciagu:")
        print("1.Losowy")
        print("2.Rosnacy")
        print("3.Malejacy")
        print("4.Staly")
        print("5.A-ksztaltny")
        typ_listy = input(">")
        print("Trwa generowanie ciagu...")
        if typ_listy == "1":
            ciag = losowa_lista_liczb(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "2":
            ciag = losowa_lista_liczb_rosnacych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "3":
            ciag = losowa_lista_liczb_malejacych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "4":
            ciag = losowa_lista_liczb_stalych(min_liczba, max_liczba, dlugosc_listy)
        elif typ_listy == "5":
            ciag = losowa_lista_a_ksztaltna(min_liczba, max_liczba, dlugosc_listy)
        print("Ciag zostal wygenerowany")
    elif opcja == '4':
        algorytm = None
        while algorytm != '0':
            print("--------------------------------------------------------------")
            print(
                "1.Generuj nowy ciag(domyslnie program nie generuje nowego ciagu przy starcie algorytmow co umozliwia ich testowanie dla identycznych danych wejciowych, ta opcja wygeneruje ciag o wlasciwosciach okreslonych w menu glownym)")
            print("2.Insertion sort")
            print("3.Shellsort")
            print("4.Selection sort")
            print("5.Heapsort")
            print("6.Quicksort(pivot skrajnie prawym elementem)")
            print("7.Quicksort(pivot losowym elementem)")
            print("0.Powrot do menu glownego")
            print("--------------------------------------------------------------")
            algorytm = input(">")
            if algorytm == '1':
                print("Trwa generowanie ciagu...")
                if typ_listy == "1":
                    ciag = losowa_lista_liczb(min_liczba, max_liczba, dlugosc_listy)
                elif typ_listy == "2":
                    ciag = losowa_lista_liczb_rosnacych(min_liczba, max_liczba, dlugosc_listy)
                elif typ_listy == "3":
                    ciag = losowa_lista_liczb_malejacych(min_liczba, max_liczba, dlugosc_listy)
                elif typ_listy == "4":
                    ciag = losowa_lista_liczb_stalych(min_liczba, max_liczba, dlugosc_listy)
                elif typ_listy == "5":
                    ciag = losowa_lista_a_ksztaltna(min_liczba, max_liczba, dlugosc_listy)
                print("Ciag zostal wygenerowany")
            if algorytm in ['2', '3', '4', '5', '6', '7']:
                print("Przed sortowaniem:")
                print(ciag)
                ciag_kopia = ciag[:]
                print("Trwa sortowanie...")
            if algorytm == '2':
                start = time.time()
                posortowana = insertion_sort(ciag_kopia)
                stop = time.time()
            elif algorytm == '3':
                start = time.time()
                posortowana = shellsort(ciag_kopia, dlugosc_listy)
                stop = time.time()
            elif algorytm == '4':
                start = time.time()
                posortowana = selection_sort(ciag_kopia)
                stop = time.time()
            elif algorytm == '5':
                start = time.time()
                posortowana = heap_sort(ciag_kopia)
                stop = time.time()
            elif algorytm == '6':
                start = time.time()
                posortowana = quicksort_right(0, len(ciag_kopia) - 1, ciag_kopia)
                stop = time.time()
            elif algorytm == '7':
                start = time.time()
                posortowana = quicksort_random(0, len(ciag_kopia) - 1, ciag_kopia)
                stop = time.time()
            if algorytm in ['2', '3', '4', '5', '6', '7']:
                print("Po sortowaniu:")
                print(posortowana)
                print("Czas sortowania: {}".format(round(stop - start, 4)))
                input("Wcisnij enter aby kontynuowac...")
