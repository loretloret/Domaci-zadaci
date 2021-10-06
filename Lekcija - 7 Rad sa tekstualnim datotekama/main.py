import datetime
import time
from string import ascii_lowercase
import pandas as pd

#⦁	Dat vam je fajl poda nazivom rezultati_testa.txt, gde je u svakoj liniji ime, prezime
#   i broj poena kao u sledećem primeru:
#   Janko Jankovic 83
#   Ana Mijatovic 86
#   Napišite program koji skenira fajl, dodaje 5 poena svakom studentu i upisuje prezime, ime
#   i novi broj poena u fajl rezultat_ispita2.txt - done

rez_test = [line.strip().split(' ') for line in open("rezultati_testa.txt", 'r')]

for i in rez_test:  # Uzima elemente iz liste za svakog studenta i dodaje mu pet bodova
    for n in i:
        if n.isdigit():
            i[2] = int(n) + 5  # Prijavljuje warning u editoru ali petlja radi kako treba

print(rez_test)
rez_test1 = open("rezultati_testa2.txt", "w")
for i in rez_test:  # Upisuje prepravljene ocene u fajl
    rez_test1.write(str(i).strip('[').strip(']').replace("'", '').replace(",", '') + '\n')

rez_test1.close()

print("*" * 100)
#######################################################################################################################

#⦁	Dat vam je fajl pod nazivom ocene.txt, u kojem svaka linija sadrži prezime, ime i
#   tri rezultata kolokvijuma za svakog studenta, kao na primer:

#  Jankovic Janko 83 77 54
#  Mijatovic Ana 86 69 90
#----------------------------------------------------------------------------------------------------------------------#

#⦁  Napišite program kojim se određuje koliko je studenata položilo sva tri kolokvijuma
#   (kolokvijum je položen ako je broj poena veći ili jednak 60) - done

#  Uzima podatke iz tekstualnog fajla i stavlja ih u listu kao element liste
rez_kolokvijum = [line.strip().split(' ') for line in open("rezultati_kolokvijuma.txt", 'r')]

kolokvijum = {}

#  Pravi recnik {Student (key): [ocena, ocena, ocena (value)]} i uklanja sve znakove sa imena
for i in rez_kolokvijum:
    kolokvijum[str(i[0:2]).strip('[').strip(']').replace("'", '').replace(",", ' ')] = i[2:]

pali_ispit_lista = []

#  Proverava svaku ocenu i upisuje imena studenata koji su prosli sva tri ispita
for k, v in kolokvijum.items():
    for i in kolokvijum[k]:
        brojac1 = 0
        if int(i) < 60 and k not in pali_ispit_lista:
            pali_ispit_lista.append(k)

print("Spisak studenata koji su polozili sva tri ispita:", "-" * 50, sep='\n')
for i in kolokvijum.keys():
    if i not in pali_ispit_lista:
        print(i, kolokvijum[i])
        print("-" * 50)

print("*" * 100)
#######################################################################################################################

#⦁	Dat vam je fajl pod nazivom logfile.txt koji lista vremena prijavljivanja i odjavljivanja
#   korisnika na sistem. Tipična linija u fajlu izgleda ovako:

#  Van Rossum, 14:22, 14:37

#⦁  Svaka linija ima tri dela razdvojena zarezom: korisničko ime, vreme prijavljivanja i vreme odjavljivanja.
#   Vremena su data u 24-tvoro časovnom formatu. Možete pretpostaviti da su sva prijavljivanja i
#   odjavljivanja u istom danu.
#----------------------------------------------------------------------------------------------------------------------#

#⦁  Napišite program koji skenira fajl i štampa sve korisnike koji su bili online najmanje jedan sat - done

#  NAPOMENA : Mozda je trebalo da odmah kreiram recnik kako bi uprostio kod da ne trosim vreme na konverzije

#  Izvlaci listu usera i njihovih vremena iz tekstualnog fajla
vreme_log = [line.strip().replace(',', '').split(' ') for line in open("log.txt", 'r')]

vreme_log_dic = {}

#  Pravi recnik {User (key): [lon ig, log out] (value)}
for i in vreme_log:
    vreme_log_dic[str(i[0:2]).strip('[').strip(']').replace("'", '').replace(",", ' ')] = i[2:]

