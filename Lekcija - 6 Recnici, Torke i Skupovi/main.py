from random import randint
import random

#⦁	Napišite program koji uzastopno traži od korisnika da unese proizvod i njegovu cenu.
#   Smestite sve unete vrednosti u rečnik čiji je ključ naziv proizvoda a vrednost cena proizvoda.
#   Kada korisnik završi sa unosom podataka za rečnik, dajte mu mogućnost da uzastopno unosi ime proizvoda pa
#   štampajte njegovu cenu ili poruku da proizvod nije u rečniku - done

proizvod_cena = {}

while True:
    proizvod = input("Unesite naziv proizvoda (kraj za izlaz): ").lower()
    if proizvod == "kraj":
        print("Dovidjenja!")
        break
    cena = eval(input("Unesite cenu tog proizvoda: "))
    proizvod_cena[proizvod] = cena

while True:
    proizvod_srch = input("Unesite proizvod za koji potrazujete cenu (kraj za izlaz): ").lower()
    if proizvod_srch == "kraj":
        break
    if proizvod_srch in proizvod_cena:
        print('{:2s}{:6.2f}'.format("$", float(proizvod_cena[proizvod_srch])))
    elif proizvod_srch not in proizvod_cena:
        print("Uneti proizvod nije na stanju!")

print("#" * 100)
#######################################################################################################################

#⦁	Koristeći rečnik kreiran u prethodnom problemu dajte mogućnost korisniku da unese neku vrednost pa
#   štampajte pa štampajte sve proizvode čija je cena manja od unete vrednosti - done

cena_srch = eval(input("Unesite cenu proizvoda koje trazite: "))

lista_proiz = [cena_2[0] for cena_2 in proizvod_cena.items() if cena_2[1] <= cena_srch]
print("Sledeci proizvodi imaju cenu manju ili jednaku od unete vrednosti:", lista_proiz)

print('#' * 100)
#######################################################################################################################

#⦁	Za ovaj zadatak koristićemo rečnik sa početka ovog poglavlja koji je kao ključ imao naziv
#   meseca a kao vrednost broj dana u mesecu.

meseci_dani = {'Januar': 31, 'Februar': 28, 'Mart': 31, 'April': 30,
        'Maj': 31, 'Jun': 30, 'Jul': 31, 'Avgust': 31,
        'Septembar': 30, 'Oktobar': 31, 'Novembar': 30, 'Decembar': 31}

print('#' * 100)
#⦁	Tražite od korisnika da unese naziv meseca, pa korišćenjem rečnika kažite mu koliko dana ima taj mesec
#   (Vodite računa da korisnik može uneti nepostojeći mesec – greškom ili namerno ) - done

meseci_in = input("Unesite mesec za proveru broja dana: ")

if meseci_in in meseci_dani:
    print(meseci_dani[meseci_in])
else:
    print("Uneli ste nepostojeci mesec!")

print('#' * 100)
#######################################################################################################################

#⦁	Štampajte sve ključeve iz rečnika u alfabetskom redosledu - done

meseci_l = list(meseci_dani.keys())
meseci_l.sort()

print(meseci_l)

print('#' * 100)
#######################################################################################################################

#⦁	Štampajte sve mesece koji imaju 31 dan - done

lista_dan = [mesec[0] for mesec in meseci_dani.items() if mesec[1] == 31]

print(lista_dan)

print('#' * 100)
#######################################################################################################################

#⦁	Štampajte (kljuc,vrednost) parove sortirane po broju dana u mesecu - done

meseci_sorted = {}
meseci_sorted_kljuc = sorted(meseci_dani, key=meseci_dani.get)

for mesec in meseci_sorted_kljuc:
    meseci_sorted[mesec] = meseci_dani[mesec]

print(meseci_sorted)

print('#' * 100)
#######################################################################################################################

#⦁	Modifikujte program tako da korisnik može da unese samo prva tri znaka - done

mesec_tri = input("Unesite prva tri slova meseca: ").lower().capitalize()
mesec_brojac = 0

for mesec in meseci_dani:
    if mesec.startswith(mesec_tri):
        print("Broj dana u", mesec + '-u je', meseci_dani[mesec])
    if mesec_tri not in mesec:
        mesec_brojac += 1

if mesec_brojac == 12:
    print("Greska, mesec nije nadjen!")

print('#' * 100)
#######################################################################################################################

#⦁	Napišite program koji koristi rečnik u kojem se nalazi deset imena korisnika i njihovih pasvorda.
#   Program treba da traži od korisnika da unesu ime i pasvord. Ako ime nije u rečniku program treba da
#   obavesti korisnika da nije registrovan u sistemu. Ako je uneto ime u rečniku ali korisnik nije uneo
#   ispravan pasvord, program treba da ga obavesti da je uneti pasvord neispravan. Ako je pasvord ispravan
#   program treba da saopšti korisniku da se ulogovao u sistem - done

