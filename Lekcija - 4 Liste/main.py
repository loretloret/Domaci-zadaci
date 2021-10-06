from random import randint

#  NAPOMENA : Za zadatke koje sam smatrao prostim nisam ostavljao komentar tako da mogu naknadno da objasnim nacin
#  na koji sam razmisljao tokom rada

#######################################################################################################################

#⦁	Napišite program koji traži od korisnika da unese listu celih brojeva. Program treba da uradi sledeće:

lista = []
lista_len = eval(input("Koliko brojeva zelite da unesete: "))

while len(lista) < lista_len:
    broj = eval(input("Unesite ceo broj: "))
    lista.append(broj)

print("-" * 50)
#⦁	Štampa ukupan broj podataka u listi - done

print("Ukupan broj podataka u listi je:", len(lista))

print("-" * 50)
#⦁	Štampa poslednji podatak u listi - done

print("Poslednji podatak u listi je:", lista[-1:])

print("-" * 50)
#⦁	Štampa listu obrnutim redosledom - done

print("Lista u obrnutom redosledu:", lista[::-1])

print("-" * 50)
#⦁	Štampa Da ako lista sadrži 5 na Ne ako ne sadrži - done

if 5 in lista:
    print("Da lista sadrzi broj 5.")
else:
    print("Ne lista nema broj 5.")

print("-" * 50)
#⦁	Štampa broj petica u listi - done

print("Brojeva 5 u listi ima:", lista.count(5))

print("-" * 50)
#⦁	Briše prvi i poslednji podatak iz liste, sortira preostale podatke i štampa rezultat - done(?)

lista_rem = lista
lista_rem = lista_rem[1:-1]

print(lista_rem)

print("-" * 50)
#⦁	Štampa koliko celih brojeva u listi je manje od 5 - done

n = 0

for i in lista:
    if i < 5:
        n += 1

print("Broj cifara manjih od 5 je: ", n)

print("#" * 50)
#######################################################################################################################

#⦁	Napišite program koji generiše listu od 20 slučajnih brojeva između 1 i 100, pa:

ran_list = []

for i in range(20):
    n = randint(1, 100)
    ran_list.append(n)

print("-" * 50)
#⦁	Štampa listu - done

print(ran_list)

print("-" * 50)
#⦁	Štampa srednju vrednost svih elemenata iz liste - done

print("Srednja vrednost brojeva iznosi:", sum(ran_list) / len(ran_list))

print("-" * 50)
#⦁	Štampa najveću i najmanju vrednost iz liste - done

print("Najveca vrednost iz liste je:", max(ran_list), "\nNajmanja vrednost iz liste je:", min(ran_list))

print("-" * 50)
#⦁	Štampa drugu najmanju i drugu najveću vrednost iz liste - done

ran_list.sort()

print("Druga najmanja vrednost je:", ran_list[1], "a druga najveca vrednost je:", ran_list[len(ran_list) - 2])

print("-" * 50)
#⦁	Štampa koliko ima parnih brojeva u listi - done

par = 0

for i in ran_list:
    if i % 2 == 0:
        par += 1

print("Broj parnih brojeva u listi je :", par)

print("#" * 50)
#######################################################################################################################

#⦁	Počnite sa listom [8,9,10]. Uradite sledeće:

lista_in = [8, 9, 10]

#⦁	Postavite drugi element (indeks 1) na 17 - done

lista_in[1] = 17

#⦁	Dodajte 4, 5, i 6 na kraj liste - done

for i in range(4, 7):
    lista_in.append(i)

#⦁	Brišite prvi element liste - done

lista_in.remove(lista_in[0])

#⦁	Sortirajte listu - done

lista_in.sort()

#⦁	Duplirajte listu - done

lista_in = lista_in * 2

#⦁	Ubacite 25 na indeksu 3 - done

lista_in.insert(3, 25)

#Na kraju treba da dobijete listu [4,5,6,25,10,17,4,5,6,10,17] - done

