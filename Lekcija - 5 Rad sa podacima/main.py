#######################################################################################################################

#⦁	Napišite program koji koristi funkcije list i range da kreirate listu [3, 6, 9, … , 99] - done

print(list(range(3, 100)))

print("#" * 100)
#######################################################################################################################

#⦁	Napišite program koji traži od korisnika da unese težinu u funtama. Program treba da konvertuje težinu u
#   kilograme i da formatizuje rezultat na jedno decimalno mesto - done

kon_in = eval(input("Unesite tezinu u funtama: "))

kon_out = kon_in * 0.453592

print('Uneta vrednost iznosi', "{:.1f}".format(kon_out), 'kg.')

print("#" * 100)
#######################################################################################################################

#⦁	Napišite program koji traži od korisnika da unese jednu reč. Presložite slova iz reči tako da budu alfabetski
#   uređena (sortirana) i štampajte tako uređenu reč. Na primer, abracadabra treba da postane aaaaabbcdrr - done

rec_sort_in = list(input("Unesite neku rec: "))
rec_sort_in.sort()
rec_sort_out = ''

for i in rec_sort_in:
    rec_sort_out += i

print(str(rec_sort_out))

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji uzima listu sa deset cena i deset proizvoda, primeni sniženje cena za 11% i
#   prikazuje izlaz kao što je dole prikazano, sa cenama pozicioniranim udesno i lepo formatizovanim - done
# Apples    $  2.45
# Oranges   $ 18.02
# itd.
# Pears     $120.03

proizvod = []
cena = []
brojac = 0

while brojac < 10:
    proizvod.append(input("Unesite proizvod: "))
    cena.append(float(input("Unesite cenu tog proizvoda: ")))
    brojac += 1

for ele_pro, ele_cen in zip(proizvod, cena):
    print('{:7s} {:^s} {:6.2f}'.format(ele_pro, "$", ele_cen - (ele_cen * 0.11)))

print("#" * 100)
#######################################################################################################################

# ⦁	Iskoristite sledeće dve liste i format metodu da kreirate listu svih karata u standardnom špilu od 52 karte, u
#   formatu vrednost boja (na primer, ‘Dama Pik’) - done(?)

# boja = ['Herc', 'Karo', 'Tref', 'Pik']
# vrednost = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Žandar', 'Dama', 'Kralj', 'As']

boja = ['Herc', 'Karo', 'Tref', 'Pik']
vrednost = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Žandar', 'Dama', 'Kralj', 'As']

for i in boja:
    for n in vrednost:
        print(i, n)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji koristi bulovske zastavice (flags) kojima se određuje da li dve
#   liste imaju zajedničkih elemenata ili ne - done


brojac_bul_in = eval((input("Koliko elemenata zelite da unesete u listu: ")))
lista_bul1 = []
lista_bul2 = []
brojac_bul = 0

while brojac_bul < brojac_bul_in:
    lista_bul1.append(input("Unesite neki string za prvu listu: "))
    lista_bul2.append(input("Unesite neki string za drugu listu: "))
    brojac_bul += 1


def zajednicki_ele(lista_bul1, lista_bul2):
    l1_set = set(lista_bul1)
    l2_set = set(lista_bul2)

    if l1_set & l2_set:
        print("Zajednicki elementi obe liste su:", list(l1_set & l2_set))
    else:
        print("Nema zajednickih elemenata!")


zajednicki_ele(lista_bul1, lista_bul2)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program kojim se kreira lista [1, 11, 111, 1111, …, 111…1],
#   gde poslednji element liste ima 100 jedinica - done

lista_niz = []

for znak_niz in range(1, 101):
    lista_niz.append('1' * znak_niz)

print("Duzina zadnjeg elementa je:", len(lista_niz[-1]))
print(lista_niz)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji nalazi sve brojeve od 1 do 1000 koji su deljivi sa 7 a završavaju se sa 6 - done

# Napomena: Radi bolje preglednosti zbog "end=' | '" ovaj deo programa pustati odvojeno

# for i in range(1, 1001):
#     if i % 7 == 0 and i % 10 == 6:
#         print(i, end=' | ')

#print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji određuje koliko brojev od 1 do 10000 sadrži u sebi cifru 3 - done

