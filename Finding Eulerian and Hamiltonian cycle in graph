import random
import sys
from timeit import default_timer as timer
from copy import deepcopy
 
 
def dfs(adj_list, visited, sublist):
    visited[sublist] = 1
    print(sublist)
    for tail in adj_list[sublist]:
        if visited[tail] == 0:
            dfs(adj_list, visited, tail)
 
 
def print_dfs(adj_list):
    visited = [0] * len(adj_list)
    for sublist in range(len(adj_list)):
        if visited[sublist] == 0:
            dfs(adj_list, visited, sublist)
 
 
def bfs(adj_list, visited, sublist_index, queue):
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
 
 
def print_bfs(adj_list):
    visited = [0] * len(adj_list)
    queue = []
    for sublist_index in range(len(adj_list)):
        if visited[sublist_index] == 0:
            bfs(adj_list, visited, sublist_index, queue)
 
 
def hamiltonian(v, visited, visited_nodes, nodes, start, path):
    visited[v] = True
    visited_nodes += 1
    for successor in nodes[v]:
        if successor == start and visited_nodes == len(nodes):
            return True
        if not visited[successor]:
            if hamiltonian(successor, visited, visited_nodes, nodes, start, path):
                path.append(successor)
                return True
    visited[v] = False
    visited_nodes -= 1
    return False
 
 
def print_hamiltonian(adjacency_list):
    visited = [False] * len(adjacency_list)
    path = [0]
    start = 0
    visited_nodes = 0
    cycle = hamiltonian(start, visited, visited_nodes, adjacency_list, start, path)
    if cycle:
        print("\nCykl Hamiltona:")
        for i in path:
            print(i)
    else:
        print("\nBrak cyklu Hamiltona.")
 
 
def euler(v, list_copy, stack):
    while list_copy[v]:
        u = list_copy[v].pop()
        list_copy[u].remove(v)
        euler(u, list_copy, stack)
    stack.append(v)
 
 
def print_euler(adjacency_list):
    stack = []
    list_copy = deepcopy(adjacency_list)
    euler(0, list_copy, stack)
    cycle = True
    for node in list_copy:
        if node != []:
            cycle = False
            break
    if cycle and stack[0] == stack[-1]:
        print("\nCykl Eulera:")
        for i in stack:
            print(i)
    else:
        print("\nBrak cyklu Eulera.")
 