time_1 = time.strptime('1', '%H')  # Jedan sat za kasniju proveru provedenog vremena

for i in vreme_log_dic.values():
    m = time.strptime(i[0], '%H:%M')  # Uzima str vremena i pretvara ih u vremenske jedinice
    n = time.strptime(i[1], '%H:%M')
    for k, v in vreme_log_dic.items():  # Provera da li su proveli vise od 1h ulogovani
        if i == v and (datetime.timedelta(hours=n.tm_hour, minutes=n.tm_min)
                       - datetime.timedelta(hours=m.tm_hour, minutes=m.tm_min))\
                >= datetime.timedelta(hours=time_1.tm_hour):
            print(k, "je bio ulogovan:", datetime.timedelta(hours=n.tm_hour, minutes=n.tm_min)
                  - datetime.timedelta(hours=m.tm_hour, minutes=m.tm_min))
            print("-" * 50)

# #  Jos jedan nacin sa 'pandas', racunanje je isto samo se manje vremena provede u klasifikaciji podataka
# #  Gledao sam nesto o tom modulu pa da odradim zadatak i na taj nacin
# lista_user = pd.read_csv('log.txt', names=['Korisnik', 'Log-In', 'Log-Out'])
#
# print("Korisnici koji su bili duze od sat vremena i njihovo provedeno vreme : ", '-' * 30, sep='\n')
# t = time.strptime('1', '%H')
# for i in range(0, len(lista_user)):
#     log_in = time.strptime(lista_user.loc[i][2][1:], '%H:%M')
#     log_out = time.strptime(lista_user.loc[i][1][1:], '%H:%M')
#     if (datetime.timedelta(hours=log_in.tm_hour, minutes=log_in.tm_min)
#             - datetime.timedelta(hours=log_out.tm_hour, minutes=log_out.tm_min)) >= datetime.timedelta(hours=t.tm_hour):
#         print(lista_user.loc[i][0], (datetime.timedelta(hours=log_in.tm_hour, minutes=log_in.tm_min)
#                                      - datetime.timedelta(hours=log_out.tm_hour, minutes=log_out.tm_min)))
#         print('-' * 30)

print("*" * 100)
#######################################################################################################################

#⦁	Dat vam je fajl pod nazivom studenti.txt. Tipična linija u fajlu je ovakva:
#   dragan katic    katic@email.mef.edu    555-3141

#   Dakle, u svakoj liniji je ime i prezime, email adresa i telefonski broj, svi razdvojeni tabovima
#   (tab je specijalan slovni znak \t). Napišite program koji čita fajl liniju-po-liniju i za svaku
#   liniju, kapitalizuje prva slova imena i prezimena i dodaje pozivni broj 011 ispred broja telefona. Program treba
#   da ove izmene upiše u novi fajl studenti2.txt, Evo kako treba da izgleda linija novog fajla:

#	Dragan Katic    katic@email.mef.edu    011-555-3141 - done

#  NAPOMENA : Zadatak je generalno uradjen na "prevaru", sve je tacno ali je moglo elegantnije da se uradi da je
#  samo jedan podatak drugaciji npr. da jedan broj ima cifru manje bilo bi netacno

studenti = [linija.strip().capitalize() for linija in open("studenti.txt", 'r')]
studenti2 = []

for i in studenti:
    i = i[:i.index(' ') + 1] + i[i.index(' ') + 1:].capitalize()
    i = i[:-8] + '011-' + i[-8:]
    studenti2.append(i)

studenti_upis = open("studenti2.txt", "w")
for i in studenti2:
    studenti_upis.write(i + '\n')

print("*" * 100)
#######################################################################################################################

#⦁	Dat vam je fajl imena.txt koji sadrži gomilu imena. Imena su imena i prezimena razdvojena blanko znakom.
#   Napišite program koji od korisnika traži da unese inicijale, na primer DK ili AM i da štampa sve osobe čija
#   imena odgovaraju tim inicijalima.

#   NAPOMENA : Generalno prost zadatak nema bitnih napomena sem sto bih mogao reci da je uradjen na najjednostavniji
#   nacin koji definitivno nije najelegantniji

imena = [line.strip() for line in open("imena.txt", 'r')]

inicijali = input("Unesite inicijale: ").upper()

