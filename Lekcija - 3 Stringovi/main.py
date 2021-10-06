from string import ascii_lowercase
import random

# ⦁	Napišite program koji traži od korisnika da unese string. Program zatim treba da štampa sledeće:

#  NAPOMENA : Prosti zadaci nema sta da se kaze za njih mislim da je sve kako treba
string = input('Unesite neki string: ')

print("-" * 50)
#    ⦁	Ukupan broj znakova u stringu - done

print("Duzina vaseg stringa je:", len(string))

print("-" * 50)
#    ⦁	String ponovljen 10 puta - done

for x in range(10):
    print(string)

print("-" * 50)
#    ⦁	Prvi znak u stringu (setite se da string indeks počinje sa 0) - done

print("Prvi znak u stringu je:", string[0])

print("-" * 50)
#    ⦁	Prva tri znaka iz stringa - done

print("Prva tri znaka u stringu su:", string[:3])

print("-" * 50)
#    ⦁	Zadnja tri znaka iz stringa - done

print("Zadnja tri znaka u stringu su:", string[-3:])

print("-" * 50)
#    ⦁	Ceo string unazad ( palindrom ) - done

print("Vas string unazad je:", string[::-1])

print("-" * 50)
#    ⦁	Sedmi znak u stringu ako string ima dovoljnu dužinu, a u suprotnom odgovarajuću poruku - done

if len(string) >= 7:
    print("Sedmi znak u stringu je:", string[6])
else:
    print('String ima manje od 7 karaktera! ')

print("-" * 50)
#    ⦁	String kod koga su odstranjeni prvi i poslednji znak - done

print("String bez prvog i poslednjeg znaka:", string[1:-1])

print("-" * 50)
#    ⦁	String sa svim velikim slovima - done

print("String sa svim velikim slovima:", string.upper())

print("-" * 50)
#    ⦁	String u kome je svako a zamenjeno sa e - done

print("Svako 'a' je zamenjeno sa 'e':", string.replace('a', 'e'))

print("-" * 50)
#    ⦁	String u kome je svako slovo ( alpha znak ) zamenjeno sa blanko znakom - done

for i in string:
    if i.isalpha():
        string = string.replace(i, ' ')

print("String u kome je svako slovo zamenjeno sa blanko znakom ' ':", string)

print("#" * 100)
#######################################################################################################################

# ⦁	Jedan jednostavan način da se proceni broj reči u stringu je da se prebroji broj blanko znakova (space) u stringu.
#    Napišite program koji traži od korisnika da unese tekst, a onda mu vraća procenjeni broj reči u tom stringu - done

input1 = input('Unesite neki string kako bi prebrojali broj reci: ')
broj_reci = input1.count(' ') + 1

print('Broj reci u unetom stringu je: ', broj_reci)

print("#" * 100)
#######################################################################################################################

# ⦁	Ljudi često zaborave da zatvore zagradu u formulama. Napišite program koji traži od korisnika da unese formulu
#    i štampa poruku da li formula ima isti broj levih i desnih zagrada - done

unos = input('Unesite neku matematicku formulu koja sadrzi zagrade: ').strip(' ')
z1 = 0
z2 = 0

#  NAPOMENA : Ako se dobro secam probao sam bez or metode ali nije htelo tako da sam
#  uradio ovako i ako nije najoptimalnije
for i in unos:
    if i in '(' or '[' or '{':
        z1 += unos.count('(') + unos.count('[') + unos.count('{')
    if i in ')' or ']' or '}':
        z2 += unos.count(')') + unos.count(']') + unos.count('}')

if z1 != z2:
    print("Formula >>", unos, "<< nema isti broj zagrada.")
else:
    print("Formula >>", unos, "<< ima isti broj zagrada.")

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese reč i štampa da li ta reč sadrži samoglasnike ili ne - done

#  NAPOMENA : Nije trazeno ali sam dodao i counter za broj samoglasnika
text = input('Unesite neki tekst kako bi proverili da li sadrzi samoglasnike: ')
samo = 0

