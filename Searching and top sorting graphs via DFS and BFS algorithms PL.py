import random


# procedury tworzenia macierzy
def create_own_matrix():
    matrix = []
    first_row = [int(x) for x in input(">").split()]
    matrix.append(first_row)
    for i in range(len(first_row) - 1):
        matrix.append([int(x) for x in input(">").split()])
    return matrix, len(first_row)


def generate_matrix(n):
    ones = (n * (n - 1)) // 4  # liczba jedynek w gornym trojkacie
    zeroes = sum([i for i in range(1, n)]) - ones  # liczba zer w gornym trojkacie
    # lista z liczbami do wypelnienia gornego trojkata,
    # jedynek jest n-1 mniej niz byc powinna aby potem recznie dodac 1 do kazdego wiersza gwarantujac spojnosc grafu
    upper_triangle = [1] * (ones - (n - 1)) + [0] * zeroes
    random.shuffle(upper_triangle)  # mieszamy liste
    matrix = []
    triangle_bound = 1  # licznik wskazujacy ile miejsc danego wiersza przypada na gorny i dolny trojkat
    for row in range(n):  # dodajemy wiersze
        # wypelniamy zerami czesc dolnotrojkatna
        lower_triangle_part = []
        for zero in range(triangle_bound):
            lower_triangle_part.append(0)
        # wypelniamy czesc gornotrojkatna
        upper_triangle_part = []
        for element in range(n - triangle_bound - 1):
            upper_triangle_part.append(upper_triangle.pop())  # usuwamy 0 lub 1 z listy i dodajemy do wiersza
        if row != n - 1:  # w ostatnim wierszu sa same zera
            upper_triangle_part.append(1)  # dodajemy 1 do wiersza by zagwarantowac spojnosc grafu
        random.shuffle(upper_triangle_part)  # mieszamy jeszcze raz zeby 1 nie zawsze bylo na koncu
        matrix.append(lower_triangle_part + upper_triangle_part)  # dodajemy wiersz
        triangle_bound += 1
    return matrix


def to_adjacency_list(matrix):
    adj_list = []
    for i in range(len(matrix)):
        adj_list.append([])
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list


def to_edge_table(matrix):
    table = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                table.append([i, j])
    return table


# procedury wyswietlania(DFS)
# macierz sasiedztwa(DFS, wyswietlanie)
def dfs_adjacency_matrix(matrix, visited, row):
    print(row)
    visited[row] = 1
    for tail in range(len(matrix)):
        if matrix[row][tail] == 1:
            if visited[tail] == 0:
                dfs_adjacency_matrix(matrix, visited, tail)


def print_dfs_adjacency_matrix(matrix):
    visited = [0] * len(matrix)
    for row in range(len(matrix)):
        if visited[row] == 0:
            dfs_adjacency_matrix(matrix, visited, row)


# lista nastepnikow(DFS, wyswietlanie)
def dfs_adjacency_list(adj_list, visited, sublist):
    visited[sublist] = 1
    print(sublist)
    for tail in adj_list[sublist]:
        if visited[tail] == 0:
            dfs_adjacency_list(adj_list, visited, tail)


def print_dfs_adjacency_list(adj_list):
    visited = [0] * len(adj_list)
    for sublist in range(len(adj_list)):
        if visited[sublist] == 0:
            dfs_adjacency_list(adj_list, visited, sublist)


# tabela krawedzi(DFS, wyswietlanie)
def dfs_edge_table(table, visited, current_edge):
    # wyswietlamy wierzcholek wyjsciowy i oznaczamy go jako odwiedzony
    if visited[current_edge[0]] == 0:
        visited[current_edge[0]] = 1
        print(current_edge[0])
    # szukamy krawedzi gdzie obecny wierzcholek wejsciowy jest wyjsiowym dla innej krawedzi
    found = False
    for edge in table:
        if current_edge[1] == edge[0]:  # jesli taki znajdziemy to
            found = True
            dfs_edge_table(table, visited, edge)  # wywolujemy ta funkcje rekurencyjnie dla znalezionej krawedzi
    # jak nie znajdziemy takiej krawedzi to oznacza to, ze obecny wierzcholek wejsciowy nie ma zadnych nastepnikow
    if not found and visited[current_edge[1]] == 0:
        visited[current_edge[1]] = 1  # oznaczamy go jako odwiedzony
        print(current_edge[1])  # i wyswietlamy


