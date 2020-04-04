import random, math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_avl(elements, i, j, height):
    # jak dane poddrzewo nie ma elementow to konczymy rekurencje
    if i > j:
        return None, height - 1
    # wybieramy środkowy element
    mid = (i + j) // 2
    root = Node(elements[mid])
    # wywolujemy funkcje dla lewego fragmentu listy
    # wysokosc przekazujemy powiekszona o 1 jako argument bo schodzimy w dol drzewa
    root.left, height_left = build_avl(elements, i, mid - 1, height + 1)
    # i dla prawego
    root.right, height_right = build_avl(elements, mid + 1, j, height + 1)
    # porownujemy wysokosc ktorego poddrzewa wyszla wieksza
    if height_left > height_right:
        height = height_left
    else:
        height = height_right
    # zwracamy korzen i wysokosc
    return root, height


def insert_to_bst(root, node, height):
    # sprawdzamy czy wstawiana wartosc jest mniejsza od obecnego node'a
    if node.value <= root.value:
        # jak nie ma lewego dziecka, to staje sie nim node z wartoscia ktora chcemy wstawic
        if root.left is None:
            root.left = node
            # zwiekszamy wysokosc o 1
            return height + 1
        # jak lewe dziecko istnieje to wywolujemy funkcje rekursywnie dla lewego poddrzewa
        else:
            # wysokosc przekazujemy powiekszona o 1 jako argument bo schodzimy w dol drzewa
            height = insert_to_bst(root.left, node, height + 1)
    # w przeciwnym razie wstawiana wartosc jest wieksza od obecnego node'a
    # operacje wykonujemy analogicznie do tego co powyzej
    else:
        if root.right is None:
            root.right = node
            return height + 1
        else:
            height = insert_to_bst(root.right, node, height + 1)
    return height


def build_bst(elements):
    # korzeniem staje sie pierwszy element listy
    root = Node(elements[0])
    # wysokosc jest teraz rowna 0
    max_height = 0
    # wstawiamy do drzewa kazdy z elementow listy po kolei
    for i in range(1, len(elements)):
        height = 0
        # wstawiamy pojedynczy element, funkcja zwraca poziom drzewa, na ktorym znajduje sie wstawiony element
        height = insert_to_bst(root, Node(elements[i]), height)
        # sprawdzamy czy wstawienie nowego elementu spowodowalo zmiane wysokosci drzewa
        if height > max_height:
            max_height = height
    # zwracamy korzen i wysokosc
    return root, max_height


# minimum znajduje sie na skrajnie lewym lisciu wiec przechodzimy do niego rekursywnie przez lewe dzieci
def bst_min(node):
    # wypisujemy element sciezki do minimum
    print(node.value)
    # jak juz nie ma lewego dziecka to dany node jest minimum
    if node.left is None:
        return node.value
    else:
        # przechodzimy do lewego dziecka
        return bst_min(node.left)


# maximum znajduje sie na skrajnie prawym lisciu, sytuacja analogiczna do bst_min
def bst_max(node):
    print(node.value)
    if node.right is None:
        return node.value
    else:
        return bst_max(node.right)


def delete_node(node, number): # na starcie na wejsciu jako node podajemy root
    # funkcja wykonuje sie az node nie bedzie pusty (dlaczego tak jest wyjasnione pozniej)
    if not node:
        return node
    # opcja 1: znalezlismy liczbe do usuniecia
    elif node.value == number:
        # opcja 1.1: nie ma prawego dziecka - za usuniety dajemy lewy, a reszta jest okej i nie trzeba nic robic
        if not node.right:
            return node.left
        # opcja 1.2: nie ma lewego dziecka - za usuniety dajemy prawy, a reszta jest okej i nie trzeba nic robic
        if not node.left:
            return node.right
        # opcja 1.3: sa 2 dzieci (lub 0, ale wtedy sie praktycznie nic nie zadzieje)
        # nalezy znalesc najmniejszy element od badanego na prawo lub
        # najmwiekszy na lewo, ponieważ one sa najbardziej zblizone do wartoscia do badanego
        # (w tej implementacji szukamy największego po lewej)
        biggest_node = node.left
        while biggest_node.right:
            biggest_node = biggest_node.left
        # za nasz wartosc badanego elementu dajemy warosc najwiekszego po lewej
        node.value = biggest_node.value
        # funkcja wykonuje sie dla elementu po prawej od badanego i bedziemy ponownie szukac
        # zblizonego elementu do niego
        node.right = delete_node(node.right, node.value)
        # cala ta rekurencja pokolei przestawia odpowiednio elementy bazujac na tym, ze na ich stare miejsce
        # wstawia elementy najbardziej zblizone wartoscia do nich, dzieki czemu drzewo sie nie psuje
    # opcja 2: dalej szukamy liczby do usuniecia
    elif node.value > number:
        node.left = delete_node(node.left, number)
    elif node.value < number:
        node.right = delete_node(node.right, number)
    return node


def delete_nodes(node, elements):
    # usuwamy kazdy z podanych elementow
    for element in elements:
        delete_node(node, element)