print(lista_in)

print("#" * 50)
#######################################################################################################################

#⦁	Tražite od korisnika da unese listu koja sadrži brojeve između 1 i 12.
#   Zatim zamenite sve brojeve koji su veći od 10 sa brojem 10 - done

list_in = []
unos_brojeva = eval(input("Koliko brojeva zelite u listi: "))

while len(list_in) < unos_brojeva:
    n = eval(input("Unesite broj izmedju 1 i 12: "))
    if 12 >= n >= 1:
        list_in.append(n)
    else:
        print("Uneti broj nije u rasponu od 1 do 12!")

for i in range(len(list_in)):
    if list_in[i] > 10:
        list_in[i] = 10

print(list_in)

print("#" * 50)
#######################################################################################################################

#⦁	Tražite od korisnika da unese listu stringova.
#   Kreirajte novu listu koja sadrži iste stringove ali bez prvog slova - done

list_str = []
list_str_out = []
kraj = 1


while kraj >= 1:
    string = input("Unesite neki string (ENTER za kraj): ")
    list_str.append(string)
    if len(string) == 0:
        kraj -= 1

list_str.remove('')

for znak in list_str:
    znak = ''.join(znak[1:])
    list_str_out.append(znak)

print("Vasa lista stringova sa uklonjenim prvim znakom je:", list_str_out, sep='\n')

print("#" * 50)
#######################################################################################################################

#⦁	Kreirajte sledeće liste korišćenjem petlji.

#⦁	Listu koja se sastoji od brojeva 0 do 49 - done

lista_broj = []

for broj in range(0, 50):
    lista_broj.append(broj)

print(lista_broj)

print("-" * 50)
#⦁	Listu koja sadrži kvadrate brojeva od 1 do 50 - done

lista_broj_kvad = []

for kvad in range(1, 50):
    lista_broj_kvad.append(kvad ** 2)

print(lista_broj_kvad)

print("-" * 50)
#⦁	Listu [‘a’, ‘bb’, ‘ccc’, ‘dddd’, … ] koja se završava sa 26 kopija slova z - done

string_abc = 'abcdefghijklmnopqrstuvwxyz'
lista_abc = []

for s in string_abc:
    s = s * (1 + string_abc.index(s))
    lista_abc.append(s)

print(lista_abc)

print("#" * 50)
#######################################################################################################################

#⦁   Napišite program koji uzima dve liste L i M, iste dužine, dodaje njihove elemente da kreira novu listu N
#    čiji su elementi sume odgovarajućih elemenata iz L i M.
#    Na primer, ako je L=[3,1,4] i M=[1,5,9], onda će N biti [4,6,13] - done

lista_L = []
lista_M = []

for i in range(5):
    n = randint(1, 100)
    m = randint(1, 100)
    lista_L.append(n)
    lista_M.append(m)

lista_N = zip(lista_L, lista_M)
lista_N = [x + y for (x, y) in lista_N]

print("Prva lista 'L':", lista_L, "\nDruga lista 'M':", lista_M, "\nSuma elemenata obe liste 'N':", lista_N)

print("#" * 50)
#######################################################################################################################

#⦁	Napišite program koji traži od korisnika da unese ceo broj,
#   pa kreira listu koja se sastoji od faktora tog broja - done

faktor_in = eval(input("Unesite ceo broj: "))
lista_faktor = []

for faktor_broj in range(1, faktor_in + 1):
    if faktor_in % faktor_broj == 0:
        lista_faktor.append(faktor_broj)

print(lista_faktor)

print("#" * 50)
#######################################################################################################################

#⦁	Kada igrate igru u kojoj se koriste dve kockice, valja znati kolike su šanse za pojavljivanje nekog ishoda.
#    Na primer verovatnoća za dobijanje 12 je oko 3%, a verovatnoća za dobijanje 7 je oko 17%.
#    Mogli bi izračunati ovo matematički, ali ne znate verovatnoću. Međutim, znate na napišete program
#    kojim ćete simulirati bacanje dve kockice 10000 puta i izračunati koliki je procenat
#    pojavljivanja ishoda 2, 3, 4, …, 12 - done