def print_dfs_edge_table(table, node_number):
    visited = [0] * node_number
    for edge_index in range(len(table)):
        dfs_edge_table(table, visited, table[edge_index])


# procedury wyswietlania(BFS)
# macierz sasiedztwa(BFS, wyswietlanie)
def bfs_adjacency_matrix(matrix, visited, row, queue):
    visited[row] = 1
    print(row)
    queue.append(row)
    while queue:
        v = queue.pop()
        for u in range(len(matrix[v])):
            if matrix[v][u] == 1:
                if visited[u] == 0:
                    visited[u] = 1
                    print(u)
                    queue.append(u)


def print_bfs_adjacency_matrix(matrix):
    visited = [0] * len(matrix)
    queue = []
    for row in range(len(matrix)):
        if visited[row] == 0:
            bfs_adjacency_matrix(matrix, visited, row, queue)


# lista nastepnikow(BFS, wyswietlanie)
def bfs_adjacency_list(adj_list, visited, sublist_index, queue):
    visited[sublist_index] = 1
    print(sublist_index)
    queue.append(sublist_index)
    while queue:
        v = queue.pop()
        for u in adj_list[v]:
            if visited[u] == 0:
                visited[u] = 1
                print(u)
                queue.append(u)


def print_bfs_adjacency_list(adj_list):
    visited = [0] * len(adj_list)
    queue = []
    for sublist_index in range(len(adj_list)):
        if visited[sublist_index] == 0:
            bfs_adjacency_list(adj_list, visited, sublist_index, queue)


# tabela krawedzi(BFS, wyswietlanie)
def bfs_edge_table(table, visited, current_edge, queue):
    visited[current_edge[0]] = 1
    print(current_edge[0])
    queue.append(current_edge[0])
    while queue:
        v = queue.pop()
        for edge in table:
            if edge[0] == v:
                if visited[edge[1]] == 0:
                    visited[edge[1]] = 1
                    print(edge[1])
                    queue.append(edge[1])


def print_bfs_edge_table(table, number_of_nodes):
    visited = [0] * number_of_nodes
    queue = []
    for edge_index in range(len(table)):
        if visited[table[edge_index][0]] == 0:
            bfs_edge_table(table, visited, table[edge_index], queue)


# sortowanie topologiczne(DFS)
# macierz sasiedztwa(DFS, sortowanie)
def top_dfs_adjacency_matrix(matrix, visited, v, solution):
    visited[v] = 1  # v oznaczamy na szaro
    cycle = False
    for u in range(len(matrix[v])):  # dla kazdego nastepnika u wierzcholka v
        if matrix[v][u] == 1:
            if visited[u] == 1 and u not in solution:  # jesli u jest odwiedzony a nie w rozwiazaniu
                cycle = True  # to istnieje cykl
                break
            if visited[u] == 0:  # jesli u jest nieodwiedzony
                cycle = top_dfs_adjacency_matrix(matrix, visited, u, solution)  # sort_top(u)
                # jesli wystapil cykl to zwraca True
    if not cycle:
        solution.append(v)  # dodajemy v do rozwiazania
        visited[v] = 2  # oznaczamy na czarno
    return cycle


def print_top_dfs_adjacency_matrix(matrix):
    visited = [0] * len(matrix)
    solution = []
    for row in range(len(matrix)):  # dla kazdego nieodwiedzonego wierzcholka
        if visited[row] != 2:
            cycle = top_dfs_adjacency_matrix(matrix, visited, row, solution)  # sort_top(u)
            # jesli wystapil cykl to zwraca True
            if cycle:
                break
    if cycle:
        print("W grafie wystapil cykl!")
    else:
        for node in range(len(solution) - 1, -1, -1):  # wyswietlamy rozwiazanie od tylu
            print(solution[node])


