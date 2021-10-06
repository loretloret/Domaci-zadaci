import time
import collections
from random import randint, shuffle

#######################################################################################################################

# ⦁	Napišite klasu Investicija sa varijablama glavnica i kamata. Konstruktor klase treba da postavi vrednosti
#   ovih varijabli. Klasa treba da ima metodu pod nazivom vrednost_posle koja vraća vrednost investicije posle n godina.
#   Formula za to je g*(1+k)**n, gde je g glavnica, a k kamata. Takođe treba da postoji i specijalna metoda __str__
#   takva da štampanje objekta rezultira sledećim izgledom:
#   Glavnica - 1000.00, Kamatna stopa - 5.12%


class Investicija:
    def __init__(self, glavnica, kamata):
        self.glavnica = glavnica
        self.kamata = kamata

    def __str__(self):
        # Glavnica - 1000.00, Kamatna stopa - 5.12 %
        return 'Glavnica - {} RSD, Kamatna stopa - {}%'.format(self.glavnica, self.kamata)

    def vrednost_posle(self, n):
        # g * (1 + k) ** n
        investicija = self.glavnica * (1 + self.kamata) ** n
        return print('{} RSD'.format(investicija))

#######################################################################################################################
# ⦁	Napišite klasu Proizvod. Klasa treba da ima varijable naziv, količina i cena koje sadrže naziv proizvoda, broj
#   proizvoda na skladištu i normalnu cenu proizvoda. Treba da postoji metoda daj_cenu koja prihvata broj proizvoda
#   koji se kupuju i vraća cenu koju treba platiti za taj broj proizvoda, kada se normalna cena primenjuje za broj
#   manji od 10, a popust od 10% za količinu između 10 i 99, a popust 20% za količinu veću od 100. Takođe treba da
#   postoji i metoda napravi_prodaju koja prihvata broj proizvoda koji se kupuju i za taj broj umanjuje vrednost
#   varijable količina.


class Proizvod:
    def __init__(self, naziv, kolicina, cena):
        self.naziv = naziv
        self.kolicina = kolicina
        self.cena = cena
        self.prodaja = 0

    def daj_cenu(self, broj):
        self.prodaja = broj
        if broj > self.kolicina:
            return "Zao nam je ali trenutno nemamo {} {} na stanju!".format(broj, self.naziv)
        if broj >= 100:
            self.kolicina -= self.prodaja
            return (self.cena * broj) - ((self.cena * broj) * 0.2)
        elif 9 < broj < 100:
            return (self.cena * broj) - ((self.cena * broj) * 0.1)
        else:
            return self.cena * broj

    def napravi_prodaju(self):
        if self.prodaja <= self.kolicina:
            self.kolicina -= self.prodaja
        else:
            pass

#######################################################################################################################

# ⦁	Napisati klasu Password_manager. Klasa treba da sadrži listu old_passwords u kojoj se nalaze korisnikovi stari
#   pasvordi. Poslednji pasvord u toj listi je korisnikov tekući pasvord. Treba da postoji metoda get_password koja
#   vraća tekući pasvord i metoda set_password koja postavlja novi pasvord. Metoda set_password treba da menja tekući
#   pasvord samo ako je novi pasvord različit od svih prethodnih pasvorda koje je korisnik do tada koristio. Na kraju
#   kreirajte i metodu is_correct koja prihvata string i vraća True ili False u zavisnosti od toga da li je string
#   jednak tekućem pasvordu ili ne.


class PasswordManager:
    old_passwords = ['1234', '4321', 'user123', '1user1']

    @staticmethod
    def set_password(n):
        if n not in PasswordManager.old_passwords:
            PasswordManager.old_passwords.append(n)

    @staticmethod
    def get_password():
        return PasswordManager.old_passwords[-1]

    @staticmethod
    def is_correct(i):
        if i == PasswordManager.old_passwords[-1]:
            return True
        else:
            return False

#######################################################################################################################

# ⦁	Napišite klasu Time čija jedina varijabla je vreme u sekundama. Klasa treba da sadrži metodu convert_to_minutes
#   koja vraća string minuta i sekundi formatiran kao u sledećem primeru: ako je broj sekundi 230, metoda treba da
#   vrati ‘3:50’. Takođe treba da postoji metoda convert_to_hours koja vraća string sati, minuta i sekundi slično kao
#   prethodna metoda