print("Spisak imena sa datim inicijalima je: ", '-' * 40, sep='\n')
for i in imena:
    if i.startswith(inicijali[:1]) and i[i.index(' ') + 1:].startswith(inicijali[1:]):
        print(i, '-' * 40, sep='\n')

print("*" * 100)
#######################################################################################################################

# ⦁	Igra rečima – Koristite fajl wordlist.txt za ovaj problem. Pronađite sledeće:

lista_reci = [line.strip() for line in open("wordlist.txt", 'r')]

# ⦁	Sve reči koje se završavaju na ime - done
brojac_ime = 0

for i in lista_reci:
    if i.endswith('ime'):
        brojac_ime += 1

print("Broj reci koje se zavrsavaju sa 'ime' je :", brojac_ime)
print('-' * 50)

# ⦁	Sve reči čije je drugo, treće i četvrto slovo ave - done

brojac_ave = 0

for i in lista_reci:
    if i[1:4] in 'ave':
        brojac_ave += 1

print(brojac_ave, "reci ima ave kao 2,3 i 4 slovo u sebi!")
print('-' * 50)

# ⦁	Koliko reči sadrži bar jedno od sledećih slova r, s, t, l, n, e - done

skup_po_slovo = set()
for i in lista_reci:
    for n in i:
        if n in 'rstlne' and i not in skup_po_slovo:
            skup_po_slovo.add(i)

print(len(skup_po_slovo), "reci u sebi sadrzi r, s, t, l, n ili e")
print('-' * 50)

# ⦁	Procenat reči koje sadrže bar jedno od slova r, s, t, l, n, e - done

print(str('{:.2f}'.format((len(skup_po_slovo) / len(lista_reci) * 100))) + '% reci sadrzi u sebi r, s, t, l, n ili e')
print('-' * 50)

# ⦁	Sve reči koje ne sadrže samoglasnike - done

skup_ne_samo = set()
for i in lista_reci:
    for n in i:
        if n in 'aeiou' and i not in skup_ne_samo:
            skup_ne_samo.add(i)

print("Broj reci koje nemaju samoglasnike je :", len(lista_reci) - len(skup_ne_samo))
print('-' * 50)

# ⦁	Sve reči koje sadrže sve samoglasnike - done

samoglasnik_broj = []

for i in lista_reci:
    zbir_samoglasnik = []
    for n in i:
        if n in 'aeiou' and n not in zbir_samoglasnik:
            zbir_samoglasnik.append(n)
    if len(zbir_samoglasnik) == 5:
        samoglasnik_broj.append(i)

print("Broj reci koje imaju sve samoglasnike :", len(samoglasnik_broj))
print('-' * 50)

# ⦁	Da li ima više desetoslovnih ili sedmoslovnih reči - done

brojac_10 = 0
brojac_7 = 0

for i in lista_reci:
    if len(i) == 10:
        brojac_10 += 1
    if len(i) == 7:
        brojac_7 += 1

if brojac_10 > brojac_7:
    print("Ima vise desetoslovnih reci!")
elif brojac_7 > brojac_10:
    print("Ima vise sedmoslovnih reci!")
else:
    print("Ima ih podjednako!")
print('-' * 50)

# ⦁	Najveću reč u listi - done

print("Najduza rec u listi je :", max(lista_reci, key=len))
print('-' * 50)

# ⦁	Sve palindrome - done

brojac_palindrom = 0

for i in lista_reci:
    if i[:].lower() == i[::-1].lower() and len(i) >= 2:
        brojac_palindrom += 1

print("Broj reci koje su palindromi je :", brojac_palindrom)
print('-' * 50)

# ⦁	Sve reči koje sadrže dupla slova (jedno do drugog) kao u rečima aardvark ili book, izuzimajući reči
#   koje se završavaju na lly - done

lista_isto_slovo = []

for i in lista_reci:
    for n in i:
        if i[i.index(n):i.index(n) + 1] == i[i.index(n) + 1:i.index(n) + 2] and i.endswith('lly') is False:
            lista_isto_slovo.append(i)

print("Broj reci koje sadrze dupla slova :", len(lista_isto_slovo))
print('-' * 50)

# ⦁	Sve reči koje sadrže q iza kojeg ne sledi u - done

brojac_q_ne_u = 0