korisnici = {"Dusan": "korisnik1", "Darko": "korisnik2", "Jovan": "korisnik3",
             "Nemanja": "korisnik4", "Milica": "nbv123", "Ana": "1233559",
             "Ivan": "xXxHunterxXx", "SoulKiller": "No1", "Aleksandar1": "enterpassword", "Lazar": "987654321"}
login = True

while login:
    korisnik = input("Unesite korisnicko ime: ")
    if korisnik in korisnici:
        while login:
            password = input("Unesite sifru: ")
            if korisnici[korisnik] == password:
                print("Dobrodosli", korisnik + "!")
                login = False
            else:
                print("Greska niste uneli pravu lozinku! \nPokusajte opet.")
    else:
        print("Greska korisnicko ime nije u sistemu! \nPokusajte opet.")

print('#' * 100)
#######################################################################################################################

#⦁	Tražite uzastopno od korisnika da unese ime tima kao i koliko je utakmica tim dobio i izgubio.
#   Smestite ove informacije u rečnik u kojem će ključ biti ime tima a vrednost lista
#   u formi [broj pobeda, broj poraza] - done

mala_liga = {}

while True:  # Loop za unos naziva timova
    tim = input("Unesite ime tima (ENTER za kraj): ").lower().capitalize()
    if tim == '':
        break
    pobede = input("Unesite broj pobeda: ")
    while not pobede.isnumeric():  # Provera formata
        print("Greska unos nije validan, pokusajte opet!")
        pobede = input("Unesite broj pobeda: ")
    else:
        porazi = input("Unesite broj poraza: ")
        while not porazi.isnumeric():  # Provera formata
            print("Greska unos nije validan, pokusajte opet!")
            porazi = input("Unesite broj poraza: ")
        else:
            mala_liga[tim] = [int(pobede), int(porazi)]  # Pravljenje recnika T: W/L
            pass

print(mala_liga)

print('#' * 100)
#######################################################################################################################

#⦁	Tražite od korisnika da unese naziv tima, pa korišćenjem rečnika izračunajte i
#   štampajte procenat pobeda koje je taj tim ostvario - done

tim_pretraga = input("Unesite ime tima: ").lower().capitalize()

if tim_pretraga in mala_liga:  # Racunanje % pobeda za uneti tim ako se nalazi u recniku
    skor_procenat = (int(((mala_liga[tim_pretraga][0] / sum(mala_liga[tim_pretraga])) * 100)))
else:
    print("Nemamo podatke za uneti klub, baza podataka se trenutno azurira.\nHvala na strpljenju.")

print(tim_pretraga, "je imao", str(skor_procenat) + '%', "pobeda ove sezone.")

print('#' * 100)
#######################################################################################################################

#⦁	Korišćenjem rečnika, kreirajte listu čiji su elementi brojevi pobeda svih timova - done

lista_pobeda = []

for k, v in mala_liga.values():
    lista_pobeda.append(k)

print("lista pobeda svih timova je:", lista_pobeda)

print('#' * 100)
#######################################################################################################################

#⦁	Korišćenjem rečnika kreirajte listu svih timova koji imaju više pobeda nego poraza - done

lista_vise_pobeda = []

for k in mala_liga.keys():
    if mala_liga[k][0] > mala_liga[k][1]:
        lista_vise_pobeda.append(k)

print(lista_vise_pobeda)

print('#' * 100)
#######################################################################################################################

#⦁	Uzastopno tražite od korisnika da unese rezultate utakmica dva tima u formi tim1 golova1 - tim2 golova2.
#   Smestite ove informacije u rečnik kod kojeg je ključ naziv tima a vrednost lista
#   oblika [broj pobeda, broj poraza] - WiP

#######################################################################################################################

#⦁	Kreirajte jednu 5 x 5 listu slučajnih brojeva od 1 do 5. Zatim napišite program koji kreira rečnik čiji su
#   ključevi brojevi iz 5 x 5 liste, a vrednosti brojevi njihovih pojavljivanja u listi. Zatim štampajte
#   tri broja sa najvećim brojem pojavljivanja - done

lista_5x5 = [[randint(1, 5) for i in range(5)] for n in range(5)]  # 5x5 lista
lista2_5x5 = [i for n in lista_5x5 for i in n]  # Ubacivanje svih elemenata 5x5 liste

print("5x5 lista nasumicnih brojeva od 1 do 5:")
for broj_5x5 in lista_5x5:  # Print 5x5 liste
    print(broj_5x5)