def undirected_graph(n, saturation):
    successful = False
    while not successful:
        successful = True
        lists = [[] for i in range(n)]
        number_of_edges = int(((n * (n - 1)) // 2) * saturation)
        hamiltonian_cycle = random.sample(range(n), n)
        # tworzymy cykl hamiltona
        for index, node in enumerate(hamiltonian_cycle):
            if index != len(hamiltonian_cycle) - 1:
                lists[node].append(hamiltonian_cycle[index + 1])
                lists[hamiltonian_cycle[index + 1]].append(node)
        lists[hamiltonian_cycle[-1]].append(hamiltonian_cycle[0])
        lists[hamiltonian_cycle[0]].append(hamiltonian_cycle[-1])
        number_of_edges -= len(hamiltonian_cycle)
        # dopelniamy graf
        for i in range(number_of_edges):
            first = random.randint(0, n - 1)
            second = random.randint(0, n - 1)
            start = timer()
            while second == first or second in lists[first]:
                second = random.randint(0, n - 1)
                if timer() - start > 0.1:
                    successful = False
                    break
            if successful:
                lists[first].append(second)
                lists[second].append(first)
                successful = True
            else:
                break
    return lists
 
 
def graph_even_deg(n, saturation):
    successful = False
    while not successful:
        successful = True
        lists = [[] for i in range(n)]
        number_of_edges = int(((n*(n-1))//2) * saturation)
        hamiltonian_cycle = random.sample(range(n), n)
        # tworzymy cykl hamiltona
        for index, node in enumerate(hamiltonian_cycle):
            if index != len(hamiltonian_cycle)-1:
                lists[node].append(hamiltonian_cycle[index+1])
                lists[hamiltonian_cycle[index+1]].append(node)
        lists[hamiltonian_cycle[-1]].append(hamiltonian_cycle[0])
        lists[hamiltonian_cycle[0]].append(hamiltonian_cycle[-1])
        number_of_edges -= len(hamiltonian_cycle)
        # dopelniamy graf
        for i in range(number_of_edges//3):
            first = random.randint(0, n-1)
            second = random.randint(0, n-1)
            start = timer()
            while second == first or second in lists[first]:
                second = random.randint(0, n - 1)
                if timer()-start > 0.1:
                    successful = False
                    break
            third = random.randint(0, n - 1)
            start = timer()
            while third == first or third == second or third in lists[first] or third in lists[second]:
                third = random.randint(0, n - 1)
                if timer()-start > 0.1:
                    successful = False
                    break
            if successful:
                lists[first].append(second)
                lists[first].append(third)
                lists[second].append(first)
                lists[second].append(third)
                lists[third].append(first)
                lists[third].append(second)
                successful = True
            else:
                break
    return lists
 
 
def graph_non_hamiltonian(n, saturation):
    successful = False
    while not successful:
        successful = True
        lists = [[] for i in range(n)]
        number_of_edges = int(((n * (n - 1)) // 2) * saturation)
        hamiltonian_cycle = random.sample(range(n), n)
        # tworzymy cykl hamiltona
        for index, node in enumerate(hamiltonian_cycle):
            if index != len(hamiltonian_cycle) - 1:
                lists[node].append(hamiltonian_cycle[index + 1])
                lists[hamiltonian_cycle[index + 1]].append(node)
        lists[hamiltonian_cycle[-1]].append(hamiltonian_cycle[0])
        lists[hamiltonian_cycle[0]].append(hamiltonian_cycle[-1])
        number_of_edges -= len(hamiltonian_cycle)
        # dopelniamy graf
        for i in range(number_of_edges // 3):
            first = random.randint(0, n - 1)
            second = random.randint(0, n - 1)
            start = timer()
            while second == first or second in lists[first]:
                second = random.randint(0, n - 1)
                if timer() - start > 0.1:
                    successful = False
                    break
            third = random.randint(0, n - 1)
            start = timer()
            while third == first or third == second or third in lists[first] or third in lists[second]:
                third = random.randint(0, n - 1)
                if timer() - start > 0.1:
                    successful = False
                    break
            if successful:
                lists[first].append(second)
                lists[first].append(third)
                lists[second].append(first)
                lists[second].append(third)
                lists[third].append(first)
                lists[third].append(second)
                successful = True
            else:
                break
            number_of_edges -= 3
        if successful:
            # izolujemy wierzcholek
            isolated = random.randint(0, n-1)
            number_of_edges += len(lists[isolated])
            lists[isolated] = []
            for i in lists:
                try:
                    i.remove(isolated)
                except:
                    pass
            # stracilismy troche krawedzi przy izolacji wiec odpowiednio dopelniamy o liczbe krawedzi ktora stracilismy
            for i in range(number_of_edges//3):
                first = random.randint(0, n-1)
                start = timer()
                while first == isolated:
                    first = random.randint(0, n - 1)
                    if timer() - start > 0.1:
                        successful = False
                        break
                second = random.randint(0, n-1)
                while second == first or second in lists[first] or second == isolated:
                    second = random.randint(0, n - 1)
                    if timer() - start > 0.1:
                        successful = False
                        break
                third = random.randint(0, n - 1)
                while third == first or third == second or third in lists[first] or third in lists[second] or third == isolated:
                    third = random.randint(0, n - 1)
                    if timer() - start > 0.1:
                        successful = False
                        break
                if successful:
                    lists[first].append(second)
                    lists[first].append(third)
                    lists[second].append(first)
                    lists[second].append(third)
                    lists[third].append(first)
                    lists[third].append(second)
                    successful = True
                else:
                    break
    return lists
 
 
sys.setrecursionlimit(100000)
option = None
created = False
while option != '0':
    print("-----------------------")
    print("1.Wpisz wlasny graf")
    print("2.Utwórz graf spójny nieskierowany o n wierzchołkach i zadanym nasyceniu grafu")
    print("3.Utworz graf z cyklem Hamiltona i nasyceniem krawedziami 30%")
    print("4.Utworz graf z cyklem Hamiltona i nasyceniem krawedziami 70%")
    print("5.Utwórz graf nieskierowany nie-hamiltonowski o nasyceniu 50%")
    print("6.Wyswietl graf(DFS)")
    print("7.Wyswietl graf(BFS)")
    print("8.Znajdz cykl Eulera")
    print("9.Znajdz cykl Hamiltona")
    print("0.Wyjscie")
    print("-----------------------")
    option = input(">")
    if option == '1':
        print("Podaj liczbe wierzcholkow:")
        n = int(input())
        graph = []
        print("Podaj sasiadujace wierzcholki kazdego z wierzcholkow:")
        for node in range(n):
            graph.append([])
            graph[-1] = [int(x) for x in input("[{}]: ".format(node)).split()]
        print(graph)
        created = True
    elif option == '2':
        print("Podaj liczbe wierzcholkow:")
        n = int(input())
        print("Podaj nasycenie w %:")
        s = float(input())/100
        graph = undirected_graph(n, s)
        created = True
    if option == '3':
        print("Podaj liczbe wierzcholkow:")
        n = int(input())
        graph = graph_even_deg(n, 0.3)
        created = True
    elif option == '4':
        print("Podaj liczbe wierzcholkow:")
        n = int(input())
        graph = graph_even_deg(n, 0.7)
        created = True
    elif option == '5':
        print("Podaj liczbe wierzcholkow:")
        n = int(input())
        graph = graph_non_hamiltonian(n, 0.5)
        created = True
    if created:
        if option == '6':
            print_dfs(graph)
            input("Wcisnij enter aby kontynuowac...")
        if option == '7':
            print_bfs(graph)
            input("Wcisnij enter aby kontynuowac...")
        elif option == '8':
            print_euler(graph)
            input("Wcisnij enter aby kontynuowac...")
        elif option == '9':
            print_hamiltonian(graph)
            input("Wcisnij enter aby kontynuowac...")
    else:
        print("Najpierw utworz graf dowolna metoda")
        input("Wcisnij enter aby kontynuowac...")