lista_count = []
trazeni_br = int(input("Unesite broj u rasponu od 1 do 10: "))

for prebrojavanje in range(1, 1001):
    if str(trazeni_br) in str(prebrojavanje):
        lista_count.append(prebrojavanje)

print("U rasponu od 1 do 1000,", len(lista_count), "broj ima u sebi", trazeni_br, "a oni su:", lista_count)

print("#" * 100)
#######################################################################################################################

# ⦁	Sabiranje nekih brojeva sa tim brojevima pročitanim unazad kao rezultat daje palindromski broj.
#   Na primer 241+142=383. Ponekad treba da ponovimo proces. Na primer 84+48=132, 132+231=363.
#   Napišite program koji pronalazi oba takva dvocifrena broja za koje se proces mora
#   ponoviti 20 puta da se dobije palindromski broj - WiP

#######################################################################################################################

# ⦁	Napišite program koji pronalazi sve parove palindromskih brojeva koji su jedan od drugog udaljeni za manje od 20.
#   Jedan takav par su brojevi 199991 i 200002 - done

# NAPOMENA: Kada sam stavio da vadi brojeve do 10000 trebalo mu je skoro 3 minuta
# tako da nisam ni probao sa vecim ciframa

pal_lista = []

for prvi in range(10, 10000):
    for drugi in range(10, 10000):
        if str(prvi)[:] == str(prvi)[::-1] and str(drugi)[:] == str(drugi)[::-1] and drugi - prvi < 20 and\
                prvi != drugi:
            pal_lista.append(prvi if prvi not in pal_lista else drugi)
            for num in pal_lista:
                if pal_lista.count(num) > 1:
                    pal_lista.remove(num)

pal_lista.sort()

print(pal_lista)

print("#" * 100)
#######################################################################################################################

# ⦁	Broj 1961 se čita na isti način ako se gleda odozgo ili odozdo. Štampajte sve brojeve
#   od 1 do 1000000 koji imaju isto takvu osobinu - WiP

# for i in range(1, 1000000):
#     if str(i)[(len(str(i)) // 2) - 1:len(str(i)) // 2 + 1] == '96'\
#             and str(i).replace('96', ' ')[:] == str(i).replace('96', ' ')[::-1]:
#         print(i)

#######################################################################################################################

# ⦁	Broj 99 ima svojstvo da ako pomnožimo njegove cifre i tome dodamo zbir njegovih cifara,
#   dobijemo nazad 99. To jest (9 · 9) + (9 + 9) = 99. Napišite program koji nalazi sve
#   brojeve manje od 10000 sa ovakvim svojstvom. (Ima ih samo devet) - done

for n in range(1, 10001):
    if n == (int(str(n)[:1]) + int(str(n)[-1:])) + (int(str(n)[:1]) * int(str(n)[-1:])):
        print(n)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program za pronalaženje najmanjeg celog broja koji zadovoljava sledeće svojstvo: Ako uzmete prvu cifru
#   i premestite je na kraj broja, broj koji dobijete je 3.5 puta veći od originalnog broja. Na primer ako
#   uzmemo broj 2958 i cifru 2 premestimo na kraj dobijemo broj 9582, koji je 3.2 puta veći od svog originala - done

#  NAPOMENA: Provera za len() je samo da bi se izbegao broj '0'

for broj_swap in range(1, 10000000):
    if len(str(broj_swap)) >= 2 and int(str(broj_swap)[1:] + str(broj_swap)[0]) == broj_swap * 3.5:
        print(broj_swap)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program kojim se određuje sa koliko se nula završava broj 1000! - done

nule_unos = eval(input("Unesite neki broj koji se zavrsava sa nulama"
                       " (u toku pnovnog unosa neka nema nule radi provere): "))
brojac = 0

if str(nule_unos)[-1:].startswith('0'):
    for i in str(nule_unos)[::-1]:
        if i == '0':
            brojac += 1
        else:
            break
    print("Uneti broj sadrzi:", brojac, "nula na kraju.")
else:
    print("Uneti broj nema nule na kraju.")

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji konvertuje decimalan broj visine date u inčima u feet-ima i inčima
#   ( 1 feet = 12 inča). Na primer 4.75 feet-a je 4 feet-a, 9 inča - done