for i in lista_reci:
    if 'q' in i and i[i.index('q') + 1:i.index('q') + 2] != 'u':
        brojac_q_ne_u += 1

print("Broj reci koje sadrze q iza koga nije u je :", brojac_q_ne_u)
print('-' * 50)

# ⦁	Sve reči koje sadrže zu bilo gde u reči - done

brojac_zu = 0

for i in lista_reci:
    if 'zu' in i:
        brojac_zu += 1

print("Broj reci koje sadrze 'zu' je :", brojac_zu)
print('-' * 50)

# ⦁	Sve reči koje sadrže ab više puta, kao što je reč habitable - done

brojac_ab = 0

for i in lista_reci:
    if i.count('ab') > 1:
        brojac_ab += 1

print("Broj reci koje sadrze 'ab' vise puta je :", brojac_ab)
print('-' * 50)

# ⦁	Sve reči sa četiri uzastopna samoglasnika - WiP

# ⦁	Sve reči koje sadrže i slovo z i slovo w - done

brojac_zw = 0

for i in lista_reci:
    for n in i:
        if 'z' in i and 'w' in i:
            brojac_zw += 1

print("Broj reci koje sadrze slovo 'z' i 'w' u sebi je :", brojac_zw)
print('-' * 50)

# ⦁	Sve reči kod kojih je prvo slovo a, treće slovo e, a peto slovo i - done

brojac_a_e_i = 0

for i in lista_reci:
    if i[:1] == 'a' and i[2:3] == 'e' and i[4:5] == 'i':
        brojac_a_e_i += 1

print("Broj reci koje imaju [a, e, i] kao 1,3 i 5 slovo je :", brojac_a_e_i)
print('-' * 50)

# ⦁	Sve reči sa dva slova - done

brojac_dva = 0

for i in lista_reci:
    if len(i) == 2:
        brojac_dva += 1

print("Broj reci koje sadrze dva slova je :", brojac_dva)
print('-' * 50)

# ⦁	Sve četvoroslovne reči koje počinju i završavaju istim slovom - done

brojac_prvo_zadnje = 0

for i in lista_reci:
    if len(i) == 4 and i[:1] == i[-1:]:
        brojac_prvo_zadnje += 1

print("Broj reci koje pocinju i zavrsavaju istim znakom a imaju cetiri slova je :", brojac_prvo_zadnje)
print('-' * 50)

# ⦁	Sve reči koje sadrže najmanje devet samoglasnika - done

samoglasnik_devet = []

for i in lista_reci:
    zbir_devet = []
    for n in i:
        if n in 'aeiou':
            zbir_devet.append(n)
    if len(zbir_devet) >= 9:
        samoglasnik_devet.append(i)
print("Broja reci koje u sebi sadrze devet ili vise samoglasnika :", len(samoglasnik_devet))
print('-' * 50)

# ⦁	Sve reči koje sadrže slova a, b, c, d, e, i f u bilo kom redosledu. Reč može da sadrži i druga slova.
#   Dva primera su reči backfield i feedback - done

lista_abcdef = []

for i in lista_reci:
    set_provera = set()
    for n in i:
        if n in 'abcdef' and n not in set_provera:
            set_provera.add(n)
    if len(set_provera) == 6:
        lista_abcdef.append(i)

print("Broj reci koje u sebi sadrze bar po jedno a, b, c, d, e i f :", len(lista_abcdef))
print('-' * 50)

# ⦁	Sve reči čija su ista četiri prava i četiri poslednja slova - done?

lista_pola_pola = []

for i in lista_reci:
    set_pola_prva = set()
    set_pola_druga = set()
    if len(i) >= 4:
        set_pola_prva.add(i[:4])
        set_pola_druga.add(i[4:])
        if set_pola_prva == set_pola_druga:
            lista_pola_pola.append(i)
print("Lista reci cija su prva cetiri slova ista kao i zadnja cetiri :", lista_pola_pola, sep='\n')
print('-' * 50)

# ⦁	Sve reči u obliku abcd*dcba, gde je * proizvoljno dugačak niz slova - WiP

# brojac_polu_palindrom = 0
#
# for i in lista_reci:
#     if i[:5] == i[-1:-5:-1]:
#         brojac_polu_palindrom += 1
#         print(i)
#
# print("Broj reci ")

# ⦁	Reč koja u sebi sadrži najviše slova i - WiP