lista_bacanje = []
lista_prebrojavanje = []
prebrojavanje = 2
p = 2  # Predstavlja broj u printu

for broj_bac in range(1000):  # Simulira 1000 bacanja dve kockice
    k1 = randint(1, 6)
    k2 = randint(1, 6)
    lista_bacanje.append(k1 + k2)

for broj_bac_list in lista_bacanje:  # Vadi % dobijanja svakog broja i stavlja u listu
    if prebrojavanje <= 12:
        if broj_bac_list == prebrojavanje:
            lista_prebrojavanje.append(lista_bacanje.count(broj_bac_list) / 10)
            prebrojavanje += 1

print("Od hiljadu bacanja sledeci brojevi se pojavljuju:")
for i in lista_prebrojavanje:  # Print postotak za svaki broj
    print(p, '>>>', i, '%')
    p += 1

print("#" * 50)
#######################################################################################################################

#⦁	Napišite program koji rotira elemente liste tako da se element na prvom indeksu pomera na drugi, drugi na treći,
#    itd., sve do poslednjeg koji se pomera na prvi indeks - done

# Napomena: Nije bilo potrebe da se stavi sve u while loop ali je zanimljivije
while True:
    try:
        broj_in = eval(input("Unesite broj sa kojim pocinje niz: "))
        broj2_in = eval(input("Unesite broj sa kojim se zavrsava: "))
    except NameError or SyntaxError:
        print("Unos nije validan, probajte opet!")
        continue
    if broj_in > broj2_in:
        print("Prvi broj mora biti manji, probajte opet!")
        continue
    else:
        # Bitan deo za ovaj zadatak
        lista_niz = [niz for niz in range(broj_in, broj2_in + 1)]
        broj_kraj = lista_niz.pop()
        lista_niz.insert(0, broj_kraj)
        print(lista_niz)
        break

print("#" * 50)
#######################################################################################################################

#⦁	 Korišćenjem for petlje kreirajte listu prikazanu dole, koja se sastoji od jedinica razdvojenih rastućim brojem nula
#    Poslednje dve jedinice treba da budu razdvojene sa deset nula.
#    [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....] - WiP

#  NAPOMENA : Tada nisam bio siguran kako da uradim ovaj zadatak pa sam ga ostavio za kasnije mada i sada nisam
#  bas 100% siguran kako bi odradio

#######################################################################################################################

#⦁	Napišite program koji briše višestruka pojavljivanja podataka u listi, tako da se podaci pojavljuju samo jednom.
#    Na primer lista [1,1,2,3,4,3,0,0] će posle takvog brisanja postati [1,2,3,4,0] - done

lista_pon = []

for broj_pon in range(8):
    pon_in = eval(input("Unesite broj (neka se neki ponavljaju): "))
    lista_pon.append(pon_in)

for pon_in in lista_pon[:]:           # for petlja preskace prvi broj posle .remove tako da
    if lista_pon.count(pon_in) > 1:   # koristimo indeks liste
        lista_pon.remove(pon_in)

print(sorted(lista_pon))

print("#" * 50)
#######################################################################################################################

#⦁	Napišite program koji traži od korisnika da unese dužinu u feet-ima. Program treba da korisniku pruži
#    mogućnost da bira jedincu u koju će ta dužina biti konvertovana. Jedinice mogu biti inči, jarde, milje, milimetri,
#    centimetri, metri ili kilometri. Iako ovo može biti urađeno if naredbama, mnogo je kraće ako koristimo liste
#    i for petlje, a takođe je mnogo lakše ako želimo da dodamo nove jedinice za konverziju - done

# Nisam mogao da nadjem 'elegantniji' izlaz iz petlje sem sa 0