for i in text:
    if i in 'aeiou':
        samo += 1

if samo > 0:
    print("Uneti tekst >>", text, "<< ima", samo, "samoglasnika.")
elif samo == 1:
    print("Uneti tekst >>", text, "<< ima", samo, "samoglasnik.")
else:
    print("Uneti tekst >>", text, "<< nema samoglasnike.")

#  NAPOMENA 2 : Ovaj gore kod je kako sam prvobitno uradio zadatak ovaj dole je kako bih ga sada uradio

# samoglasnik_unos = input("Unesite neki string da prebrojimo broj samoglasnika u njemu : ").lower()
#
# rez_samoglasnik = filter(lambda i: i in 'aeiou', list(samoglasnik_unos))
#
# print("Uneti string ima :", len(list(rez_samoglasnik)), "samoglasnika!")

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese string. Program treba da kreira novi string novi_string
#    od unetog stringa tako da se drugi znak unetog stringa zameni sa zvezdicom i da se na kraj stringa dodaju
#    tri znaka uzvika. Na kraju treba štampati novi_string. Tipičan izlaz može da izgleda ovako:
#        Unesite string: Qbert
#                        Q*ert!!! - done(?)

# NAPOMENA : U slucaju da se drugi znak ponavlja npr 'a' svaki znak menja sa '*' probao sam neke
# druge metode ali se uvek desava ista stvar

stari_string = input("Unesite neki string kako bi drugo slovo zamenili znakom '*': ")
novi_string = stari_string.replace(stari_string[1], '*') + '!!!'

print(novi_string)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese string s pa konvertuje s u mala slova,
#    da iz s ukloni sve tačke i zareze, i da štampa rezultat - done

# NAPOMENA: Nisam siguran (davno bese kad sam ovo radio) ali mislim da sam pokusao sa strip metodom i
# nije htelo da radi kako treba pa sam onda isao preko ovog ord
s = input('Unesite neki string koji sadrzi velika, mala slova, tacke i zareze: ').lower()

s1 = s.translate({ord(i): None for i in ',.'})

print(s1)

print("#" * 100)
#######################################################################################################################

# ⦁	Napišite program koji traži od korisnika da unese reč pa odredi da li je uneta reč palindrom ili ne.
#    Palindrom je reč koja se čita jednako sleva na desno kao s desna na levo ( na primer: anavolimilovana) - done

# NAPOMENA : string unos_pali1 sam napravio samo zbog ispisa da se vidi tacno sta je korisnik uneo
unos_pali = input('Unesite neki string kako bi proverili da li je palindrom: ')
unos_pali1 = unos_pali
unos_pali = unos_pali.lower()
unos_pali = unos_pali.replace(' ', '')

if unos_pali[:] == unos_pali[::-1]:
    print('Uneti string >>', unos_pali1, '<< je palindrom')
else:
    print('Uneti string >>', unos_pali1, '<< nije palindrom')

print("#" * 100)
#######################################################################################################################

# ⦁	U nekoj školi email adrese studenata se završavaju sa @student.college.edu, dok se adrese profesora
#    završavaju sa @prof.college.edu. Napišite program koji najpre traži od korisnika koliko će email
#    adresa uneti, a zatim korisnik unosi te adrese. Nakon što su sve adrese unete program treba da štampa poruku
#    da li su sve adrese bile studentske ili je bilo i nekih profesorskih adresa - done

#  NAPOMENA : Mozda je moglo efikasnije da se odradi nisam siguran
broj_mail = int(input('Koliko adresa zelite da unesete (brojem). Adrese se zavrsavaju sa @prof.college.edu i'
                      '@student.college.edu: '))
mail_lista = []
prof_broj = 0
stud_broj = 0

while len(mail_lista) < broj_mail:
    mail = input('Unesite mail-adresu: ')
    mail_lista.append(mail)