# lista nastepnikow(DFS, sortowanie)
def top_dfs_adjacency_list(adj_list, visited, v, solution):
    visited[v] = 1  # v oznaczamy na szaro
    cycle = False
    for u in adj_list[v]:  # dla kazdego nastepnika u wierzcholka v
        if visited[u] == 1 and u not in solution:  # jesli u jest odwiedzony a nie w rozwiazaniu
            cycle = True  # to istnieje cykl
            break
        if visited[u] == 0:  # jesli u jest nieodwiedzony
            cycle = top_dfs_adjacency_list(adj_list, visited, u, solution)  # sort_top(u)
            # jesli wystapil cykl to zwraca True
    if not cycle:
        solution.append(v)  # dodajemy v do rozwiazania
        visited[v] = 2  # oznaczamy na czarno
    return cycle


def print_top_dfs_adjacency_list(adj_list):
    visited = [0] * len(adj_list)
    solution = []
    for sublist_index in range(len(adj_list)):  # dla kazdego nieodwiedzonego wierzcholka
        if visited[sublist_index] != 2:
            cycle = top_dfs_adjacency_list(adj_list, visited, sublist_index, solution)  # sort_top(u)
        # jesli wystapil cykl to zwraca True
        if cycle:
            break
    if cycle:
        print("W grafie wystapil cykl!")
    else:
        for node in range(len(solution) - 1, -1, -1):  # wyswietlamy rozwiazanie od tylu
            print(solution[node])


# tabela krawedzi(DFS, sortowanie)
def top_dfs_edge_table(table, visited, solution, v):
    visited[v] = 1  # oznaczamy na szaro
    cycle = False
    for edge in table:
        if edge[0] == v:  # dla kazdego nastepnika u wierzcholka v
            if visited[edge[1]] == 1 and edge[1] not in solution:  # jesli u jest odwiedzony a nie w rozwiazaniu
                cycle = True  # to istnieje cykl
                break
            if visited[edge[1]] == 0:  # jesli u jest nieodwiedzony
                cycle = top_dfs_edge_table(table, visited, solution, edge[1])  # sort_top(u)
                # jesli wystapil cykl to zwraca True
    if not cycle:
        solution.append(v)  # dodajemy v do rozwiazania
        visited[v] = 2  # oznaczamy na czarno
    return cycle


def print_top_dfs_edge_table(table, node_number):
    visited = [0] * node_number
    solution = []
    for edge_index in range(len(table)):  # dla kazdego nieodwiedzonego wierzcholka
        if visited[table[edge_index][0]] != 2:
            cycle = top_dfs_edge_table(table, visited, solution, table[edge_index][0])  # sort_top(u)
            # jesli wystapil cykl to zwraca True
            if cycle:
                break
    if cycle:
        print("W grafie wystapil cykl!")
    else:
        for node in range(len(solution) - 1, -1, -1):  # wyswietlamy rozwiazanie od tylu
            print(solution[node])


# sortowanie topologiczne(BFS)
# macierz sasiedztwa(BFS, sortowanie)
def print_top_bfs_adjacency_matrix(matrix):
    in_degrees = [0] * len(matrix)  # tworzymy tabele ze stopniami wejsciowymi wierzcholkow
    for row in matrix:
        for in_index in range(len(row)):  # jak spotkamy nastepnika
            if row[in_index] == 1:
                in_degrees[in_index] += 1  # to zwiekszamy jego stopien wejsiowy
    solution = []
    cycle = False
    # szukamy wierzcholka z zerowym stopniem wejsiowym
    while len(solution) != len(matrix):  # dopoki nie ma w rozwiazaniu wszystkich wierzcholkow
        degree_index = 0
        while in_degrees[degree_index] != 0:  # szukamy indeks wierzcholka z zerowym stopniem wejsiowym
            degree_index += 1
            if degree_index > len(matrix) - 1:  # indeks wyszedl poza rozmiar listy, nie ma zer
                # czyli nie ma wierzcholka bez poprzednikow
                cycle = True  # mamy cykl
                break
        if not cycle:
            solution.append(degree_index)  # zapisujemy wierzcholek do rozwiazania
            for tail_index in range(len(matrix[degree_index])):  # nastepnikom tego wierzcholka zmniejszany
                if matrix[degree_index][tail_index] == 1:  # jest stopien wejsiowy
                    in_degrees[tail_index] -= 1
            in_degrees[degree_index] = -1  # -1 oznacza wierzcholek zapisany do rozwiazania
        if cycle:
            break
    if cycle:
        print("W grafie wystapil cykl!")
    else:
        for node in solution:
            print(node)