# liste za cuvanje unosa i konverzija
lista_kon_in = []
lista_inc = []
lista_yr = []
lista_mil = []
lista_mm = []
lista_cm = []
lista_m = []
lista_km = []
lista_kon_out = [lista_inc, lista_yr, lista_mil, lista_mm, lista_cm, lista_m, lista_km]

# Unos vrednosti
while True:
    feet_in = eval(input("Unesite vrednost u feet-ima (0 za konverziju): "))
    lista_kon_in.append(feet_in)
    if feet_in == 0:
        lista_kon_in.remove(0)  # Posle break-a unosi se i 0 pa je ovaj deo bloka brise iz liste
        break

# Konverzija unosa
for feet_unos in lista_kon_in:
    lista_inc.append(feet_unos * 12)
    lista_yr.append(feet_unos * 0.333333)
    lista_mil.append(feet_unos * 0.000189394)
    lista_mm.append(feet_unos * 304.8)
    lista_cm.append(feet_unos * 30.48)
    lista_m.append(feet_unos * 0.3048)
    lista_km.append(feet_unos * 0.0003048)

# Biranje prikaza
for kon_element in lista_kon_out:
    kon_unos = eval(input("Izaberite konverziju >>> 1 za inc, 2 za yr, 3 za mil, 4 za mm, 5 za cm, 6 za m, "
                    "7 za km i 0 za kraj: "))
    if kon_unos == 0:
        print("Dovidjenja!")
        break
    print(lista_kon_out[kon_unos - 1])

print("#" * 50)
#######################################################################################################################

#⦁	Postoji neprobojna šifra pod nazivom „jednokratni ključ“. Način na koji ona radi je da pomerate svako slovo
#   poruke za slučajan broj između 1 i 26, sa preklapanjem azbuke ako je potrebno. Na primer ako je slovo koje
#   treba šifrirati y a slučajni pomak 5, tada je novo slovo d. Svako slovo dobija svoj pomak, pa nam je potrebno
#   onoliko slučajnih pomaka koliko ima slova u poruci. Kao primer recimo da je korisnik uneo reč secret . Program
#   treba da generiše 6 slučajnih brojeva između 1 i 26. Pretpostavimo da su generisani brojevi 1, 3, 2, 10, 8, i 2.
#   Šifrovana poruka će biti thebmv.

#  NAPOMENA : Ostavio sam ovaj zadatak za kasnije da ne gubim vreme posto nisam bio siguran kako da ga resim
#  tako da cu se vratiti kasnije na njega samo da ispunim 50% za sve setove

#  Neki generalni plan je da razbijem string u listu i za svaki indeks preko randint-a nadjem slovo sa istim
#  indeksom u ascii_lowercase a te indekse cuvam u novoj listi za sledeci deo sa desifrovanjem

#---------------------------------------------------------------------------------------------------------------------#

#⦁	Napišite program koji traži od korisnika da unese poruku, pa tu poruku šifrira korišćenjem gornjeg metoda.
#   Najpre konvertujte string u mala slova. Svaki blanko znak i znak interpunkcije treba da ostane nepromenjen.
#   Na primer Secret!!! postaje thebmv!!! korišćenjem gornjih pomaka.

#---------------------------------------------------------------------------------------------------------------------#

#⦁	Napišite program koji dešifruje poruke šifrovane na gornji načina. Razlog zašto se ovaj metod zove
#   „jednokratni ključ“ je zato što se slučajni pomaci koriste samo jedanput. Šifra bi mogla biti lako razbijena
#   ako bi se isti pomaci koristili u više poruka. Čak štaviše, ovaj metod je potpuno siguran samo ako su slučajni
#   brojevi stvarno slučajni što nije slučaj sa randint funkcijom koja daje takozvane pseudo slučajne brojeve. Za
#   potrebe kriptografije postoje drugi pouzdaniji načini generisanja slučajnih brojeva.

#######################################################################################################################

print("To bi bio kraj ovog seta vezbi hvala na strpljenju!", "Dovidjenja!", sep='\n')