#######################################################################################################################

# ⦁	Napišite program koji pomaže u igri reči. Korisnik unese reč a program koristi listu reči da odredi da li
# korisnikova reč postoji ili ne - done

lista_reci_loop = [line.strip() for line in open("wordlist.txt", 'r')]

while True:
    rec_in = input("Unesite neku englesku rec : ").lower()
    if rec_in == 'kraj':
        print("Dovidjenja!")
        break
    elif rec_in in lista_reci_loop:
        print("Bravo vasa rec", rec_in, "se nalazi u listi!")
    else:
        print("Zao nam je nemamo tu rec! \nPokusajte opet.")

print('#' * 50)
#######################################################################################################################

# ⦁	Pretpostavimo da napišemo sve reči iz liste reči unazad pa ih aranžiramo (sortiramo) alfabetski. Napišite
#   program koji štampa zadnju reč iz te modifikovane liste - done

lista_reci_zadnja = [line.strip()[::-1] for line in open("wordlist.txt", 'r')]
lista_reci_zadnja.sort()

print(lista_reci_zadnja[-1])

print('#' * 50)
#######################################################################################################################

# ⦁	Napišite jednostavan program za proveru spelovanja (spell-checking) nekog teksta. Korisnik treba da unese
#   string a program štampa sve reći za koje misli da su pogrešno napisane. To bi trebalo da budu one reči
#   koje nisu u listi reči - done

lista_reci_spellcheck = [line.strip() for line in open("wordlist.txt", 'r')]

string_spellcheck = input("Unesite neki string na engleskom : ")

lista_gresaka = []

for i in string_spellcheck.split(' '):
    if i not in lista_reci_spellcheck:
        lista_gresaka.append(i)

if len(lista_gresaka) > 1:
    print("Unete reci", lista_gresaka, "nisu gramaticki tacne!")
elif len(lista_gresaka) == 0:
    print("Bravo to je tacno napisana recenica!")
else:
    print("Uneta rec", lista_gresaka, "nije gramaticki tacna!")

print('#' * 50)
#######################################################################################################################

# ⦁	Ukrštenice: Kada rešavate ukrštenicu često imate reč u kojoj znate nekoliko slova, ali ne sva. Možete da
#   napišete program koji vam može pomoći u takvim situacijama. U programu korisnik treba da unese reč sa slovima
#   koje zna i sa zvezdicama za ona slova koja ne zna. Program treba da štampa listu svih reči koje odgovaraju takvom
#   opisu. Na primer ako korisnik unese th***ly program treba da štampa reči koje bi mogle da budu rešenje, kao što
#   su reči thickly i thirdly - WiP

lista_ukrstenica = [line.strip() for line in open("wordlist.txt", 'r')]

#######################################################################################################################

# ⦁	Tražite od korisnika da unese više slova. Zatim pronađite sve reči koje se mogu napraviti od tih slova, uz
#   dozvoljeno ponavljanje - done

slova_input = set(input("Unesite neka slova :").lower())
lista_reci_out = []

for i in lista_ukrstenica:
    if slova_input == set(i):
        lista_reci_out.append(i)

print(lista_reci_out)

print('#' * 50)
#######################################################################################################################

# ⦁	Korišćenjem liste reči, napravite rečnik čiji ključevi su slova od a do z a vrednosti su procenti reči u
#   kojima se ta slova pojavljuju - done

recnik_reci = dict()

for slovo in ascii_lowercase:
    brojac = 0
    for i in lista_ukrstenica:
        if slovo in i:
            brojac += 1
    recnik_reci[slovo] = '{:.2f}%'.format((brojac / len(lista_ukrstenica)) * 100)

print(recnik_reci)

print('#' * 50)
#######################################################################################################################

# ⦁	Korišćenjem liste reči, napravite rečnik čiji ključevi su slova od a do z a vrednosti su procenti pojavljivanja
#   tog slova u odnosu na ukupan broj slova u listi (time se meri frekvencija pojavljivanja slova) - done

recnik_reci_slovo = dict()

slova_zbir = 0
for i in lista_ukrstenica:
    for n in i:
        slova_zbir += 1

for slovo in ascii_lowercase:
    brojac = 0
    for i in lista_ukrstenica:
        if slovo in i:
            brojac += 1
    recnik_reci_slovo[slovo] = '{:.2f}%'.format((brojac / slova_zbir) * 100)