# lista nastepnikow(BFS, sortowanie)
def print_top_bfs_adjacency_list(adj_list):
    in_degrees = [0] * len(adj_list)  # tworzymy tabele ze stopniami wejsciowymi wierzcholkow
    for sublist in adj_list:  # dla kazdej listy nastepnikow
        for tail in sublist:
            in_degrees[tail] += 1  # kazdemu nastepnikowi zwiekszamy jego stopien wejsiowy
    solution = []
    cycle = False
    while len(solution) != len(adj_list):  # dopoki nie ma w rozwiazaniu wszystkich wierzcholkow
        degree_index = 0
        while in_degrees[degree_index] != 0:  # szukamy indeks wierzcholka z zerowym stopniem wejsiowym
            degree_index += 1
            if degree_index > len(adj_list) - 1:  # indeks wyszedl poza rozmiar listy, nie ma zer
                # czyli nie ma wierzcholka bez poprzednikow
                cycle = True  # mamy cykl
                break
        if not cycle:
            solution.append(degree_index)  # zapisujemy wierzcholek do rozwiazania
            for tail in adj_list[degree_index]:  # nastepnikom tego wierzcholka
                in_degrees[tail] -= 1  # zmniejszany jest stopien wejsiowy
            in_degrees[degree_index] = -1  # -1 oznacza wierzcholek zapisany do rozwiazania
        if cycle:
            break
    if cycle:
        print("W grafie wystapil cykl!")
    else:
        for node in solution:
            print(node)


# tabela krawedzi(BFS, sortowanie)
def print_top_bfs_edge_table(table, number_of_nodes):
    in_degrees = [0] * number_of_nodes  # tworzymy tabele ze stopniami wejsciowymi wierzcholkow
    for edge in table:  # dla kazdej krawedzi
        in_degrees[edge[1]] += 1  # nastepnikowi zwiekszamy stopien wejsiowy
    solution = []
    cycle = False
    while len(solution) != number_of_nodes:  # dopoki nie ma w rozwiazaniu wszystkich wierzcholkow
        degree_index = 0
        while in_degrees[degree_index] != 0:  # szukamy indeks wierzcholka z zerowym stopniem wejsiowym
            degree_index += 1
            if degree_index > number_of_nodes - 1:  # indeks wyszedl poza rozmiar listy, nie ma zer
                # czyli nie ma wierzcholka bez poprzednikow
                cycle = True  # mamy cykl
                break
        if not cycle:
            solution.append(degree_index)  # zapisujemy wierzcholek do rozwiazania
            for edge in table:
                if edge[0] == degree_index:
                    in_degrees[edge[1]] -= 1  # nastepnikom tego wierzcholka zmniejszany jest stopien wejsiowy
            in_degrees[degree_index] = -1  # -1 oznacza wierzcholek zapisany do rozwiazania
        if cycle:
            break
    if cycle:
        print("W grafie wystapil cykl!")
    else:
        for node in solution:
            print(node)


