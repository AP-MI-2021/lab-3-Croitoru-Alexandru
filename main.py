from math import *

'''
Determina daca un numar este antipalindrom
'''
def is_antipalindrome(n):
    '''
    :param n: nr intreg
    :return: returneaza true daca este antipalindrom si false in caz contrar
    '''
    n = str(n)
    lungime = len(n) - 1
    i = 0
    ok = 1
    while i < lungime :
        if n[i]==n[lungime]:
            ok=0
        i+=1
        lungime-=1
    if ok==0:
        return False
    else: return True

'''
calculeaza cel mai mare numar prim, aflat sub valoarea n
'''
def get_largest_prime_below(n):
    '''
    :param n: numar intreg
    :return: Returneaza numarul prim
    '''
    for i in range(n-1, 1, -1):
        ok=1
        for j in range(2, int(sqrt(i))+1):
            if i%j==0:
                ok=0
        if ok == 1:
            return i

'''
transforma un numar din baza 10, in baza 2
'''
def get_base_2(n:str):
    '''
    :param n: numarul in baza 10, sub forma de string
    :return: returneaza sub forma de string, numarul convertit in baza 2
    '''
    if n == '0':
        return '0'
    n = int(n)
    lst = []
    s = ''
    while n:
        lst.append(n%2)
        n = n // 2
    for i in range(len(lst)-1, -1, -1):
        s = s + str(lst[i])
    return s

def test_get_largest_prime_below():
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(16) == 13

def test_get_base_2():
    assert get_base_2('10') == '1010'
    assert get_base_2('123') == '1111011'
    assert get_base_2('16') == '10000'
    assert get_base_2('0') == '0'

def test_is_antipalindrome():
    assert is_antipalindrome(232) is False
    assert is_antipalindrome(10) is True
    assert is_antipalindrome(2424) is True
    assert is_antipalindrome(111) is False

test_is_antipalindrome()
test_get_largest_prime_below()
test_get_base_2()

option = '''
Daca doriti sa aflati cel mai mare numar prim, mai mic decat o valoare, scrieti "1".  
Daca doriti sa transformati un numar din baza 10 in baza 2, scrieti "2". 
Daca doriti sa aflati daca un numar este antipalindrom, scrieti "3".
Daca doriti sa opriti programul, apasati ctrl + c, sau scrieti "4".
'''

def main():
    while True:
        optiune = input(option)
        if optiune == '1':
            numar = int(input("Scrieti valoarea:"))
            print(f"Cel mai mare numar prim, mai mic decat {numar}, este: " + str(get_largest_prime_below(numar)))
        elif optiune == '2':
            numar = input("Scrieti numarul pe care doriti sa-l convertiti: ")
            print(f"Numarul {numar} convertit in baza 2 este: " + get_base_2(numar))
        elif optiune == '3':
            numar = int(input("Scrieti numarul dumneavoastra: "))
            if is_antipalindrome(numar) == False:
                print(f"Numarul {numar} nu este antipalindrom.")
            else: print(f"Numarul {numar} este antipalindrom.")
        elif optiune == '4':
            print("Programul a fost oprit!")
            break
        else: print("Comanda neexistenta.")

if __name__ == '__main__':
  main()


  def get_longest_alternating_sign(lst: list[int]):
      l = []
      l_temp = []
      for i in range(0, len(lst) - 1):
          numar1 = lst[i]
          numar2 = lst[i + 1]
          if numar1 * numar2 > 0:
              l_temp.append(numar1)
              if len(l_temp) > len(l):
                  l = l_temp
              l_temp = []
          if numar1 * numar2 < 0:
              l_temp.append(numar1)
      return l


  ceva = get_longest_alternating_sign([5, 7, -5, 9, -15, 15, 13, -20])
  print(ceva)


def get_longest_alternating_sign(lst: list[int]):
    l = []
    l_temp = []
    for i in range(0, len(lst) -1):
        numar1 = lst[i]
        numar2 = lst[i+1]
        if numar1*numar2 > 0:
            l_temp.append(numar1)
            if len(l_temp) > len(l):
                l = l_temp
            l_temp = []
        if numar1*numar2 < 0:
            l_temp.append(numar1)
    return l



ceva = get_longest_alternating_sign([5,7,-5,9,-15,15,13,-20])
print(ceva)