for i in mail_lista:
    if i.endswith('@prof.college.edu'):
        prof_broj += 1
    else:
        stud_broj += 1

print('Broj unetih adresa: ', broj_mail, '\nAdresa studenata: ', stud_broj, '\nAdresa profesora: ', prof_broj)

print("#" * 100)
#######################################################################################################################

# ⦁	Tražite od korisnika da unese broj, a zatim štampajte po sledećoj mustri tako
#    da poslednji broj bude onaj koji je korisnik uneo: - done
#                                                       1
#                                                        2
#                                                         3
#                                                          4

unos_broj = int(input('Unesite neki broj (zarad bolje preglednosti neka bude broj do 10): '))
raz = ' '

for n in range(1, unos_broj + 1):
    print(raz * n, n)

print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unese string, a zatim štampa svako slovo iz stringa duplirano
#     i u posebnom redu. Na primer ako je korisnik uneo HEY, izlaz treba da bude ovakav - done
#                                                       HH
#                                                       EE
#                                                       YY

unos_double = input('Unesite neki string kako bi duplirali svako slovo u njemu: ')

for slovo in unos_double:
    print(slovo * 2)

print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unese reč koja sadrži slovo a. Program treba da štampa sledeće
#     dve linije: U prvoj liniji treba da štampa deo stringa do pojavljivanja prvog slova a uključujući i slovo a,
#     a u drugoj treba da štampa ostatak stringa. Sledi primer izlaza - done
#     Unesite reč koja sadrži slovo a: buffalo
#                                      buffa
#                                      lo

slovo_in = input("Unesite neku rec koja sadrzi slovo 'a': ")

print(slovo_in[:slovo_in.index('a') + 1])
print(slovo_in[slovo_in.index('a') + 1:])

print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unese reč a onda kapitalizuje ( konvertuje u veliko slovo )
#     svako drugo slovo iz reči. Tako ako korisnik unese reč rhinoceros, program će štampati rHiNoCeRoS - done

unos_string = input('Unesite neku rec kako bi kapitalizovali svako drugo slovo: ').lower()

izlaz_string = ''.join((i.upper() if n % 2 != 0 else i for n, i in enumerate(unos_string)))

print(izlaz_string)

print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unese dva stringa iste dužine. Program treba da proveri
#     da li su stvarno uneti stringovi iste dužine. Ako nisu, program štampa odgovarajuću poruku i završava rad.
#     Ako jesu iste dužine program treba da štampa alternativno slova iz oba stringa. Na primer ako je korisnik
#     uneo stringove abcde i ABCDE program će štampati AaBbCcDdEe - done

str1 = input('Unesite jedan string: ')
str2 = input('Unesite jos jedan string: ')
str3 = ''

if len(str1) != len(str2):
    print('Uneti stringovi nisu iste duzine!')
else:
    for i in range(len(str1)):
        str3 += str1[i]
        str3 += str2[i]

print(str3)

print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unesu svoje ime i prezime malim slovima,
#     pa kapitalizuje prva slova svakog dela imena - done

ime_unos = input('Unesite vase ime i prezime malim slovima: ').title()

print(ime_unos)

print("#" * 100)
#######################################################################################################################

# ⦁	 Kada sam bio dečak igrali smo igru „Smešna priča“. Način na koji smo igrali bio je da bi me drug pitao
#     da mu kažem neke reči koje bi on ubacivao u neku priču. Priča bi na taj način postajala smešna sa rečima
#     koje sam mu dao, jer ja nisam znao o čemu se u priči radi. Reči su bile obično iz nekoliko kategorija
#     kao na primer mesta, životinje, i tako dalje. Vi treba da napišete program za igranje „Smešne priče“.
#     Prvo treba da napravite priču u kojoj ćete da izostavite neke reči. Vaš program treba da traži od korisnika
#     da unese te reči iz kategorija koje mu saopštite. Zatim štampate čitavu priču sa dodatim rečima.
#     Evo jednog jednostavnog primera, a vi možete koristiti vašu priču - done
#         Enter a college class: PROGRAMMING
#         Enter an adjective: HAPPY
#         Enter an activity: PLAY BASKETBALL
#         PROGRAMMING class was really HAPPY today.  We learned how to
#         PLAY BASKETBALL today in class.  I can't wait for tomorrow's class!