inch = eval(input("Unesite neku velicinu u incima: "))
ft = inch * 0.08333333333333333
inch_clean = (ft % 1) * 12
ft_clean = ft // 1

print("Uneta vrednost u inch >>", inch, "<<", "\niznosi:", ft, "ft.", "ili", ft_clean, "ft. i", inch_clean, "incha")

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji ponavlja pitanje kojim se od korisnika traži da unese fudbalski skor u obliku
#   broj pobeda-broj poraza, na primer(27-13 ili 21-3). Korisnik označava da je završio sa unosom kada unese kraj.
#   Program treba da štampa najveći i najmanji skor od svih unetih skorova - done

skor = []
skor1 =[]
skor_raz = []
skor_prikaz = []
loop = True
loop1 = True

#  Za print najmanje i najvise pobeda
while loop1:
    skor1_unos = input("Unesite fudbalski skor u sezoni oblika W-L (kraj za prekid): ")
    if skor1_unos == 'kraj':
        loop1 = False
    else:
        skor1.append(skor1_unos[:skor1_unos.index('-')])

skor1.sort()

print("Najmanje pobeda:", skor1[0], "\nNajvise pobeda:", skor1[-1])


#  Za najbolji skor u procentima
while loop:
    skor_unos = input("Unesite fudbalski skor u sezoni oblika W-L (kraj za prekid): ")
    if skor_unos == 'kraj':
        loop = False
    else:
        skor.append(skor_unos[:skor_unos.index('-')])
        skor_raz.append(skor_unos[skor_unos.index('-') + 1:])

for i, n in zip(skor, skor_raz):
    skor_prikaz.append(str(int((int(i) / (int(i) + int(n)) * 100))) + '%')

skor_prikaz.sort(reverse=True)

print("Najbolji procenat pobeda je:", skor_prikaz[0], "\nNajgori procenat pobeda je je:", skor_prikaz[-1])

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji ponavlja pitanje o datumu rođenja u formatu mesec/dan (kao 12/25 ili 2/14).
#   Korisnik označava da je završio sa unosom kada unese kraj. Program treba da štampa koliko je od unetih rođendana
#   bilo u februaru i koliko ih je bilo 25-tog u mesecu ( u bilo kom mesecu) - done(?)

# NAPOMENA: nisam definisao tacan broj dana u svakom mesecu samo sam napravio program da odradi zadatak
#           ako je potrebno mogu da prepravim

loop_rodj = True
datumi_mesec = []
datumi_dan = []

while loop_rodj:
    datumi_unos = input("Unesite datum rodjenja u formatu mm/dd, kao 12/25 ili 2/14 (kraj za izlaz): ")
    datumi_unos = datumi_unos.replace('0', '')
    if datumi_unos == 'kraj':
        loop_rodj = False
    # Samo neke provere za greske nisam hteo previse da komplikujem
    elif datumi_unos.count('/') != 1\
            or int(datumi_unos[:datumi_unos.index('/')]) > 12\
            or int(datumi_unos[datumi_unos.index('/') + 1:]) > 31\
            or len(datumi_unos[:datumi_unos.index('/')]) > 2\
            or len(datumi_unos[datumi_unos.index('/') + 1:]) > 2:
        print("GRESKA, molimo vas da unos bude u formatu mm/dd!")
        if datumi_unos == 'kraj':
            break
    else:
        datumi_mesec.append(datumi_unos[:datumi_unos.index('/')])
        datumi_dan.append(datumi_unos[datumi_unos.index('/') + 1:])

februar = datumi_mesec.count('2')
dvadeset_peti = datumi_dan.count('25')

print("Broj rodjendana u februaru:", februar, "\nBroj rodjendana 25-og:", dvadeset_peti)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese datum u obliku mm/dd/yy i konvertuje ga u govorni oblik.
#   Na primer 02/04/77 treba da se konvertuje u Februar 4, 1977 - done

from datetime import datetime

datum = input("Unesite datum u obliku mm/dd/gg (npr. 02/04/77): ")

datum = datetime.strptime(datum, "%m/%d/%y")

