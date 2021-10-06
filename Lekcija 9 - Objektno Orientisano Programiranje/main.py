from classes import *


#######################################################################################################################

# ⦁	Napišite klasu Investicija sa varijablama glavnica i kamata. Konstruktor klase treba da postavi vrednosti
#   ovih varijabli. Klasa treba da ima metodu pod nazivom vrednost_posle koja vraća vrednost investicije posle n godina.
#   Formula za to je g*(1+k)**n, gde je g glavnica, a k kamata. Takođe treba da postoji i specijalna metoda __str__
#   takva da štampanje objekta rezultira sledećim izgledom:
#   Glavnica - 1000.00, Kamatna stopa - 5.12% - done(?)

#  NAPOMENA : Nisam siguran da je ovo dobro posto na glavnicu od 1000 dobijem nekih 50+ miliona
#  na 5 god sa kamatom od 2%
g = eval(input("Unesite glavnicu : "))
k = eval((input("Unesite kammatnu stopu: ")))

invest = Investicija(g, k)

print(invest)

invest.vrednost_posle(eval(input("Na koliko godina: ")))

print('#' * 50)
#######################################################################################################################

# ⦁	Napišite klasu Proizvod. Klasa treba da ima varijable naziv, količina i cena koje sadrže naziv proizvoda, broj
#   proizvoda na skladištu i normalnu cenu proizvoda. Treba da postoji metoda daj_cenu koja prihvata broj proizvoda
#   koji se kupuju i vraća cenu koju treba platiti za taj broj proizvoda, kada se normalna cena primenjuje za broj
#   manji od 10, a popust od 10% za količinu između 10 i 99, a popust 20% za količinu veću od 100. Takođe treba da
#   postoji i metoda napravi_prodaju koja prihvata broj proizvoda koji se kupuju i za taj broj umanjuje vrednost
#   varijable količina - done

proizvod = Proizvod('Jabuke', 300, 85.5)
print(proizvod.kolicina)

print(proizvod.daj_cenu(eval(input("Koliko jabuka zelite: "))))
proizvod.napravi_prodaju()

print(proizvod.kolicina)

print('#' * 50)
#######################################################################################################################

# ⦁	Napisati klasu Password_manager. Klasa treba da sadrži listu old_passwords u kojoj se nalaze korisnikovi stari
#   pasvordi. Poslednji pasvord u toj listi je korisnikov tekući pasvord. Treba da postoji metoda get_password koja
#   vraća tekući pasvord i metoda set_password koja postavlja novi pasvord. Metoda set_password treba da menja tekući
#   pasvord samo ako je novi pasvord različit od svih prethodnih pasvorda koje je korisnik do tada koristio. Na kraju
#   kreirajte i metodu is_correct koja prihvata string i vraća True ili False u zavisnosti od toga da li je string
#   jednak tekućem pasvordu ili ne - done


print("Trenutna lozinka je:", PasswordManager.get_password())

PasswordManager.set_password(input("Unesite novu lozinku: "))

print("Trenutna lozinka je:", PasswordManager.get_password())

print(PasswordManager.is_correct(input("Unesite novu lozinku radi provere: ")))

print('#' * 50)
#######################################################################################################################

# ⦁	Napišite klasu Time čija jedina varijabla je vreme u sekundama. Klasa treba da sadrži metodu convert_to_minutes
#   koja vraća string minuta i sekundi formatiran kao u sledećem primeru: ako je broj sekundi 230, metoda treba da
#   vrati ‘3:50’. Takođe treba da postoji metoda convert_to_hours koja vraća string sati, minuta i sekundi slično kao
#   prethodna metoda - done

sek = Time(eval(input("Unesite broj sekundi: ")))

print(Time.convert_to_minutes(sek))
print(Time.convert_to_hours(sek))

print('#' * 50)
#######################################################################################################################

# ⦁	Napišite klasu Wordplay. Klasa treba da sadrži listu reči. Korisnik ove klase treba da klasi prosledi listu reči
#   koju će koristiti. Klasa treba da ima sledeće metode:

lista_klase = []

while True:
    rec = input("Unesite neki string (kraj za izlaz): ")
    if rec == 'kraj':
        break
    lista_klase.append(rec)


# ⦁	words_with_length(length) — vraća listu svih reči dužine length - done

len_rec = eval(input("Unesite vrednost za duzine stringova koje trazite: "))

print(Wordplay(lista_klase).words_with_length(len_rec))

print('-' * 50)
# --------------------------------------------------------------------------------------------------------------------#

# ⦁	starts_with(s) — vraća listu reči koje počinju stringom s - done

start_rec = input("Unesite string sa kojim pocinju elementi koje trazite: ")