class Time:
    def __init__(self, sekunde):
        self.sekunde = sekunde

    def convert_to_minutes(self):
        str_min = time.strftime('%M:%S', time.gmtime(self.sekunde))
        return str_min

    def convert_to_hours(self):
        str_sati = time.strftime('%H:%M:%S', time.gmtime(self.sekunde))
        return str_sati

#######################################################################################################################

# ⦁	Napišite klasu Wordplay. Klasa treba da sadrži listu reči. Korisnik ove klase treba da klasi prosledi listu reči
#   koju će koristiti. Klasa treba da ima sledeće metode:


class Wordplay:
    def __init__(self, l1):
        self.l1 = l1

# ⦁	words_with_length(length) — vraća listu svih reči dužine length
    def words_with_length(self, length=0):
        return [i for i in self.l1 if len(i) == length]

# ⦁	starts_with(s) — vraća listu reči koje počinju stringom s
    def starts_with(self, start=''):
        return [i for i in self.l1 if i.startswith(start)]

# ⦁	ends_with(s) — vraća listu reči koje se završavaju stringom s
    def ends_with(self, end=''):
        return [i for i in self.l1 if i.endswith(end)]

# ⦁	palindromes() — vraća listu svih palindromskih reči iz liste reči
    def palindromes(self):
        return [i for i in self.l1 if i[::1] == i[::-1]]

# ⦁	only(L) — vraća listu reči koje sadrže samo slova koja su u L
    def only(self, word=''):
        # return [i for i in self.l1 if set(i) == set(word) and len(list(i)) == len(list(word))]
        return [i for i in self.l1 if collections.Counter(i) == collections.Counter(word)]

# ⦁	avoids(L) — vraća listu reči koje ne sadrže slova iz L
    def avoids(self, word=''):
        return [i for i in self.l1 if len(set(i) & set(word)) == 0]

#######################################################################################################################

# ⦁	Napišite klasu Converter. Korisnik će proslediti dužinu i jedincu mere kada bude kreirao objekat iz ove
#   klase – na primer c = Converter(9, ‘inč’). Moguće jedinice su inč, fit, jard, milja, kilometar, metar, centimetar i
#   milimetar. Za svaku od ovih jedinica treba da postoji metod koji vraća dužinu konvertovanu u tu jedinicu. Na primer,
#   korišćenjem Converter objekta kreiranog gore, korisnik može pozvati c.feet() i dobiti 0.75 kao rezultat.


class Converter:
    baza = {'mm': 1.0, 'cm': 10.0, 'm': 1000.0, 'km': 1000000.0, 'inch': 25.4, 'foot': 304.8,
            'yard': 914.4, 'mile': 1609344}

    def __init__(self, num, mera):
        self.num = num * Converter.baza[mera]
        self.mera = mera

    def getmera(self):
        return self.mera

    def getvrednost(self):
        return self.num / Converter.baza[self.mera]

    def konverzija(self, mera): return Converter(self.num / Converter.baza[mera], mera)

    def inch(self):
        return self.konverzija('inch')

    def foot(self):
        return self.konverzija('foot')

    def yard(self):
        return self.konverzija('yard')

    def mile(self):
        return self.konverzija('mile')

    def km(self):
        return self.konverzija('km')

    def m(self):
        return self.konverzija('m')

    def cm(self):
        return self.konverzija('cm')

    def mm(self):
        return self.konverzija('mm')

    def __str__(self):
        if self.mera in ['mm', 'cm', 'm', 'km']:
            return '{:.1f} {}'.format(self.getvrednost(), self.getmera())
        else:
            return '{:.3f} {}'.format(self.getvrednost(), self.getmera())

#######################################################################################################################

# ⦁	Iskoristite klasu Standard_deck koja je definisana u ovom poglavlju, za kreiranje jedne uprošćene verzije igre sa
#   kartama koja se zove Rat. U ovoj igri postoje dva igrača. Svaki od njih počinje sa jednom polovinom špila. Svaki od
#   igrača okreće po jednu kartu sa vrha špila. Jača karta dobija protivničku kartu i obe idu na dno pobednika. Ako je
#   nerešeno obe karte se izbacuju iz igre. Igra se završava kada jedan od igrača ostane bez ijedne karte.