print(recnik_reci_slovo)

print('#' * 50)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese jednu reč, pa se pronalaze sve manje reči koje mogu biti
#   napravljene od slova unete reči. Broj pojavljivanja slova u manjoj reči ne sme premašiti broj tih slova u
#   unetoj reči.

#######################################################################################################################

# ⦁	Napišite program koji učitava fajl koji sadrži email adrese, svaka u posebnoj liniji. Program treba da štampa
#   string koji se sastoji od svih email adresa razdvojenih tačka-zarezom - done

lista_mail = [line.strip() for line in open("mail.txt", 'r')]
str_mail = ''
for i in lista_mail:
    str_mail += ''.join(i + ';')

print(str_mail)

print('-' * 50)
#----------------------------------------------------------------------------------------------------------------------#

#   Napišite program isti kao ovaj gore, ali samo sa adresama koje se ne završavaju sa @prof.mef.edu - done

str_mail2 = ''
for i in lista_mail:
    if i.endswith('@prof.edu.rs'):
        str_mail2 += ''.join(i + ';')

print(str_mail2)

print('#' * 50)
#######################################################################################################################

# ⦁	Fajl temperature.txt sadrži prosečne temperature za svaki dan u godini u nekom gradu. Svaka linija u fajlu
#   sastoji se od datuma, napisanog u formatu mesec/dan, iza koga sledi jedan blanko znak pa prosečna temperatura za
#   taj dan. Vaš program treba da pronađe 30-to dnevni period u kojem je došlo da najvećeg porasta temperature.

#  NAPOMENA : Nisam uspeo da nadjem taj fajl, jedini koji imam sa temperaturama je sa predavanja ali nije to taj

#######################################################################################################################

# ⦁	U jednom od ranijih poglavlja pisali smo program za igru u kojoj se u nekoj priči izostave neke reči. Vaš
#   program je trebalo da traži od korisnika da unese reči sa kojima će biti zamenjene izostavljene reči u priči.
#   Zatim se tako „popravljena“ priča štampa. Prepravite taj program tako da se priča učitava iz fajla. Čitanje priče
#   iz fajla omogućava ljudima, koji ne znaju da programiraju, da koriste svoje priče a da ne moraju da
#   menjaju program - done?

#  NAPOMENA : Zbog nacina na koji sam uradio zadatak (sa %s) napisao bi poruku korisniku da obelezi rec sa
#  placeholder pa bi u programu menjao to sa %s kako bi se program nastavio, ne znam da li se ovo uvazava
#  kao uradjen zadatak

story = str(line.strip() for line in open("user-story.txt", 'r'))

story.replace('place_holder', '%s')

place = input('Enter a place (exp. house, room, kitchen...): ')
pet = input('Enter any animal (exp. horse, duck, pigeon...): ')
obj = input('Enter an object (exp. balloon, soda can, toilet paper...):')
adj = input('Enter an adjective: ')
name = input('Enter a song name: ')

print(story % (place, pet, obj, adj, name, obj))

print('#' * 50)
#######################################################################################################################

# ⦁	Akronim je skraćenica koja koristi prvo slovo iz svake reči u rečenici. Akronime vidimo svuda. Na primer FMEF
#   Fakultet za menadžment, ekonomiju i finansije, ili RTS je Radio Televizija Srbije. Napišite program kojim se unosi
#   akronim a program slučajno bira reči iz liste reči koje odgovaraju tom akronimu. Dole je prikazan tipičan rezultat
#   koji se očekuje od programa

#   Unesite akronim: ABC
#   ['addressed', 'better', 'common']

#   Unesite akronim: BRIAN
#   ['bank', 'regarding', 'intending', 'army', 'naive']

#######################################################################################################################

# ⦁	Ovaj problem je jedna verzija igre Jotto. Kompjuter slučajno bira jednu petoslovnu reč bez ponovljenih slova.
#   Korisnik ima nekoliko pokušaja da pogodi reč. Pri svakom pokušaju korisnik dobije informaciju koliko je
#   slova pogodio.

#######################################################################################################################

print("To bi bio kraj ovog seta vezbi hvala na strpljenju!", "Dovidjenja!", sep='\n')