print(Wordplay(lista_klase).starts_with(start_rec))

print('-' * 50)
# --------------------------------------------------------------------------------------------------------------------#

# ⦁	ends_with(s) — vraća listu reči koje se završavaju stringom s - done

end_rec = input("Unesite string sa kojim se zavrsavaju elementi koje trazite: ")

print(Wordplay(lista_klase).ends_with(end_rec))

print('-' * 50)
# --------------------------------------------------------------------------------------------------------------------#

# ⦁	palindromes() — vraća listu svih palindromskih reči iz liste reči - done

print(Wordplay(lista_klase).palindromes())

print('-' * 50)
# --------------------------------------------------------------------------------------------------------------------#

# ⦁	only(L) — vraća listu reči koje sadrže samo slova koja su u L - done

print(Wordplay(lista_klase).only(input("Unesite neki string (vraca listu reci koje sadrze samo ta slova): ")))

print('-' * 50)
# --------------------------------------------------------------------------------------------------------------------#

# ⦁	avoids(L) — vraća listu reči koje ne sadrže slova iz L - done

print(Wordplay(lista_klase).avoids(input("Unesite neki string (vraca listu elemenata koje nemaju ta slova): ")))

print('#' * 50)
#######################################################################################################################

# ⦁	Napišite klasu Converter. Korisnik će proslediti dužinu i jedincu mere kada bude kreirao objekat iz ove
#   klase – na primer c = Converter(9, ‘inč’). Moguće jedinice su inč, fit, jard, milja, kilometar, metar, centimetar i
#   milimetar. Za svaku od ovih jedinica treba da postoji metod koji vraća dužinu konvertovanu u tu jedinicu. Na primer,
#   korišćenjem Converter objekta kreiranog gore, korisnik može pozvati c.feet() i dobiti 0.75 kao rezultat - done

x = Converter(eval(input("Unesite vrednost: ")), input("Unesite meru (mm, cm, m, km, inch, foot, mile): "))

print('Uneta mera:', x)

print('Iznosi', x.inch())
#######################################################################################################################

# ⦁	Iskoristite klasu Standard_deck koja je definisana u ovom poglavlju, za kreiranje jedne uprošćene verzije igre sa
#   kartama koja se zove Rat. U ovoj igri postoje dva igrača. Svaki od njih počinje sa jednom polovinom špila. Svaki od
#   igrača okreće po jednu kartu sa vrha špila. Jača karta dobija protivničku kartu i obe idu na dno pobednika. Ako je
#   nerešeno obe karte se izbacuju iz igre. Igra se završava kada jedan od igrača ostane bez ijedne karte.

#######################################################################################################################

# ⦁	Napišite klasu koja nasleđuje klasu Card_group iz ovog poglavlja. Izvedena klasa treba da napravi špil karata koji
#   sadrži herceve (hearts) i pikove (spades), samo sa vrednostima karata od 2 do 10 u svakoj od ove dve boje. Dodajte
#   i metod next2 koji vraća dve karte sa vrha špila.

#######################################################################################################################

# ⦁	Napišite klasu Rock_paper_scissors koja implementira logiku igre Rock-paper-scissors. U ovoj igri igrač igra protiv
#   kompjutera određeni broj rundi. Klasa treba da ima varijablu koja sadrži broj rundi, tekuću rundu, kao i broj
#   pobeda za svakog igrača. Treba da postoje metode za dobijanje kompjuterskog izbora poteza, određivanje pobednika
#   runde, i provere da li je neko ukupni pobednik cele igre. Možete dodati i druge metode koje smatrate pogodnim za
#   ovu igru - done


papir_kamen_makaze = RockPaperScissors(eval(input("Unesite zeljeni broj rundi: ")))

papir_kamen_makaze.game()

papir_kamen_makaze.pobednik()

#######################################################################################################################

# ⦁	Napišite klasu Poker_hand koja sadrži listu Card objekata. Klasa treba da sadrži sledeće metode:

# ⦁	has_royal_flush, has_straight_flush, has_four_of_a_kind,

# --------------------------------------------------------------------------------------------------------------------#

# ⦁	has_full_house, has_flush, has_straight,

# --------------------------------------------------------------------------------------------------------------------#

# ⦁	has_three_of_a_kind, has_two_pair, has_pair

# --------------------------------------------------------------------------------------------------------------------#

# ⦁	Takođe treba da postoji metoda best koja vraća string koji pokazuje koja je najjača „ruka“ koja se može napraviti
#   od raspoloživih karata.

#######################################################################################################################

print("To bi bio kraj ovog seta vezbi hvala na strpljenju!", "Dovidjenja!", sep='\n')