# broj_karta = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Zandar", "Kraljica", "Kralj"]
# znak_karta = ["Pik", "Karo", "Herc", "Tref"]
#
#
# class Karta:
#     def __init__(self, broj, znak):
#         self.broj = broj
#         self.znak = znak
#
#     def __str__(self):
#         return '{} {}'.format(self.broj, self.znak)
#
#
# class StandardDeck(Karta):
#     def __init__(self, broj, znak):   # Prijavljuje mi da nema super a ovako mi trazi broj i znak
#         super().__init__(broj, znak)  # tako da nisam siguran kako da namestim
#         self.spil = []
#         self.napravi()
#
#     def napravi(self):
#         self.spil = [Karta(broj, znak) for broj in broj_karta for znak in znak_karta]
#         shuffle(self.spil)
#
#     def prikaz(self):
#         for karta in self.spil:
#             print(karta)
#
#     def igra(self):
#         p1 = []
#         p2 = []
#         for i in self.spil:
#             if (self.spil.index(i) + 1) % 2 == 0:
#                 p1.append(i)
#             else:
#                 p2.append(i)
#         shuffle(p1)
#         shuffle(p2)
#         while len(p1) != 0 or len(p1) != 0:
#             print("Igrac 1:", p1[0])
#             print("Igrac 2:", p2[0])

#######################################################################################################################

# ⦁	Napišite klasu koja nasleđuje klasu Card_group iz ovog poglavlja. Izvedena klasa treba da napravi špil karata koji
#   sadrži herceve (hearts) i pikove (spades), samo sa vrednostima karata od 2 do 10 u svakoj od ove dve boje. Dodajte
#   i metod next2 koji vraća dve karte sa vrha špila.

#######################################################################################################################

# ⦁	Napišite klasu Rock_paper_scissors koja implementira logiku igre Rock-paper-scissors. U ovoj igri igrač igra protiv
#   kompjutera određeni broj rundi. Klasa treba da ima varijablu koja sadrži broj rundi, tekuću rundu, kao i broj
#   pobeda za svakog igrača. Treba da postoje metode za dobijanje kompjuterskog izbora poteza, određivanje pobednika
#   runde, i provere da li je neko ukupni pobednik cele igre. Možete dodati i druge metode koje smatrate pogodnim za
#   ovu igru.


class RockPaperScissors:
    def __init__(self, br_rundi):
        self.br_rundi = br_rundi
        self.tr_runda = 1
        self.p1_pobeda = 0
        self.p2_pobeda = 0

    def game(self):
        while self.tr_runda <= self.br_rundi:
            znak = ['Papir', 'Kamen', 'Makaze']
            p2 = znak[randint(0, 2)]
            p1 = input("Odaberite znak: ").lower().capitalize()
            print("Player 2:", p2)

            if p1 == 'Papir' and p2 == 'Kamen':
                self.p1_pobeda += 1
                self.tr_runda += 1
            elif p1 == 'Kamen' and p2 == 'Makaze':
                self.p1_pobeda += 1
                self.tr_runda += 1
            elif p1 == 'Makaze' and p2 == 'Papir':
                self.p1_pobeda += 1
                self.tr_runda += 1
            elif p1 == p2:
                self.tr_runda += 1
            else:
                self.p2_pobeda += 1
                self.tr_runda += 1

    def pobednik(self):
        if self.p1_pobeda > self.p2_pobeda:
            print('Pobedili ste! \nCestitamo!')
            print('Player 1: ', self.p1_pobeda, ', Player 2: ', self.p2_pobeda)
        elif self.p1_pobeda < self.p2_pobeda:
            print('Pobednik je Player 2! \nVise srece sledeci put.')
            print('Player 1: ', self.p1_pobeda, ', Player 2: ', self.p2_pobeda)
        else:
            print('Rezultat je neresen!')
            print('Player 1: ', self.p1_pobeda, ', Player 2: ', self.p2_pobeda)


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
