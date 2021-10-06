from math import factorial
from random import randint

#⦁	Napišite funkciju pod nazivom pravougaonik koja prihvata dva cela broja m i n kao argumente i štampa m × n boks
#   koji se sastoji od zvezdica. Dole je prikazan izlaz funkcije pravougaonik(2,4) - done
#        ****
#        ****


def pravougaonik(m, n):
    for i in range(m):
        print('*' * n)


m = eval(input("Unesite broj redova : "))
n = eval(input("Unesite broj kolona : "))

pravougaonik(m, n)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju pod nazivom dodaj_uzvicnik koja prihvata listu stringova i dodaje znak uzvika (!) na kraj
#   svakog od stringova iz liste. Program treba da modifikuje originalnu listu i ne vraća ništa - done


def dodaj_uzvicnik():
    for string in range(len(lista_str)):
        lista_str[string] = lista_str[string] + '!'


lista_str = []

while True:
    str_unos = input('Unesite neki string (kraj za izlaz): ')
    if str_unos == 'kraj':
        break
    lista_str.append(str_unos)

dodaj_uzvicnik()

print(lista_str)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite istu funkciju ali da ona ne modifikuje originalnu listu već da vraća novu listu - done


def dodaj_uzvicnik2():
    lista_str2 = []
    for string in lista_str_in:
        lista_str2.append(string + '!')
    return print(lista_str2)


lista_str_in = []

while True:
    str_unos2 = input('Unesite neki string (kraj za izlaz): ')
    if str_unos2 == 'kraj':
        break
    lista_str_in.append(str_unos2)

dodaj_uzvicnik2()

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju suma_cifara koja prihvata jedan ceo broj num i vraća sumu njegovih cifara - done


def suma_cifara(num):
    suma_list = list(num)
    suma = 0
    for element in suma_list:
        suma += int(element)
    return suma


broj = input("Unesite neki visecifren broj : ")

print(suma_cifara(broj))

print('#' * 50)
#######################################################################################################################

#⦁	Digitalni koren nekog broja n se dobija na sledeći način: Saberemo cifre broja n da dobijemo novi broj.
#   Saberimo cifre tog broja da dobijemo novi broj. Nastavljamo ovaj proces sve dok broj dobijen sabiranjem cifara
#   ne bude jednocifren. Taj broj je digitalni koren. Na primer, ako je n=45893, posle sabiranja njegovih cifara imamo
#   4+5+8+9+3 = 29. Saberemo cifre broja 29 pa dobijemo 2+9=11. Sada saberemo cifre broja 11i dobijemo 1+1=2. Pošto je
#   2 jednocifren, on je digitalni koren broja 45893. Napišite funkciju koja vraća digitalni koren celog broja n - done


def digi_koren(num):
    if num == 0:
        return 0
    broj_digi = 0
    for i in range(0, len(num)):
        broj_digi = (broj_digi + int(num[i])) % 9

    if broj_digi == 0:
        return 9
    else:
        return broj_digi % 9


digi_broj = input("Unesite neki visecifren broj : ")

print(digi_koren(digi_broj))

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju prva_razlika koja prihvata dva stringa i vraća prvu poziciju na kojoj se stringovi razlikuju.
#   Ako su stringovi identični funkcija vraća -1 - done


def prva_razlik(string1, string2):
    if len(string1) != len(string2):
        print("Stringovi nisu iste duzine!")
    else:
        for i in range(0, len(string1)):
            if string1[i] != string2[i]:
                return print(string1.index(string1[i]))
            else:
                if string1 == string2:
                    return print(-1)


str1 = input("Unesite jedan string : ")
str2 = input("Unesite jos jedan string : ")

prva_razlik(str1, str2)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju binom koja prihvata dva cela broja n i k i vraća binomijalni koeficijent
#   n C k. Definicija: n C k = n!/(k!(n-k)!) - done


def binom(x, y):
    return factorial(x) / (factorial(y) * (factorial(x - y)))


fac1, fac2 = eval(input("Unesite vrednost za x i y (npr 13, 10) : "))

if fac1 < fac2:
    print("Broj x mora biti veci od y!")
else:
    print(binom(fac1, fac2))

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju koja prihvata ceo broj n i vraća slučajan ceo broj sa tačno n cifara. Na primer ako je n
#   jednako 3,tada bi 125 i 593 bili validne vrednosti za vraćanje iz funkcije, ali bi 093 bilo neispravno jer je to
#   u stvari broj 93, koji je dvocifren - done