def print_pre_order(node):
    # wypisujemy w kolejnosci korzen->lewy->prawy
    print(node.value)
    if node.left is not None:
        print_pre_order(node.left)
    if node.right is not None:
        print_pre_order(node.right)


def print_in_order(node):
    # wypisujemy w kolejnosci lewy->korzen->prawy
    if node.left is not None:
        print_in_order(node.left)
    print(node.value)
    if node.right is not None:
        print_in_order(node.right)


def delete_tree(node):
    # usuwamy w kolejnosci lewy->prawy->korzen
    if node.left is not None:
        delete_tree(node.left)
    if node.right is not None:
        delete_tree(node.right)
    node.value = None


def rotate_right(node):
    if node.right is None and node.left is None:
        return node
    else:
        while node.left is not None:
            p = node.left
            node.left = p.right
            p.right = node
            node = p
        node.right = rotate_right(node.right)
        return node


def rotate_left(node, rotations, m):
    if rotations == m:
        return node
    else:
        p = node.right
        node.right = p.left
        p.left = node
        node = p
        node.right = rotate_left(node.right, rotations + 1, m)
        return node


def balance(root, n):
    root = rotate_right(root)
    m = 2 ** math.floor(math.log2(n + 1)) - 1
    root = rotate_left(root, 0, n - m)
    while m > 1:
        m //= 2
        root = rotate_left(root, 0, m)
    return root


sequence_type = None
while sequence_type != '0':
    print("-----------------------")
    print("1.Podaj wlasny ciag")
    print("2.Wygeneruj losowy ciag")
    print("0.Wyjscie")
    print("-----------------------")
    sequence_type = input(">")
    if sequence_type == '1':
        print("Podaj ciag oddzielajac liczby spacjami(np. \"1 2 3\"). Ciag moze miec maksymalnie 10 elementow.")
        try:
            numbers = [int(x) for x in input('>').split()]
            if len(numbers) not in range(1, 11):
                print("Nieodpowiednia liczba elementow!")
                sequence_type = None
        except Exception:
            print("Wystapil blad! Niepoprawny format danych.")
            sequence_type = None
    elif sequence_type == '2':
        print("Podaj dlugosc ciagu:")
        n = int(input(">"))
        if n in range(1, 11):
            numbers = random.sample(range(n), n)
        else:
            print("Nieodpowiednia liczba elementow!")
            sequence_type = None
    if sequence_type in ['1', '2']:
        option = None
        tree_built = False
        while option != '0':
            print("--------------------------------------------------------------")
            print("Obecny ciag:", numbers)
            print("1.Konstruuj drzewo AVL metoda polowienia binarnego")
            print("2.Konstruuj drzewo BST wstawiajac elementy ciagu po kolei")
            print("3.Znajdz minimum i maksimum oraz wypisz sciezke poszukiwania")
            print("4.Usun elementy o podanych wartosciach")
            print("5.Wypisz elementy drzewa w porzadkach in-order i pre-order")
            print("6.Usun cale drzewo metoda post-order")
            print("7.Zrownowaz drzewo przez rotacje")
            print("0.Wyjscie")
            print("--------------------------------------------------------------")
            option = input(">")
            if option == '1':
                sorted_numbers = sorted(numbers)
                tree_root, tree_height = build_avl(sorted_numbers, 0, len(numbers) - 1, 0)
                print("Operacja zostala wykonana. Wysokosc drzewa:", tree_height)
                input("Wcisnij enter aby kontynuowac...")
                tree_built = True
            elif option == '2':
                tree_root, tree_height = build_bst(numbers)
                print("Operacja zostala wykonana. Wysokosc drzewa:", tree_height)
                input("Wcisnij enter aby kontynuowac...")
                tree_built = True
            if tree_built:
                if option == '3':
                    print("Sciezka do minimum:")
                    minimum = bst_min(tree_root)
                    print("Sciezka do maksimum:")
                    maximum = bst_max(tree_root)
                    print("Minimum: {}, Maksimum: {}".format(minimum, maximum))
                    input("Wcisnij enter aby kontynuowac...")
                elif option == '4':
                    print("Podaj liczby do usuniecia oddzielajac je spacjami(np. \"1 2 3\"):")
                    try:
                        to_delete = [int(x) for x in input(">").split()]
                        delete_nodes(tree_root, to_delete)
                    except Exception:
                        print("Wystapil blad! Niepoprawny format danych.")
                elif option == '5':
                    print("In-order:")
                    print_in_order(tree_root)
                    print("Pre-order")
                    print_pre_order(tree_root)
                    input("Wcisnij enter aby kontynuowac...")
                elif option == '6':
                    delete_tree(tree_root)
                elif option == '7':
                    tree_root = balance(tree_root, len(numbers))
                    print("Operacja zostala wykonana.")
                    input("Wcisnij enter aby kontynuowac...")
            else:
                print("--------------------------------------------------------------")
                print("Przed skorzystaniem z opcji 3-7 nalezy zbudowac drzewo!")