pet_pet = {k_5x5: (lista2_5x5.count(k_5x5)) for k_5x5 in range(1, 6)}  # Recnik sa brojem ponavljanja svake
                                                                       # cifre od 1 do 5 iz 5x5 liste

print("Recnik sa brojevima liste 5x5 i brojem ponavljanja za svaki:", pet_pet, sep='\n')

lista_broj_5x5 = []  # Lista 3 broja sa najvise ponavljanja
for broj_5x5_max in range(3):  # Ubacivanje 3 broja sa najvise ponavljanja
    lista_broj_5x5.append(sorted(pet_pet, key=pet_pet.get, reverse=True)[broj_5x5_max:broj_5x5_max + 1])

for kljuc_5x5 in lista_broj_5x5:
    for broj_5x5_v in kljuc_5x5:
        print("Broj:", broj_5x5_v, "se ponavlja:", pet_pet[broj_5x5_v])  # Stampanje 3 broja sa najvise ponavljanja
                                                                         # i koliko tih ponavljanja ima
print('#' * 100)
#######################################################################################################################

#⦁	Korišćenjem rečnika za špil karata ( rečnik sa početka poglavlja) kreirajte jednu prostu igru u kojoj dvojica
#   igrača dobijaju po tri karte. Igrač sa najjačom kartom pobeđuje. Ako oba igrača imaju istu najjaču kartu
#   pobeđuje onaj koji ima drugu najjaču kartu, ako je i tada nerešeno upoređuju se treće karte. Ako su kod oba
#   igrača sve tri karte iste „jačine“ partija je nerešena - done

spil_karata = {i: [n for n in range(2, 16)] for i in ['Tref', 'Pik', 'Karo', 'Herc']}  # Generise spil karata
prvi_igrac = []
drugi_igrac = []

while len(prvi_igrac) < 3 and len(drugi_igrac) < 3:
    a = random.choice(list(spil_karata.keys()))  # Odredjuje nasumicno znak karte
    prvi_igrac.append([a, random.choice(list(spil_karata[a]))])  # Dodeljuje nasuminco izabranu kartu igracu
    b = random.choice(list(spil_karata.keys()))  # Odredjuje nasumicno znak karte
    drugi_igrac.append([b, random.choice(list(spil_karata[b]))])  # Dodeljuje nasuminco izabranu kartu igracu

print("Prvi igrac ima:", prvi_igrac, "\nDrugi igrac ima:", drugi_igrac)

brojac_prvi = 0
brojac_drugi = 0

for i, n in zip(prvi_igrac, drugi_igrac):  # Provera za svaku kartu kod oba igraca
    if int(i[1]) > int(n[1]):
        brojac_prvi += 1
    else:
        if int(n[1]) > int(i[1]):
            brojac_drugi += 1

if brojac_prvi > brojac_drugi:
    print("Prvi igrac pobedjuje!")
elif brojac_prvi == brojac_drugi:
    print("Nereseno! Probajte opet.")
else:
    print("Drugi igrac pobedjuje!")

print('#' * 100)
#######################################################################################################################

#⦁	Korišćenjem rečnika za špil karata ( rečnik sa početka poglavlja), podelite tri karte. Odredite sledeće:
#⦁	Da li su sve tri karte iste boje (fleš) - done

crno_brojac = 0
crveno_brojac = 0

for i in prvi_igrac:
    if i[0] in ['Tref', 'Pik']:
        crno_brojac += 1
    else:
        if i[0] in ['Karo', 'Herc']:
            crveno_brojac += 1

if crno_brojac == 3 or crveno_brojac == 3:
    print("Cestitamo dobili ste Fleš!")
else:
    print("Vise srece drugi put!")

print('#' * 100)
#######################################################################################################################

#⦁	Da li su sve tri karte iste vrste (triling) - done
#⦁	Da li postoji par istih (ali ne i triling) - done

triling_par = []

for i in prvi_igrac:
    triling_par.append(int(i[1]))

for i in range(2, 15):
    if triling_par.count(i) == 3:
        print("Cestitamo dobili ste Triling!")
    else:
        if triling_par.count(i) == 2:
            print("Cestitamo dobili ste par!")

print('#' * 100)
#######################################################################################################################

#⦁	Da li tri karte čine liniju (kao recimo 2,3,4 ili (10, Žandar, Dama) - done

lista_linija = []

for i in prvi_igrac:
    lista_linija.append(i[1])

lista_linija.sort()

if lista_linija[0] + 2 == lista_linija[1] + 1 == lista_linija[2]:
    print("Dobili ste 3 karte u liniji!")
else:
    print("Karte nisu u liniji.")

print('#' * 100)
#######################################################################################################################