def slucajan_broj(num):
    s = ''.join(str(randint(1, 9)))
    while len(s) < num:
        for i in range(num - 1):
            s += ''.join(str(randint(0, 9)))
    return print(s)


broj_random = eval(input("Unesite neki ceo pozitivan broj : "))

slucajan_broj(broj_random)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju broj_faktora koja prihvata ceo broj i vraća koliko faktora (delioca) ima taj broj - done


def faktor(num):
    i = 1
    faktor_lista = []
    while i <= num:
        if num % i == 0:
            faktor_lista.append(i)
        i += 1
    return print(len(faktor_lista))


faktor_broj = eval(input("Unesite neki broj : "))

faktor(faktor_broj)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju faktori koja prihvata ceo broj i vraća listu njegovih faktora - done

#  NAPOMENA : Ako sam dobro razumeo zadatak funkcija je ista kao i u predhodnom samo bih vracao listu ne len od iste

#######################################################################################################################

#⦁	Napišite funkciju najbliži koja prihvata listu brojeva L i broj n i vraća najveći element iz L koji nije
#   veći od n. Na primer ako je L=[1,6,3,9,11] a n=8, tada funkcija treba da vrati 6, zato što je 6 najbliža vrednost
#   broju 8 u L, a koja nije veća od 8 - done


def najblizi(l, n):
    lista_inner = [i for i in l]
    for i in lista_inner[:]:
        if i >= n:
            lista_inner.remove(i)
    lista_inner.sort(reverse=True)
    return print(lista_inner[0])


lista_najblizi = [1, 22, 15, 6, 8, 10, 33, 45, 27, 9, 7, 17, 12, 5]

najblizi(lista_najblizi, 26)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju poklapanje koja prihvata dva stringa i vraća koliko ima poklapanja između dva stringa. Poklapanje
#   je slučaj kada stringovi imaju isto slovo na istoj poziciji. Na primer, ‘python’ i ‘path’ se poklapaju na prvom,
#   trećem i četvrtom slovu, pa funkcija treba da vrati 3 - done


def poklapanja(string1, string2):
    brojac = 0
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            brojac += 1
    return print(brojac)


str_pok1 = input("String 1 : ").lower()
str_pok2 = input("String 2 : ").lower()

poklapanja(str_pok1, str_pok2)

print('#' * 50)
#######################################################################################################################

#⦁	Setimo se da ako je s neki string tada s.find(‘a’) pronalazi poziciju (indeks) prvog slova a u s. Problem je što
#   ona ne pronalazi sve pozicije slova a. Napišite program findall koji za dati string i za dato slovo, vraća listu
#   koja sadrži sve pozicije na kojima se nalazi to slovo u stringu. Funkcija treba da vrati praznu listu ako se
#   slovo ne nalazi u stringu - done


def findall(string_in, znak_in):
    lista_find = [indeks for indeks, znak_out in enumerate(string_in) if znak_out == znak_in]
    print(lista_find)


find_string = input("Uesite neki string : ").lower()
find_slovo = input("Unesite znak za koji zelite indekse : ").lower()

findall(find_string, find_slovo)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju promeni_velicinu koja za dati string vraća string u kojem su sva velika slova zamenjena
#   malim i obratno - done


def promeni_velicinu(string_prom_in):
    string_prom_out = ''
    promena = map(lambda slovo: slovo.lower() if slovo == slovo.upper() else slovo.upper(), string_prom_in)
    for i in promena:
        string_prom_out += ''.join(i)
    print("Vas string sa zamenjenim velikim i malim slovima :", string_prom_out)


promeni_string = input("Unesite neki string : ")

promeni_velicinu(promeni_string)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju is_sorted koja za datu listu vraća True ako je lista sortirana, a False u suprotnom slučaju - done


def is_sorted(lista_sort):
    lista_sort1 = lista_sort.copy()
    lista_sort1.sort()
    if lista_sort == lista_sort1:
        print("Sortirano")
    else:
        print("Nije")


lista_in = [1, 2, 3, 4]

is_sorted(lista_in)

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju root koja za dati broj x i ceo broj n vraća x1/n. Pri definiciji funkcije postavite
#   podrazumevajuću (default) vrednost za n da bude 2 - done


def root(num, n=2):
    return num * (1/n)


print(root(3))

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju one_away koja prihvata dva stringa i vraća True ako su stringovi iste dužine i razlikuju se
#   samo u jednom slovu, kao na primer bike/hike ili water/wafer - done


def one_away(s, s1):
    brojac = 0
    if len(s) == len(s1):
        for i in range(len(s)):
            if s[i] != s1[i]:
                brojac += 1
        if brojac <= 1:
            return True
        else:
            return False
    else:
        return False