story = '''
I went to this girl's %s the week after she beat the shit out of my %s.
While everyone was getting trashed, I went around putting %s inside all the curtain rods
and so like weeks went by and they couldn't figure out why the house smelled like %s guano.
They caught me through this video where these guys at the party were singing %s while I was
in the background with a can of %s.'''

place = input('Enter a place (exp. house, room, kitchen...): ')
pet = input('Enter any animal (exp. horse, duck, pigeon...): ')
obj = input('Enter an object (exp. balloon, soda can, toilet paper...):')
adj = input('Enter an adjective: ')
name = input('Enter a song name: ')

print(story % (place, pet, obj, adj, name, obj))

print("#" * 100)
#######################################################################################################################

# ⦁	 Kompanije često pokušavaju da personalizuju svoje ponude tako da ih učine atraktivnijim za klijente.
#     Jedan jednostavan način je da ubace ime osobe na različita mesta u ponudi. Naravno, kompanije ne ukucavaju
#     sva ta imena ručno, sve se generiše pomoću računara. Napišite program koji će da traži od korisnika da unese
#     svoje ime i prezime a onda generiše ponudu kao što je ona prikazana dole - done
#         Enter name: George Washington

#         Dear George Washington,

#         I am pleased to offer you our new Platinum Plus Rewards
#         card at a special introductory APR of 47.99%.  George,
#         an offer like this does not come along every day, so I
#         urge you to call now toll-free at 1-800-314-1592. We
#         cannot offer such a low rate for long, George, so call
#         right away.

letter = '''Dear {name} {lastname},

            I am pleased to offer you our new Platinum Plus Rewards
            card at a special introductory APR of 47.99%. {name},
            an offer like this does not come along every day, so I
            urge you to call now toll-free at 1-800-314-1592. We
            cannot offer such a low rate for long, {name}, so call 
            right away.'''

person_name = {'name': input('Enter name: '), 'lastname': input('Enter lastname: ')}

print(letter.format(**person_name))

print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji generiše 26-linijski blok parcijalno prikazan dole.
#     Koristite petlju koja sadrži jednu ili dve print naredbe.
#         abcdefghijklmnopqrstuvwxyz
#         bcdefghijklmnopqrstuvwxyza
#         cdefghijklmnopqrstuvwxyzab
#         itd.
#         yzabcdefghijklmnopqrstuvwx
#         zabcdefghijklmnopqrstuvwxy

#  NAPOMENA : Prebaci prvo slovo na zadnje mesto i obratno ali nisam siguran kako da prodjem kroz string posto
#  ovako samo printa sredinu sa promenama krajeva

# string = 'abcdefghijklmnopqrstuvwxyz'
#
# for n in range(len(string)):
#     kraj = string[n + 0]
#     pocetak = string[-1 - n]
#     string = kraj + string[1:-1] + pocetak
#     print(pocetak, kraj)
#     print(string)

#######################################################################################################################

# ⦁	 Cilj ove vežbe je da proveri da li možete da rešite neke zadatke bez upotrebe in operatora i count
#     i index metoda, korišćenjem samo varijabli, for petlji i if naredbi.

#  NAPOMENA : Za ovaj set zadataka nisam siguran da li sam ispunio uslove posto na pocetku pise da je vezba bez
#  upotrebe indexa i count metoda a u svakoj ponaosob se trazi izuzimanje samo odredjene stvari

# ⦁	Bez korišćenja in operatora, napišite program koji traži od korisnika da unese string i jedna znak,
#    pa da štampa da li se taj znak pojavljuje u stringu - done(?)

