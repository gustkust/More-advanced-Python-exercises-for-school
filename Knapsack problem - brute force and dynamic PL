import random


# funkcja generujaca plik, zrobilem tak zeby wygodnie mozna bylo podawac n i c jako argument
# jako 3 argument mozna podac tez nazwe pliku, ale nie trzeba, domyslnie jest "dane.txt"
# procz tego mozna podac tez minimalne i maksymalne wartosci cen i wag, ale nie trzeba
# domyslnie dla obu jest przedzial <1,10>, wiec ogolnie do wywolania funkcji wystarczaja 2 argumenty(n i c)
def generate(n, capacity, filename="dane.txt", min_value=1, max_value=10, min_weight=1, max_weight=10):
    with open(filename, "w") as file:
        file.write("{}\n{}\n".format(capacity, n))
        for line in range(n):
            file.write("{} {}\n".format(random.randint(min_value, max_value), random.randint(min_weight, max_weight)))


def read_file(filename):
    with open(filename, "r") as file:  # otwieramy plik, nie trzeba zamykac bo z tym with po tym wcieciu sie sam zamknie
        capacity = int(file.readline())  # odczytujemy c
        n = int(file.readline())  # oraz n
        items = []
        for line in range(n):  # czytamy kolejne wiersze
            items.append([int(x) for x in file.readline().split()])  # dodajemy do tablicy, split usuwa spacje i znak nowej linii, i liczby konwertujemy na int
            # uwaga: indeks 0 ma wartosc a 1 waga tak jak w poleceniu, ale w prezentacji jest odwrotnie zapisywane
    return capacity, n, items  # zwracamy c, n i wiersze z wartosciami i wagami


def knapsack_brute_force(filename="dane.txt"):
    capacity, n, items = read_file(filename)  # funkcja czyta plik i zwraca c, n i wiersze
    max_value = 0  # fmax = 0
    for x in range(1, 2**n):  # dla każdej liczby X od 1 do 2 n -1
        bin_reversed = list(reversed(bin(x)[2:])) # zakoduj X w systemie binarnym, kazda liczba reprezentuje inna sytuacje, bin zwraca stringa
        #  [2:] bo bin dodaje '0b' na poczatku
        #  odwrocone bo tak wygodniej, znak o indeksie 0 odnosi sie do przedmiotu o indeksie 0, itd.
        weight_sum = 0
        for i, digit in enumerate(bin_reversed):
            if digit == '1':  # 1 odnosi sie do sytuacji, gdy przedmiot i-ty dodamy do plecaka (a zero gdy nie dodamy ofc)
                weight_sum += items[i][1]  # sumujemy wagi przedmiotow w plecaku
        if weight_sum <= capacity:  # sprawdzamy czy dla takiej sytuacji mozna zmiescic przedmioty do plecaka
            value_sum = 0
            for i, digit in enumerate(bin_reversed):
                if digit == '1':
                    value_sum += items[i][0]  # sumumemy wartosci przedmiotow w plecaku
            if value_sum > max_value:  # if f(x) > fmax
                max_value = value_sum  # fmax = f(x)
                solution = []  # dana sytuacja jest do tej pory najlepsza
                for i, digit in enumerate(bin_reversed):
                    if digit == '1':
                        solution.append(i)  # wiec dodajemy rozwiazanie, jak znajdzie pozniej lepsze to jest zamieniane ofc
    return solution  # zwracamy rozwiazanie


def knapsack_dynamic_programming(filename="dane.txt"):
    capacity, n, items = read_file(filename)  # funkcja czyta plik i zwraca c, n i wiersze
    # budowa tablicy
    matrix = [[0] * (capacity+1)]  # wypelnienie pierwszego rzedu zerami
    for row in range(n):  # wypelniamy pozostale rzedy
        wi = items[row][1]  # wyznaczamy wi
        pi = items[row][0]  # i pi
        matrix.append([0])  # pierwsze w rzedzie zawsze jest zero
        j = 1
        while wi > j:  # pierwsza opcja z tej funkcji w klamrze
            matrix[row + 1].append(matrix[row][j])  # przepisujemy wiersz z góry dopoki warunek spelniony
            j += 1
        while j <= capacity:  # druga opcja
            greater = max(matrix[row][j], matrix[row][j - wi] + pi)  # dodajemy max z tych dwoch wartosci z prezentacji
            matrix[row + 1].append(greater)
            j += 1
    # wyznaczanie rozwiązania
    j -= 1
    i = n
    solution = []
    while i != 0:  # idziemy od ostatniego rzedu do pierwszego
        if matrix[i][j] > matrix[i - 1][j]:  # warunek z prezentacji
            solution.append(i-1)  # dodajemy do rozwiazania
            j -= items[i-1][1]  # przesuwamy sie w lewo tak jak na prezentacji
        i -= 1  # czy sa rowne nie trzeba sprawdzac, po prostu pomijamy, tak czy siak zmniejszamy i
    return list(reversed(solution))  # zwracamy odwrocone zeby bylo ladniej


# generate(20, 20)
print(knapsack_brute_force(), "brute force")
print(knapsack_dynamic_programming(), "dynamic programming")