string1_in = input("Unos 1 : ").lower()
string2_in = input("Unos 2 : ").lower()

print(one_away(string1_in, string2_in))

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju primes koja za dati broj n vraća listu prvih n prostih brojeva. Neka podrazumevajuća vrednost
#   za n bude 100 - done


def primes(n=100):
    primes_lista = []
    for prime in range(2, n + 1):
        if all(prime % i != 0 for i in range(2, prime)):
            primes_lista.append(prime)
    return primes_lista


num_prime = input("Unesite ceo pozitivan broj : ")

if len(num_prime) == 0:
    print(primes())
else:
    print(primes(int(num_prime)))

print('-' * 50)
#---------------------------------------------------------------------------------------------------------------------#

#⦁	Modifikujte gornju funkciju tako da ima i jedan opcioni argument pod nazivom start koji omogućava da lista
#   startuje sa vrednošću većom od 2.Funkacija treba da vrati listu prvih n prostih brojeva koji su veći ili jednaki
#   vrednosti varijable start. Podrazumevajuća vrednost za start treba da bude 2 - done


def primes1(start=2, n1=100):
    if start > n1:
        return "Vrednost za pocetak niza mora biti manja od vrednosti za kraj!"
    else:
        primes_lista = []
        for prime in range(start, n1 + 1):
            if all(prime % i != 0 for i in range(2, prime)):
                primes_lista.append(prime)
        return primes_lista


num_start = input("Unesite pozitivan ceo broj za pocetak niza : ")
num_prime1 = input("Unesite pozitivan ceo broj za kraj niza : ")

if len(num_prime1) == 0:
    print(primes1())
else:
    print(primes1(int(num_start), int(num_prime1)))

print('#' * 50)
#######################################################################################################################

#⦁	Napišite funkciju koja za dati ceo broj, vraća naziv toga broja na engleskom (srpskom) jeziku. Na primer, za broj
#   123456 kao argument funkcija treba da vrati „ one hundred twenty-three thousand, four hundred fifty-six“.

#######################################################################################################################

#⦁	Napišite funkciju merge koja prihvata dve sortirane liste (istih ili različitih dužina), i spaja (merdžuje) ih
#   u jednu sortiranu listu - done


def merge(l1, l2):
    l1.extend(l2)
    l1.sort()
    return l1


merge_while = True
lista_1 = []
lista_2 = []

while True:
    l1_in = input("Unesite element za prvu listu (ENTER za kraj) : ")
    if l1_in == '':
        break
    lista_1.append(int(l1_in))
while True:
    l2_in = input("Unesite element za drugu listu (ENTER za kraj) : ")
    if l2_in == '':
        break
    lista_2.append(int(l2_in))

print(merge(lista_1, lista_2))

print('-' * 50)
#---------------------------------------------------------------------------------------------------------------------#

#⦁	Uradite isto korišćenjem sort metode - done?

#  NAPOMENA : U predhodnom delu sam uradio sa metodom sort() tako da nisam siguran sta treba uraditi

#def merge(l1, l2):
#    l3 = l1 + l2
#    l3.sort()
#    return l3

#---------------------------------------------------------------------------------------------------------------------#

#⦁	Uradite ovo bez korišćenja sort metode - done


# def merge(l1, l2):
#     l1.extend(l2)
#     for i in range(len(l1)):
#         for n in range(i + 1, len(l1)):
#             if l1[i] > l1[n]:
#                 l1[i], l1[n] = l1[n], l1[i]
#     return l1

print('#' * 50)
#######################################################################################################################

#⦁	U jednom od prethodnih poglavlja smo za proveru da li se neka reč nalazi u listi reči koristili naredbu
# if rec in lista_reci:
#   Ovo je nažalost veoma sporo, ali postoji brži način koji se zove binarno pretraživanje (binary search).
#   Da implementiramo binarno pretraživanje u nekoj funkciji, počinjemo sa poređenjem varijable rec sa rečju iz
#   sredine liste lista_reci. Ako su iste završili smo traženje i možemo da vratimo True. S druge strane ako rec
#   dolazi pre reči iz sredine, onda traženje treba da nastavimo u prvoj polovini liste. Ako rec dolazi posle sredine,
#   tada traženje nastavljamo u drugoj polovini liste. Ponavljamo ovaj proces sve dok ili ne pronađemo traženu reč ili
#   nemamo više gde da tražimo ,u kom slučaju vraćamo False. Operatori < i > mogu biti iskorišćeni za alfabetsko
#   poređenje stringova - WiP

#######################################################################################################################