option = None
created = False
while option != '0':
    print("-----------------------")
    print("1.Podaj wlasna macierz sasiedztwa")
    print("2.Wygeneruj macierz sasiedztwa")
    print("3.Wyswietl wszystkie reprezenacje")
    print("4.Wyswietlanie wierzcholkow grafu dla wszystkich reprezentacji(DFS)")
    print("5.Wyswietlanie wierzcholkow grafu dla wszystkich reprezentacji(BFS)")
    print("6.Sortowanie topologiczne dla wszystkich reprezentacji(DFS)")
    print("7.Sortowanie topologiczne dla wszystkich reprezentacji(BFS)")
    print("0.Wyjscie")
    print("-----------------------")
    option = input(">")
    if option == '1':
        print(
            "Wypelnij macierz zerami i jedynkami. Liczba wierszy do wpisania zależy od dlugosci wiersza. Przykład wiersza macierzy: \"0 1 0\".")
        adj_matrix, n = create_own_matrix()
        adjacency_list = to_adjacency_list(adj_matrix)
        edge_table = to_edge_table(adj_matrix)
        created = True
    elif option == '2':
        print("Podaj liczbe wierzcholkow grafu:")
        n = int(input(">"))
        adj_matrix = generate_matrix(n)
        adjacency_list = to_adjacency_list(adj_matrix)
        edge_table = to_edge_table(adj_matrix)
        created = True
    if created:
        if option == '3':
            print("Macierz sasiedztwa:")
            for adj_row in adj_matrix:
                print(adj_row)
            input("Wcisnij enter aby kontynuowac...")
            print("Lista nastepnikow:")
            for out, sub_list in enumerate(adjacency_list):
                print(str(out) + ":", sub_list)
            input("Wcisnij enter aby kontynuowac...")
            print("Tabela krawedzi:")
            for edge_ in edge_table:
                print(edge_[0], "→", edge_[1])
            input("Wcisnij enter aby kontynuowac...")
        elif option == '4':
            print("Macierz sasiedztwa(wyswietlanie, DFS)")
            print_dfs_adjacency_matrix(adj_matrix)
            input("Wcisnij enter aby kontynuowac...")
            print("Lista nastepnikow(wyswietlanie, DFS)")
            print_dfs_adjacency_list(adjacency_list)
            input("Wcisnij enter aby kontynuowac...")
            print("Tabela krawedzi(wyswietlanie, DFS)")
            print_dfs_edge_table(edge_table, n)
            input("Wcisnij enter aby kontynuowac...")
        elif option == '5':
            print("Macierz sasiedztwa(wyswietlanie, BFS)")
            print_bfs_adjacency_matrix(adj_matrix)
            input("Wcisnij enter aby kontynuowac...")
            print("Lista nastepnikow(wyswietlanie, BFS)")
            print_bfs_adjacency_list(adjacency_list)
            input("Wcisnij enter aby kontynuowac...")
            print("Tabela krawedzi(wyswietlanie, BFS)")
            print_bfs_edge_table(edge_table, n)
            input("Wcisnij enter aby kontynuowac...")
        elif option == '6':
            print("Macierz sasiedztwa(sortowanie, DFS)")
            print_top_dfs_adjacency_matrix(adj_matrix)
            input("Wcisnij enter aby kontynuowac...")
            print("Lista nastepnikow(sortowanie, DFS)")
            print_top_dfs_adjacency_list(adjacency_list)
            input("Wcisnij enter aby kontynuowac...")
            print("Tabela krawedzi(sortowanie, DFS)")
            print_top_dfs_edge_table(edge_table, n)
            input("Wcisnij enter aby kontynuowac...")
        elif option == '7':
            print("Macierz sasiedztwa(sortowanie, BFS)")
            print_top_bfs_adjacency_matrix(adj_matrix)
            input("Wcisnij enter aby kontynuowac...")
            print("Lista nastepnikow(sortowanie, BFS)")
            print_top_bfs_adjacency_list(adjacency_list)
            input("Wcisnij enter aby kontynuowac...")
            print("Tabela krawedzi(sortowanie, BFS)")
            print_top_bfs_edge_table(edge_table, n)
            input("Wcisnij enter aby kontynuowac...")
    else:
        print("Najpierw stworz macierz sasiedztwa")
        input("Wcisnij enter aby kontynuowac...")