print(datum.strftime("%B %d, %Y"))

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji od korisnika traži da unese razlomak u obliku stringa kao što je ‘1/2’ ili ‘8/24’.
#   Program treba da izvrši skraćivanje razlomka i da štampa rezultat. (Skraćivanje razlomka je postupak u kojem se
#   brojilac i imenilac dele zajedničkim deliocem dok god takav postoji) - done

razlomak_unos = input("Unesite razlomak poput 1/2 ili 8/24: ")

brojilac = int(razlomak_unos[:razlomak_unos.index('/')])
imenilac = int(razlomak_unos[razlomak_unos.index('/') + 1:])

for delioc in range(2, brojilac + 1):
    if brojilac % delioc == 0 and imenilac % delioc == 0:
        brojilac = brojilac // delioc
        imenilac = imenilac // delioc

print("Za uneti razlomak:", razlomak_unos, "skraceni razlomak je:", str(brojilac) + "/" + str(imenilac))

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program kojim se nalaze sva rešenje sledećeg problema: Ako jedan mango košta $5,
#   jedan grejpfrut košta $3, a tri jabuke koštaju $1, koliko mango, grejpfruta i jabuka
#   čiji ukupan broj je 100 se može kupiti za $100?

#######################################################################################################################

# ⦁	Evo jedne stare zagonetke koju možete rešiti korišćenje „brutalne sile“, tako što ćete napisati program koji
#   ispituje sve mogućnosti: U izrazu 43+57=207 svaka cifra je za jedan različita od svoje stvarne vrednosti.
#   Koja je od mogućih zamena daje tačan rezultat? - WiP

#######################################################################################################################

# ⦁	Napišite program koji nalazi celobrojna rešenja Pell-ove jednačine x2-2y2=1, gde su x i y između 1 i 100 - done

lista_x = []
lista_y = []

for x in range(1, 101):
    for y in range(1, 101):
        if (x ** 2) - 2 * (y ** 2) == 1:
            lista_x.append(x)
            lista_y.append(y)

print("Resenja jednacine: X2 - 2Y2 = 1 za X, Y u skupu realnih brojeva od 1 do 100 su:")

for x, y in zip(lista_x, lista_y):
    print("X =", x, "Y =", y)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese broj, a zatim štampa sve načina na koje taj broj može
#   biti prikazan kao razlika dva perfektna kvadrata, x2-y2, gde su x i y između 1 i 1000. Pisanje brojeva kao
#   razlike dva kvadrata je jedan od inteligentnih tehnika da se faktorišu veliki brojevi - done

import math

#  NAPOMENA: jedini nacin na koji sam znao da izvucem perfektan kvadrat ali je tesko da se unese pravi broj
#            jedino ako korisnik inputuje nesto poput 25000 ili da se izbaci poruka da nema savrsenih kvadrata
#            osim ako ima jos neki nacin da se dodje do resenja ali ja nisam siguran kako

broj_kvad = eval(input("Unesite ceo broj N kako bi nasli resenje za N = x2 - y2: "))
lista_kvad_x = []
lista_kvad_y = []

for kvad_x in range(1, 1000):
#    koren_x = math.sqrt(kvad_x)
    for kvad_y in range(1, 1000):
#        koren_y = math.sqrt(kvad_y)
        if (kvad_x ** 2) - (kvad_y ** 2) == broj_kvad: #and int(koren_x * koren_x) == kvad_x\
                #and int(koren_y * koren_y) == kvad_y:
            lista_kvad_x.append(kvad_x)
            lista_kvad_y.append(kvad_y)

print("lista resenja za x:", lista_kvad_x, "Lista resenja za y:", lista_kvad_y, sep='\n')

for x_kvad, y_kvad in zip(lista_kvad_x, lista_kvad_y):
    print("Za x2(", x_kvad, ") - y2(", y_kvad, ") =", (x_kvad ** 2) - (y_kvad ** 2))

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program kojim se simuliraju svi mogući ishodi bacanja četiri kockice i izračunavaju sume svih parova
#   kockica u tom bacanju. Na primer ako je bacanje dalo ishod 5 1 2 4, sume su 6,8,9,3,5 i 6. Za svaku moguću sumu
#   os 1 do 12, nađite ukupan broj simuliranih bacanja u kojima se ta suma pojavljuje, kao i procenat pojavljivanja te
#   sume u svim bacanjima. Štampajte broj pojavljivanja i procenat na jedno decimalno mesto. Da proverite ispravnost
#   rada vašeg programa suma 2 se pojavljuje 171 put ili u 13,2 %.