str_pretraga_in = input("Unesite neki string koji sadrzi znake poput !, $, % itd.: ")
znak_pretraga_in = input("Unesite znak za koji zelite proveru: ")
str_pretraga_out = str_pretraga_in.count(znak_pretraga_in)

if str_pretraga_out > 0:
    print("Uneti znak se nalazi u stringu!")
else:
    print("Nema unetog znaka u stringu!")

print("-" * 100)
# ⦁	Bez korišćenja count metode, napišite program koji traži od korisnika da unese string i jedan znak,
#    pa da prebroji koliko se puta znak pojavljuje u stringu - done(?)

str_num1 = input("Unesite neki string koji moze da sadrzi vise od jednog znaka '!': ")
str_num2 = str_num1.replace('!', '')
num = len(str_num1) - len(str_num2)
if len(str_num1) > len(str_num2):
    print("Uneti string sadrzi znak '!' koji se u njemu nalazi", num, 'puta.')
else:
    print("Uneli ste string bez znaka '!'.")

print("-" * 100)
# ⦁	Bez upotrebe index metoda, napišite program koji traži od korisnika da unese string, pa da štampa indeks prvog
#    pojavljivanja znaka u stringu. Ako se znak ne pojavljuje u stringu program treba to i da kaže.

string_index_in = input("Unesite neki string koji sadrzi znak poput !, $, % itd.: ")
znak_index_in = input("Unesite znak koji zelite da nadjete: ")
count_indeks = 0

for slovo in string_index_in:
    count_indeks += 1
    if slovo in znak_index_in:
        count_indeks -= 1  #  Oduzima 1 da se izbegne greska kada je znak na kraju stringa
        break

if count_indeks >= len(string_index_in):
    print("Uneti znak nije u stringu!")
else:
    print("Uneti znak se nalazi na indeksu :", count_indeks)


print("#" * 100)
#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unese jedan veliki ceo broj, pa se tom broju dodaju zarezi
#     kao kada se zapisuju iznosi novca. Na primer, ako korisnik unese 1000000, izlaz će biti 1,000,000 - done

num_in = int(input('Unesite neki broj (radi vezbe neka bude veci od 1000 npr. 970055): '))
num_out = '{:,}'.format(num_in)

print(num_out)

print("#" * 100)
#######################################################################################################################

# ⦁	 Anagram neke reči je reč koja se dobija kada se ispremeštaju slova te reči.
#     Na primer dva anagrama reči idle su deli i lied. Napišite program koji traži od korisnika da unese string
#     pa štampa jedan slučajan anagram, drugim rečima slučajan raspored slova originalnog stringa - done

ana_in = input('Unesite neku rec kako bi napravili anagram: ')
ana_list = list(ana_in)

random.shuffle(ana_list)
ana_out = ''.join(ana_list)

print(ana_out)

print("#" * 100)
#######################################################################################################################

# ⦁	 Jedan jednostavan način za šifriranje poruka je premeštanje slova. Jedan način premeštanja je da se najpre
#     uzmu sva slova na parnim pozicijama a zatim sva slova na neparnim pozicijama. Na primer string message bi
#     bio kodiran kao msaeesg jer su slova na parnim pozicijama m, s, a, e (sa indeksima 0, 2, 4, i 6) a slova
#     sa neparnim pozicijama e, s, g (sa indeksima 1, 3, i5).
#     a.	Napišite program koji traži od korisnika da unese string,
#           pa korišćenjem ovog metoda štampa šifrovanu verziju stringa.
#     b.	Napravite program koji dešifruje string koji je bio šifrovan na gornji način - WiP

#  NAPOMENA : Nisam siguran kako da uradim ovaj zadatak (nisam mnogo vremena hteo da gubim na udaranje
#  glave o zid pa sam nastavio dalje)

#######################################################################################################################

