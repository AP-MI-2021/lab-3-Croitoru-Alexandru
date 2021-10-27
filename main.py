"""
3. Numerele au semne alternante.
Funcția de calcul: get_longest_alternating_signs(lst: list[int]) -> list[int]
"""

def citire_lista():
    l = []
    p = input("Introduceti numerele separate prin ',': ")
    numar = p.split(",")
    for i in numar:
        l.append(float(i))
    return l

def get_longest_alternating_signs(l):
    length = 1
    maxim = 1
    indexfinal = 0
    lst = []
    for i in range(0, len(l) - 1, 1):
        numar1 = l[i]
        numar2 = l[i+1]
        if numar1 > 0 and numar2 < 0 or numar1 < 0 and numar2 > 0:
            length = length + 1
            if length > maxim:
                maxim = length
                indexfinal = i + 1
        else:
            length = 1
    for i in range(indexfinal - maxim + 1, indexfinal + 1, 1):
        lst.append(l[i])
    return lst

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([13, -5, 16, -3, 13, 16, 17]) == [13, -5, 16, -3, 13]
test_get_longest_alternating_signs()

"""
13. Toate numerele sunt formate din cifre prime.
Funcția de calcul: get_longest_prime_digits(lst: list[int]) -> list[int]
"""

def numere_prime(x):
    if x < 2:
        return False
    for i in range(2, x // 2 + 1, 1):
        if x % i == 0:
            return False
    return True

def test_numere_prime():
    assert numere_prime(3) == True
    assert numere_prime(7) == True
    assert numere_prime(6) == False
    assert numere_prime(10) == False
test_numere_prime()

def cifre_prime(x):
    while x > 0:
        if numere_prime(x % 10) == True:
            x = x // 10
        else:
            return False
    return True

def test_is_prime():
    assert cifre_prime(33) == True
    assert cifre_prime(57) == True
test_is_prime()

def get_longest_prime_digits(l):
    length = 0
    maxim = 0
    indexfinal = 0
    lst = []
    for i in range(0, len(l), 1):
        if cifre_prime(l[i]) == True:
            length = length + 1
            if length > maxim:
                maxim = length
                indexfinal = i
        else:
            length = 0
    for i in range( indexfinal - maxim + 1, indexfinal + 1, 1):
        lst.append(l[i])
    return lst

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([55,37,25,46,48]) == [55,37,25]
test_get_longest_prime_digits()

"""
14. Toate numerele au partea întreagă egală cu partea fracționară.
Funcția de calcul: get_longest_equal_int_real(lst: list[float]) -> list[float]
"""

def numaram_cifre(n):
    c = 0
    while n > 0:
        c = c + 1
        n = n // 10
    return c

def get_longest_equal_int_real(l):
    length = 0
    maxim = 0
    finalindex = 0
    lst = []
    for i in range(0, len(l), 1):
        numar1 = int(l[i])
        numar2 = l[i] - int(l[i])
        c = numaram_cifre(numar1)
        numar2 = numar2 * (10**c)
        if numar1 == 0 and numar2 != 0:
            length = 0
            continue
        if numar1 == int(numar2):
            length = length + 1
            if length > maxim:
                maxim = length
                finalindex = i
        else:
            length = 0
    for i in range(finalindex - maxim + 1, finalindex + 1, 1):
        lst.append(l[i])
    return lst

def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([15.15, 16.16, 17.17, 18.20, 21.22]) == [15.15, 16.16, 17.17]
test_get_longest_equal_int_real()

def main():
    while True:
        print(" Daca doriti sa introduceti o lista de numere, apasati tasta 1 ")
        print(" Daca doriti sa va afiseze lista de numere, apasati tasta 2 ")
        print(" Daca doriti sa stiti subsecventa maxima de numere alternante, apasati tasta 3")
        print(" Daca doriti sa aflati subsecventa maxima de numere care detin toate cifrele prime, apasati tasta 4")
        print(" Aflati daca numarul dumneavoastra are partea intreaga cu partea fractionara, apasati tasta 5 ")
        print(" Pentru oprirea programului, apasati tasta x ")

        optiune = input("Scrieti optiunea dorita: ")

        if optiune == "1":
            lista = citire_lista()
        elif optiune == "2":
            print("Lista dumneavoastra este: ", lista)
        elif optiune == "3":
            print(get_longest_alternating_signs(lista))
        elif optiune == "4":
            print(get_longest_prime_digits(lista))
        elif optiune == "5":
            print(get_longest_equal_int_real(lista))
        elif optiune == "x":
            break
        else:
            print("Optiunea dorita nu este existenta, introduceti o valoare valida!")
main()