#######################################################################################################################

# ⦁	U magičnim kvadratima, svaki red, svaka kolona i obe dijagonale imaju istu sumu. Jedan parcijalno popunjeni
#   magični kvadrat je prikazan dole. Napišite program koji proverom svih mogućnosti popunjava ovaj magični kvadrat.

#   5 _ _
#   _ 6 2
#   3 8 _

#######################################################################################################################

# ⦁	Sledeće je jedan koristan deo programa za igru Podmornice. Pretpostavimo da imamo jednu 5 x 5 listu sastavljenu od
#   nula i M slova. Napišite program kojim se kreira nova 5 x 5 lista koja ima M slova na istom mestu kao i originalna
#   lista, ali umesto nula ima brojeve koji pokazuju koliko ima susednih M slova ( susednih ili horizontalno,
#   vertikalno ili dijagonalno). Dole je prikazan jedan primer. [Pomoć: „kratak spoj“ može biti od pomoći
#   slučajeve „probijanja“ indeksa]

#    0 M 0 M 0          1 M 3 M 1
#    0 0 M 0 0          1 2 M 2 1
#    0 0 0 0 0          2 3 2 1 0
#    M M 0 0 0          M M 2 1 1
#    0 0 0 M 0          2 2 2 M 1

#######################################################################################################################

# ⦁	Paskalov trougao je prikazan na donjoj slici. Sa spoljašnje strane su jedinice, a svaki drugi broj u trouglu
#   je zbir dva broja neposredno iznad njega.

#	Napišite program koji generiše Paskalov trougao. Omogućite korisniku da unese broj redova. Obezbedite da trougao
#	bude lepo formatizovan, kao ovaj prikazan dole.

#            1
#          1   1
#        1   2   1
#      1   3   3   1
#    1   4   6   4   1
#  1   5  10  10   5   1

#######################################################################################################################

# ⦁	Za dva datuma unesena kao stringovi u formi mm/dd/yyyy gde su godine između 1901 i 2099, odredite koliko ima
#   dana između njih. Evo nekoliko informacija koje mogu biti od pomoći: Prestupne godine između 1901 i 2099 pojavljuju
#   se svake četvrte godine počev od 1904 . Februar ima 28 dana, a 29 u prestupnoj godini. Novembar, April, Jun, i
#   Septembar imaju po 30 dana. Ostali meseci imaju po 31 dan.

#######################################################################################################################

# ⦁	Monte Karlo simulacije se mogu koristiti za procenu raznih stvari uključujući i verovatnoću pri bacanju novčića
#   ili kockica. Kao primer za procenu verovatnoće bacanja dve šestice sa dve kockice, možemo koristiti generator
#   slučajnih brojeva da simuliramo bacanje kockica hiljadama puta i da prebrojimo slučajeve pojave dve šestice i
#   izračunamo procenat pojavljivanja dve šestice.

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Procenite verovatnoću pojavljivanja Jamba pri bacanju pet kockica. Jamb nastaje kada svih pet kockica
#   padnu na isti broj.

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Procenite verovatnoću pojavljivanja „linije“ pri bacanju 5 kockica. „Linija“ nastaje kada se pojave
#   brojevi 1-2-3-4-5 ili 2-3-4-5-6 bilo kojim redosledom.

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Procenite srednje najduže uzastopno pojavljivanje „glave“ ili „pisma“ pri bacanju novčića 200 puta.

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Procenite srednji broj potrebnih bacanja novčića pre nego što se pojavi pet uzastopnih „glava“.

#----------------------------------------------------------------------------------------------------------------------#

#⦁	Procenite srednji broj bacanja novčića pre nego se pojavi string s, gde je s string glava i pisama
#   kao na primer „GGPPG“.

#######################################################################################################################

print("To bi bio kraj ovog seta vezbi hvala na strpljenju!", "Dovidjenja!", sep='\n')