# ⦁	 Generalnija verzija gornje tehnike šifriranja je takozvana „cik-cak“ šifra, u kojoj se umesto razdvajanja
#     parnih i neparnih pozicija, razdvajanje vrši na tri, četiri ili više grupa. Na primer, u slučaju razdvajanja
#     na tri grupe, string „secret message“ bi bila podeljena u tri grupe. Prva grupa bi bila „sr sg“, odnosno slova
#     sa indeksima 0, 3, 6, 9 i 12. Druga grupa „eemse“, od slova sa indeksima 1, 4, 7, 10, i 13. Poslednja, treća
#     grupa „ctea“ od slova sa indeksima 2, 5, 8, i 11. Šifrovana poruka bi bila „sr sgeemsectea“.
#     a.	Napišite program koji traži od korisnika da unese string, pa korišćenjem „cik-cak“
#           metode šifrira uneti tekst podelom na tri grupe.
#     a.	Napišite program za dešifrovanje podele na tri grupe.
#     b.	Napišite program koji traži od korisnika da unese string i jedan ceo broj kojim se kazuje na koliko
#           grupa će biti podeljena poruka ( tri, četiri, ili bilo koji drugi broj ). Šifrovati string „cik-cak“ metodom
#     c.	Napišite program koji dešifruje „cik-cak“ u generalnom slučaju - WiP

#  NAPOMENA : Vazi isto kao i za predhodni zadatak

#######################################################################################################################

# ⦁	 U matematičkoj analizi izvod od x4 je 4x3. Izvod od x5 je 5x4. Izvod od x6 je 6x5. Ova šema se nastavlja.
#     Napišite program koji traži od korisnika da unese izraze kao što su x3 ili x5 i da štampa njihov izvod.
#     Na primer ako korisnik unese x3, program treba da štampa 3x2 - done

#  NAPOMENA : Nije najoptimalnije resenje ali mislim da sam tada ovaj zadatak radio oko 2h
izraz = input("Unesite izraz poput x3, z6, y23 itd: ")
izraz_list = []
izraz_list_slovo = []

for i in izraz:
    if i.isalpha():
        izraz_list_slovo.append(i)
    else:
        izraz_list.append(i)

izraz_num = int(''.join(izraz_list))
izraz_slovo = str(''.join(izraz_list_slovo))
izraz_out = str(izraz_num) + izraz_slovo + str(izraz_num - 1)

print(izraz_out)

print("#" * 100)
#######################################################################################################################

# ⦁	 U algebarskim izrazima simbol za množenje se često izostavlja, kao na primer 3x+4y ili 3(x+5).
#    Računari preferiraju izraze kod kojih je prisutan simbol za množenje 3*x+4*y ili 3*(x+5). Napišite program koji
#    traži od korisnika da unese algebarski izraz a onda insertuje simbol za množenje tamo gde je potrebno - WiP

# NAPOMENA : Nisam stigao da uradim zadatak, tokom pauze ili za vreme prakse cu se vratiti na ovaj.
# Generalni plan je da preko indeksa i .isalpha/.isdigit prolazim kroz petlju i ubacujem * gde je potrebno sa
# dodatkom jednog od predhodnih zadataka za proveru zagrada kao bonus.

#######################################################################################################################

# ⦁	 Napišite program koji traži od korisnika da unese naziv varijable, i štampa „Ispravan naziv varijable“ ako je
#     naziv varijable u skladu sa pravilima, a štampa „Neispravan naziv varijable“
#     ako naziv nije u skladu sa pravilima - done

varijabla = input("Unesite naziv varijable: ")

#  Neka najprostija sema za proveru verovatno sam nesto propustio
if varijabla == varijabla.title() or varijabla[0:1] not in ascii_lowercase or varijabla.count(' ') > 0\
        or varijabla.startswith('_'):
    print("Naziv varijable mora poceti sa malim slovom abecede i mora imati '_' umesto razmaka!")
else:
    print("Uneli ste validan naziv varijable!")


#######################################################################################################################

print("To bi bio kraj ovog seta vezbi hvala na strpljenju!", "Dovidjenja!", sep='\n')