#⦁	Korišćenjem rečnika za špil karata ( rečnik sa početka poglavlja) i Monte Karlo simulacije procenite
#   verovatnoću da se dobije fleš kada se podeli pet karata - done

spil_karata_Flesh = {i: [n for n in range(2, 16)] for i in ['Tref', 'Pik', 'Herc', 'Karo']}  # Pravljenje spila
flesh_broj = 0
brojac = 0

while brojac < 1000000:
    ruka_pet = []
    while len(ruka_pet) < 5:  # Deljenje 5 karata
        karta = random.choice(list(spil_karata_Flesh.keys()))  # Odredjuje nasumicno znak karte
        ruka_pet.append([karta, random.choice(list(spil_karata_Flesh[karta]))]) # Dodeljuje nasuminco
                                                                                # izabranu kartu igracu
    karta_znak = {}
    karta_broj = []

    for i in ruka_pet:
        for n in i:
            if i.index(n) % 2 != 1:
                karta_znak[n] = []  # Dodeljuje znak karte kao key recniku

    for i in ruka_pet:
        karta_broj.append(i[1])  # Probao sam da dodajem vrednost karte kao value u recnik
                        # ali nisam uspeo pa sam prebacio sve na listu
    karta_broj.sort()  # Sortira listu vrednosti karata radi lakse provere
    brojac += 1

    if len(karta_znak.keys()) == 1 and karta_broj[0] + 4 == karta_broj[1] + 3\
            == karta_broj[2] + 2 == karta_broj[3] + 1 == karta_broj[4]:  # Provera za flesh
        flesh_broj += 1

print("U", brojac, "deljenja priblizna sansa za dobijanje flesha je:", str((flesh_broj / brojac) * 100) + '%')

#######################################################################################################################

#⦁	U nekom od ranijih poglavlja sreli smo se sa šifriranjem teksta. Kod šifriranja se svako slovo teksta
#   zamenjuje sa nekim drugim slovom. Na primer svako a zamenjujemo sa e, svako b sa a itd. Napišite program koji
#   traži od korisnika da unese dva stringa. Zatim utvrdite da li drugi string može da bude šifrirana verzija prvog
#   stringa kod kojeg je izvršena zamena slova kako je gore navedeno. Na primer string CXYZ ne može biti šifriran
#   string BOOK jer se O pojavljuje sa dva različita slova u šifriranim string CXYZ. Takođe, CXXK nije šifrirana
#   verzija od BOOK jer se K zamenilo sa samim sobom. S druge strane CXXZ može biti šifriran string BOOK.
#   Problem može biti rešen sa ili bez rečnika.13.

#######################################################################################################################

#⦁	Pretpostavimo da vam je data sledeća lista stringova
#	L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

#   Ovakvi nizovi se pojavljuju na raznim mestima uključujući DNA kodove. Korisnik ima string sa samo nekim od slova
#   a ostala mesta su popunjena sa zvezdicama. Na primer a**a****. Korisnik bi želeo da zna koji string iz liste
#   odgovara njegovom parcijalnom stringu. U primeru koji je dat, a**a****, ovoj mustri bi moglo da odgovara prvi i
#   treći član liste. Jedan način da se reši ovaj problem je da se kreira rečnik čiji ključevi bi bili indeksi za ona
#   slova iz korisnikovog stringa koja nisu zvezdice, a vrednosti u rečniku bi bila sama ta slova. Napišite program
#   koji koristi ovaj način (ili neki drugi načina ) za pronalaženje stringova koji odgovaraju stringu koji
#   unese korisnik ( mustri)

#######################################################################################################################

#⦁	Rečnici predstavljaju pogodan način za smeštanje (pamćenje) struktuiranih podataka. Evo jednog takvog primera
#   d=[{'ime':'Janko', 'telefon':'555-1414', 'email':'janko@mail.net'},
#      {'ime':'Marko', 'telefon':'555-1618', 'email':'marko@mail.net'},
#      {'ime':'Ana', 'telefon':'555-3141', 'email':'';},
#      {'ime':'Jovana', 'telefon':'555-2718', 'email':'jovana@mail.net'}]

#⦁	 Napišite program koji čita ovaj rečnik i štampa sledeće:

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Sve korisnike čiji telefonski broj se završava sa 8.

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Sve korisnike koji nemaju email adresu.

#######################################################################################################################

#⦁	Napišite program kojim se nalazi unija i presek sledećih skupova - done
#   A = {1, 2, 3, 4, 5}
#   B = {4, 5, 6, 7, 8}

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Skup A:", A)
print("Skup B:", B)
print("Unija skupa A i B je:", A | B)
print("Presek skupova A i B je:", A & B)

#######################################################################################################################

print("To bi bio kraj ovog seta vezbi hvala na strpljenju!", "Dovidjenja!", sep='\n')
